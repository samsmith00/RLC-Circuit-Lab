from manim import *

from scenes.underdampedManim import Underdamped
from scenes.overdampedManim import Overdamped
from scenes.criticallyDampedManim import Critically_Damped

def run_scenes(): 
    for scene in [Underdamped, Overdamped, Critically_Damped]: 
        scene_to_run = scene()
        scene_to_run.render()

if __name__ == "__main__": 
    run_scenes()