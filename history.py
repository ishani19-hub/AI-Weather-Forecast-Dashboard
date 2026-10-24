import json
import os


FILE_NAME = "history.json"



# -----------------------------
# Load Search History
# -----------------------------

def load_history():


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
# Save History
# -----------------------------

def save_history(history):


    with open(
        FILE_NAME,
        "w"
    ) as file:


        json.dump(
            history,
            file,
            indent=4
        )





# -----------------------------
# Add Search
# -----------------------------

def add_history(city):


    history = load_history()



    # Remove duplicate

    if city in history:

        history.remove(city)



    # Add latest search first

    history.insert(
        0,
        city
    )



    # Keep only last 10 searches

    history = history[:10]



    save_history(
        history
    )





# -----------------------------
# Clear History
# -----------------------------

def clear_history():


    save_history(
        []
    )