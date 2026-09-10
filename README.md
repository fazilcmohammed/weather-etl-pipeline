# Automated Weather Data ETL Pipeline 🌦️

## Overview
An end-to-end Data Engineering pipeline that automatically extracts live weather data for global cities, transforms the JSON payloads into structured formats, and loads the cleaned data into a relational database for downstream analytics. 

This project demonstrates core ETL concepts, API integration, data modeling, and automated task scheduling.

## 🏗️ Architecture & Data Flow
1. **Extract:** Python script calls the OpenWeatherMap REST API to fetch real-time climate data for New York, London, Tokyo, Sydney, and Mumbai.
2. **Transform:** Raw nested JSON data is flattened and cleaned using Pandas. Timezones are standardized, and unneeded metadata is filtered out.
3. **Load:** The structured DataFrame is loaded into a local PostgreSQL database using SQLAlchemy.
4. **Orchestrate:** The pipeline is scheduled to run autonomously every day at 9:00 AM using Windows Task Scheduler (with fault tolerance enabled for missed runs).

## 🛠️ Technology Stack
* **Language:** Python 3
* **Libraries:** `pandas`, `requests`, `SQLAlchemy`, `psycopg2-binary`, `python-dotenv`
* **Database:** PostgreSQL
* **Orchestration:** Windows Task Scheduler
* **Version Control:** Git & GitHub

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YourUsername/weather-etl-pipeline.git](https://github.com/YourUsername/weather-etl-pipeline.git)
cd weather-etl-pipeline
```
### 2. Install dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```
### 3. Configure Database and API Keys
This project uses .env files to keep credentials secure. Create a .env file in the root directory. Use the provided .env.example as a template:
```bash
API_KEY=your_openweathermap_api_key_here
DB_PASS=your_postgres_password_here
```
### 4. Database Setup
Ensure PostgreSQL is running locally on port 5432 and create a database named weather_db. The script will automatically create the daily_weather table on its first run.

### 5. Execute the Pipeline
```bash
python weather_etl.py
```
### Future Enhancements
[ ] Containerization: Wrap the application and database in Docker for easier deployment.

[ ] Cloud Migration: Host the database on AWS RDS and run the script via AWS Lambda or EC2.

[ ] Advanced Orchestration: Migrate the scheduling from Task Scheduler to Apache Airflow.
