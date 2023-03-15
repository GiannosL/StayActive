class TestDummyData:

    def find_exercises(self):
        import os

        assert os.path.isfile('../data/info.yaml')