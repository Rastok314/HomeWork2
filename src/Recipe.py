from src.Ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")
        else:
            new_recipe = Recipe(self.title, [])
            for i in self.ingredients:
                ingredient = Ingredient(i.name, i.quantity*ratio, i.unit)
                new_recipe.add_ingredient(ingredient)
        return new_recipe
            
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        ingredients = "\n".join(str(i) for i in self.ingredients)
        return f"{self.title}\n{ingredients}"