# This function basically just wraps the built in json.dump 
# function while also closing the file.
import json

def to_json_file(export_file, users):
    json.dump(users, export_file, indent=4)
    export_file.close()