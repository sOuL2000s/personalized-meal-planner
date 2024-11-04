import random

# Sample meal options based on dietary preferences
meals = {
    "Vegetarian": ["Veggie Salad", "Lentil Soup", "Tofu Stir-fry", "Vegetable Pasta"],
    "Vegan": ["Quinoa Salad", "Vegan Wrap", "Vegetable Curry", "Fruit Smoothie"],
    "Keto": ["Grilled Chicken Salad", "Cauliflower Rice", "Keto Pancakes", "Avocado Omelette"]
}

# Function to create a meal plan
def generate_meal_plan(diet_type, calories_per_meal):
    if diet_type not in meals:
        return "Diet type not available. Please choose from Vegetarian, Vegan, or Keto."
    
    plan = {}
    for day in ["Monday", "Wednesday", "Friday"]:
        plan[day] = {
            "Breakfast": random.choice(meals[diet_type]),
            "Lunch": random.choice(meals[diet_type]),
            "Dinner": random.choice(meals[diet_type]),
            "Calories": calories_per_meal
        }
    return plan

# User input
diet_type = "Vegan"  # Example diet type
calories_per_meal = 500  # Example calorie goal per meal

# Generate meal plan
meal_plan = generate_meal_plan(diet_type, calories_per_meal)
print("Your Meal Plan:")
for day, details in meal_plan.items():
    print(f"\n{day}:")
    for meal, item in details.items():
        print(f"{meal}: {item}")
