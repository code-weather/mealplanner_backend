""" A MealController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Meal import Meal


class MealController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
        Get().route("/show", MealController)
        """
        id = self.request.param("id")
        return Meal.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
        Get().route("/index", MealController)
        """
        return Meal.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", MealController)
        """
        days = self.request.input("days")
        subject = self.request.input("subject")
        meal = Meal.create({"days": days, "subject": subject})
        return meal

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
        Post().route("/update", MealController)
        """
        days = self.request.input("days")
        subject = self.request.input("subject")
        id = self.request.param("id")
        Meal.where("id", id).update({"days": days, "subject": subject})
        return Meal.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", MealController)
        """
        id = self.request.param("id")
        meal = Meal.where("id", id).get()
        Meal.where("id", id).delete()
        return meal
