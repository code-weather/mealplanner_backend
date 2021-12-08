"""MealTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Meal import Meal

class MealTableSeeder(Seeder):
    def run(self):
        Meal.create({"days": "Sunday", "subject": "Meal of the day"})
        Meal.create({"days": "Monday", "subject": "Meal of the day"})
        Meal.create({"days": "Tuesday", "subject": "Meal of the day"})
        Meal.create({"days": "Wednesday", "subject": "Meal of the day"})
        Meal.create({"days": "Thursday", "subject": "Meal of the day"})
        Meal.create({"days": "Friday", "subject": "Meal of the day"})
        Meal.create({"days": "Saturday", "subject": "Meal of the day"})