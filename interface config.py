import jinja2,yaml

def configure_interfaces(interfaces):
    print(f"Configuring interfaces:{interfaces}")

#load yaml file with interface data
    with open('interfaces.yaml', 'r') as yaml_file:
        interfaces_data = yaml.safe_load(yaml_file)

#load jinja template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('interface_template.j2')


#Iterate through interfaces and configure
for interface in interface_data['interfaces']:
    config = template.render(interface - interface)
    configure_interfaces(config)


    