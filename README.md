# Coffeetracker
A Python and Qt-App which lets you track the amount of consumables (e.g. coffees) in your department (and more).
With this App you can add a quantity to a Database of coworkers and estimate the consumption or similar (in case of this example we use coffee).
Later you can even chose to pay your debt (if you need to pay for it) or just generate competition graphs just for fun and to know who is the biggest junkie.

More Features are to come.

## Minimal Requirements

```
- Python 3.6
- PyQt5
- Matplotlib 3.1
- numpy
```
The packages can usually be installed from Pypi with the `pip install 'packagename'` or your system according command.

A Raspberry Pi is not directly needed but highly recommended for the use. I use a 3b Model with a 3.5" Screen (480x320 px) and the according casing for that screen to build a cheap an mobile device.

## Features

This app gives you the possibility to select your name and then add a quantity of the given item name to it. If it's desired you can also assign a price to that item, which gets added as debt to the user account. Otherwise the cost can also be set to zero, just to track the amount. Furthermore you can pay your debts or load credit to you account, add new accounts (in case you are not there yet), plot leader boards or change existing entries (e.g. change mistakes in naming or disable users who are not active anymore). There is also a threshold where the call to payment message will appear on the mainscreen. If this threshold is exceeded by the factor 1.5 the usere will also get an active message after each entry, until the debts are reduced again.

Mainscreen where you start:

![alt text](https://github.com/AndreWohnsland/Coffeetracker/blob/master/pictures/mainscreen.PNG "mainscreen")

Build in keyboard and numpad for typing:

![alt text](https://github.com/AndreWohnsland/Coffeetracker/blob/master/pictures/keyboard.PNG "keyboard")
![alt text](https://github.com/AndreWohnsland/Coffeetracker/blob/master/pictures/numpad.PNG "numpad")

Plotting the leader board:

![alt text](https://github.com/AndreWohnsland/Coffeetracker/blob/master/pictures/leaderboard.PNG "leaderboard")

Feel free to try it out and give me feedback on it!

## Install PyQt5 on RaspberryPi

You will need at least PyQt5 on your RaspberryPi. More information can be found at [riverbank](https://riverbankcomputing.com/software/pyqt/intro).\
To install PyQt5 on your Pi run:
```
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
```

## Install PyQt5 on other Systems

If you want to run some testing on other systems, you can get PyQt5 [here](https://www.riverbankcomputing.com/software/pyqt/download5).\
As long as you are using a supported version of Python you can install PyQt5 from [PyPi](https://pypi.org/project/PyQt5/) by running:
```
pip3 install PyQt5
```

## Development on Non-Pi Hardware

As long as you are working on another hardware (for example on a Windows or macOS engine) best is to set the `devenvironment` to `True`, it will enable your cursor on the touchscreen:
```python
devenvironment = True
```

## Setting up the Program Parameters
There are some options before the first start you can set. For usual testing i recommend setting `devenvironment` to `True` for programming and adjustments, otherwise set it to false. The `app_width` and `app_height` parameters refer to your touchscreen resolution. In this case its a 3.5" Screen. As a DB name, you can choose whatever name you find fitting or prefer.\
For the quantities there are basically three options: First, you can set a price on the quantity, if it costs nothing you can set it to zero. Then you can name the quantity, in our case it's coffee. And lastly, you can set a threshold, at which a call to payment label is shown when the according user is selected. Furthermore, if the threshold is exceeded by factor 1.5 (feel free to change it in you code) the user will also get a messagebox reminding him to pay (we could even go further with emailing or stuff like that, if we implement the email address into our DB).
```python
devenvironment = True           # enables or disables your cursor
app_width = 480
app_height = 320
db_name = "tracker_test"    
paymentcall_threshold = 10      # When the pay message got displayed (critical is 1.5 that value)
quantcosts = 0.25               # cost of one quant (can also be 0)
quantname = "coffee"            # name of your quants 
```