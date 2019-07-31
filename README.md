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

As long as you are working on another hardware (for example on a Windows or macOS engine) best is to set the devenv to `True`, it will enable your cursor on the touchscreen:
```python
devenvironment = True
```
