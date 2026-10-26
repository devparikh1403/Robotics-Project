
from controller import Robot, Motion
import os

robot = Robot()
timestep = int(robot.getBasicTimeStep())

motion_dir = os.path.join(
    os.path.dirname(__file__), "motions"
)

def load_motion(filename):
    path = os.path.join(motion_dir, filename)

    if not os.path.isfile(path):
        raise FileNotFoundError(f"Missing motion: {path}")

    motion = Motion(path)

    if not motion.isValid():
        raise RuntimeError(f"Invalid motion: {filename}")

    return motion

forward = load_motion("Forwards50.motion")
left = load_motion("TurnLeft60.motion")
right = load_motion("TurnRight60.motion")

# Loop the motions while each is active
forward.setLoop(True)
left.setLoop(True)
right.setLoop(True)

sequence = [
    ("forward", forward, 7.0),
    ("left", left, 5.0),
    ("forward", forward, 7.0),
    ("right", right, 5.0),
]

index = 0
state_start = robot.getTime()

name, motion, duration = sequence[index]
motion.play()

print("Continuous autonomous movement started")

while robot.step(timestep) != -1:
    elapsed = robot.getTime() - state_start

    if elapsed >= duration:
        motion.stop()

        # Advance to the next action, wrapping around forever
        index = (index + 1) % len(sequence)
        name, motion, duration = sequence[index]

        motion.play()
        state_start = robot.getTime()

        print("Now:", name)


