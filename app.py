import streamlit as st
from get_position import get_iss_position, history_to_dataframe
from weather import get_weather, format_weather
from location import get_location

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

        loca = get_location(lat, lon)
        if loca is None:
            st.write("ISS is over water")
        else:
            st.write(f"Currently over: {loca}")

        weath = get_weather(lat,lon)
        if weath is None:
            st.warning("Weather unavailable")
        else:
            temp,cloud,wind = weath
            st.write(format_weather(temp,cloud,wind))

        
        st.map(df, zoom= 6)

show_tracker()
