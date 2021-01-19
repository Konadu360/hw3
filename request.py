# using the request module to get interface info of a cisco IOS-XE router
# import libraries, request, json and pprint
import requests, json, pprint, urllib3

# store router info, user access details and headers in a dict
router={
        "IP": "10.10.20.48",
        "PORT": 443,
        "name": "developer",
        "pass": "C1sco12345"
    }
header={
        "accept": "application/yang-data+json", 
        "Content-Type": "application/yang-data+json"
    }       

# define the url and insert router details 

url='https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet2'
url=url.format(router["IP"],router["PORT"])
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print(url)


# using the request module, get the interface GigabitEthernet1 info
# parse the json data into a python dict and print the info out
req=requests.get(url,auth=(router["name"],router["pass"]),headers=header,verify=False)
response=json.loads(req.text)
pprint.pprint(response['Cisco-IOS-XE-interfaces-oper:interface']['name'])
