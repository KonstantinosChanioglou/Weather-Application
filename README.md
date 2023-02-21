# WeatherApp
Wheather App Python Project 


Before running the programm you need to install (For Windows):
-> pip3 install requests
-> pip3 install tk
-> pip3 install geopy


# How to run 
    
-> Enter your API key for OpenWeatherMap into WeatherApp/Model/weather.py
-> Then run: python .\main.py
-> Optionally: When you run the app Berlin weather and forecast loads by default. 
   If you want to change it, change the parameter value of the Controller object in WeatherApp/main.py



#   Report   

The project is implemented using the MVC template.
-> Model defines data structure
-> View defines user's interface
-> Controller defines control logic

First of all I created the packages which are Model, View, Controller. Inside each the folders, __init__.py file must exists to define that these folders are packages of the project.

--- Model ---
Beggining with the Model package and weather.py. The class' constructor recieves a location parameter and initiates the latitude and longitude variables.
Then the callApiCurrent(), callApiForecast() are responsible for calling the API servise of OpenWeatherMap for the current weather and forecast respectively.
All the get functions returns the respective information from the api call response.
