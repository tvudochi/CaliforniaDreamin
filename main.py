from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from config.settings import DATA
from src.request_csv import read_csv


hot = FastAPI()

@hot.get("/hot")
def get_json():
    df = read_csv(DATA)
    df_json = df.to_json(orient='records')  # List of dicts
    json_list = json.loads(df_json)  # Conversion : str --> JSON object
    return JSONResponse(content=json_list)

