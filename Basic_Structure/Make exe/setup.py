from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = "C:\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python35-32\\tcl\\tcl8.6"

setup(name="City Weather",
      version='1',
      description='This is to show the current Weaher of cities',
      executables=[Executable("weather_Calculator.py")])
