#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def teste_motor(motor):
    test_motor.run_target(500, 360)
    

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

# Para sensor de toque

# sensor = TouchSensor(Port.S2) # set port
# print(sensor.pressed())

# Para sensor Ultrasonico 

# sensor = UltrasonicSensor(Port.S2)# set port
# print(sensor.distance())

# Para sensor de COR
# sensor = ColorSensor(Port.S2) # set port
# print(sensor.color()) # Mostra color
# print(sensor.reflection()) #mostra Refracao 

test_motor = Motor(Port.B)
# test_motor.run_target(500, 360)
teste_motor(test_motor)




# while center_button:
#     if sensor.pressed():
#         ev3.speaker.beep()
#         break


# print(sensor.pressed())


