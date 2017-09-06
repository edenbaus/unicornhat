# Unicornhat
## This repo contains a few Python scripts for the Pimoroni Unicorn phat
## The unicornhelper.py file contains a series of base functions for plotting lines, boarders, increasing/decreasing RGB values and a few others.
## The .ipynb notebook files are equivalent to their respective .py equivalent
## The unicornwalk.py file generates random walks on a grid based on the phat dimension. The moving light resets once it reaches a boundary pixel
## The unicornweather.py file is a fun little program that scrapes the current weather conditions and displays
- ##  Temperature degrees F
- ##  Humidity %
- ##  Percipitation %
- ##  Wind Speed MPG

### Temperature is on a color scale:
- ### Blue: 0 - 32 degrees F
- ### Green: 33 - 74 degrees F
- ### Red 75: - 100 degrees F

### The Number of Acticated LEDs is on a scale:
- ### Temperature: linshuffle(np.linspace(low,high,10),temperature) <strong>func in unicornhelper.py</strong>
- ### Humidity: int(numpy.ceil(humidity * 8 / 100))
- ### Precipitation: int(numpy.ceil(humidity * 8 / 100))
- ### Wind Speed MPH: int(np.log2(windspeed))
