# Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
# You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
# Make sure you get your head around what your code does + add your own comments to explain each part of the code
#
#
# Steps:
#
# Create version of parse_json_to_dict.py but for parsing/converting YAML to a dictionary

### 1. Parsing/Converting YAML to a Dictionary
import yaml

def parse_yaml_to_dict(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Example usage
yaml_file = 'example.yaml'
data_dict = parse_yaml_to_dict(yaml_file)
print(data_dict)

### 2. Validating a YAML File
import  yaml
def validate_yaml_file(yaml_file):
    try:
        with open(yaml_file, 'r') as file:
            yaml.safe_load(file)
        print(f"{yaml_file} is a valid YAML file.")
    except Exception as exc:
        print(f"{yaml_file} is not a valid YAML file. Error: {exc}")

# Example usage
json_file = 'C:\\Users\\omoto\\OneDrive\\Documents\\Github\\tech264_python\\learning_python\\yaml\\student.json'
yaml_file = 'C:\\Users\\omoto\\OneDrive\\Documents\\Github\\tech264_python\\learning_python\\yaml\\student.yaml'
validate_yaml_file(yaml_file)



### 3. YAML to JSON File Conversion Script
import json
import yaml

def convert_yaml_to_json(yaml_file, json_file):

    with open(yaml_file, 'r') as y_file:
        data = yaml.safe_load(y_file)

    with open(json_file, 'w') as j_file:
        json.dump(data, j_file, indent=4)


json_file = 'C:\\Users\\omoto\\OneDrive\\Documents\\Github\\tech264_python\\learning_python\\yaml\\student.json'
yaml_file = 'C:\\Users\\omoto\\OneDrive\\Documents\\Github\\tech264_python\\learning_python\\yaml\\student.yaml'
convert_yaml_to_json(yaml_file, json_file)




### 4. Check if an Entire Folder's Contents are Valid YAML
import os
def validate_yaml_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as file:
                    yaml.safe_load(file)
                print(f"{filename} is a valid YAML file.")
            except yaml.YAMLError as exc:
                print(f"{filename} is not a valid YAML file. Error: {exc}")

# Example usage
folder_path = 'path/to/your/folder'
validate_yaml_folder(folder_path)


# Create version of validate_json_file.py but for checking a YAML file
# Create a YAML to JSON file conversion script
# If time (leave until last): Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)
#
# Helpful documentation:
#
# JSON Documentation: json_folder — JSON encoder and decoder — Python 3.12.6 documentation
# Pyyaml Documentation: pyyaml.org/wiki/PyYAMLDocumentation
#
# Post a link to these exact tasks in the chat at COB