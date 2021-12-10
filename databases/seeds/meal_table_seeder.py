"""MealTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Meal import Meal

class MealTableSeeder(Seeder):
    def run(self):
        Meal.create({"day": "sunday", "meal": "breakfast", "name": "A Southwest omelet with bell peppers and chorizo"})
        Meal.create({"day": "sunday", "meal": "lunch", "name": "Super Simple Chicken Cauliflower Fried Rice"})
        Meal.create({"day": "sunday", "meal": "dinner", "name": "Superfood Meatballs and Keto Creamed Spinach"})
        Meal.create({"day": "monday", "meal": "breakfast", "name": "Pancakes with Blueberry Butter"})
        Meal.create({"day": "monday", "meal": "lunch", "name": "Zesty Chili Lime Keto Tuna Salad"})
        Meal.create({"day": "monday", "meal": "dinner", "name": "Lemon Herb Low Carb Keto Meatloaf"})
        Meal.create({"day": "tuesday", "meal": "breakfast", "name": "Three Quick n’ Easy Keto Egg Muffins"})
        Meal.create({"day": "tuesday", "meal": "lunch", "name": "Italian Turkey Casserole"})
        Meal.create({"day": "tuesday", "meal": "dinner", "name": "Portobello Bun Cheeseburger with Celeriac Everything Oven Fries and Homemade Keto Mayo"})
        Meal.create({"day": "wednesday", "meal": "breakfast", "name": "Keto Avocado Egg Bowls"})
        Meal.create({"day": "wednesday", "meal": "lunch", "name": "Crispy Cheesy Chicken Salad"})
        Meal.create({"day": "wednesday", "meal": "dinner", "name": "4 oz grilled ribeye steak, 2 tbsp grass-fed butter, and 2 cups of mixed leafy greens with 1 tbsp avocado oil"})
        Meal.create({"day": "thursday", "meal": "breakfast", "name": "Avocado Breakfast Bowl"})
        Meal.create({"day": "thursday", "meal": "lunch", "name": "Keto Parmesan Chicken"})
        Meal.create({"day": "thursday", "meal": "dinner", "name": "Cheesy Broccoli Meatza"})
        Meal.create({"day": "friday", "meal": "breakfast", "name": "Acai Almond Butter Smoothie"})
        Meal.create({"day": "friday", "meal": "lunch", "name": "Keto Beef Stew"})
        Meal.create({"day": "friday", "meal": "dinner", "name": "Creamy Mushroom Chicken"})
        Meal.create({"day": "saturday", "meal": "breakfast", "name": "Keto Boosted Coffee"})
        Meal.create({"day": "saturday", "meal": "lunch", "name": "Low Carb Crispy Keto “Fried” Chicken and one cup steamed broccoli"})
        Meal.create({"day": "saturday", "meal": "dinner", "name": "Low Carb Keto Lasagna"})