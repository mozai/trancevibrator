""" Python control of the ASCII Corporation Trance Vibrator device
works with the Drmn' Trance Vibe device too
"""
# props to Tim Cexx (blink_led) and HIROSE Masaaki (Perl module)
# TODO: get this working in OSX and in Windows
import usb
import time
__version__ = "2018.04.20"
__author__ = 'Moses "Mozai" Moore'


class Trancevibrator:
  """ state and control of an ASCII Corporation Trance Vibrator
  as the one that came with the game "Rez" for the Playstation 2
  """

  def __init__(self, vendorid=0x0b49, productid=0x064f):
    " return a handle to a Trace Vibrator device if it exists "
    self.device = usb.core.find(idVendor=vendorid, idProduct=productid)
    if self.device is None:
      raise Exception("USB connection failure")
    self.was_kernel_driver = False
    if self.device.is_kernel_driver_active(0):
      self.device.detach_kernel_driver(0)
      self.was_kernel_driver = True
      # call device.attach_kernel_driver(0) later ?
    time.sleep(0.1)  # dead-chicken waving
    self.device.set_configuration()
    # needed another time-gap in Windows between set-conf and 'reset'
    time.sleep(0.1)

  def __enter__(self):
    # noop
    return self

  def __exit__(self, err_type, err_value, err_trace):
    # stop the device from blinking & shaking
    # before discarding or throwing an exception
    self.device.ctrl_transfer(65, 0, 0, 768)
    if self.was_kernel_driver:
      usb.util.dispose_resources(self.device)

  def blink_led(self, led_value=0, duration=0):
    """ blinks the Trance Vibrator's (non-existent) LED lights
    led_value is uses the last three bits for LEDs #3, #2 and #1
    duration is seconds to keep blinking before shutting off
    """
    # are ASCII Trance Vibrator hidden LEDs independently controlled?
    # Yep! The lowest 3 bits of Index, one for each LED
    if led_value != (led_value & 7):
      raise ValueError("led_value must be 0 or 1-7")
    value = 0
    index = 768 + led_value
    retval = self.device.ctrl_transfer(65, 0, value, index)
    # time.sleep(0.1)  # more dead-chicken waving
    if duration:
      time.sleep(duration)
      self.blink_led(0)
    return retval

  def vibrate(self, speed=0, duration=0):
    """ shakes the Trance Vibrator; speeds are 0-255, 0 to stop.
    duration is seconds to keep vibrating before shutting off
    low speeds may be undetectable but still run the motor
    """
    if speed < 0:
      speed = 0
    elif speed > 255:
      speed = 255
    speed_value = speed << 8 | speed
    speed_index = 768 + (speed & 15)
    # RequestType, Request, Value, Index, data_or_Length, timeout
    retval = self.device.ctrl_transfer(65, 0, speed_value, speed_index)
    # time.sleep(0.1)  # more dead-chicken waving
    if duration:
      time.sleep(duration)
      self.vibrate(0)
    return retval
