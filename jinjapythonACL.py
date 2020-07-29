#Import ipaddress Standard Library
import ipaddress

#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader
 
#Import YAML from PyYAML
import yaml
 
#Load data from YAML file into Python dictionary and modify
config = yaml.full_load(open('acldata.yml'))
print(config)
for ace in config['aces']:
    if 'network' in ace:
        myip = ipaddress.IPv4Network(ace['network'])
        ace['network'] = str(myip.network_address) + ' ' + str(myip.hostmask)

#Load Jinja2 template and work through conditionals
env = Environment(loader = FileSystemLoader(''), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('acltemplate.j2')
print()

#Render template using data and print the output
print('Access List:')
print(template.render(config))