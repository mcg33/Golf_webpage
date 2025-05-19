'''
This script loads a JSON database from a file and returns the data as a Python dictionary.
'''
import json

def load_db(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

db = load_db('fake_db.json')