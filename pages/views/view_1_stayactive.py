import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from pages.utilities.my_utils import Utils
from pages.view_models.view_model_stayactive import StayActiveViewModel


class StayActiveView:
    @staticmethod
    def run() -> None:
        # multiple pages with wide view
        st.set_page_config(page_title="Eve", layout="wide")

        # remove watermark
        Utils.remove_watermark()

        # page title
        st.write("# Eve")
        st.write('## Stay active')
        st.write('---')

        # 
        st.write("### How are you feeling today?")
        feeling_meter = st.slider("Physical state", 0, 10, 5)
        st.write('')

        upcoming_col, update_col = st.columns([1, 1])

        upcoming_col.dataframe(StayActiveViewModel.fetch_schedule())

        update_col.write('Do you want to update your progress?')
        update_btn = update_col.button('Update')

        if update_btn:
            switch_page("personal info")
