import requests
api_key = "9155f6fce577271e892256723e6e062f"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Ho Chi Minh"
# def fetch_data():
#     print("fetching weather data from WeatherStack API ...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("API Response successfully")
#         return response.json()
#     except Exception as e:
#         print("An error occurred")
#         raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Ho Chi Minh City, Vietnam', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Ho Chi Minh City', 'country': 'Vietnam', 'region': '', 'lat': '10.750', 'lon': '106.667', 'timezone_id': 'Asia/Ho_Chi_Minh', 'localtime': '2025-07-16 18:49', 'localtime_epoch': 1752691740, 'utc_offset': '7.0'}, 'current': {'observation_time': '11:49 AM', 'temperature': 26, 'weather_code': 296, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0033_cloudy_with_light_rain_night.png'], 'weather_descriptions': ['Light Rain'], 'astro': {'sunrise': '05:39 AM', 'sunset': '06:20 PM', 'moonrise': '10:33 PM', 'moonset': '10:12 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 72}, 'air_quality': {'co': '1024.9', 'no2': '39.96', 'o3': '100', 'so2': '39.59', 'pm2_5': '59.2', 'pm10': '61.42', 'us-epa-index': '3', 'gb-defra-index': '3'}, 'wind_speed': 13, 'wind_degree': 225, 'wind_dir': 'SW', 'pressure': 1007, 'precip': 0.6, 'humidity': 89, 'cloudcover': 75, 'feelslike': 28, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}


if __name__ == '__main__':
    # fetch_data()
    mock_fetch_data()