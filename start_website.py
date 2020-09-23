from flask import Flask, render_template, Response, request, redirect, url_for
import os
import time

from random import randint
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import threading
import argparse
import csv
import requests

import xml.etree.ElementTree as ET
import xmltodict
import re

import logging
import os.path
import mysql.connector
from mysql.connector import errorcode
from data_store import DataStore
from VideoUpload.mail_logging import MailLogging

import http.client
import httplib2
import urllib.request
from urllib.error import URLError, HTTPError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

"""
Function from reuters_video_request.py
"""

def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# Method for RT API Calls and recursive parsing of returned XML Content
# First Level parsing

def get_root_xml_data():
    # HTML header
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    header = {
        'User-Agent': USER_AGENT
    }
    t0 = time.time()
    uname = "reutersvideos.api"
    pword = "OhnXhFZkEMJBHBC"
    if uname and pword is None:
        logging.info('Missing API credentials!')
    else:
        try:
            # RT auth token API endpoint URL
            auth_url = "https://commerce.reuters.com/rmd/rest/xml/login?username={uname}&password={pword}"

            auth_resp = requests_retry_session().get(auth_url,
                                                     timeout=3,
                                                     headers=header)
            auth_str = auth_resp.text
            auth_xml = ET.fromstring(auth_str)
            # Retrieved auth auth_token
            global auth_token
            auth_token = auth_xml.text
            logging.info('Got auth token: {auth_token}')
            # API Endpoint URL for channels
            root_url = 'http://rmb.reuters.com/rmd/rest/xml/channels?token={auth_token}'
            root_resp = requests_retry_session().get(root_url, timeout=3, headers=header)
            root_str = root_resp.text
            root_xml = ET.fromstring(root_str)

            return root_xml
        except requests.exceptions.ConnectionError as errh:
            logging.info('Error connection: {}'.format(errh))
            return None
        else:
            logging.info('Eventually worked!')
        finally:
            t1 = time.time()
            logging.info('Took {} seconds'.format(t1 - t0))


class ReutersVideoRequest:
    def __init__(self):
        self.xml_data = get_root_xml_data()
        self.DB = DataStore()
        self.DB.connect_mysql()

    def update_database(self, test=False, outfile=None, videos=False):
        channels = [child.text for child in self.xml_data if child.tag != 'status']
        wanted_channels = ['kby493', 'CLE548', 'hml568', 'Iwu647', 'SNi892', 'aWi668', 'QTZ240', 'acz723', 'XHS867', 'sst663', 'pfg657', 'bov020', 'mvw448']
        channels = list(set(wanted_channels).intersection(channels))
        if channels:
            logging.info('Successfully filtered channels.')
        row_count = 0
        # Attempting to connect to MySQL DB
        # Prevents exhaustive iteration for bug fixing
        if test is True:
            channels = channels[:1]
        try:
            for channel in channels:
                channels_url = 'http://rmb.reuters.com/rmd/rest/xml/items?channel={channel}&token={auth_token}'
                channels_resp = requests.get(channels_url)
                channels_str = channels_resp.text
                channels_xml = ET.fromstring(channels_str)
                # verify status code before retrieving and saving data
                if channels_resp.status_code == 200:
                    logging.warning('\nData retrieved from channel={channel}\n')
                    # xmltodict parser to get values for storing in sql
                    # output is OrderedDict
                    try:
                        channels_dict = xmltodict.parse(channels_str)
                        channels_result = channels_dict['results']['result']
                        for result in channels_result:
                            # Get videos only
                            if videos is True:
                                if result.get('mediaType') != "V":
                                    continue
                            id = result.get('id', 'NULL')
                            guid = result.get('guid', 'NULL')
                            version = result.get('version', 'NULL')
                            dateCreated = result.get('dateCreated', 'NULL').replace('T', ' ').strip('Z')
                            slug = result.get('slug', 'NULL')
                            source = result.get('source', 'NULL')
                            language = result.get('language', 'NULL')
                            headline = result.get('headline', 'NULL')
                            mediaType = result.get('mediaType', 'NULL')
                            priority = result.get('priority', 'NULL')
                            geo = result.get('geography', 'NULL')
                            geography = ','.join(geo) if isinstance(geo, list) else geo
                            channel = result.get('channel', 'NULL')
                            author = result.get('author', 'NULL')
                            previewUrl = result.get('previewUrl', 'NULL')
                            size = result.get('size', 'NULL')
                            dimensions = result.get('dimensions', 'NULL')
                            # Third level parsing
                            items_url = 'http://rmb.reuters.com/rmd/rest/xml/item?id={id}&token={auth_token}'
                            items_resp = requests.get(items_url)
                            items_str = items_resp.text

                            # verify status code before retrieving and saving data
                            if items_resp.status_code == 200:
                                logging.info('Data retrieved from item?id={id}')

                                # create data for mail debug
                                # Take the video link (1080p) and put status = New
                                id = id.split("_")[1]
                                part_video_url = re.compile('http://[a-z].*8256M.*MP4').findall(items_str)[1]
                                description = re.compile(r'<description.*>(.*)</description>').findall(items_str)[1] + "\n" +\
                                              "\n".join(re.compile(r'<p>(.+)</p>').findall(items_str))
                                video_url = '{part_video_url}?token={auth_token}'
                                tags = ",".join(re.compile(r'<keyword>(.*)</keyword>').findall(items_str)).lower()
                                thumbnail = re.compile('http://[a-z].*BASEIMAGE:[0-9]+X[0-9]+').findall(items_str)[1] + "?token={auth_token}"
                                recordingDate = re.compile(r'<firstCreated>(.*)</firstCreated>').findall(items_str)[0]
                                status = 'New'
                                # Store to DB
                                sql_data = (id, guid, version, dateCreated, slug,
                                            source, language, headline, mediaType,
                                            priority, geography, channel, author,
                                            previewUrl, size, dimensions, items_str,
                                            video_url, status, description, tags,
                                            thumbnail, recordingDate)
                                save = self.DB.store_data(data=sql_data)
                                # if successfully saved in database we will put also in email
                                if save:
                                    global debug_email
                                    debug_email += id + ', ' + channel + ',' + headline + '\n'
                                row_count += 1 if save is True else 0
                                logging.info('Row count: {row_count}')
                                # CSV store_data
                                if outfile is not None:
                                    csv_data = [id, guid, version, dateCreated, slug,
                                                source, language, headline, mediaType,
                                                priority, geography, channel, author,
                                                previewUrl, size, dimensions, items_str,
                                                video_url, status, description, tags,
                                                thumbnail, recordingDate]
                                    headers = ['id', 'guid', 'version', 'dateCreated',
                                               'slug', 'source', 'language', 'headline',
                                               'mediaType', 'priority', 'geography',
                                               'channel', 'author', 'previewUrl', 'size',
                                               'dimensions', 'cdata', 'videoUrl', 'status',
                                               'description', 'tags', 'thumbnail', 'recordingDate']
                                    success_write = self.DB.write_to_csv(outfile=outfile, header=headers, row=csv_data)

                    except Exception as e:
                        logging.error('API call error: {e}') 

            # Display total rows inserted
            logging.info('Total records inserted: {row_count}')
            if debug_email:
                mail_logging.send_mail('New request for videos', "{}\n\nGetRT works !".format(debug_email))
            # Close DB Connection
            self.DB.close()
            logging.info('Completed')
        except Exception as e:
            logging.error(e)

def reuters_video_request():
    csv_filepath = os.path.dirname(os.path.realpath(__file__)) + "/historyYT.csv"

    reuters_vr = ReutersVideoRequest()
    reuters_vr.update_database(test=False, outfile=csv_filepath, videos=True)
    logging.warning("Database: Successfully updated")

"""
Functions from the second script: main.py
"""

def connect_mysql():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="user",
            password="pass",
            database="MyDB",
            charset="utf8"
        )
        return mydb

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("Database does not exist")
        else:
            logging.error(err)

def change_status(old_status, new_status):
    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        query = """ UPDATE newtable SET status = %s where status = %s"""
        val = (new_status, old_status, )
        #cursor.execute(query, val)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        logging.error("Something went wrong with mysql update: {}".format(err))

def second_script():
    logging.basicConfig(filename=os.path.dirname(os.path.realpath(__file__)) + '/reuters-3rdScript.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
    mail_logging = MailLogging('asherswing@gmail.com')

    result = change_status('New', 'Upload')
    logging.warning("Result: {}".format(result))


"""
Functions from the third script upload.py
"""

def get_authenticated_service(args):
    flow = flow_from_clientsecrets(
        CLIENT_SECRETS_FILE,
        scope=YOUTUBE_UPLOAD_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE
    )

    storage = Storage(CREDETIALS_REAL_PATH)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        # start new js proccess and get key
        try:
            credentials = run_flow(flow, storage, args)
        except:
            logging.error("Credetials error")
        # put key in console

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))

def initialize_upload(youtube, options):
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category
        ),
        status=dict(
            privacyStatus=options.privacyStatus
        ),
        recordingDetails=dict(
            recordingDate=options.recordingDate
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        # The chunksize parameter specifies the size of each chunk of data, in
        # bytes, that will be uploaded at a time. Set a higher value for
        # reliable connections as fewer chunks lead to faster uploads. Set a lower
        # value for better recovery on less reliable connections.
        #
        # Setting "chunksize" equal to -1 in the code below means that the entire
        # file will be uploaded in a single HTTP request. (If the upload fails,
        # it will still be retried where it left off.) This is usually a best
        # practice, but if you're using Python older than 2.6 or if you're
        # running on App Engine, you should set the chunksize to something like
        # 1024 * 1024 (1 megabyte).
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    resumable_upload(insert_request)

def resumable_upload(insert_request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            logging.info("Uploading file...")
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    logging.warning('Link youtube https://www.youtube.com/watch?v={} was successfully uploaded.'.format(
                        response['id']))
                    global ytUrl
                    global youtube_video_id
                    ytUrl = 'https://www.youtube.com/watch?v=' + response['id']
                    youtube_video_id = response['id']
                else:
                    exit(f'The upload failed with an unexpected response: {response}')
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = "A retriable HTTP error {0} occured:\n{1}".format(e.resp.status, e.content)
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occured: {e}"

        if error is not None:
            logging.error(error)
            retry += 1
            if retry > MAX_RETRIES:
                logging.error("Youtube: No longer attempting to retry.")
                exit()

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            logging.info(f'Sleeping {sleep_seconds} seconds and then retrying...')
            time.sleep(sleep_seconds)


def cut_text(old_text, maxlength=100, delimiter=' '):
    new_text = ''
    for word in old_text.split(delimiter):
        # +1 to have one space after every word
        if (len(word) + 1) < maxlength:
            maxlength -= (len(word) + 1)
            new_text += word + delimiter
        else:
            continue
    return new_text

def get_data(mail_logging):
    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, headline, description, videoUrl, tags, thumbnail, recordingDate, channel FROM newtable "
            "where status='Upload' ORDER BY dateCreated LIMIT 1;")
        row = cursor.fetchall()

        cursor.close()
        conn.close()

        if not row:
            logging.error('Empty database result')
            mail_logging.send_mail('No new videos', 'No video in database to be upload')
            return []
        else:
            for column in row:
                id = column[0]
                title = column[1].encode('utf8')
                description = column[2].encode('utf8')
                videoUrl = column[3]
                tags = column[4].encode('utf8')
                thumbnail = column[5]
                recordingDate = column[6]
                channel = column[7]

            return {'id': id, 'title': title, 'description': description, 'videoUrl': videoUrl, 'tags': tags,
                    'thumbnail': thumbnail, 'recordingDate': recordingDate, 'channel': channel}

    except mysql.connector.Error as err:
        logging.error(err)


def update_status(id, status):
    try:
        conn = connect_mysql()
        cursor = conn.cursor()
        query = """ UPDATE newtable SET status = %s, ytUrl = %s WHERE id = %s;"""
        val = (status, ytUrl, id,)
        cursor.execute(query, val)
        conn.commit()
        print("Updated ytUrl")
        logging.warning("Successfully set status -> uploaded for {}".format(id))
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        logging.error("Something went wrong with mysql update: {}".format(err))


def delete_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            logging.error("{} error on delete!".format(filename))


def download_video(my_video):
    filename = os.path.dirname(os.path.realpath(__file__)) + "/" + my_video["id"].replace(":", "") + ".mp4"

    try:
        urllib.request.urlretrieve(my_video['videoUrl'], filename)
    except HTTPError as e:
        update_status(my_video['id'], 'Error')
        logging.critical('The video server couldn\'t fulfill the request.')
        logging.critical('Error code: ', e.code)
        logging.error('The video can\'t be downloaded from link: {}'.format(my_video['videoUrl']))
        exit()
    except URLError as e:
        update_status(my_video['id'], 'Error')
        logging.critical('We failed to reach a server.')
        logging.critical('Reason: ', e.reason)
        logging.error('The video can\'t be downloaded from link: {}'.format(my_video['videoUrl']))
        exit()
    except:
        update_status(my_video['id'], 'Error')
        logging.error('The video can\'t be downloaded from link: {}'.format(my_video['videoUrl']))
        exit()


def upload_video(my_video):
    std_description = "\n\nSubscribe: http://smarturl.it/reuterssubscribe \
                                    \n\nReuters brings you the latest business, finance and breaking news video from around the globe. \
                                    Our reputation for accuracy and impartiality is unparalleled.\
                                    \n\nGet the latest news on: http://reuters.com/ \
                                    \nFollow Reuters on Facebook: https://www.facebook.com/Reuters \
                                    \nFollow Reuters on Twitter: https://twitter.com/Reuters \
                                    \nFollow Reuters on Instagram: https://www.instagram.com/reuters/?hl=en"

    filename = os.path.dirname(os.path.realpath(__file__)) + "/" + my_video['id'].replace(":", "") + ".mp4"

    # do not exceed the limit of description
    my_decription = cut_text(my_video['description'].decode("utf8"), 4200, '.') + std_description

    # encode the video id in tags
    my_tag = my_video['id'] + "," + my_video['tags'].decode("utf8") + ",コロナウイルス,reuters,business,finance,news,politics,top news" \
    																",headlines,breaking news,news today,bloomberg,thomson reuters,coronavirus,trump"

    my_tag = cut_text(my_tag, 450, delimiter=',')

    # keep title to max length
    my_title = cut_text(my_video['title'].decode("utf8"))

    # standard parse from youtube doc
    argparser.add_argument("--file", help="Video file to upload", default=filename)
    argparser.add_argument("--title", help="Video title", default=my_title)
    argparser.add_argument("--description", help="Video description",
                           default=my_decription)
    argparser.add_argument("--category", default="25",
                           help="Numeric video category.")
    argparser.add_argument("--keywords", help="Video keywords, comma separated",
                           default=my_tag)
    argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
                           default=VALID_PRIVACY_STATUSES[1], help="Video privacy status.")
    argparser.add_argument("--recordingDate", default=my_video['recordingDate'], help="The value is specified in ISO "
                                                                                      "8601 format.")
    args = argparser.parse_args()

    if not os.path.exists(args.file):
        logging.error('Invalid file or missing')
        exit()

    youtube = get_authenticated_service(args)

    try:
        initialize_upload(youtube, args)
        update_status(my_video['id'], 'Done')

        logging.warning('Successfuly uploaded video with id: {}, ytUrl:{}, title:{}'.format(my_video['id'], ytUrl,
                                                                                            my_video['title']))
        mail_logging.send_mail('Successfuly upload new video', '{}, {}, {}'.format(my_video['id'], ytUrl, my_video['title']))
        delete_file(filename)
    except HttpError as e:
        update_status(my_video['id'], 'Error')
        mail_logging.send_mail('Failed',
                               "Video id: {}\nAn HTTP error {} occurred:\n{}".format(my_video['id'], e.resp.status,
                                                                                     e.content))
        logging.error("An HTTP error {0} occurred:\n{1}".format(e.resp.status, e.content))
        delete_file(filename)


def set_thumbnail(my_video, args=None):
    thumbnail_url = my_video['thumbnail']
    thumb_name = my_video["id"].replace(":", "")
    filename = ""

    try:
        filename = os.path.dirname(os.path.realpath(__file__)) + "/" + thumb_name + ".jpg"
        urllib.request.urlretrieve(thumbnail_url, filename)
    except HTTPError as e:
        logging.critical('The thumbnail server couldn\'t fulfill the request.')
        logging.critical('Error code: ', e.code)
        logging.error('The thumbnail can\'t be downloaded from link: {}'.format(thumbnail_url))
        exit()
    except URLError as e:
        logging.critical('We failed to reach a server.')
        logging.critical('Reason: ', e.reason)
        logging.error('The thumbnail can\'t be downloaded from link: {}'.format(thumbnail_url))
        exit()
    except:
        logging.error('The thumbnail can\'t be downloaded from link: {}'.format(thumbnail_url))
        exit()

    if os.path.exists(filename):
        try:
            youtube = get_authenticated_service(args)
            global youtube_video_id
            request = youtube.thumbnails().set(videoId=youtube_video_id, media_body=MediaFileUpload(filename))
            response = request.execute()
            logging.warning("Successfuly SET thumbnail")
            delete_file(filename)
        except:
            logging.warning("ERROR set thumbnail - API")
            delete_file(filename)
    else:
        logging.warning("ERROR set thumbnail")


def choose_yt_channel(my_video):
    global credentials_dinamyc_file, CREDETIALS_REAL_PATH

    arabic_channel = ['XHS867']
    english_channel = ['kby493', 'CLE548', 'hml568', 'Iwu647', 'SNi892', 'aWi668', 'QTZ240', 'acz723']
    german_channel = ['sst663']
    japan_channel = ['pfg657']
    spanish_channel = ['bov020']
    russian_channel = ['mvw448']

    all_channels = dict({'arabic': arabic_channel, 'english': english_channel, 'german': german_channel,
                         'japan': japan_channel, 'spanish': spanish_channel, 'russian': russian_channel})

    for key, value in all_channels.items():
        if my_video['channel'] in value:
            credentials_dinamyc_file = key + '.json'
            CREDETIALS_REAL_PATH = credentials_static_path + credentials_dinamyc_file

    if not credentials_dinamyc_file:
        mail_logging.send_mail('ERROR channel select', 'No channel selected')
        update_status(my_video['id'], 'Error')
        logging.error('No channel selected')
        exit()


def upload():
    logging.basicConfig(filename=os.path.dirname(os.path.realpath(__file__)) + '/reuters-youtube.log', filemode='a+',
                        format='%(name)s - %(levelname)s - %(message)s')
    mail_logging = MailLogging('asherswing@gmail.com')
    credentials_static_path = os.path.dirname(os.path.realpath(__file__)) + "/oauth-channels/"
    credentials_dinamyc_file = ""
    CREDETIALS_REAL_PATH = credentials_static_path + credentials_dinamyc_file

    # Explicitly tell the underlying HTTP transport library not to retry, since
    # we are handling retry logic ourselves.
    httplib2.RETRIES = 1

    # Maximum number of times to retry before giving up.
    MAX_RETRIES = 10

    # Always retry when these exceptions are raised.
    RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
                            http.client.IncompleteRead, http.client.ImproperConnectionState,
                            http.client.CannotSendRequest, http.client.CannotSendHeader,
                            http.client.ResponseNotReady, http.client.BadStatusLine)

    # Always retry when an apiclient.errors.HttpError with one of these status
    # codes is raised.
    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    CLIENT_SECRETS_FILE = os.path.dirname(os.path.realpath(__file__)) + "/client_secret.json"

    # This OAuth 2.0 access scope allows an application to upload files to the
    # authenticated user's YouTube channel, but doesn't allow other types of access.
    YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # This variable defines a message to display if the CLIENT_SECRETS_FILE is
    # missing.
    MISSING_CLIENT_SECRETS_MESSAGE = """
    WARNING: Please configure OAuth 2.0

    To make this sample run you will need to populate the client_secrets.json file
    found at:

    %s

    with information from the API Console
    https://console.developers.google.com/

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    CLIENT_SECRETS_FILE))

    VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")
    ytUrl = ""
    youtube_video_id = ""
    #Main of the function
    my_video = get_data(mail_logging)

    if my_video:
        choose_yt_channel(my_video)
        download_video(my_video)
        upload_video(my_video)
        set_thumbnail(my_video)
    else:
        logging.error('No video to be upload')
        exit()


def last_fifty_videos():
    mysqlConnection = connect_mysql()
    cursor = mysqlConnection.cursor()
    cursor.execute("SELECT id, guid, version, dateCreated, source, language, mediaType, \
     priority, geography, channel, author, previewUrl, videourl, status, ytUrl, headline \
     FROM newtable ORDER BY dateCreated limit 50")
    row = cursor.fetchall()
    cursor.close()
    mysqlConnection.close()
    return row
app = Flask(__name__)
    
@app.route("/")
def index():
    file = open("status.txt", "r")
    full_page = render_template('index.html', Status= "Status: " + file.read()) 
    tableHtml = "<div><div><table style=\"width: 100%;\" border=\"1\">"

    file = open("templates/tableTop.html","r")
    
    tableHtml = tableHtml + file.read()

    file.close()
    row = last_fifty_videos()
    for i in row:
        tableHtml = tableHtml+ render_template('table.html', id=i[0].split("_",1)[1],version=i[1],
        datecreated=i[2],source=i[3],language=i[4],mediatype=i[5],priority=i[6],
        geography=i[7],channel=i[8],author=i[9],previewurl=i[10],
        videourl=i[11],status=i[12],yturl=i[13])
    tableHtml = tableHtml + "</table></div></div>"
    full_page = full_page + tableHtml
    return full_page
@app.route("/start", methods=['POST'])
def start():
    statusfile = open("status.txt", "r")
    safeThreading = statusfile.read()
    statusfile.close()
    if safeThreading == "Stopped":
        file = open("status.txt", "w")
        file.write("Started")
        file.close()
        thread = threading.Thread(target=run)
        thread.start()
    return "Started"

@app.route("/stop", methods=['POST'])
def stop():
    file = open("status.txt", "w")
    file.write("Stopped")
    file.close()
    
    row = last_fifty_videos()
    
    tableHtml = "<div><div><table style=\"width: 100%;\" border=\"1\">"

    file = open("templates/tableTop.html","r")
    
    tableHtml = tableHtml + file.read()

    file.close()
    for i in row:
        tableHtml = tableHtml+ render_template('table.html', id=i[0].split("_",1)[1],version=i[1],
        datecreated=i[2],source=i[3],language=i[4],mediatype=i[5],priority=i[6],
        geography=i[7],channel=i[8],author=i[9],previewurl=i[10],
        videourl=i[11],status=i[12],yturl=i[13])
    tableHtml = tableHtml + "</table></div></div>"

    return tableHtml

def run():
    flag = True 
    while flag == True:
        time.sleep(1)
        statusfile = open("status.txt", "r")
        print("here")
        def runscript():
            if statusfile.read() == "Started":
                # os.system("cd ReutersUploadYT/Database && python reuters_video_request.py")
                # time.sleep(15)
                # First script was replaced by a function with the same name 
                reuters_video_request()
                print("first script ran")
                # os.system("cd ReutersUploadYT/3rdScript && python main.py")
                #time.sleep(5)
                # The main.py script was replaced by the function second_script   
                second_script()
                print("second script ran")
                # os.system("cd ReutersUploadYT/VideoUpload && python upload.py")
                # time.sleep(2)
                # The upload.py script was replaced by a function of the same name
                upload()
                print("third script ran")
                return True 
            else:
                return False
                #break
        flag = runscript()
        statusfile.close()
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
