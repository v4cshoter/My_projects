cook = {"Cook Book": [
    {"Dish A": ["oil", "bacon", "oil"]},
    {"Dish B": ["eggs", "oil", "eggs"]}
]}


def get_unique_key(cook_book):
    unique_ingredients = set()
    for dish in cook_book["Cook Book"]:
        for ingredients in dish.values():
            unique_ingredients.update(ingredients)
    return unique_ingredients


print(get_unique_key(cook))
