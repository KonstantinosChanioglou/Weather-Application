from View.view import View
from Model.weather import Weather

from PIL import ImageTk, Image


class Controller():

    def __init__(self, location) -> None: #type-check the method and raise an error
        self.view = View(self)
        self.weather = Weather(location)
        self.updateGui(self.weather)
        

    def updateGui(self, weather):
        
        #print("Photos/"+weather.getCurrentPhoto()+".png")
        #self.view.varPhoto = "Photos/"+weather.getCurrentPhoto()+".png"
        print("===Photos/"+weather.getCurrentPhoto()+".png")
        image = Image.open("Photos/"+weather.getCurrentPhoto()+".png")#("Photos/01d.png")
        photo = ImageTk.PhotoImage(image)
        

        self.view.varPhoto.set(photo)
        self.view.varDateTime.set(weather.getCurrentDateTime())
        self.view.varCondition.set(weather.getCurrentCondition())
        self.view.varTemp.set(weather.getCurrentTemp())
        self.view.varFeelsLike.set(weather.getCurrentFeelsLike())
        self.view.varHumidity.set(weather.getCurrentHumidity())
        self.view.varWindSpeed.set(weather.getCurrentWind())
        self.view.varLocation.set(weather.getLocation())

        for step in range(0,3): #avoid the first measurement
            #print("photo:","Photos/"+weather.getForecastPhoto(step+1)+".png")
            self.view.varForecastPhoto[step].set(weather.getForecastPhoto(step+1))
            self.view.varForecastDateTime[step].set(weather.getForecastDateTime(step+1))
            self.view.varForecastCondition[step].set(weather.getForecastCondition(step+1))
            self.view.varForecastTemp[step].set(weather.getForecastTemp(step+1))
            self.view.varForecastFeelsLike[step].set(weather.getForecastFeelsLike(step+1))
            self.view.varForecastHumidity[step].set(weather.getForecastHumidity(step+1))
            self.view.varForecastWindSpeed[step].set(weather.getForecastWind(step+1))


    def handleSearchButton(self, event=None):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.weather.callApiCurrent()
            self.weather.callApiForcast()
            self.updateGui(self.weather)
        

    def main(self):
        self.view.main()