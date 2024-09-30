# In groups of 2-3, create a script that converts Valid JSON to Valid YAML.
#
# Create a new Python file json2yaml.py for this task.
#
# Valid JSON:

# {
#   "name": "John Doe",
#   "age": 30,
#   "isStudent": false,
#   "courses": ["Python", "DevOps"],
#   "address": {
#     "street": "123 Main St",
#     "city": "Anytown"
#   }
# }
#
# Valid YAML:
#
# name: John Doe
# age: 30
# isStudent: false
# courses:
#   - Python
#   - DevOps
# address:
#   street: 123 Main St
#   city: Anytown
#
# Starting code:

import json
import os
import sys
import yaml



# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json_folder> <target_file.yaml>")



with (open(sys.argv[1], "r") as json_file):
    json_data = json.load(json_file)

    # 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
    if not len(sys.argv) > 2:
        yaml_obj = yaml.dump(json_data)
        print(yaml_obj)
        exit(0)

    # 2.2 Check the target file doesn't already exist
    if  os.path.exists(sys.argv[2]):
        print("Path already exists")

    else:
        # 2.3 If previous conditions not met, then save YAML file
        with open(sys.argv[2], "w") as yaml_file:
            yaml.dump(json_data, yaml_file)





