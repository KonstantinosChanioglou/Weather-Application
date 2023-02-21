# WeatherApp
Weather App Python Project 


Before running the program you need to install (For Windows):
-pip3 install requests
-pip3 install tk
-pip3 install geopy


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
->Beginning with the Model package and weather.py. The class constructor receives a location parameter and initiates the latitude and longitude variables by calling getLocationInfo function which returns these two values.
->Then the callApiCurrent(), callApiForecast() are responsible for calling the API service of OpenWeatherMap for the current weather and forecast respectively.
->All the get functions returns the respective information from the api call response.



--- View ---
->The class constructor creates the window and initiates all the variables. It creates the main fraim and calls all the functions which add the information to the window.
->The createSearchBarFrame function is responsible for creating the search bar at the top of the window and specifies the callback function to be handleSearchButton (Controller class)
->The createCurrentWeatherFrame function creates all the labels and the values for the currentWeatherFrame. It uses the grid method to position the labels and the values.
->The createDevider function creates a divider between the current weather frame and the forecast weather frame.
->The createForecastWeatherFrame function creates all the labels and the values for the currentWeatherFrame. It uses the grid method to position the labels and the values.
-> The main functions executes the mainloop in order for the window to stay open




--- Controller ---
-> Controllers constructor is responsible to initialize view and model objects and to run the updateGui function
-> The updateGui function uses the se function to update all the variables in the view class in order to be updated on the window which is displayed
-> The handleSearchButton is responsible for calling the api functions with the location that user wrote in the search bar and then to update the gui with the new values.


#ToDO
At this time the images are static. The goal is to update them according with the return value of the api.


#Flow

The main.py calls the Controller __init__ and main function.
Controller calls the view and weather __init__ functions and mainloop is running for the window
At the weather the __init__ is running and the api methods are called.
At the view the window and the fields are created in the __init__ function. Sequentially all the frames are created with their labels and values.
At this time a full cycle has been completed and on the window is displayed the weather for Berlin.

If the user enters an new location handleSearchButton in the controller will be triggered and call the api methods. All the fields will be updated from the updateGui function except from the images which will be fixed.
