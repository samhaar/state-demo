import streamlit as st


def show():
    st.write(
        """
        ## 💯 Counter

        The most basic example: Store a count in `st.session_state` and increment when clicked.
        """
    )
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    def increment():
        st.session_state.counter += 1

    def increment_by_value(value):
        st.session_state.counter += value

    def increment_by_value_kwargs(value=1):
        st.session_state.counter += value

    st.write("Counter:", st.session_state.counter)

    st.subheader('Simple Callback')
    with st.echo():
        st.button("Plus one!", on_change=increment)

    value = st.number_input('Enter a value', value=0, step=1)

    st.subheader('Callback with Args')
    with st.echo():
        st.button('Plus Value', on_change=increment_by_value, args=(value, ))

    st.subheader('Callback with kwargs')
    with st.echo():
        st.button('Plus Default value', on_change=increment_by_value_kwargs)

    st.subheader('Callback with kwargs')
    with st.echo():
        st.button('Plus Input value', on_change=increment_by_value_kwargs, kwargs=dict(value=value))