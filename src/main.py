import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from image_processing import process_video
from path_planning import a_star
from motor_control import navigate
from pid_controller import PIDController


def main():
    # Image processing to get a clear view of the environment
    process_video()

    # Grid example and A* path planning
    grid = [[0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]
    start = (0, 0)
    goal = (4, 4)
    path = a_star(start, goal, grid)
    print("Planned Path:", path)

    # Start navigation with obstacle avoidance
    navigate()

if __name__ == "__main__":
    main()
