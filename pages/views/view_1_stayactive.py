import streamlit as st

from pages.utilities.my_utils import Utils


class StayActiveView:
    @staticmethod
    def run() -> None:
        # multiple pages with wide view
        st.set_page_config(page_title="Eve", layout="wide")

        # remove watermark
        Utils.remove_watermark()

        # page title
        st.write("# StayActive")

        # 
        st.write("## How are you feeling today?")
        feeling_meter = st.slider("Physical state", 0, 10, 5)
