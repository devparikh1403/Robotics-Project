
from controller import Robot, Motion
import os

robot = Robot()
timestep = int(robot.getBasicTimeStep())

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "motions", "Forwards50.motion")

print("Motion path:", path)

forward = Motion(path)

if not forward.isValid():
    raise RuntimeError("Motion file is invalid")

print("Motion loaded. Starting playback...")
forward.setLoop(True)
forward.play()

while robot.step(timestep) != -1:
    print("Motion is playing:", not forward.isOver())
