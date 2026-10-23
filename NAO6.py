from controller import Robot, Motion
import os

robot = Robot()
timestep = int(robot.getBasicTimeStep())

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "motions", "SideStepRight.motion")

print("Motion path:", path)
print("File exists:", os.path.isfile(path))

if not os.path.isfile(path):
    raise FileNotFoundError(path)

right = Motion(path)

if not right.isValid():
    raise RuntimeError("Right motion file is invalid")

print("Right motion loaded. Starting playback...")

right.setLoop(True)
right.play()

while robot.step(timestep) != -1:
    pass
