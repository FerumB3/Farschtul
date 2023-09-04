import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def get_temperature():
    r = requests.get = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2"
    response = requests.get(requests)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find("span", class_="temperature").text.strip()
        return temperature
    else:
        print("не змогли отримати данні")
        return None

def insert_data(date_time, temperature):
    conn = sqlite3.connect("weather_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS weather (date_time DATETIME, temperature TEXT)")
    cursor.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (date_time, temperature))
    conn.commit()
    conn.close()

current_date_time = datetime.now().strftime;

temperature = get_temperature()

if temperature:
    insert_data(current_date_time, temperature)
    print(f"данні добавлені у базу данних: {current_date_time}, Температура: {temperature}")
else:
    print("Не змогли знайти данні.")