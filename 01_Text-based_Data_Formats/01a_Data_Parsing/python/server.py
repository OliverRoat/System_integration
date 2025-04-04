import os
import sys
import xml.etree.ElementTree as ET
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
import yaml
import httpx

# Add the directory containing parse_files.py to the sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))

from parse_files import parse_csv, parse_json, parse_yaml, parse_xml, parse_txt

app = FastAPI()

# Change directory to the location of the data files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

SERVER_A_URL = "http://localhost:5194"

@app.get("/csv")
def get_csv():
    data = parse_csv('me.csv')
    csv_content = "\n".join([",".join(str(value) if value is not None else "" for value in row.values()) for row in data])
    return PlainTextResponse(content=csv_content, media_type="text/plain")

@app.get("/json")
def get_json():
    data = parse_json('me.json')
    return JSONResponse(content=data)

@app.get("/yaml")
def get_yaml():
    data = parse_yaml('me.yaml')
    yaml_content = yaml.dump(data)
    return PlainTextResponse(content=yaml_content, media_type="text/plain")

@app.get("/xml")
def get_xml():
    data = parse_xml('me.xml')
    xml_content = ET.tostring(ET.Element("root", data), encoding='unicode')
    return PlainTextResponse(content=xml_content, media_type="application/xml")

@app.get("/txt")
def get_txt():
    data = parse_txt('me.txt')
    return PlainTextResponse(content=data, media_type="text/plain")

@app.get("/proxy/{file_type}")
async def proxy_to_server_a(file_type: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SERVER_A_URL}/DataParsing/{file_type}")
        if response.headers.get("content-type") == "application/json":
            return JSONResponse(content=response.json())
        else:
            return PlainTextResponse(content=response.text, media_type=response.headers.get("content-type"))
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)