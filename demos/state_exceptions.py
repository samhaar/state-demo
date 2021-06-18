import streamlit as st


def show():
    st.write(
        """
        ## 💯 Exceptions

        Reload the app to get rid of the exception
        """
    )

    st.subheader('File Uploader Exception')
    with st.echo():
        def uploaded():
            # Trying to set the state of File Uploader via the session state API
            # should throw an exception
            st.session_state.my_file_uploader = 'x'

        files = st.file_uploader('Upload a file', key='my_file_uploader', on_change=uploaded)

    st.write('---')

    st.subheader('Button Exception')
    with st.echo():
        def callback():
            # Trying to set the state of the button via the session state API
            # should throw an exception
            st.session_state.my_file_uploader = 'x'

        st.button(label='Submit', key='my_button', on_change=callback)

    st.write('---')

    st.subheader('Key Error Exception')
    with st.echo():
        if st.checkbox(label='Check to see exception'):
            st.write(st.session_state.undefined_key)

    st.write('---')
    st.subheader('Form Widget Callback Exception')
    with st.echo():
        # Trying to define a callback for an individual widget
        # inside a form throws an exception
        def form_callback():
            st.write('Inside form callback')

        if st.checkbox(label='Check to see exception', key='form_checkbox'):
            with st.form(key='my_form'):
                checkbox = st.checkbox('Toggle me', on_change=form_callback)
                submit = st.form_submit_button(label='Submit')

    st.write('---')

    st.subheader('Setting state via API after Widget declaration')
    with st.echo():
        # Trying to define a callback for an individual widget
        # inside a form throws an exception
        def form_callback():
            st.write('Inside form callback')

        if st.checkbox(label='Check to see exception', key='form_checkbox'):
            with st.form(key='my_form'):
                checkbox = st.checkbox('Toggle me', on_change=form_callback)
                submit = st.form_submit_button(label='Submit')