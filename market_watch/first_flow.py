from asyncio import tasks
from dataclasses import field
import os
from dotenv import load_dotenv
import requests
import pandas as pd
from prefect import flow, task

@task
def make_authentication_header():
    load_dotenv()

    TWITTER_API_KEY=os.getenv('TWITTER_API_KEY')
    TWITTER_API_KEY_SECRET=os.getenv('TWITTER_API_SECRET')
    TWITTER_BEARER_TOKEN=os.getenv('TWITTER_BEARER_TOKEN')

    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}

    return headers

@task
def make_param_strings():

    competitors = [
        'apacheairflow', 
        'astronomerio']
        # '3098fsdc89f8uj'
        # ]

    competors_url_string = ','.join(competitors)

    username_param = f'by?usernames={competors_url_string}' 
    fields_param = '&user.fields=public_metrics'

    return (username_param, fields_param)

@task
def make_api_call(headers, username_param, fields_param='&user.fields=public_metrics'):
    base_url = 'https://api.twitter.com/2/users/'
    response = requests.request(
        "GET", 
        base_url + username_param + fields_param, 
        headers=headers
        )

    return response


@flow
def data_output():

    headers = make_authentication_header()
    print(headers.result())
    param_strings = make_param_strings()
    print(param_strings.result())
    # print('HIIIIII -USER', username_param.result())
    # print(fields_param.result())
    # response = make_api_call(headers, username_param, fields_param)
    # print(response.result().json())

if __name__ == '__main__':
    print('HIII')
    data_output()


