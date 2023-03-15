from streamlit import markdown, warning, error, success


class Utils:
    @staticmethod
    def remove_watermark():
        """ 
        Hide: 'Made with Streamlit'
        """
        hide_streamlit_style = "<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>"
        markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    @staticmethod
    def node_warning():
        warning("Warning.")
    
    @staticmethod
    def annotation_warning():
        warning("Warning.")
    
    @staticmethod
    def everything_warning():
        warning("Warning.")
    
    @staticmethod
    def interaction_error(file_type:str):
        error(f"Error.")
    
    @staticmethod
    def model_trained():
        success("Success!")
    
    @staticmethod
    def model_not_trained():
        error("Error!")


class Terminal_Colors:
    header = "\033[95m"
    okblue = "\033[94m"
    okcyan = "\033[96m"
    okgreen = "\033[92m"
    warning = "\033[93m"
    fail = "\033[91m"
    endc = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"
