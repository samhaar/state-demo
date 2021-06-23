import streamlit as st


def show():
    st.write(
        """
        ## 💯 Forms

        Manipulate widgets within a form and show write them to the screen
        """
    )

    def form_callback():
        # Access or manipulate form element state via keys
        st.write(st.session_state.my_slider)
        st.write(st.session_state.my_checkbox)

        st.session_state.my_slider = 7

    with st.form(key='my_form'):
        slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
        checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
        submit_button = st.form_submit_button(label='Submit', on_click=form_callback)