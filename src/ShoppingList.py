from src.Ingredient import Ingredient
from src.Recipe import Recipe

class ShoppingList:
    def __init__(self, _items: list):
        self._items = _items
        
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
        
    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        ingredients_dict = dict()
        
        for i, _ in self._items:
            key = (i.name, i.unit)
            ingredients_dict[key] = ingredients_dict.get(key, 0) + i.quantity

        ingredients_list = [Ingredient(name, ingredients_dict[(name, unit)], unit) for name, unit in ingredients_dict]
        ingredients_list = sorted(ingredients_list, key = lambda x: x.name)
        
        return ingredients_list

    def __add__(self, other: "ShoppingList"):
        new_list = ShoppingList(self._items + other._items)
        return new_list