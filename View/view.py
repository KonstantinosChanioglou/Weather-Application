import tkinter as tk
from tkinter.constants import *
from tkinter import StringVar
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image

class View(tk.Tk): #View inherits from tkinter

    def __init__(self,  controller): #SELF IS A TK.tK OBJECT NOW
        super().__init__()
        self.geometry("1000x700") #window dimensions

        #---Define Variables
        self.controller = controller
        self.bind('<Return>', self.controller.handleSearchButton)
        self.varSearch = StringVar()

        self.varLocation = StringVar()
        self.varCountry = StringVar()
        self.varPhoto = StringVar()
        self.varDateTime = StringVar()
        self.varCondition = StringVar()
        self.varTemp = StringVar()
        self.varFeelsLike = StringVar()
        self.varHumidity = StringVar()
        self.varWindSpeed = StringVar()

        self.varForecastPhoto = list()
        self.varForecastDateTime = list()
        self.varForecastCondition = list()
        self.varForecastTemp = list()
        self.varForecastFeelsLike = list()
        self.varForecastHumidity = list()
        self.varForecastWindSpeed = list()
        
        for step in range(0,3):
            self.varForecastPhoto.append(StringVar())
            self.varForecastDateTime.append(StringVar())
            self.varForecastCondition.append(StringVar())
            self.varForecastTemp.append(StringVar())
            self.varForecastFeelsLike.append(StringVar())
            self.varForecastHumidity.append(StringVar())
            self.varForecastWindSpeed.append(StringVar())

        self.mainFrame = Frame()
        self.mainFrame.pack()
        self.createSearchBarFrame()
        self.createCurrentWeatherFrame()
        self.createDivider()
        self.createForecastWeatherFrame()
    

    def createSearchBarFrame(self):
        self.frameSearchBar = Frame(self.mainFrame)
        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleSearchButton)
        self.comboSearch.pack(padx=30, pady=30, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def createCurrentWeatherFrame(self):
        self.currentWeatherFrame = Frame(self.mainFrame)
        self.headerFrame = Frame(self.mainFrame, width=50, height=50)
        self.currentWeatherFrame['padding'] = (5,10,5,30)
        
        #---Labels---
        labelDateTime = Label(self.currentWeatherFrame, text='Date & Time:')
        labelCondition = Label(self.currentWeatherFrame, text='Current Condition:')
        labelTemp = Label(self.currentWeatherFrame, text='Tempreture (C):')
        labelFeelsLike = Label(self.currentWeatherFrame, text='Feels Like (C):')
        labelHumidity = Label(self.currentWeatherFrame, text='Humidity (%):')
        labelWindSpeed = Label(self.currentWeatherFrame, text='Wind Speed (m/s):')
        

        #---Labels attach to the grid
        labelDateTime.grid(row=2, column=0, pady=5, sticky=W)
        labelCondition.grid(row=3, column=0, pady=5, sticky=W)
        labelTemp.grid(row=4, column=0, pady=5, sticky=W)
        labelFeelsLike.grid(row=5, column=0, pady=5, sticky=W)
        labelHumidity.grid(row=6, column=0, pady=5, sticky=W)
        labelWindSpeed.grid(row=7, column=0, pady=5, sticky=W)  
        
        # Create an object of tkinter ImageTk
        image = Image.open("Photos/01d.png") #default image instead of self.varPhoto[step] and ToDo
        photo = ImageTk.PhotoImage(image)
        
        
        location = Label(self.headerFrame, textvariable=self.varLocation, font=('Times', 18))
        country = Label(self.headerFrame, textvariable=self.varCountry, font=('Times', 11))
        img = Label(self.headerFrame, image=photo)
        img.image = photo
        dateTime = Label(self.currentWeatherFrame, textvariable=self.varDateTime)
        condition = Label(self.currentWeatherFrame, textvariable=self.varCondition)
        temp = Label(self.currentWeatherFrame,  textvariable=self.varTemp)
        feelsLike = Label(self.currentWeatherFrame,  textvariable=self.varFeelsLike)
        humidity = Label(self.currentWeatherFrame,  textvariable=self.varHumidity)
        windSpeed = Label(self.currentWeatherFrame,  textvariable=self.varWindSpeed)
        
        location.pack(padx=3, pady=20, side=LEFT) 
        country.pack(padx=2, pady=20, side=LEFT)
        img.pack( padx=20, pady=20, side=RIGHT)
        
        dateTime.grid(row=2, column=1, padx=60, pady=5, sticky=E)
        condition.grid(row=3, column=1, padx=60, pady=5, sticky=E)
        temp.grid(row=4, column=1, padx=60, pady=5, sticky=E)
        feelsLike.grid(row=5, column=1, padx=60, pady=5, sticky=E)
        humidity.grid(row=6, column=1, padx=60, pady=5, sticky=E)
        windSpeed.grid(row=7, column=1, padx=60, pady=5, sticky=E)        
               
        self.headerFrame.pack()
        self.currentWeatherFrame.pack()



    def createDivider(self):
        # horizontal separator
        ttk.Separator(
            master=self.mainFrame,
            orient=HORIZONTAL,
            style='TSeparator',
            class_= ttk.Separator,
            takefocus= 1,
            cursor='plus'    
        ).pack(fill=X, expand=True)
 


    def createForecastWeatherFrame(self):
        self.forecastWeatherFrame = Frame(self.mainFrame)
        self.imagesFrame = Frame(self.forecastWeatherFrame, width=50, height=50)
        
        #---Labels---
        labelDateTime = Label(self.forecastWeatherFrame, text='Date & Time:')
        labelCondition = Label(self.forecastWeatherFrame, text='Current Condition:')
        labelTemp = Label(self.forecastWeatherFrame, text='Tempreture (C):')
        labelFeelsLike = Label(self.forecastWeatherFrame, text='Feels Like (C):')
        labelHumidity = Label(self.forecastWeatherFrame, text='Humidity (%):')
        labelWindSpeed = Label(self.forecastWeatherFrame, text='Wind Speed (m/s):')

        #---Labels attach to the grid
        labelDateTime.grid(row=1, column=0, pady=5, sticky=W)
        labelCondition.grid(row=2, column=0, pady=5, sticky=W)
        labelTemp.grid(row=3, column=0, pady=5, sticky=W)
        labelFeelsLike.grid(row=4, column=0, pady=5, sticky=W)
        labelHumidity.grid(row=5, column=0, pady=5, sticky=W)
        labelWindSpeed.grid(row=6, column=0, pady=5, sticky=W)

        #---Values---
        img = list()
        dateTime = list()
        condition  = list()
        temp = list()
        feelsLike = list()
        humidity = list()
        windSpeed = list()

        #---Forecast
        for step in range(0,3):
            
            # Create an object of tkinter ImageTk
            image = Image.open("Photos/01d.png") #default image instead of self.varPhoto[step] and ToDo
            photo = ImageTk.PhotoImage(image)
            
            img.append(Label(self.forecastWeatherFrame, image=photo))
            img[step].image = photo
            dateTime.append(Label(self.forecastWeatherFrame, textvariable=self.varForecastDateTime[step]))
            condition.append(Label(self.forecastWeatherFrame, textvariable=self.varForecastCondition[step]))
            temp.append(Label(self.forecastWeatherFrame,  textvariable=self.varForecastTemp[step]))
            feelsLike.append(Label(self.forecastWeatherFrame,  textvariable=self.varForecastFeelsLike[step]))
            humidity.append(Label(self.forecastWeatherFrame,  textvariable=self.varForecastHumidity[step]))
            windSpeed.append(Label(self.forecastWeatherFrame,  textvariable=self.varForecastWindSpeed[step]))
        
            img[step].grid(row=0, column=step+1, padx=40, pady=5, sticky=E)
            dateTime[step].grid(row=1, column=step+1, padx=40, pady=5, sticky=E)
            condition[step].grid(row=2, column=step+1, padx=40, pady=5, sticky=E)
            temp[step].grid(row=3, column=step+1, padx=40, pady=5, sticky=E)
            feelsLike[step].grid(row=4, column=step+1, padx=40, pady=5, sticky=E)
            humidity[step].grid(row=5, column=step+1, padx=40, pady=5, sticky=E)
            windSpeed[step].grid(row=6, column=step+1, padx=40, pady=5, sticky=E)        
        
        self.forecastWeatherFrame.pack()
        
    def main(self):
        self.mainloop()
