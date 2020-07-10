#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader
 
#Import YAML from PyYAML
import yaml
 
#Load data from YAML file into Python dictionary
config = yaml.full_load(open('acldata.yml'))
print(config)

#Load Jinja2 template
env = Environment(loader = FileSystemLoader(''), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('acltemplate.j2')
print()
#Render template using data and print the output
print('Access List:')
print(template.render(config))

