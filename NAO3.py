from controller import Robot, Motion
import os

robot = Robot()
timestep = int(robot.getBasicTimeStep())

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "motions", "SideStepLeft.motion")

print("Motion path:", path)
print("File exists:", os.path.isfile(path))

if not os.path.isfile(path):
    raise FileNotFoundError(path)

left = Motion(path)

if not left.isValid():
    raise RuntimeError("Left motion file is invalid")

print("Left motion loaded. Starting playback...")

left.setLoop(True)
left.play()

while robot.step(timestep) != -1:
    pass


