
"""
this code is used to access network devices on cisco DNA center 
and print detail info such as, ip addr, intf type etc
copyright konaduyiadom kwasi
email konaduyiadom360@gmail.com
"""

#import relevant libraries to execute the code
import json,pprint,urllib3,requests, argparse
from device_info import dnac


#store header information to parsed in the REST-API request
headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
        }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#define function to download authentication token 
def login_token(hostname,port,user,passwd):
    #use the REST-API to request for the token
    #use json loads to parse the return data into dictionary and return Token
    token_url="https://{}:{}/dna/system/api/v1/auth/token".format(hostname,port)
    token_request=requests.post(token_url,auth=(user,passwd),headers=headers,verify=False)
    token_response=json.loads(token_request.text)
    return token_response['Token']

#define code to download network devices in the DNA center
def network_device(hostid,portid,auth_token):
    #store the return token in the headers dict
    #use the REST-API to download the device list by parsing it through the request module
    device_url="https://{}:{}/dna/intent/api/v1/network-device".format(hostid,portid)
    headers["x-auth-token"]=auth_token
    device_request=requests.get(device_url,headers=headers,verify=False)
    device_list=json.loads(device_request.text)
    return device_list["response"]


#main program to execute 
if __name__ == "__main__":
    #take source and destination ip from the command line
    parser=argparse.ArgumentParser()
    parser.add_argument("source_ip",help="source_ip_address")
    parser.add_argument("destination_ip", help="destination_ip_address")
    arg=parser.parse_args()

    #store the source and destination ip address from the command line
    source_ip_addr=arg.source_ip
    destination_ip_addr=arg.destination_ip

    #print information
    print("source ip: {}".format(source_ip_addr))
    print("destination ip: {}".format(destination_ip_addr))

    #call the function to parse login details and store in variables auth_token and net_device
    auth_token=login_token(dnac['host'],dnac['port'],dnac['username'],dnac['password'])
    net_device=network_device(dnac['host'],dnac['port'],auth_token)

    #loop through the net_device and print details
    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format('HOSTNAME','FAMILY', "MANAGEMENT IP ADDR", 'ROLE', "PLATFORM-ID","SOFTWARE VERSION", 'UP TIME'))
    for items in net_device:
        print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(items['hostname'],items['family'],items['managementIpAddress'], items['role'], items['platformId'], items['softwareVersion'],items['upTime']))
    print('\n\n')