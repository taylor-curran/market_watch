
from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

DeploymentSpec(
    name="my-first-deployment",
    flow_location="./first_flow.py",
    flow_name="Get User Data from Twitter API",
    parameters={
        'BEAERER_TOKEN': 'TWITTER_BEARER_TOKEN',
        'users':[
            'apacheairflow', 
            'astronomerio'
            ],
            'fields': 'public_metrics'
        },
    tags=['Twitter_API'],
    flow_runner=SubprocessFlowRunner()
)

# Input data
# users = [
#     'apacheairflow', 
#     'astronomerio'
#     ]
# fields = 'public_metrics'

# r = data_output(BEARER_TOKEN='TWITTER_BEARER_TOKEN', users=users, fields=fields)
