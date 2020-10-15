from scrapinghub import ScrapinghubClient
import logging
from requests import get, Session
import csv

'''Programa que serve para gerenciamento do site SCRAPINGHUB.COM'''

apikey = u'a103bede59104d20a3fcdd4573996355'
client = ScrapinghubClient(apikey)

project = client.get_project(263925)
projects = project.spiders.list()

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level = logging.INFO,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

logger.info("Starting downloading")

for projeto in projects:
    name_spider = project.spiders.get(projeto['id'])
    # print(name_spider.key, name_spider.name)
    spider = project.spiders.get(name_spider.name)
    jobs_summary = spider.jobs.iter()
    job_keys = [j['key'] for j in jobs_summary]
    # campos = ['_type', 'data', 'probabilidade', 'sensacaoTermica', 'temperaturaMaxima','temperaturaMinima', 'texto']
    # campos = ['_type', 'data', 'probabilidade', 'sensacaoTermica', 'temperaturaMaxima','temperaturaMinima', 'texto']
    campos = ['_type', 'chest']
    for job_key in job_keys:
        print(job_key)
        # Get the corresponding job from the key, as "job"
        job = project.jobs.get(job_key)
        print(job)
        # url = f'https://storage.scrapinghub.com/items/{job_key}' \
        # '?apikey=a103bede59104d20a3fcdd4573996355' \
        # '&format=csv' \
        # '&saveas=items_climatempo_22.csv' \
        # f'&fields={",".join([field for field in campos])}' \
        # '&include_headers=1'
        # with Session() as s:
        #     try:
        #         download = s.get(url)
        #         decoded_content = download.content.decode('utf-8')
        #         cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        #         my_list = list(cr)
        #         for row in my_list:
        #             print(row)
        #     except:
        #         ...
    # break
        # Check to see if the job was completed
        # if job.metadata.get(u'close_reason') == u'finished':
        #     # Create an empty list that will store all items (dictionaries)
        #     itemsDataFrame = pd.DataFrame()
        #     for item_aggelia in job.items.iter():
        #         # Save all items (dictionaries) to the DataFrame
        #         itemsDataFrame = itemsDataFrame.append(item_aggelia, ignore_index=True)
        #         job_key_name = job_key.split("/")[2]
        #         # Export a pickle
        #         # Check that the list is not empty
        #         if not itemsDataFrame.empty:
        #             for meta in job.metadata.iter():
        #                 if meta[0] == u"scrapystats":
        #                     timestamp = meta[1][u'finish_time'] / 1000.0
        #             dt = datetime.fromtimestamp(timestamp)
        #         # Check for empty fields
        #         colList = itemsDataFrame.columns.tolist()
        #         for col in colList:
        #             if itemsDataFrame[col].isnull().all():
        #                 logger.warning("Found Null Field, in job " + job_key_name + ": " + col)
        #             # Delete the job from ScrapingHub
        #         logger.debug("Deleting job " + job_key_name)
        #         # job.delete()
        #     else:
        #         logger.info(
        #             "Encontrou um trabalho que não terminou corretamente. Job key: "
        #             + job_key + ". close_reason:" + job.metadata.get(u'close_reason')
        #         )
