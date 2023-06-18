import requests
from geopy.geocoders import Nominatim
import re
import sys

# ANSI escape sequences for text colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
ORANGE = '\033[38;5;208m'
RED = '\033[91m'
END_COLOR = '\033[0m'


def fetch_weather(latitude, longitude):
    # OpenWeatherMap API key
    api_key = '57c253ebd9ce680670bdf985084fd8eb'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        temperature -= 273.15  # Convert K -> C
        humidity = data['main']['humidity']
        return temperature, humidity

    return None, None


def convert_location_to_coordinates(location_name):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location_name, exactly_one=False)

    if location:
        return [(loc.latitude, loc.longitude, f"{loc.address.split(',')[0]}, {loc.address.split(',')[-2].strip()}, {loc.address.split(',')[-1].strip()}") for loc in location]

    return []


def display_city_options(city_options):
    print("\nMultiple cities found with the same name. Please select the desired city:")
    for i, loc in enumerate(city_options, 1):
        print(f"{i}. {loc[2]}")


def get_selected_city(city_options, selection):
    try:
        index = int(selection)
        if 1 <= index <= len(city_options):
            return city_options[index - 1]
    except ValueError:
        pass

    return None


def get_user_location():
    try:
        geolocator = Nominatim(user_agent="weather_app")
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = geolocator.geocode(data['city'])
        if location:
            return location.latitude, location.longitude
    except:
        pass

    return None, None


def main(city_names):
    user_latitude, user_longitude = get_user_location()
    print("\nYOUR REQUESTED DATA: \n")
    if user_latitude is not None and user_longitude is not None:
        user_location = (user_latitude, user_longitude)
        city_names.insert(0, user_location)
    else:
        print(RED + "Failed to retrieve your location. Weather data will be provided only based on city names." + END_COLOR)

    for city_name in city_names:
        # Remove extra spaces in between words
        city_name = re.sub(' +', ' ', str(city_name))
        # Remove special characters
        city_name = re.sub(r'[^\w\s]', '', city_name)

        city_options = convert_location_to_coordinates(city_name)

        if len(city_options) == 1:
            latitude, longitude, city_name = city_options[0]
            location = f"{latitude}, {longitude}"

            if latitude is not None and longitude is not None:
                temperature, humidity = fetch_weather(latitude, longitude)

                if temperature is not None and humidity is not None:
                    print(GREEN + f"\nCity: {city_name}" + END_COLOR)
                    temperature_statement = f"The temperature is {temperature:.2f}°C."
                    humidity_statement = f"The humidity is {humidity}%."
                    if temperature > 25:
                        print(ORANGE + temperature_statement + " It's hot." + END_COLOR)
                    else:
                        print(BLUE + temperature_statement + " It's cold." + END_COLOR)
                    print(YELLOW + humidity_statement + END_COLOR)
                    if humidity > 70:
                        print(YELLOW + "It's humid. Don't forget to stay hydrated." + END_COLOR)
                else:
                    print(RED + f"Failed to fetch weather data for the city: {city_name}" + END_COLOR)
            else:
                print(RED + f"Failed to convert location to coordinates for the city: {city_name}" + END_COLOR)
        elif len(city_options) > 1:
            display_city_options(city_options)
            selection = input("\nEnter the number corresponding to the desired city: ")
            selected_city = get_selected_city(city_options, selection)

            if selected_city is not None:
                latitude, longitude, city_name = selected_city
                location = f"{latitude}, {longitude}"

                if latitude is not None and longitude is not None:
                    temperature, humidity = fetch_weather(latitude, longitude)

                    if temperature is not None and humidity is not None:
                        print(GREEN + f"\nCity: {city_name}" + END_COLOR)
                        temperature_statement = f"The temperature is {temperature:.2f}°C."
                        humidity_statement = f"The humidity is {humidity}%."
                        if temperature > 25:
                            print(ORANGE + temperature_statement + " It's hot." + END_COLOR)
                        else:
                            print(BLUE + temperature_statement + " It's cold." + END_COLOR)
                        print(YELLOW + humidity_statement + END_COLOR)
                        if humidity > 70:
                            print(YELLOW + "It's humid. Don't forget to stay hydrated." + END_COLOR)
                    else:
                        print(RED + f"Failed to fetch weather data for the city: {city_name}" + END_COLOR)
                else:
                    print(RED + f"Failed to convert location to coordinates for the city: {city_name}" + END_COLOR)
            else:
                print(RED + "Invalid selection. Please try again." + END_COLOR)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        city_names = sys.argv[1:]
        main(city_names)
    else:
        print(RED + "No command line arguments provided." + END_COLOR)
        print(YELLOW + "Please enter city names separated by commas:" + END_COLOR)
        user_input = input("> ")
        city_names = [city.strip() for city in user_input.split(",")]
        main(city_names)
