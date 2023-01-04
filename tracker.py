from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 1500 #kcal
PROTEIN_GOAL = 140 #g
FAT_GOAL = 80 #g
CARBS_GOAL = 100 #g

today = []


class FoodItem:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False

while not done:
    print("""
    (1) Enter the name of the food item
    (2) Visualize progress
    (3) Quit
    """)