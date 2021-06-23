import streamlit as st
import datetime


def show():
    st.write(
        """
        ## 💯 Validating that widgets work with Session State

        Reload the app to get rid of any exceptions
        """)

    st.subheader('Date Input')
    with st.echo():
        if 'my_date' not in st.session_state:
            st.session_state.my_date = datetime.date(2019, 7, 6)
        st.date_input(label='When is your birthday?', key='my_date')

    st.write('---')

    st.subheader('Time Input')
    with st.echo():
        if 'my_time' not in st.session_state:
            st.session_state.my_time = datetime.time(8, 45)

        st.time_input(label='Set an alarm for', key='my_time')

    st.write('---')