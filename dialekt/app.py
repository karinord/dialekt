import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Registrering av dialektord")
st.text("Dette er en oversikt over dialektord og betydning.") 

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
   ])

st.subheader("Ny registrering")

# Get the number of columns in the DataFrame
number_of_columns = st.session_state.df.shape[1]

# Initialize the index for the new row
new_row_index = -1

# Create a form for adding new data
with st.form(key="add form", clear_on_submit= True):
    cols = st.columns(number_of_columns)
    new_row = []

    for i in range(number_of_columns):
        new_row.append(cols[i].text_input(st.session_state.df.columns[i]))

    if st.form_submit_button("Legg til"):
            new_row_index = st.session_state.df.shape[0] + 1
            st.session_state.df.loc[new_row_index] = new_row

st.subheader("Oversikt over poster")

edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")


