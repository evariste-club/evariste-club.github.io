import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import requests
import markdown

# Page configuration
st.set_page_config(
    page_title="Évariste - IIIT-D Math Club",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #3498db;
    }
    .event-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .math-formula {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #e74c3c;
        font-family: 'Courier New', monospace;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 🧮 Évariste Math Club")
st.sidebar.markdown("---")

# Navigation menu
page = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Home", "📚 Study Materials", "🎯 ProSort Euler", "🔐 PWNHUB CTF", "📝 Blog", "📅 Events", "👥 About Us"]
)

# Home page
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Évariste</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #7f8c8d;">IIIT-D\'s Premier Mathematics Club</h2>', unsafe_allow_html=True)
    
    # Welcome section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎉 Welcome to Évariste!
    
    Welcome to the brand new website for Évariste, IIIT-D's math club! Here, you can find all the resources 
    you need to get involved with the club, including information about upcoming events, study materials, 
    past question papers, and more.
    
    Our mission is to foster a love for mathematics and create a community of passionate learners who 
    explore the beauty and elegance of mathematical concepts together.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Members", "45+", "↗️ +12%")
    with col2:
        st.metric("Events This Month", "8", "↗️ +3")
    with col3:
        st.metric("Study Sessions", "24", "↗️ +6")
    with col4:
        st.metric("CTF Challenges", "15", "↗️ +5")
    
    # Featured content
    st.markdown('<h3 class="section-header">🚀 What's New</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="event-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🎯 ProSort Euler
        **New Event with FooBar for ESYA'25!**
        
        Join us for an exciting mathematical challenge that combines problem-solving with competitive programming.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="event-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🔐 PWNHUB CTF
        **Capture The Flag Challenges**
        
        Test your cybersecurity skills with our custom CTF boxes - Ellie and Benjamin!
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Study Materials page
elif page == "📚 Study Materials":
    st.markdown('<h2 class="section-header">📚 Study Materials</h2>', unsafe_allow_html=True)
    
    # Subject categories
    subjects = ["Linear Algebra", "Calculus", "Number Theory", "Graph Theory", "Combinatorics", "Probability"]
    selected_subject = st.selectbox("Select Subject:", subjects)
    
    if selected_subject == "Linear Algebra":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Linear Algebra Resources
        
        **Core Topics:**
        - Vector Spaces and Subspaces
        - Linear Transformations
        - Eigenvalues and Eigenvectors
        - Matrix Decompositions
        
        **Recommended Books:**
        - Linear Algebra Done Right by Sheldon Axler
        - Introduction to Linear Algebra by Gilbert Strang
        
        **Practice Problems:** [Download PDF]
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Interactive matrix calculator
        st.subheader("🧮 Matrix Calculator")
        st.markdown("Enter a 2x2 matrix to find its eigenvalues:")
        
        col1, col2 = st.columns(2)
        with col1:
            a11 = st.number_input("a₁₁", value=1.0, key="a11")
            a21 = st.number_input("a₂₁", value=0.0, key="a21")
        with col2:
            a12 = st.number_input("a₁₂", value=0.0, key="a12")
            a22 = st.number_input("a₂₂", value=1.0, key="a22")
        
        matrix = np.array([[a11, a12], [a21, a22]])
        eigenvalues = np.linalg.eigvals(matrix)
        
        st.markdown(f"**Matrix:**")
        st.write(matrix)
        st.markdown(f"**Eigenvalues:** {eigenvalues}")
        
    elif selected_subject == "Number Theory":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Number Theory Resources
        
        **Core Topics:**
        - Prime Numbers and Factorization
        - Congruences and Modular Arithmetic
        - Quadratic Residues
        - Diophantine Equations
        
        **Recommended Books:**
        - Elementary Number Theory by David Burton
        - A Classical Introduction to Modern Number Theory by Ireland & Rosen
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Prime number generator
        st.subheader("🔢 Prime Number Generator")
        n = st.slider("Generate first N prime numbers", 1, 100, 10)
        
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        primes = []
        num = 2
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
        
        st.write(f"First {n} prime numbers: {primes}")

# ProSort Euler page
elif page == "🎯 ProSort Euler":
    st.markdown('<h2 class="section-header">🎯 ProSort Euler</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    An event we're doing with FooBar for ESYA'25. This is a unique competition that combines 
    mathematical problem-solving with programming challenges.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Exercise 1
    st.subheader("📝 Exercise 1: The First Exercise")
    st.markdown("Some introduction")
    
    with st.expander("Task 1: First"):
        st.markdown("**Statement:** First")
        st.markdown("**Hint:** Hint")
    
    with st.expander("Task 2: Second"):
        st.markdown("**Statement:** Second")
        st.markdown("**Mathematical Expression:** a² = 100")
        st.markdown("**Solution:** a = ±10")
    
    # Interactive problem solver
    st.subheader("🧮 Problem Solver")
    problem_type = st.selectbox("Select Problem Type:", ["Linear Equation", "Quadratic Equation", "System of Equations"])
    
    if problem_type == "Linear Equation":
        st.markdown("**Solve: ax + b = c**")
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("a", value=2.0, key="a_linear")
        with col2:
            b = st.number_input("b", value=3.0, key="b_linear")
        with col3:
            c = st.number_input("c", value=7.0, key="c_linear")
        
        if a != 0:
            x = (c - b) / a
            st.success(f"**Solution:** x = {x}")
        else:
            st.error("Invalid equation: 'a' cannot be zero")

# PWNHUB CTF page
elif page == "🔐 PWNHUB CTF":
    st.markdown('<h2 class="section-header">🔐 PWNHUB</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    CTF's we started organizing. This website will be updated in due time, but till then, 
    find the old website [here](https://github.com/evariste-club/evariste-club.github.io/blob/main/pwnhub/index.html).
    """)
    
    # Ellie CTF Box
    st.subheader("🎯 Ellie")
    st.markdown("""
    Our very first box! The goal was to familiarize myself and others with the basic infrastructure, 
    `ssh`'ing into a box and using simple commands to retrieve a flag.
    """)
    
    with st.expander("Hints for Ellie"):
        st.markdown("""
        **Hint 1:** Start with basic enumeration
        **Hint 2:** Check for open ports and services
        **Hint 3:** Look for hidden files and directories
        **Hint 4:** Use common Linux commands
        """)
    
    # Benjamin CTF Box
    st.subheader("🎯 Benjamin")
    st.markdown("The second one!")
    
    # Display the meme image
    st.image("https://i.imgflip.com/4b0f1g.jpg", width=300, caption="The Meme")
    
    with st.expander("Hints for Benjamin"):
        st.markdown("""
        **Hint 1:** This one is more challenging than Ellie
        **Hint 2:** Look for web vulnerabilities
        **Hint 3:** Check for file upload vulnerabilities
        **Hint 4:** SQL injection might be involved
        """)
    
    # CTF Progress Tracker
    st.subheader("📊 CTF Progress Tracker")
    
    ctf_data = {
        "Box": ["Ellie", "Benjamin"],
        "Difficulty": ["Easy", "Medium"],
        "Status": ["Completed", "In Progress"],
        "Points": [100, 200],
        "Time Taken": ["2 hours", "4 hours"]
    }
    
    df = pd.DataFrame(ctf_data)
    st.dataframe(df, use_container_width=True)

# Blog page
elif page == "📝 Blog":
    st.markdown('<h2 class="section-header">📝 Blog Files</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    A sort of blog I'm hoping to maintain (based on the input of one of our team member, 8 or so months ago).
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sample blog posts
    blog_posts = [
        {
            "title": "Introduction to Graph Theory",
            "author": "Math Club Team",
            "date": "2024-01-15",
            "excerpt": "Exploring the fascinating world of graphs and their applications in computer science and mathematics."
        },
        {
            "title": "The Beauty of Prime Numbers",
            "author": "Math Club Team",
            "date": "2024-01-10",
            "excerpt": "Understanding the fundamental building blocks of mathematics and their mysterious patterns."
        },
        {
            "title": "Linear Algebra in Machine Learning",
            "author": "Math Club Team",
            "date": "2024-01-05",
            "excerpt": "How linear algebra powers modern machine learning algorithms and data science applications."
        }
    ]
    
    for post in blog_posts:
        with st.expander(f"📄 {post['title']}"):
            st.markdown(f"**Author:** {post['author']}")
            st.markdown(f"**Date:** {post['date']}")
            st.markdown(f"**Excerpt:** {post['excerpt']}")
            st.button("Read More", key=f"read_{post['title']}")

# Events page
elif page == "📅 Events":
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

# About Us page
elif page == "👥 About Us":
    st.markdown('<h2 class="section-header">👥 About Évariste</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ### Our Mission
    
    Évariste is IIIT-D's premier mathematics club, dedicated to fostering a love for mathematics 
    and creating a vibrant community of learners, problem-solvers, and mathematical enthusiasts.
    
    ### What We Do
    
    - **Study Sessions:** Regular meetings to discuss mathematical concepts and solve problems
    - **Competitions:** Host and participate in mathematical competitions and CTF challenges
    - **Workshops:** Organize workshops on various mathematical topics
    - **Research:** Encourage mathematical research and exploration
    - **Community:** Build a supportive network of mathematics enthusiasts
    
    ### Join Us!
    
    Whether you're a beginner or an advanced mathematician, there's a place for you in Évariste. 
    We welcome all levels of expertise and enthusiasm for mathematics.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact information
    st.subheader("📞 Contact Us")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Email:** evariste@iiitd.ac.in
        **Discord:** Évariste Math Club
        **Location:** IIIT-D Campus
        """)
    with col2:
        st.markdown("""
        **Meeting Time:** Every Friday, 4:00 PM
        **Room:** Mathematics Department
        **Faculty Advisor:** Dr. Mathematics
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 2rem;">
    <p>© 2024 Évariste Math Club, IIIT-D. Built with ❤️ and Streamlit.</p>
</div>
""", unsafe_allow_html=True)
