from kubernetes import client, config # kubernetes lib
import os # os lib
import slack # slack lib
config.load_incluster_config() # load kubernetes config
# client = slack.WebClient(token=os.environ['SLACK_API_TOKEN']) # setup slack
v1a=client.AppsV1Api() # prep k8s api for listing deployments
print("Listing deployments:")
ret = v1a.list_deployment_for_all_namespaces(watch=False) # fetch all deployments
for i in ret.items:
    print("%s\t%s\t%s" % (i.metadata.namespace, i.metadata.name, i.metadata.labels)) # print some info about each deployment
    # response = client.chat_postMessage(channel='#random',text=i.metadata.name) # slack to be tested
    # assert response["ok"]  # slack to be tested
