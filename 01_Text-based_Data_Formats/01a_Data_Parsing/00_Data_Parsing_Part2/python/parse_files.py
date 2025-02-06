import csv
import json
import yaml
import xml.etree.ElementTree as ET
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def parse_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def parse_json(file_path):
    with open(file_path, mode='r') as file:
        return json.load(file)

def parse_yaml(file_path):
    with open(file_path, mode='r') as file:
        return yaml.safe_load(file)

def parse_xml(file_path):
    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child):
                parsed_data[child.tag] = parse_element(child)
            else:
                if child.tag in parsed_data:
                    if isinstance(parsed_data[child.tag], list):
                        parsed_data[child.tag].append(child.text)
                    else:
                        parsed_data[child.tag] = [parsed_data[child.tag], child.text]
                else:
                    parsed_data[child.tag] = child.text
        return parsed_data

    tree = ET.parse(file_path)
    root = tree.getroot()
    return parse_element(root)

def parse_txt(file_path):
    with open(file_path, mode='r') as file:
        return file.read()

if __name__ == "__main__":
    csv_data = parse_csv('me.csv')
    json_data = parse_json('me.json')
    yaml_data = parse_yaml('me.yaml')
    xml_data = parse_xml('me.xml')
    txt_data = parse_txt('me.txt')

    print("CSV Data:", csv_data)
    print("JSON Data:", json_data)
    print("YAML Data:", yaml_data)
    print("XML Data:", xml_data)
    print("TXT Data:", txt_data)