import requests

api_key = "72bc7d2410d6afc7d9a2501574352ccd"


def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    filter_data = filter_data[:8*forecast_days]
    if kind == "Temperature":
        filter_data = [dict["main"]["temp"] for dict in filter_data]
    if kind == "Sky":
        filter_data = [dict["weather"][0]["main"] for dict in filter_data]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))
