import streamlit as st


def show():
    st.write(
        """
        ## 💯 File Uploader

        Callbacks with File Uploader
        """
    )

    def uploaded():
        st.write('Inside the file uploader callback')

    files = st.file_uploader('Upload a file', key='my_file_uploader', on_change=uploaded)
    st.write(st.session_state.my_file_uploader)