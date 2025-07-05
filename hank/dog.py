import numpy as np
import random
import pandas as pd

class Hank:
    def __init__(self, name="Hank", age=3, favorite_toy="ball"):
        self.name = name
        self.age = age
        self.favorite_toy = favorite_toy
        self.treat_log = pd.DataFrame(columns=['treat_name', 'num_treats', 'timestamp'])

    def greet(self):
        return f"Hi! I'm {self.name}, a {self.age}-year-old good boy who loves {self.favorite_toy}!"

    def bark(self):
        return "Woof! 🐾"

    def random_fact(self):
        facts = [
            f"{self.name} loves peanut butter.",
            f"{self.name} knows how to sit, stay, and high five!",
            f"{self.name} is a very good boy.",
            f"{self.name} once chased 3 squirrels in 5 minutes.",
        ]
        return random.choice(facts)

    def fetch(self, toy=None):
        if toy is None:
            toy = self.favorite_toy
        return f"{self.name} fetches the {toy} and brings it back to you!"
    
    def sleep(self):
        return f"{self.name} is now sleeping peacefully. Zzz... 💤"
    
    def give_hank_treat(self, treat="dog biscuit", num_treats = 1):

        # First log the treat being given
        treat_log = {
            'treat_name': treat,
            'num_treats': num_treats,
            'timestamp': np.datetime64('now', 's')
        }

        # Create a DataFrame with a single row
        df = pd.DataFrame([treat_log])

        # Append the new row to the existing treat_log DataFrame
        self.treat_log = pd.concat([self.treat_log, df], ignore_index=True)

        return f"{self.name} happily accepts a {treat} and wags his tail! 🐶"
    
    def get_treat_log(self):
        if self.treat_log.empty:
            return "No treats have been given yet."
        else:
            return self.treat_log
    

    
