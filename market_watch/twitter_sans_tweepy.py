import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

TWITTER_API_KEY=os.getenv('TWITTER_API_KEY')
TWITTER_API_KEY_SECRET=os.getenv('TWITTER_API_SECRET')
TWITTER_BEARER_TOKEN=os.getenv('TWITTER_BEARER_TOKEN')

headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
base_url = 'https://api.twitter.com/2/users/'

competitors = ['apacheairflow', 'astronomerio']

usernames_param = 'by?usernames=apacheairflow,astronomerio' 
fields_param = '&user.fields=public_metrics'

response = requests.request(
    "GET", 
    base_url + usernames_param + fields_param, 
    headers=headers
    )

print(response.json()['data'])

df = pd.DataFrame(response.json()['data'])

print(df.head())

print(df.columns)



