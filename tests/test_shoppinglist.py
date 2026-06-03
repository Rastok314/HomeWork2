import pytest

from src.ShoppingList import ShoppingList
from src.Recipe import Recipe
from src.Ingredient import Ingredient

def test_add_items():
    recipe = Recipe("Пицца", [])
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))

    sl = ShoppingList([])
    sl.add_recipe(recipe, 2)

    assert len(sl._items) == 1

    ingredient, title = sl._items[0]

    assert title == "Пицца"
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 1000
    assert ingredient.unit == "г"

def test_invalid_portions():
    recipe = Recipe("Пицца", [])

    sl = ShoppingList([])

    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)
        
def test_remove_recipe():
    recipe = Recipe("Пицца", [])
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))

    sl = ShoppingList([])
    sl.add_recipe(recipe, 1)
    sl.remove_recipe("Пицца")

    assert len(sl._items) == 0

def test_no_error():
    sl = ShoppingList([])
    sl.remove_recipe("Bobik")

def test_get_sum():
    r1 = Recipe("Пицца", [])
    r1.add_ingredient(Ingredient("Мука", 500, "г"))

    r2 = Recipe("Хлеб", [])
    r2.add_ingredient(Ingredient("Мука", 200, "г"))

    sl = ShoppingList([])
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)

    result = sl.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 700

def test_get_list_sorted():
    r = Recipe("Test", [])
    r.add_ingredient(Ingredient("Рис", 1, "кг"))
    r.add_ingredient(Ingredient("Греча", 1, "кг"))

    sl = ShoppingList([])
    sl.add_recipe(r, 1)

    result = sl.get_list()

    names = [i.name for i in result]
    assert names == sorted(names)

def test_add_shopping_lists():
    r1 = Recipe("Пицца", [])
    r1.add_ingredient(Ingredient("Мука", 500, "г"))

    r2 = Recipe("Хлеб", [])
    r2.add_ingredient(Ingredient("Мука", 200, "г"))

    sl1 = ShoppingList([])
    sl2 = ShoppingList([])

    sl1.add_recipe(r1, 1)
    sl2.add_recipe(r2, 1)

    sl1_before = sl1._items.copy()
    sl2_before = sl2._items.copy()

    sl3 = sl1 + sl2

    assert len(sl3._items) == len(sl1_before) + len(sl2_before)
    assert sl1._items == sl1_before
    assert sl2._items == sl2_before