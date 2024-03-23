import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Registrering av dialektord")
st.text("Dette er en oversikt over dialektord og betydning.") 

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
       {"Prefiks": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {"Prefiks": "ein", "Dialektord": "massjin", "Betydning": "maskin", "Bøying": "massjin-massjin-massjinar-massjinane", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "sk-> sj"},
       {"Prefiks": "å", "Dialektord": "siddja", "Betydning": "sitte", "Bøying": "siddja-sete-sat-sote", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "tte -> ddj"},
   ])

st.subheader("Ny registrering")

# Function to create input field based on column data type
def create_input_field(col_name, col_type):
    if col_name in ["Merknader", "Bruk"]:
        return st.text_area(label=col_name)
    else:
        if col_type == "object":
            return st.text_input(label=col_name)
        elif col_type == "int64":
            return st.number_input(label=col_name)
        elif col_type == "bool":
            return st.checkbox(label=col_name)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
       {"Prefiks": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {"Prefiks": "ein", "Dialektord": "massjin", "Betydning": "maskin", "Bøying": "massjin-massjin-massjinar-massjinane", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "sk-> sj"},
       {"Prefiks": "å", "Dialektord": "siddja", "Betydning": "sitte", "Bøying": "siddja-sete-sat-sote", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "tte -> ddj"},
   ])

# Initialize the index for the new row
new_row_index = -1

# Create a form for adding new data
with st.form(key="add form", clear_on_submit=True):
    # Get the number of columns in the DataFrame
    number_of_columns = st.session_state.df.shape[1]

    # Initialize an empty list to store user input
    user_input = []

    # Iterate over DataFrame columns
    for col_name, col_type in st.session_state.df.dtypes.items():
        # Create input field based on column data type
        user_input.append(create_input_field(col_name, str(col_type)))

    # Add a submit button to the form
    submit_button = st.form_submit_button(label="Legg til")

# Task 2: Append user input to the dataframe st.session_state.df

# If the form is submitted
if submit_button:
    # Initialize an empty dictionary to store user input
    new_row = {}

    # Iterate over DataFrame columns and user input
    for col_name, input_value in zip(st.session_state.df.columns, user_input):
        # Append user input to the dictionary
        new_row[col_name] = input_value

    # Append the new row to the DataFrame
    new_row_index = st.session_state.df.shape[0] + 1
    #st.session_state.df = st.session_state.df.append(new_row, ignore_index=True)
    st.session_state.df.loc[new_row_index] = new_row

st.subheader("Oversikt over poster")

edited_df = st.data_editor(st.session_state.df)

