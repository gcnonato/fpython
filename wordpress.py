from wordpress import API

base_url = "http://books.home.local/omniana"
api_path = "/wp-json/pressbooks/v2/"
wpapi = API(
    url=base_url,
    consumer_key="thisismykey",
    consumer_secret="thisismysecret",
    api="wp-json",
    version="pressbooks/v2",
    wp_user="phil",
    wp_pass="thisismypassword",
    oauth1a_3leg=True,
    creds_store="~/.wc-api-creds3.json",
    callback="http://books.home.local/omniana/api-test"
)
print("creating new chapter")
resource = "chapters"
data = {
    "content": "test",
    "title": "test",
    "status": "publish",
    "chapter-type": 48,
    "part": 27
}

try:
    response = wpapi.post(base_url+api_path+resource, data)
    pprint(response.json())
except Exception as e:
    print("couldn't post")
    print(e)
