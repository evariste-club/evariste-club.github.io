
import streamlit as st
import streamlit.components.v1 as components
from utils import layout, footer


layout.load()


HTML_BG = """
<style>
  body {
    background-color: transparent !important;
  }
</style>
<iframe src="https://www.shadertoy.com/embed/3fXyRf?gui=false&t=10&paused=false&muted=false"
    style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"
    frameborder="0"
    allowfullscreen>
</iframe>
"""

# components.html(HTML_BG, height=1000, width=0)
components.html(HTML_BG, height=0 )

st.markdown("""
    <div style='text-align: center;'>
        <h1><strong>Évariste</strong></h1>
        <p>Welcome to the official homepage of our Maths Club! ✨</p>
    </div>
""", unsafe_allow_html=True)


footer.load()
