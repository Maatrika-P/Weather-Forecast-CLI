# Weatherly :sunny: :cloud: :umbrella:

A dynamic and user-friendly weather CLI that brings you real-time weather updates from around the world. Stay informed about the latest temperature and humidity levels, ensuring you're always prepared for the elements. With colorful visual cues and interactive features, Weatherly provides an engaging weather experience like no other. Powered by Bing API, OpenWeatherMap, and enhanced with GitHub Copilot, Weatherly is your go-to companion for all things weather. Let's embark on a meteorological adventure together! 🌍🌤️🌡️💦

## Features :sparkles:

- Fetch weather data based on city names or user location
- Display temperature and humidity information with color-coded formatting
- Supports multiple cities with the same name, allowing the user to select the desired city
- Appropriate error handling for the city names such as involvement of special characters, numbers or extra spaces.
- An example command line argument can be `python weather_cli.py Delhi Hy der#abad`

   ![image](https://github.com/Maatrika-P/Weather-Forecast-CLI/assets/135828608/5e1cd3e4-44da-451f-a5b8-d3971534c9e5)


## Installation :computer:

1. Clone the repository: `[[git clone https://github.com/your-username/weather-app.git](https://github.com/Fastest-Coder-First/Python-Weather-Forecast-CLI.git)`
2. Install dependencies: `pip install -r requirements.txt`
3. Don't forget to go to https://openweathermap.org/api and get your api key
4. And https://www.microsoft.com/en-us/bing/apis/bing-web-search-api to get your api key 


## Usage :sun_behind_small_cloud:

1. Run the cli: `python weather_cli.py city1 city2 city3`
   - Replace `city1`, `city2`, etc., with the names of the cities you want to get weather data for.
   - Example: `python weather_cli.py Srinagar Hyderabad` (city names separated by spaces)
   - You will be prompted to choose your desired options from the available locations with the same/similar names.
   - Choose your desired location and Hoorayy!!
  
![image](https://github.com/Maatrika-P/Weather-Forecast-CLI/assets/135828608/dd597478-bcb1-4414-9133-ca76157fab24)


2. Alternatively, run the cli without command line arguments:
   - Example: `python weather_cli.py`
   - Enter city names separated by commas when prompted.
   - You will be prompted to choose your desired options from the available locations with the same/similar names.
   - Choose your desired location and Hoorayy!!
  
   ![image](https://github.com/Maatrika-P/Weather-Forecast-CLI/assets/135828608/0128b22b-1f17-4232-9b8d-f89ac9a133b5)



## Architecture Diagram 🏛️
- This is the general workflow of the CLI application.

![image](https://github.com/Fastest-Coder-First/Python-Weather-Forecast-CLI/assets/135828608/279d0d40-6668-4a8e-bf61-1d70e360dcfb)


## Credits :clap:

- Powered by Bing API for geocoding and OpenWeatherMap API for weather data.
- AI assistance provided by GitHub Copilot.


## Contributions and feedback are welcome! 🙌

We welcome contributions to improve our project. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request



