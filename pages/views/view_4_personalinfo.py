import yaml
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
        height_col1, height_col2, _ = st.columns([1, 1, 1])
        weight_col1, weight_col2, _ = st.columns([1, 1, 1])
        fitness_col1, fitness_col2, _ = st.columns([1, 1, 1])
        health_col1, health_col2, _ = st.columns([1, 1, 1])
        preferences_col1, preferences_col2, _ = st.columns([1, 1, 1])
        place_col1, place_col2, _ = st.columns([1, 1, 1])

        personal_data = load_info()


        age_col1.write("## Please enter your age")
        individual_age = age_col2.text_input("-", f"{personal_data['age']}")

        height_col1.write("## Please enter your height (cm)")
        height = height_col2.text_input("-", f"{personal_data['height']}")

        weight_col1.write("## Please enter your current weight (Kg)")
        weight = weight_col2.text_input("-", f"{personal_data['weight']}")

        fitness_col1.write("## Please rate your fitness level")
        fitness_level = fitness_col2.slider("-", 1, 10, int(personal_data['fitness']))

        health_col1.write("## Do you have any of these conditions?")
        default_health = personal_data['health'].split(',') if personal_data['health'] else None
        health_condition = health_col2.multiselect("-", ['PCOS', 'Endometriosis', 'Menstrual irregularities'], default=default_health)

        preferences_col1.write("## Workout preferences")
        default_preferences = personal_data['preferences'].split(',') if personal_data['preferences'] else None
        workout_preferences = preferences_col2.multiselect("-", ['Yoga', 'Cardio', 'Strength training'], default=default_preferences)

        place_col1.write("## Workout facilities")
        default_place = personal_data['place-id'].split(',') if personal_data['place-id'] else None
        place_id = place_col2.multiselect("-", ['PT', 'Gym', 'Social'], default=default_place)

        update_button = st.button('Update data')

        if update_button:
            save_data(age=individual_age,
                      height=height,
                      weight=weight,
                      fit_level=fitness_level,
                      health=health_condition,
                      work_pref=workout_preferences,
                      place=place_id)


def save_data(age, height, weight, fit_level, health, work_pref, place):
    data = {
        'age': age,
        'height': height,
        'weight': weight,
        'fitness': fit_level,
        'health': ','.join(health),
        'preferences': ','.join(work_pref),
        'place-id': ','.join(place)
    }
    with open('data/info.yaml', 'w+') as f:
        for key, value in data.items():
            f.write(f'{key}: {value}\n')


def load_info(filename='data/info.yaml'):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return None
