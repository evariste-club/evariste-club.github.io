
import streamlit as st
from utils import footer, layout

layout.load()


st.markdown('<h2 class="section-header">📅 Upcoming Events</h2>', unsafe_allow_html=True)

# Event calendar
events = [
    {
        "name": "ProSort Euler Competition",
        "date": "2024-02-15",
        "time": "10:00 AM",
        "location": "IIIT-D Campus",
        "description": "Mathematical problem-solving competition with FooBar for ESYA'25"
    },
    {
        "name": "Linear Algebra Workshop",
        "date": "2024-02-20",
        "time": "2:00 PM",
        "location": "Room 301",
        "description": "Deep dive into eigenvalues, eigenvectors, and matrix decompositions"
    },
    {
        "name": "CTF Challenge Day",
        "date": "2024-02-25",
        "time": "11:00 AM",
        "location": "Computer Lab",
        "description": "Hands-on cybersecurity challenges with our custom CTF boxes"
    }
]

for event in events:
    st.markdown('<div class="event-card">', unsafe_allow_html=True)
    st.markdown(f"""
    ### 🎯 {event['name']}
    **📅 Date:** {event['date']} at {event['time']}
    **📍 Location:** {event['location']}
    **📝 Description:** {event['description']}
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.button("Register", key=f"reg_{event['name']}")
    with col2:
        st.button("Add to Calendar", key=f"cal_{event['name']}")
    st.markdown('</div>', unsafe_allow_html=True)


footer.load()
