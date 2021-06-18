import streamlit as st


def show():
    st.write(
        """
        ## 💯 CRUD

        Basic Create, Read, Update and Delete Operations
        """
    )


    # initialize
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    with st.echo():
        st.write('Items in Session state', st.session_state)

    st.subheader('Print each item in a loop')
    with st.echo():
        for item in st.session_state.items():
            st.write(item)

    st.subheader('Print each key in a loop')
    with st.echo():
        for key in st.session_state.keys():
            st.write('Key:', key)

    st.subheader('Print each value in a loop')
    with st.echo():
        for value in st.session_state.values():
            st.write('Value:', value)

    st.subheader('Add a dictionary to Session state')
    st.session_state.my_dict = {
        'Peter': 'Pan'
    }

    st.write(st.session_state)

    st.subheader('Mutate the dictionary in Session state')
    st.session_state.my_dict['Peter'] = 'Pahn'

    st.write(st.session_state)

    st.subheader('Empty Session state')
    with st.echo():
        for key in st.session_state.keys():
            del st.session_state[key]

    st.write(st.session_state)