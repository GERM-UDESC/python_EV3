#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Functions




# PRincipal Code

if __name__ == "__main__":
    # Create your objects here.
    ev3 = EV3Brick()
    # start = TouchSensor(Port.S1) # sem necessidade
    light_sensor = ColorSensor(Port.S3)
    motor_left = Motor(Port.C)
    motor_right = Motor(Port.D)


    # Write your program here.
    ev3.speaker.beep()
    while True:
        print(light_sensor.reflection())
        if light_sensor.reflection()>10:
            motor_right.run(500)
            motor_left.brake()
        else:
            motor_right.brake()
            motor_left.run(500)

    v3.speaker.beep()


