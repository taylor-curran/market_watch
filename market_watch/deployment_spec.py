
from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

DeploymentSpec(
    name="my-first-deployment",
    flow_location="./first_flow.py",
    flow_name="Get User Data from Twitter API",
    parameters={
        'BEARER_TOKEN': 'TWITTER_BEARER_TOKEN',
        'users':[
            'apacheairflow', 
            'astronomerio'
            ],
            'fields': 'public_metrics'
        },
    tags=['Twitter_API'],
    flow_runner=SubprocessFlowRunner()
)
