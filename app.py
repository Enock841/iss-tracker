import streamlit as st
from get_position import get_iss_position

st.title("ISS TRACKER")
result = get_iss_position()
if result is None:
    st.error("ISS data couldn't be loaded")
else:
    lat,lon,when = result
    st.metric("Latitude",f"{lat:.2f}")
    st.metric("Longitude",f"{lon:.2f}")
    st.write(f"Last updated: {when.strftime('%H:%M:%S')} UTC")
