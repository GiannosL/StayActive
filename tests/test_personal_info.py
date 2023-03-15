import os
from pages.views.view_3_workoutdesign import load_info
from pages.views.view_4_personalinfo import load_info as load_info4

class TestFiles:
    def test_find_info(self):
        assert os.path.isfile('data/info.yaml')

    def test_find_workout(self):
        assert os.path.isfile('data/workout.csv')

    def test_number_of_entries(self):
        data = load_info()
        assert len(data) == 4

    def test_info_variables(self):
        variables = ['age', 'height', 'weight', 'fitness', 'health', 'preferences', 'place-id']
        data = load_info4()

        for var in variables:
            assert var in data