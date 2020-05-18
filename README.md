
#### Environment Setup

pip3 install -r requirements.txt

npm install -g azure-functions-core-tools

python3 -m venv .venv
source .venv/bin/activate

func init FunctionProjTest

```shell
$ func init FunctionProjTest
 Select a number for worker runtime:
 1. dotnet
 2. node
 3. python
 4. powershell
 Choose option: 3
 python
 Found Python version 3.7.5 (python3).
 Writing .funcignore
 Writing .gitignore
 Writing host.json
 Writing local.settings.json
 Writing /Users/estorch/Documents/personal/gitrepo/azure-function-custom-dns-record/FunctionProjTest/.vscode/extensions.json
```

```shell
$ cd FunctionProjTest

$ func new
Select a number for template:
1. Azure Blob Storage trigger
2. Azure Cosmos DB trigger
3. Azure Event Grid trigger
4. Azure Event Hub trigger
5. HTTP trigger
6. Azure Queue Storage trigger
7. Azure Service Bus Queue trigger
8. Azure Service Bus Topic trigger
9. Timer trigger
Choose option: 9
Timer trigger
Function name: [TimerTrigger] CustomDnsRecordFunction
Writing /Users/estorch/Documents/personal/gitrepo/azure-function-custom-dns-record/FunctionProjTest/CustomDnsRecordFunction/readme.md
Writing /Users/estorch/Documents/personal/gitrepo/azure-function-custom-dns-record/FunctionProjTest/CustomDnsRecordFunction/__init__.py
Writing /Users/estorch/Documents/personal/gitrepo/azure-function-custom-dns-record/FunctionProjTest/CustomDnsRecordFunction/function.json
The function "CustomDnsRecordFunction" was created successfully from the "Timer trigger" template
```

```shell
$ func host start 
```

```shell
$ pip3 install azure-mgmt-privatedns
```

#### Azure CLI Command

```shell 
$ az network private-dns record-set list --subscription  --resource-group  --zone-name 
```

#### Azure Functions
https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer

#### Python Function

https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#python-version
https://docs.microsoft.com/en-us/python/api/azure-mgmt-dns/azure.mgmt.dns.dnsmanagementclient?view=azure-python

https://azuresdkdocs.blob.core.windows.net/$web/python/azure-mgmt-privatedns/0.1.0/azure.mgmt.privatedns.operations.html#azure.mgmt.privatedns.operations.RecordSetsOperations

https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate?tabs=bash

#### Deploy with terraform

https://adrianhall.github.io/typescript/2019/10/23/terraform-functions/

https://www.olivercoding.com/2018-06-24-terraform/
https://vgaltes.com/post/deploying-azure-functions-using-terraform/
https://stackoverflow.com/questions/56905696/how-to-import-azure-function-app-in-azure-api-management-using-terraform

#### Python

https://virtualenv.pypa.io/en/latest/user_guide.html#introduction


#### Examples

https://medium.com/@k.giguz/getting-started-with-azure-python-functions-abd4d88706f7

https://github.com/yokawasa/azure-functions-python-samples/tree/master/v2functions/timer-trigger-cosmosdb-output-binding
https://github.com/yokawasa/azure-functions-python-samples/tree/master/v2functions/http-trigger-blob-sas-token

