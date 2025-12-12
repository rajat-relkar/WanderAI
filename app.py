import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itineary Planner")
st.write("Plan your itineary by entering number of days for the trip, your city and interests")

load_dotenv()

with st.form("planner_form"):
    days = st.text_input("Enter number of days for your trip (enter an integer value)")
    city = st.text_input("Enter the city you want to visit")
    interests = st.text_input("Enter your interests (comma-seperated)")
    submitted = st.form_submit_button("Generate Itineary")

    if submitted:
        if days and city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_days(days)
            planner.set_interests(interests)
            itineary = planner.create_itineary()

            st.subheader("📄 Your Itineary")
            st.markdown(itineary)

        else:
            st.warning("Please fill Days, City or Interest to move forward")


