import streamlit as st
from utils import layout, footer

layout.load()

st.markdown("""
    <style>
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            margin-top: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        .section-header {
            font-size: 2em;
            margin-top: 1em;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)


# Section Header
st.markdown('<h2 class="section-header">👥 About Évariste</h2>', unsafe_allow_html=True)

# Card Content
st.markdown("""
<div class="card">
  <h3>Our Mission</h3>
  <p>
    Évariste is IIIT-D's premier mathematics club, dedicated to fostering a love for mathematics 
    and creating a vibrant community of learners, problem-solvers, and mathematical enthusiasts.
  </p>

  <h3>What We Do</h3>
  <ul>
    <li><strong>Study Sessions:</strong> Regular meetings to discuss mathematical concepts and solve problems</li>
    <li><strong>Competitions:</strong> Host and participate in mathematical competitions and CTF challenges</li>
    <li><strong>Workshops:</strong> Organize workshops on various mathematical topics</li>
    <li><strong>Research:</strong> Encourage mathematical research and exploration</li>
    <li><strong>Community:</strong> Build a supportive network of mathematics enthusiasts</li>
  </ul>

  <h3>Join Us!</h3>
  <p>
    Whether you're a beginner or an advanced mathematician, there's a place for you in Évariste. 
    We welcome all levels of expertise and enthusiasm for mathematics.
  </p>
</div>
""", unsafe_allow_html=True)

# Contact Information

footer.load()
