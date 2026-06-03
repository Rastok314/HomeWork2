import pytest

from src.Ingredient import Ingredient
from src.Recipe import Recipe

def test_recipe_creation():
    ing = Ingredient("Мука", 500, "г")
    recipe = Recipe("Пицца", [ing])

    assert recipe.title == "Пицца"
    assert recipe.ingredients == [ing]

def test_add_new():
    recipe = Recipe("Пицца", [])

    ing = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(ing)

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ing

def test_add_existing():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 200, "г")

    recipe = Recipe("Пицца", [ing1])
    recipe.add_ingredient(ing2)

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 700.0
    
def test_scale_returns_new():
    ing = Ingredient("Мука", 500, "г")
    recipe = Recipe("Пицца", [ing])

    scaled = recipe.scale(2)

    assert scaled is not recipe
    assert isinstance(scaled, Recipe)

def test_scale_multiplies_quantity():
    ing = Ingredient("Мука", 500, "г")
    recipe = Recipe("Пицца", [ing])

    scaled = recipe.scale(2)

    assert scaled.ingredients[0].quantity == 1000.0
    
def test_len():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Сахар", 200, "г")

    recipe = Recipe("Пицца", [ing1, ing2])

    assert len(recipe) == 2