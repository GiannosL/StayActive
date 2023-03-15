import streamlit as st

from pages.utilities.my_utils import Utils


class ExercisesView:
    @staticmethod
    def run() -> None:
        # remove watermark
        Utils.remove_watermark()

        # page title
        mond, thurs, satur = st.columns([1, 1, 1])

        with mond:
            st.write('# Monday')
            
            compl_btn2 = st.button('Workout Completed!')
            if compl_btn2:
                st.success('Workout completed')

            st.write('### Personal Training')

            workout = {'Exercise': ['plank', 'lunge', 'wall sits', 'static bicep curls'],
                       'Sets': ['5', '3', '3', '5']}
            
            st.table(workout)
            st.write('')
            # plank
            st.video(data='https://www.youtube.com/watch?v=pSHjTRCQxIw&ab_channel=ScottHermanFitness')
            # lunge
            st.video('https://www.youtube.com/watch?v=QOVaHwm-Q6U&ab_channel=Bowflex')
            # wall sits
            st.video('https://www.youtube.com/watch?v=-cdph8hv0O0&ab_channel=FitnessBlender')
            # static bicep curls
            st.video('https://www.youtube.com/watch?v=vtoUmOEJXYA&ab_channel=Strong%27N%27SexyFitness')

        with thurs:
            st.write('# Thursday')

            compl_btn1 = st.button('Workout Completed! ')
            if compl_btn1:
                st.success('Workout completed')

            st.write('### Yoga')

            st.video('https://www.youtube.com/watch?v=j7rKKpwdXNE&ab_channel=YogaWithAdriene')
            

        with satur:
            st.write('# Saturday')

            compl_btn3 = st.button('Workout Completed!  ')
            if compl_btn3:
                st.success('Workout completed')

            st.write('### Bodycombat')

            st.video('https://www.youtube.com/watch?v=xbABGepKT2o&ab_channel=LesMills')
