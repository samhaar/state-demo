import streamlit as st


def show():
    st.write(
        """
        ## 💯 Two Sliders

        Mirror two sliders
        """
    )

    to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
    to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

    MIN_CELSIUS, MAX_CELSIUS = -100.0, 100.0

    state = st.session_state

    if 'celsius' not in st.session_state:
        state.celsius = MIN_CELSIUS

    # Callbacks if something changes
    def celsius_changed():
        celsius = state.celsius
        state.fahrenheit = to_fahrenheit(celsius)

    def fahrenheit_changed():
        fahrenheit = state.fahrenheit
        state.celsius = to_celsius(fahrenheit)

    # Display the sliders.
    st.slider("Celsius",
              min_value=MIN_CELSIUS,
              max_value=MAX_CELSIUS,
              on_change=celsius_changed, key='celsius')

    st.slider("Fahrenheit",
              min_value=to_fahrenheit(MIN_CELSIUS),
              max_value=to_fahrenheit(MAX_CELSIUS),
              value=to_fahrenheit(state.celsius),
              on_change=fahrenheit_changed, key='fahrenheit')

    st.write('Celsius', state.celsius)
    st.write('Fahrenheit', state.fahrenheit)