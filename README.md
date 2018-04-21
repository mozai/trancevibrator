# trancevibrator
Python module to control ASCII Corporation ("Rez") Trance Vibrator prehipheral.
Written by Moses "Mozai" Moore

## Usage

    import time
    from trancevibrator import Trancevibrator

    rez_device = Trancevibrator()
    rez_device.vibrate(128)
    time.sleep(1)
    rez_device.vibrate(250)
    time.sleep(1)
    rez_device.vibrate(0)

Don't forget to set vibration to '0' before you exit the program, unless
you want it to keep vibrating after you no longer control it.


## TODO
- option to stop vibration when the Trancevibrator object is discarded.  
  \__del__() method has a race condition with PyUSB so it doesn't work;
  maybe look into the `with` protocol, or the `atexit` module
- get this working in macOS and Windows


## Acknowledgements
- ASCII Corporation, for the game Rez and the moxie to make haptic gaming
  for the Playstation 2
- Tim "cexx.org" Cexx, who was looking into controlling the absent LEDs on the device
- HIROSE "hirose31" Masaaki, hirose31-at-gmail.com, author of the Perl Module

