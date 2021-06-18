import streamlit as st

from . import counter
from . import crud
from . import forms
from . import two_sliders
from . import file_uploader
from . import state_exceptions



def show():

    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/279/joystick_1f579-fe0f.png",
        width=100,
    )
    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    counter.show()



def show_crud():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    crud.show()
    st.write("---")


def show_forms():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    forms.show()
    st.write("---")


def show_sliders():

    st.write(
        """
        # Try out Session State!
        One of the longest & most highly requested features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        """
    )

    st.write("---")
    two_sliders.show()
    st.write("---")


def show_file_uploader():

    st.write("---")
    file_uploader.show()
    st.write("---")


def show_exceptions():
    st.write("---")
    state_exceptions.show()
    st.write("---")


if __name__ == "__main__":
    show()