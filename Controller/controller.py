from View.view import View
from Model.weather import Weather


class Controller():

    def __init__(self, location) -> None: #type-check the method and raise an error
        self.view = View(self)
        self.weather = Weather(location)
        self.updateGui(self.weather)

    def updateGui(self, weather):
        
        self.view.varLocation.set(weather.getLocation())
        self.view.varCountry.set(weather.getCountry())
        self.view.varPhoto.set(weather.getCurrentPhoto())
        self.view.varDateTime.set(weather.getCurrentDateTime())
        self.view.varCondition.set(weather.getCurrentCondition())
        self.view.varTemp.set(weather.getCurrentTemp())
        self.view.varFeelsLike.set(weather.getCurrentFeelsLike())
        self.view.varHumidity.set(weather.getCurrentHumidity())
        self.view.varWindSpeed.set(weather.getCurrentWind())

        for step in range(0,3): 
            self.view.varForecastPhoto[step].set(weather.getForecastPhoto(step))
            self.view.varForecastDateTime[step].set(weather.getForecastDateTime(step))
            self.view.varForecastCondition[step].set(weather.getForecastCondition(step))
            self.view.varForecastTemp[step].set(weather.getForecastTemp(step))
            self.view.varForecastFeelsLike[step].set(weather.getForecastFeelsLike(step))
            self.view.varForecastHumidity[step].set(weather.getForecastHumidity(step))
            self.view.varForecastWindSpeed[step].set(weather.getForecastWind(step))


    def handleSearchButton(self, event=None):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.weather.callApiCurrent()
            self.weather.callApiForcast()
            self.updateGui(self.weather)
        

    def main(self):
        self.view.main()