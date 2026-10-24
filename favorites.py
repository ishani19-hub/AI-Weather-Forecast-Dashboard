import json
import os


FILE_NAME = "favorites.json"



# -----------------------------
# Load Favorites
# -----------------------------

def load_favorites():

    if not os.path.exists(FILE_NAME):

        return []


    try:

        with open(
            FILE_NAME,
            "r"
        ) as file:


            return json.load(file)



    except:

        return []





# -----------------------------
# Save Favorites
# -----------------------------

def save_favorites(favorites):


    with open(
        FILE_NAME,
        "w"
    ) as file:


        json.dump(
            favorites,
            file,
            indent=4
        )





# -----------------------------
# Add Favorite
# -----------------------------

def add_favorite(city):


    favorites = load_favorites()


    if city not in favorites:


        favorites.append(city)


        save_favorites(
            favorites
        )


        return True



    return False





# -----------------------------
# Remove Favorite
# -----------------------------

def remove_favorite(city):


    favorites = load_favorites()


    if city in favorites:


        favorites.remove(city)


        save_favorites(
            favorites
        )


        return True



    return False
