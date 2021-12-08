"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "MealController@index").name("index"),
        Get("/@id", "MealController@show").name("show"),
        Post("/", "MealController@create").name("create"),
        Put("/@id", "MealController@update").name("update"),
        Delete("/@id", "MealController@destroy").name("destroy")
    ], prefix="/meals", name="meals")
]
