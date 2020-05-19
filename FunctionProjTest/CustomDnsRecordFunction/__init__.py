import datetime
import logging
from azure.mgmt.privatedns import PrivateDnsManagementClient
from azure.mgmt.privatedns.operations import RecordSetsOperations
from azure.common.credentials import ServicePrincipalCredentials
import re

import azure.functions as func

# Replace this with your subscription id
SUBSCRIPTION_ID = ''

# sp_rbac_consul_infra_read_app_id
CLIENT_ID = ''

# sp_rbac_consul_infra_read_secret
SECRET = ''

#sp_read_azkeyvault_tenant
TENANT = ''

# dev
private_zone_name = ''

resource_group_name = ''

RESOURCE = 'https://management.azure.com/'

CONSUL_HOSTNAME_PATTERN = '^(\w+\-\w+\-\w+\-consul)[0-9a-zA-Z]+$'

def list_records():
    credentials = ServicePrincipalCredentials(
        client_id = CLIENT_ID,
        secret = SECRET,
        tenant = TENANT,
        resource = RESOURCE
    )

    client = PrivateDnsManagementClient(credentials, SUBSCRIPTION_ID)

    # https://docs.microsoft.com/en-us/python/api/azure-mgmt-privatedns/azure.mgmt.privatedns.operations.record_sets_operations.recordsetsoperations?view=azure-python
    # https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/network/azure-mgmt-dns/azure/mgmt/dns/v2016_04_01/_dns_management_client.py
    # ops = RecordSetsOperations(client, config, serializer, deserializer)

    records = client.record_sets.list(resource_group_name, private_zone_name)

    # dict group -> instances
    group_to_hostnames_dict = {}

    for rec in records:
        match = re.search(CONSUL_HOSTNAME_PATTERN, rec.name)
        if (match):
            rec_name = rec.name
            rec_group = match.group(1)

            if rec_group not in group_to_hostnames_dict:
                group_to_hostnames_dict[rec_group] = []

            dict_entry = group_to_hostnames_dict[rec_group]
            dict_entry.append(rec_name)


    print(group_to_hostnames_dict)

    return None

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('Invoking list_records at %s', utc_timestamp)
    list_records()
    logging.info('Invoked list_records at %s', utc_timestamp)
