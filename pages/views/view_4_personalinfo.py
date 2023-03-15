import streamlit as st

from pages.utilities.my_utils import Utils

class PersonalInfoView:
    @staticmethod
    def run() -> None:
        # remove watermark
        Utils.remove_watermark()

        # page title
        st.write("# Personal data")
        st.write("---")

        age_col1, age_col2, _ = st.columns([1, 1, 1])
        weight_col1, weight_col2, _ = st.columns([1, 1, 1])
        height_col1, height_col2, _ = st.columns([1, 1, 1])
        fitness_col1, fitness_col2, _ = st.columns([1, 1, 1])
        health_col1, health_col2, _ = st.columns([1, 1, 1])
        preferences_col1, preferences_col2, _ = st.columns([1, 1, 1])
        place_col1, place_col2, _ = st.columns([1, 1, 1])


        age_col1.write("## Please enter your age")
        individual_age = age_col2.text_input("", "20")

        height_col1.write("## Please enter your height (cm)")
        height = height_col2.text_input("", "180")

        weight_col1.write("## Please enter your current weight (Kg)")
        weight = weight_col2.text_input("", "80")

        fitness_col1.write("## Please rate your fitness level")
        fitness_level = fitness_col2.slider("", 1, 10, 1)

        health_col1.write("## Do you have any of these conditions?")
        health_condition = health_col2.multiselect("", ['PCOS', 'Endometriosis', 'Menstrual irregularities'])

        preferences_col1.write("## Workout preferences")
        workout_preferences = preferences_col2.multiselect("", ['Yoga', 'Cardio', 'Strength training'])

        place_col1.write("## Workout facilities")
        place_id = place_col2.multiselect("", ['PT', 'Gym', 'Social'])

        update_button = st.button('Update data')




