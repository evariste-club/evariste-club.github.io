import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import requests
import markdown
import streamlit as st


def prosort_euler():
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


if __name__=='__main__':
    prosort_euler()
