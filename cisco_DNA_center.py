"""
 below code is used to access the cisco DNA platform to print details of devices
 on the platform. yhe cisco DNA center is used to manage network devices or sort of work as a management
 platform to manage all devices on the network
 name: kwasi yiadom konadu
 email: konaduyiadom360@gmail.com

"""
# import modules requesrs, urllib3, json,pprint to execute 
import requests,urllib3,json,pprint

if __name__ == "__main__":

    # initialize variables to store headers and login details
    headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
    }
    dnac={
        "username": "devnetuser",
        "password": "Cisco123!",
        "host": "sandboxdnac.cisco.com",
        "port": 443
    }

    # define urls to download token and also access the platform
    # call the urllib3 module to disable insecurerequestwarning

    url_token="https://{}:{}/dna/system/api/v1/auth/token".format(dnac['host'],dnac['port'])
    url_device="https://{}/dna/intent/api/v1/network-device".format(dnac['host'])
    url_intf="https://{}/dna/intent/api/v1/interface".format(dnac['host'])
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # retrieve the token using the requests module by parsing info such as headers and auth
    # store the token in the headers dictionary as x-auth-token
    response_token=requests.post(url_token,headers=headers,auth=(dnac['username'],dnac['password']),verify=False)
    authen=json.loads(response_token.text)
    headers['x-auth-token']=authen['Token']
    # pprint.pprint(headers)

    #parse the headers to the request module and download network devices
    # parse the retrieve data to python dict and store in a variable device
    response_device=requests.get(url_device,headers=headers,verify=False)
    device=json.loads(response_device.text)
    dnac['network_device_id']=device['response'][0]['id']

    #get interfaces of each network device
    response_intf=requests.get(url_intf,headers=headers,verify=False)
    interfaces=json.loads(response_intf.text)

    #get specific device based on its id
    url_dev1="https://{}/dna/intent/api/v1/interface/network-device/{}".format(dnac['host'],dnac['network_device_id'])
    response_dev1=requests.get(url_dev1,headers=headers,verify=False)
    
    # loop through the stored data and print hostname, family ip addr, etc
    details=device['response']
    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format('HOSTNAME','FAMILY', "MANAGEMENT IP ADDR", 'ROLE', "PLATFORM-ID","SOFTWARE VERSION", 'UP TIME'))
    for items in details:
        print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(items['hostname'],items['family'],items['managementIpAddress'], items['role'], items['platformId'], items['softwareVersion'],items['upTime']))
    print('\n\n')

    url_topo='https://sandboxdnac.cisco.com/dna/intent/api/v1/topology/l3/OSPF'
    repo=requests.get(url_topo,headers=headers,verify=False)
    response_topo=json.loads(repo.text)
    pprint.pprint(response_topo)
    # intf_details=interfaces['response']
    # print('{:<20} {:<20}'.format('PID','PORT-NAME'))
    # for intfd in intf_details:
    #     print('{:<20} {:<20}'.format(intfd['pid'],intfd['portName']))
    # print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format('PID','PORT-NAME', "IP ADDR", 'INTF_TYPE', "VLAN-ID","STATUS", 'MAC-ADDR'))
    # for intfd in intf_details:
    #     print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(intfd['pid'],intfd['portName'],intfd['ipv4Address'], intfd['interfaceType'], intfd['vlanId'], intfd['status'],intfd['macAddress']))
   
    dev1=json.loads(response_dev1.text)
    dev1_intf=dev1['response']
    print('{:<20} {:<20}'.format('PID','PORT-NAME'))
    for intfd in dev1_intf:
        print('{:<20} {:<20}'.format(intfd['pid'],intfd['portName']))
