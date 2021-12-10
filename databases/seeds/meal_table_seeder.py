"""MealTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Meal import Meal

class MealTableSeeder(Seeder):
    def run(self):
        Meal.create({"day": "sunday", "meal": "breakfast", "name": "meal_1"})
        Meal.create({"day": "sunday", "meal": "lunch", "name": "meal_1"})
        Meal.create({"day": "sunday", "meal": "dinner", "name": "meal_1"})
        Meal.create({"day": "monday", "meal": "breakfast", "name": "meal_2"})
        Meal.create({"day": "monday", "meal": "lunch", "name": "meal_2"})
        Meal.create({"day": "monday", "meal": "dinner", "name": "meal_2"})
        Meal.create({"day": "tuesday", "meal": "breakfast", "name": "meal_3"})
        Meal.create({"day": "tuesday", "meal": "lunch", "name": "meal_3"})
        Meal.create({"day": "tuesday", "meal": "dinner", "name": "meal_3"})
        Meal.create({"day": "wednesday", "meal": "breakfast", "name": "meal_4"})
        Meal.create({"day": "wednesday", "meal": "lunch", "name": "meal_4"})
        Meal.create({"day": "wednesday", "meal": "dinner", "name": "meal_4"})
        Meal.create({"day": "thursday", "meal": "breakfast", "name": "meal_5"})
        Meal.create({"day": "thursday", "meal": "lunch", "name": "meal_5"})
        Meal.create({"day": "thursday", "meal": "dinner", "name": "meal_5"})
        Meal.create({"day": "friday", "meal": "breakfast", "name": "meal_6"})
        Meal.create({"day": "friday", "meal": "lunch", "name": "meal_6"})
        Meal.create({"day": "friday", "meal": "dinner", "name": "meal_6"})
        Meal.create({"day": "saturday", "meal": "breakfast", "name": "meal_7"})
        Meal.create({"day": "saturday", "meal": "lunch", "name": "meal_7"})
        Meal.create({"day": "saturday", "meal": "dinner", "name": "meal_7"})