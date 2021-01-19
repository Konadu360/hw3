"""
using the ncclient module fuction(manager) to access cisco ios-xe router.
The manger module in ncclient establishes a persistent connection to the device
we will also leverage on the xmltodict module to convert the 
xml data to a dict string and use the json module to parse the data
to python dict

"""
# import modules ncclient,json, xmltodict, and pprint
import json,xmltodict,pprint
from ncclient import manager

# store router info and auth details in a dict
router={"IP": "10.10.20.48", "PORT": 830, "NAME": "developer","PASS": "C1sco12345"}
# router = {
#              "IP": "ios-xe-mgmt.cisco.com",
#              "PORT": 10000,
#              "NAME": "developer",
#              "PASS": "C1sco12345"
#            }
# construct a sample xml filter and pass as a parameter to get the interface info
get_filter="""
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
             <name>GigabitEthernet1</name>
            </interface>
            <interface>
             <name>GigabitEthernet2</name>
            </interface>
            <interface>
             <name>GigabitEthernet3</name>
            </interface>
         </interfaces>
    </filter>
    """

# using the connect function in manager module, pass params such as hostname, port and auth details
device=manager.connect(host=router["IP"],port=router["PORT"],username=router["NAME"],password=router["PASS"],hostkey_verify=False, look_for_keys=False)

# retrieve interface configs,parse the xml data to dict and
# print interface
response=device.get_config('running',get_filter)

xml_to_dict=xmltodict.parse(response.xml)
pprint.pprint(xml_to_dict)
# pprint.pprint(xml_to_dict['rpc-reply']['data']['interfaces']['interface'][0]['name']['#text'])
"""
or we can parse the ordered dict to json, loop over it to print all interfaces
# """
jason=json.loads(json.dumps(xml_to_dict))
print('Interface Details:')
print('---------------------')
for interface in jason['rpc-reply']['data']['interfaces']['interface']:
    print('{}:{}'.format('Name',interface['name']['#text']))
    print('{}:{}\n'.format('Description',interface['description']))
  
    # print('{}:{}'.format("Address",interface['ipv4']['address']['ip']))
    # interface['ipv4']['address']['netmask'])))
    # print('{}:{}\n'.format('Type',interface['type']['#text']))



