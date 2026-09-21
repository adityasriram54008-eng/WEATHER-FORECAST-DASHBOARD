import requests

API_KEY = "875e82edf31411c4c2f99ea5d8c73577"

def get_data(place, forecast_days = None, type = None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]

    if type == "Temperature":
        filtered_data = [dic["main"]["temp"] for dic in filtered_data]
    if type == "Sky":
        filtered_data = [dic["weather"][0]["main"] for dic in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place = "Tokyo"))
