from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 1500 #kcal
PROTEIN_GOAL = 140 #g
FAT_GOAL = 80 #g
CARBS_GOAL = 100 #g

today = []


@dataclass
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

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food item!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        proteins = int(input("Proteins: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = FoodItem(name, calories, proteins, fats, carbs)
        today.append(food)
        print("Successfully added!")

    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
        axs[0, 0].set_title("MacroNutrients Distribution")

        fig.tight_layout()
        plt.show()
