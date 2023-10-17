import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from .models import Room


class RoomSuggestionModel:
    def __init__(self):
        self.model = None

    def train(self):
        # Load the dataset from the Room model
        rooms = Room.objects.all()
        df = pd.DataFrame(list(rooms.values()))

        # Preprocess the data
        X = df[["price_per_day", "num_beds"]]
        y = df["room_type"]

        # Train the machine learning model
        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def save_model(self, model_path):
        # Save the trained model
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        # Load the trained model
        self.model = joblib.load(model_path)

    def predict_suggested_room(self, user_preferences):
        # Preprocess user preferences
        user_preferences = pd.DataFrame(
            {
                "price_per_day": [user_preferences["price_per_day"]],
                "num_beds": [user_preferences["num_beds"]],
            }
        )

        # Make room suggestions
        suggested_room_type = self.model.predict(user_preferences)

        return suggested_room_type
