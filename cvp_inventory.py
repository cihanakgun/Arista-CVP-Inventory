#__author__ = 'Cihan AKGUN'
#cihan.akgun@gmail.com
from cvprac.cvp_client import CvpClient
from cvprac.cvp_api import CvpApi
import urllib3
import ssl
import argparse
from getpass import getpass
import pprint


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True)
args = parser.parse_args()
switchuser = args.username

switchpass = getpass()

ip_list = []
inventory = []
cvp = ['192.168.1.10','192.168.1.11','192.168.1.14']
clnt = CvpClient()

for x in cvp:
    clnt.connect([x], switchuser, switchpass)
    clntapi = CvpApi(clnt)
    local_inventory = clntapi.get_inventory()
    for z in local_inventory:
        inventory.append(z)


for device in inventory:
    ip_list.append(device['ipAddress'])

print (ip_list)
