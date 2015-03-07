import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from ebaysdk.finding import Connection as Finding
from ebaysdk.shopping import Connection as Shopping
from ebaysdk.exception import ConnectionError


try:
    api = Finding(config_file='ebay.yaml')
    response = api.execute('findCompletedItems', {'keywords': 'iphone 5c', 'paginationInput' : {'entriesPerPage ': 2}})
    print(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())

# try:
#     api = Finding(config_file='ebay.yaml')
#     response = api.execute('findItemsAdvanced', {'keywords': 'iphone 5c', 'paginationInput' : {'entriesPerPage ': 2}})
#     print(response.dict())
# except ConnectionError as e:
#     print(e)
#     print(e.response.dict())

# try:
#     api = Shopping(config_file='ebay.yaml')
#     api_request = {
#       'ItemID': '400834335122',
#       # 'IncludeSelector': 'Details'
#     }
#     response = api.execute('GetSingleItem', api_request)
#     print(response.dict())
#     if api.error():
#         print(api.error())
# except ConnectionError as e:
#     print(e)
#     print(e.response.dict())
