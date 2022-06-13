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


competitors = [
    'apacheairflow', 
    'astronomerio'
    '3098fsdc89f8uj'
    ]

# competors_url_string = ','.join(competitors)

usernames_param = f'by?usernames={competors_url_string}' 
fields_param = '&user.fields=public_metrics'

response = requests.request(
    "GET", 
    base_url + usernames_param + fields_param, 
    headers=headers
    )



print(response.json())
# print(response.json()['data'])

# df = pd.DataFrame(response.json()['data'])

# print(df.head())

# print(df.columns)

# df.to_csv('public_metrics.csv')



