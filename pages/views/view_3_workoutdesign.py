import yaml
import pandas as pd
import streamlit as st

from pages.utilities.my_utils import Utils


class WorkoutDesignView:
    @staticmethod
    def run() -> None:

        # remove watermark
        Utils.remove_watermark()

        st.write('# Design your workouts')
        st.write('---')
        exercise_selection = load_info()

        chest = st.multiselect('Select chest exercises', exercise_selection['chest'].split(','), max_selections=3)
        st.write('\n')
        back = st.multiselect('Select back exercises', exercise_selection['back'].split(','), max_selections=3)
        st.write('\n')
        legs = st.multiselect('Select legs exercises', exercise_selection['legs'].split(','), max_selections=3)
        st.write('\n')
        shoulders = st.multiselect('Select shoulders exercises', exercise_selection['shoulders'].split(','), max_selections=3)
        st.write('\n')

        create_btn = st.button('Create workout program')
        if create_btn:
            generate_program([chest, back, legs, shoulders])

            st.write('# Workout suggestion')
            st.write('---')
            workout = pd.read_csv('data/workout.csv')
            st.table(workout)
        
        

def load_info(filename='data/exercises.yaml'):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return None


def generate_program(my_lists):
    from random import randint

    with open('data/workout.csv', 'w+') as f:
        f.write('exercise,sets,reps\n')
        for body_part in my_lists:
            for exercise in body_part:
                f.write(f'{exercise},{randint(3, 5)},{randint(8, 20)}\n')
