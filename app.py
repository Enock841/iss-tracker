import streamlit as st
from get_position import get_iss_position, history_to_dataframe

st.title("ISS Tracker")

if "history" not in st.session_state:
    st.session_state.history = []    

@st.fragment(run_every=10)

def show_tracker():
    result = get_iss_position()
    if result is None:
        st.error("ISS data couldn't be loaded")
    else:
        st.session_state.history.append(result)
        lat,lon,when = result
        st.metric("Latitude",f"{lat:.2f}")
        st.metric("Longitude",f"{lon:.2f}")
        st.write(f"Last updated: {when.strftime('%H:%M:%S')} UTC")
        df = history_to_dataframe(st.session_state.history)
        st.write(f"Positions collected: {len(st.session_state.history)}")
        
        st.map(df)

show_tracker()
