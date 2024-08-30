spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    """Return a list of the spiciest foods."""
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    """Print the names of spicy foods."""
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return a list of spicy foods from a specific cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    """Print the names of the spiciest foods."""
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """Return the average heat level of spicy foods."""
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list."""
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
