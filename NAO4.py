from controller import Robot, Motion
import os

robot = Robot()
timestep = int(robot.getBasicTimeStep())

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "motions", "Backwards.motion")

print("Motion path:", path)
print("File exists:", os.path.isfile(path))

if not os.path.isfile(path):
    raise FileNotFoundError(path)

backward = Motion(path)

if not backward.isValid():
    raise RuntimeError("Backward motion file is invalid")

print("Backward motion loaded. Starting playback...")

backward.setLoop(True)
backward.play()

while robot.step(timestep) != -1:
    pass
