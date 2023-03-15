import pandas as pd


class StayActiveViewModel:
    @staticmethod
    def fetch_schedule():
        default_workouts = {'Day':['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 
                            'Workout': ['-', '-', '-', '-', '-'],
                            'Location': ['-', '-', '-', '-', '-'],}
        df = pd.DataFrame(default_workouts)
        
        return df