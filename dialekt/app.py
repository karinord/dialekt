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

#num_new_rows = st.sidebar.number_input("Add Rows",1,50)
ncol = st.session_state.df.shape[1]  # col count
rw = -1

with st.form(key="add form", clear_on_submit= True):
    cols = st.columns(ncol)
    rwdta = []

    for i in range(ncol):
        rwdta.append(cols[i].text_input(st.session_state.df.columns[i]))

    # you can insert code for a list comprehension here to change the data (rwdta) 
    # values into integer / float, if required

    if st.form_submit_button("Legg til"):
            rw = st.session_state.df.shape[0] + 1
            st.session_state.df.loc[rw] = rwdta

st.subheader("Oversikt over poster")

#st.dataframe(st.session_state.df)
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")



"""import streamlit as st
import pandas as pd

 



df = pd.DataFrame(
    [
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
       {" ": "et", "Dialektord": "kådn", "Betydning": "korn", "Bøying": "kådn-kåddne-kådn-kåddne", "Bruk": "", "Merknader": "test", "tvil": True, "Endring": "rn -> dn"},
   ]
)

edited_df = st.data_editor(df, num_rows="dynamic")
"""
 

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

#st.markdown(f"Your favorite command is **{favorite_command}** 🎈")