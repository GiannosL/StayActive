import os

from pages.views.view_3_workoutdesign import load_info

class DoTests:
    def test_find_info(self):
        assert os.path.isfile('../data/info.yaml')

    def test_find_workout(self):
        assert os.path.isfile('../data/workout.yaml')

    def test_number_of_entries(self):
        data = load_info()
        assert len(data) == 5