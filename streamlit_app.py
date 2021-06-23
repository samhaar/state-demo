import sys
from pathlib import Path

# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))

# try:
#     sys.path.remove(str(parent))
# except ValueError:  # Already removed
#     pass

import streamlit as st

#VERSION = ".".join(st.__version__.split(".")[:2])
# st.set_page_config(page_title=f"New features in Streamlit {VERSION}")

from demos import session_state

previous_version = "0.82.0"
demo_pages = {
    "Counter": session_state.show,
    "Crud": session_state.show_crud,
    'Forms': session_state.show_forms,
    '2 sliders': session_state.show_sliders,
    'File Uploader': session_state.show_file_uploader,
    'Exceptions': session_state.show_exceptions,
    'Widgets API': session_state.show_widgets,
}



contributors = []

intro = f"""
Launch candidate for Session State
"""

release_notes = f"""
---
**Key Features**
- CRUD
- Iteration
- Callbacks
- Misc Features
    - **Clear Cache** clears the state
    - `st.forms` interactions work
    - `st.file_uploader` interactions look good


**Error Scenarios**
- Key or Attribute Errors when trying to access undefined variables
- Trying to set state using the `key` for `st.button` and `st.file_uploader` throws an exception
- Trying to set the state via the API after widget declaration throws a warning
- Throw a warning when state is set via the API and then at widget declaration time there is a default value
- Defining a callback for an individual widget inside a `st.form`

**Apps**
- Linked Sliders
"""
# End release updates


def draw_main_page():
    st.write(
        f"""
        # Prototype based off Streamlive v{VERSION}!
        """
    )

    st.write(intro)

    st.write(release_notes)


# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    pages.insert(0, "Release Notes")
    st.sidebar.title(f"State Demos")
    query_params = st.experimental_get_query_params()
    # TODO: This doesn't work yet. Locally it actually works, but on Streamlit Sharing 
    #   it doesn't somehow. The query params are actually read and parsed correctly, 
    #   but it doesn't manage to set the index based on it. Seems to be a weird 
    #   interaction between the widget value in session state and value given in arg.
    #   See if this is fixed in final session state version.
    if "page" in query_params and query_params["page"][0] == "headliner":
        index = 1
    else:
        index = 0
    selected_demo = st.sidebar.radio("", pages, index, key="pages")
else:
    selected_demo = "Release Notes"

# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
else:
    draw_main_page()
