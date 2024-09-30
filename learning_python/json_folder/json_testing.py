# Research:
#
# What is encoding vs serialising (very quick, two or three dot points to understand the difference)
# Work out which one of them are you doing with the subtasks below
# Starting code:
import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
# Subtasks:
#
# Convert this Python dictionary into a JSON-formatted string
import json
json_string = json.dumps(servers_dict)

# Convert dictionary to JSON and save to a file
with open('servers.json', 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)

# Read the file to verify the conversion
with open('servers.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)  # Print to verify the content
# Extra guidance:
#
# Use the json library
# Write any other code necessary to test things converted correctly
# Use Gen AI (ChatGPT or Google Gemini) to help speed up these tasks as much as you need to.  However what's important is that:
# You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
# Add your own comments to explain each part of the code
