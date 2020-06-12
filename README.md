# SDR PTT

This code implements a Push To Talk (PTT) function using a simple push button.
The target is a Software Defined Radio with REST endpoints that can control
the transmitter, like the [LIME SDR Mini](https://limemicro.com/products/boards/limesdr-mini/)

I use the [Adafruit FT232H Breakout board](https://www.adafruit.com/product/2264) with a
button attaced to the `C0` input pin connected via USB to a PC. Assuming the same computer
is running the [SDR Angel](https://github.com/f4exb/sdrangel) software, this code hits
a REST endpoint to turn on/off the transmitter, thus simulating a PTT.

Before running this software follow the excellent install instruction for the `FT232H` found
on the [Adafruit site](https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/overiew)