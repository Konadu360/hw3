import re,string, pprint
# with open('sampleconfig.cfg', 'r') as f:
#     configfile=f.read()
# # print(configfile)

# regen='(?sm)interface (\S*)(?:(?!^!$).)*service-policy.input.WIRELESS_IN.*?!$'
# data = re.findall(regen, configfile)
# print(data)


with open("crr01euclwi_LS_final_v5.cfg", "r") as f:

    config=f.read().splitlines("!")
print(config)

# regen='(?sm)interface (\S*)(?:(?!^!$).)*service-policy.output.QSP-ALL-CORE-PROTECTED-OUT.*?!$'

# regen1='(?sm)interface (\S*)(?:(?!^!$).)*ipv4.access-group.DMCA_REDIRECT_IPV4_FILTER ingress.*?!$'
# regen2='(?sm)interface (\S*)(?:(?!^!$).)*metric.100.*?!$'

# data = re.findall(regen, config)
# data1=re.findall(regen1, config)
# data2=re.findall(regen2, config)
# print(data,"\n\n", data1, "\n\n", data2)




# f = open("sampleconfig.cfg")
# cfgdata = f.read()
# print(cfgdata)
# pat=re.compile('(interface.*?)!$',re.DOTALL|re.M)
# pat2 = re.compile("service-policy.input.WIRELESS-IN")

# data = pat.findall(cfgdata)
# i=0
# while i < len(data):
#     if  pat2.findall(data[i]):
#         print (data[i].split("\n")[0])
#         i = i+1

#     else:
#         i = i+1
#         pass