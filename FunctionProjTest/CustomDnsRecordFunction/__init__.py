import datetime
import logging
from azure.mgmt.privatedns import PrivateDnsManagementClient
from azure.mgmt.privatedns.operations import RecordSetsOperations
from azure.common.credentials import ServicePrincipalCredentials

import azure.functions as func

# Replace this with your subscription id
SUBSCRIPTION_ID = ''

CLIENT_ID = ''
SECRET = ''
TENANT = ''

RESOURCE = ''
RESOURCE = "https://storage.azure.com/"

credentials = ServicePrincipalCredentials(
    client_id = CLIENT_ID,
    secret = SECRET,
    tenant = TENANT,
    resource = RESOURCE
)

client = PrivateDnsManagementClient(credentials, SUBSCRIPTION_ID)
# ops = RecordSetsOperations(client, config, serializer, deserializer)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
