#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from time import sleep



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.

def start(ev3, motor_right, motor_left):
    sleep(5)
    while light_sensor.reflection() <10:
        motor_right.run(500)
        motor_left.run(500)
    motor_right.brake()
    motor_left.brake()
    


def rodar(ev3, motor_right, motor_left):
    motor_left.run(500)
    motor_right.run(-450)
    

    


if __name__ == "__main__":
    # Create your objects here.
    ev3 = EV3Brick()
    light_sensor = ColorSensor(Port.S3)
    motor_left = Motor(Port.C)
    motor_right = Motor(Port.D)
    ultra_left = UltrasonicSensor(Port.S1)
    ultra_right =UltrasonicSensor(Port.S4)


    start(ev3, motor_right, motor_left)
    motor_right.run_angle(-500, 450)
    motor_right.run(500)
    motor_left.run(500)

    
    while True:
        while light_sensor.reflection() <10:
            if ultra_left.distance() < 450 or ultra_right.distance() < 450:
                if ultra_left.distance() < ultra_right.distance() and light_sensor.reflection() <10:
                    motor_right.run(450)
                    motor_left.run(500)
                elif ultra_left.distance() > ultra_right.distance() and light_sensor.reflection() <10:
                    motor_right.run(500)
                    motor_left.run(450)
                else:
                    if light_sensor.reflection() <10:
                        motor_right.run(500)
                        motor_left.run(500)
            else:
                rodar(ev3, motor_right, motor_left)
        
        motor_right.run_angle(-500, 450)
        motor_right.run(500)
        motor_left.run(500)

        

