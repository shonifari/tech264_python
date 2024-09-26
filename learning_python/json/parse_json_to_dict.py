# Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
# You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
# Make sure you get your head around what your code does + add your own comments to explain each part of the code
#
#
# Steps:
#
# Create a new file servers.json and add this JSON to it:
#
# {
# 	"server1": {
# 		"hostname": "web-server-1",
# 		"ip_address": "192.168.1.1",
# 		"role": "web",
# 		"status": "active"
# 	},
# 	"server2": {
# 		"hostname": "db-server-1",
# 		"ip_address": "192.168.1.2",
# 		"role": "database",
# 		"status": "maintenance"
# 	}
# }
# Create a file called parse_json_to_dict.py and add code to it to: Steps:
#
# Use 'with' to open the file created above
import json

with open("servers.json","rb") as f:
    # Parse contents the JSON file into a Python dictionary named "servers"
    servers = json.loads(f.read())
#
# Print out the type of "servers"
print(type(servers))

# Print out the dictionary record with the key "server1"
print(servers.get('server1'))
# Print out the dictionary record with the key "server2"
print(servers.get('server2'))


# Print all of the keys and values. Output should be:


for k,v in servers.items():
    print(f"Key and value: '{k}' = '{v}'")

    for subk, subv in v.items():
        print(f"Record key and sub value: '{subk}' = '{subv}'")

# Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
#   Record key and sub value: 'hostname' = 'web-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.1'
#   Record key and sub value: 'role' = 'web'
#   Record key and sub value: 'status' = 'active'
# Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
#   Record key and sub value: 'hostname' = 'db-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.2'
#   Record key and sub value: 'role' = 'database'
#   Record key and sub value: 'status' = 'maintenance'
# Extra guidance:
# Use Gen AI (ChatGPT or Google Gemini) to help speed up these tasks as much as you need to