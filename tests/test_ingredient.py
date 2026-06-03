import pytest

from src.Ingredient import Ingredient

def test_creation():
    ingredient = Ingredient("Мука", 500, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

def test_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_eq_different_quantity():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 200, "г")
    assert ing1 == ing2

def test_eq_different_name():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Сахар", 500, "г")
    assert ing1 != ing2

def test_eq_different_unit():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 500, "тонн")
    assert ing1 != ing2