# from jinja2 import Environment, FileSystemLoader
# Env=Environment(loader=FileSystemLoader('.'))
# template=Env.get_template('template.j2')
# interface_dict={'name':'GigabitEthernet0/1','description':'Server Port','vlan':10,'uplink':False,}
# print(template.render(interface=interface_dict))

# print('\n')
# # USING CLASS TO ACHIEVE THE SAME GOAL
# # class NetworkInterface(object):
# #     def __init__(self,name,description,vlan,uplink=True):
# #         self.name=name
# #         self.description=description
# #         self.vlan=vlan
# #         self.uplink=uplink
# # interface_obj=NetworkInterface('GigabitEthernet0/1','Server Port',10)
# # print(template.render(interface=interface_obj))

# # USING LIST STRTEGY
# # -----------------------
# from jinja2 import Environment, FileSystemLoader
# Env=Environment(loader=FileSystemLoader('.'))
# template=Env.get_template('template2.j2')
# intlist=['GigabitEthernet0/1','GigabitEthernet0/2','GigabitEthernet0/3','GigabitEthernet0/4']
# print(template.render(interface_list=intlist))


# # USING DICT STRTEGY
# #  -----------------------
# from jinja2 import Environment, FileSystemLoader
# Env=Environment(loader=FileSystemLoader('.'))
# template=Env.get_template('template3.j2')
# intdict={'GigabitEthernet0/1':'server port one','GigabitEthernet0/2':'server port two','GigabitEthernet0/3':'server port three','GigabitEthernet0/4':'server port four'}
# print(template.render(inter_dict=intdict))


# # USING LIST OF DICT STRTEGY
# #  -----------------------
# from jinja2 import Environment, FileSystemLoader
# Env=Environment(loader=FileSystemLoader('.'))
# template=Env.get_template('template4.j2')
# interfaces=[
#     {'name':'GigabitEthernet0/1',
#     'desc':'uplink port',
#     'uplink':True,
#     },
#     {
#     'name':'GigabitEthernet0/2',
#     'desc':'server port two',
#     'vlan':'10'
#     },
#     {
#     'name':'GigabitEthernet0/3',
#     'desc':'server port three',
#     'vlan':'10'
#     },
#     {
#     'name':'GigabitEthernet0/4',
#     'desc':'server port four',
#     'vlan':'10'
#     }
# ]
# print(template.render(interface_list=interfaces))
    


#importing yaml into the code
# from jinja2 import Environment, FileSystemLoader
# import yaml
# Env=Environment(loader=FileSystemLoader('.'))
# template=Env.get_template('template4.j2')
# with open('example1.yml') as f:
#     data = yaml.load(f,yaml.SafeLoader)
#     print(data)
#     print(template.render(interface_list=data))




# CREATING CUSTOM FILTERS

#importing yaml into the code
# from jinja2 import Environment, FileSystemLoader
# import yaml
# Env=Environment(loader=FileSystemLoader('.'))
# def get_interface_speed(interface_name):
#     if 'gigabit' in interface_name.lower():
#         return 1000
#     if 'fast' in interface_name.lower():
#         return 100
# Env.filters['get_interface_speed']=get_interface_speed
# template=Env.get_template('template4.j2')
# with open('example1.yml') as f:
#     data = yaml.load(f,yaml.SafeLoader)
#     print(data)
#     print(template.render(interface_list=data))


# USING EXISTING PYTHON CODE 
# from jinja2 import Environment, FileSystemLoader
# from bracket_expansion import bracket_expansion
# Env=Environment(loader=FileSystemLoader('.'))
# Env.filters['bracket_expansion']=bracket_expansion
# template=Env.get_template('template.j2')

# print(template.render(iface_pattern='GigabitEthernet0/0/[0-3]'))



# TEMPLATE INHERITAN JINJA
#importing yaml into the code
from jinja2 import Environment, FileSystemLoader
import yaml
Env=Environment(loader=FileSystemLoader('.'))
def get_interface_speed(interface_name):
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
Env.filters['get_interface_speed']=get_interface_speed
template=Env.get_template('vlanstemp.j2')
with open('example1.yml') as f:
    data = yaml.load(f,yaml.SafeLoader)
    print(data)
    print(template.render(interface_list=data))
