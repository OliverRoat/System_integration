import uvicorn

def main():
    uvicorn.run("01_Text-based_Data_Formats.01a_Data_Parsing.python.server:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()