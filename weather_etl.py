import os
from datetime import datetime
import pandas as pd
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env
load_dotenv()

# EXTRACT
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITIES = ["New York", "London", "Tokyo", "Sydney", "Mumbai"]

raw_data = []
print("Extracting data...")
for city in CITIES:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        raw_data.append(response.json())
    else:
        print(f"Failed to fetch data for {city} (Status: {response.status_code})")

# TRANSFORM
print("Transforming data...")
clean_data = []

for data in raw_data:
    clean_data.append({
        "city": data["name"],
        "temperature_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_condition": data["weather"][0]["description"],
        "timestamp": datetime.now(),
    })

df = pd.DataFrame(clean_data)
print(df.head())

# LOAD 
print("Loading to PostgreSQL...")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

df.to_sql("daily_weather", engine, if_exists="append", index=False)
print("ETL Pipeline completed successfully!")