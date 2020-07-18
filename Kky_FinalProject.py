# # Finding location with ip address/domain name
# # I want to find the location and ISP based on the query of its IP address
# # The information is in an API hence structured in a dictionary format (JSON)
#
# # Importing request module to retrieve data from site and time module to provide current time
# import requests
#
# from time import localtime, strftime
# strftime("%Y-%m-%d %H:%M:%S", localtime())
#
# # These are the URLs that are used to query the location based on IP/Domain
# Url = requests.get("http://ip-api.com/json/ohio.edu")
# Url1 = requests.get("http://ip-api.com/json/google.com")
# Url2 = requests.get("http://ip-api.com/json/stanford.edu")
# Url3 = requests.get("http://ip-api.com/json/mtn.com.gh")
#
# # parse json---convert into python
# data = Url.json()
# data1 = Url1.json()
# data2 = Url2.json()
# data3 = Url3.json()
#print(data)
#
# # Create a class DataRecord with attributes that stores the time and username
# class DataRecord():
#     def __init__(self):
#         self.CreationTime= strftime("%Y-%m-%d %H:%M:%S", localtime())
#         self.Entered_By = ''
#
# # Create subclass to store with attributes that stores IP address, location and ISP
# class Sub_DataRecord(DataRecord):
#
#     def __init__(self, IP_address, IP_addr_location, IP_addr_ISP):
#
#
#         self.IP_address = IP_address
#         self.IP_addr_location = IP_addr_location
#         self.IP_addr_ISP = IP_addr_ISP
#
#     # invoking attributes of parent class in subclass
#         DataRecord.__init__(self)
#
# #get and set data attributes for IP address, Location and ISP
#     def get_ip_address(self):
#         print(self.IP_address)
#
#     def get_IP_addr_location(self):
#         print(self.IP_addr_location)
#
#     def get_IP_addr_ISP(self):
#         print(self.IP_addr_ISP)
#
#     def set_ip_address(self, user_ip_address):
#         self.IP_address = user_ip_address
#
#     def set_IP_addr_location(self, user_IP_addr_location):
#         self.IP_addr_location = user_IP_addr_location
#
#     def set_IP_addr_ISP(self, user_IP_addr_ISP):
#         self.IP_addr_ISP = user_IP_addr_ISP
#
# # create function show data to output the combination of all data fields
#     def ShowData(self):
#         return"IP address: {}, Location:  {}, ISP:  {}, Created By: {}, At: {} ".format(self.IP_address, self.IP_addr_location, self.IP_addr_ISP,username, self.CreationTime)
#
#
# username = input("Enter your name:")
# print('\n Created by',username)
#
# #Create instances for all four querries
# kky = Sub_DataRecord(data['query'],data['city'],data['org'])
# kky1 = Sub_DataRecord(data1['query'], data1['city'], data1['org'])
# kky2 = Sub_DataRecord(data2['query'], data2['city'], data2['org'])
# kky3 = Sub_DataRecord(data3['query'], data3['city'], data3['org'])
# kky.creator = username
# print(kky.CreationTime,'\n')
#
#
# kky.get_ip_address()
# kky.set_ip_address("127.0.0.1")
# kky.ShowData()
#
# kky1.get_ip_address()
# kky1.set_ip_address("40.0.0.1")
# kky1.ShowData()
#
# kky2.get_ip_address()
# #kky2.set_ip_address()
# kky2.ShowData()
#
# kky3.get_ip_address()
# #kky3.set_ip_address()
# kky3.ShowData()
# # # write Data to ABC file
# with open("ABC.txt", "w") as f:
#     f.write(" {}\n".format(kky.ShowData()))
#
#     #f.write(" {}\n {}\n {}\n {}\n".format(kky.ShowData(),kky1.ShowData(), kky2.ShowData(), kky3.ShowData()))
# print(kky.Entered_By)
#


#FINAL PROJECT
# Finding location with ip address/domain name
# I want to find the location of an organisation based on the query of its IP address/domain name
# The information is structured in a dictionary format (JSON)



# Importing request module to retrieve data from site and time module to provide current time
import requests
import json
from string import Template
from time import localtime, strftime
strftime("%Y-%m-%d %H:%M:%S", localtime())
origin =input("Please enter domain name or Ip address (example: ohio.edu/ 8.8.8.8) : ")
#  URL that is used to query the location based on IP/Domain
Ur = Template("http://ip-api.com/json/${oc}")
getreq = Ur.substitute(oc = origin)
print(getreq)
Url = requests.get(url = getreq)

# origin1 =input("Please enter domain name or Ip address (example: ohio.edu/ 8.8.8.8) : ")
# #  URL that is used to query the location based on IP/Domain
# Ur1 = Template("http://ip-api.com/json/${oc}")
# getreq1 = Ur1.substitute(oc = origin1)
# print(getreq1)
# Url1 = requests.get(url = getreq1)
Url1 = requests.get("http://ip-api.com/json/google.com")
Url2 = requests.get("http://ip-api.com/json/stanford.edu")
Url3 = requests.get("http://ip-api.com/json/mtn.com.gh")

# parse json---convert into python
data = Url.json()
data1 = Url1.json()
data2 = Url2.json()
data3 = Url3.json()
print(data)

# Create a class DataRecord with attributes that stores the time and username
class DataRecord():
    def __init__(self):
        self.CreationTime= strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.Entered_By = ''

# Create subclass to store with attributes that stores IP address, location and ISP
class Sub_DataRecord(DataRecord):

    def __init__(self, IP_address, IP_addr_location, IP_addr_ISP):
        self.IP_address = IP_address
        self.IP_addr_location = IP_addr_location
        self.IP_addr_ISP = IP_addr_ISP

# Invoking attributes of parent class in subclass
        DataRecord.__init__(self)

#get and set data attributes for IP address, Location and ISP
    def get_ip_address(self):
        print(self.IP_address)

    def get_IP_addr_location(self):
        print(self.IP_addr_location)

    def get_IP_addr_ISP(self):
        print(self.IP_addr_ISP)

    def set_ip_address(self, user_ip_address):
        self.IP_address = user_ip_address

    def set_IP_addr_location(self, user_IP_addr_location):
        self.IP_addr_location = user_IP_addr_location

    def set_IP_addr_ISP(self, user_IP_addr_ISP):
        self.IP_addr_ISP = user_IP_addr_ISP

# create function show data to output the combination of all data fields
    def ShowData(self):
        return"IP address: {}, Location: {}, ISP: {}, Created By: {}, At: {} ".format(self.IP_address, self.IP_addr_location, self.IP_addr_ISP, username, self.CreationTime)

#Main code
username = input("Enter your name:")
print('\n Created by',username)

# Create instances for the queries
# note: files were in json format meaning stored in a dictionary format, hence the keys are used to get values for each record
kky = Sub_DataRecord(data['query'],data['city'],data['org'])
kky1 = Sub_DataRecord(data1['query'], data1['city'], data1['org'])
kky2 = Sub_DataRecord(data2['query'], data2['city'], data2['org'])
kky3 = Sub_DataRecord(data3['query'], data3['city'], data3['org'])
kky.creator = username
kky.get_ip_address()

# eg. change the original ip and set ip address to this ip
kky.set_ip_address("127.0.0.1")
kky.ShowData()


kky1.get_ip_address()
kky1.set_ip_address("40.0.0.1")
kky1.ShowData()

kky2.get_ip_address()
#kky2.set_ip_address()
kky2.ShowData()

kky3.get_ip_address()
#kky3.set_ip_address()
kky3.ShowData()

# write data to a file called ABC.txt
with open("ABC.txt", "w") as f:
    f.write(" {}\n {}\n {}\n {}\n".format(kky.ShowData(), kky1.ShowData(), kky2.ShowData(), kky3.ShowData()))
    print(kky.Entered_By)
