# trancevibrator
Python module to control ASCII Corporation ("Rez") Trance Vibrator prehipheral.
Written by Moses "Mozai" Moore

## Usage

    from trancevibrator import Trancevibrator

    with Trancevibrator() as TRANCE:
      for i in range(0, 257, 64):
        print("vibrate({})".format(i))
        TRANCE.vibrate(i, 1.0)

    ---

    from trancevibrator import Trancevibrator
    import time

    rez_device = Trancevibrator()
    rez_device.vibrate(128)
    time.sleep(1)
    rez_device.vibrate(250)
    time.sleep(1)
    rez_device.vibrate(0)

If you don't use the `with` structure, and you don't use the duration param
for `.vibrate()`, keep in mind the device will not stop vibrating unless
you use `.vibrate(0)` before your program ends, or you unplug the device.
Since an exception could crash your program, use `with` unless you have
a good reason.

## INSTALL

In Debian Linux, I used `apt-get install python-usb`.  Well,
`python3-usb`.  It also brings in `libusb-1.0`.  I would get
"usb.core.USBError: Errno 13 Access denied" if I didn't run as root,
but I believe there's a way to configure udev to create the USB device
files with different group owner and permissions.

In macOS, `sudo easy_install pyusb` for the Python2.7 you already have,
but I needed to use homebrew for `brew install libusb` otherwise I would
get "usb.core.NoBackendError: No backend available".  Aside from installing
pyusb, I didn't need to run as root.


## TODO
- get this working in MS-Windows


## Acknowledgements
- ASCII Corporation, for the game Rez and the moxie to make haptic gaming
  for the Playstation 2
- Tim "cexx.org" Cexx, who was looking into controlling the absent LEDs
  on the device
- HIROSE "hirose31" Masaaki, hirose31-at-gmail.com, author of the Perl Module

