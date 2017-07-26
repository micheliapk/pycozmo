import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

class Cozmic(object):

    INCHES_TO_CM = 25
    def __init__(self, robot):
        self.robot = robot

    def move_forward(self, distance=3, speed=75):
        self.robot.drive_straight(distance_mm(distance * self.INCHES_TO_CM),
                                  speed_mmps(speed)).wait_for_completed()

    def turn_left(self, angle=90):
        self.robot.turn_in_place(degrees(angle)).wait_for_completed()

    def turn_right(self, angle=90):
        self.robot.turn_in_place(degrees(-angle)).wait_for_completed()

    def draw_triangle(self):
        self.robot.say_text('Triangle').wait_for_completed()

def cozmo_program(robot: cozmo.robot.Robot):
    cozmic1 = Cozmic(robot)

    cozmic1.move_forward(distance=9)
    cozmic1.turn_right(angle=90)
    cozmic1.move_forward(distance=10)
    cozmic1.turn_left(angle=90)
    cozmic1.move_forward(distance=9)
    cozmic1.turn_right(angle=90)
    cozmic1.move_forward(distance=7)


    #cozmic1.turn_left()

    #cozmic1.move_forward()


if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
