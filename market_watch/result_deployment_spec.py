
from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

DeploymentSpec(
    name="result-my-first-deployment",
    flow_location="./result_first_flow.py",
    flow_name="RESULT Get User Data from Twitter API",
    parameters={
        'BEARER_TOKEN': 'TWITTER_BEARER_TOKEN',
        'users':[
            'apacheairflow', 
            'astronomerio'
            ],
            'fields': 'public_metrics'
        },
    tags=['RESULT'],
    flow_runner=SubprocessFlowRunner()
)
