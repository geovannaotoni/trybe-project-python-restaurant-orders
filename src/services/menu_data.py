import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader

            for name, price, ingredient, recipe_amount in data:
                new_dish = Dish(name, float(price))
                new_ingr = Ingredient(ingredient)

                if new_dish not in self.dishes:
                    new_dish.add_ingredient_dependency(
                        new_ingr, int(recipe_amount)
                    )
                    self.dishes.add(new_dish)
                else:
                    for dish in self.dishes:
                        if dish.name == name:
                            dish.add_ingredient_dependency(
                                new_ingr, int(recipe_amount)
                            )
