#!/usr/bin/python3

from datetime import datetime
import requests
import configparser
from optparse import OptionParser

optionParser = OptionParser()
optionParser.add_option("-c", "--config", dest="config_filename", help="Config file", metavar="FILE")
(options, args) = optionParser.parse_args()

configParser = configparser.ConfigParser()
configParser.read(options.config_filename)
config = configParser['cloudflare']

content = [
	'# https://www.cloudflare.com/ips',
	'# Updated: {:%d.%m.%Y %H:%M:%S}'.format(datetime.now()),
	''
]

request = requests.get(config['ipv4'])
for line in request.iter_lines():
	content.append('set_real_ip_from %s;' % line.decode('utf-8'))
content.append('')

request = requests.get(config['ipv6'])
for line in request.iter_lines():
	content.append('set_real_ip_from %s;' % line.decode('utf-8'))
content.append('')

content.append('real_ip_header CF-Connecting-IP;')

with open(config['output'], 'w') as file:
	file.writelines(map(lambda item: item + '\n', content))
	file.close()
