from src.Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        self.diet_type = diet_type
        super().__init__(title, ingredients or [])

    def scale(self, ratio: float):
        temp = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, temp.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"