import streamlit as st


def load():
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





# footer

# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #7f8c8d; padding: 2rem;">
#     <p>© 2025 Évariste Math Club, IIIT-D. Built with ❤️</p>
# </div>
# """, unsafe_allow_html=True)
