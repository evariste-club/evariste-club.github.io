
import streamlit as st
from utils import layout, footer

layout.load()


st.markdown('<h2 class="section-header">Blog</h2>', unsafe_allow_html=True)

st.markdown("""
A sort of blog I'm hoping to maintain (based on the input of one of our team member, 8 or so months ago).
""")

# Sample blog posts
# blog_posts = [
#     {
#         "title": "Introduction to Graph Theory",
#         "author": "Math Club Team",
#         "date": "2024-01-15",
#         "excerpt": "Exploring the fascinating world of graphs and their applications in computer science and mathematics."
#     },
#     {
#         "title": "The Beauty of Prime Numbers",
#         "author": "Math Club Team",
#         "date": "2024-01-10",
#         "excerpt": "Understanding the fundamental building blocks of mathematics and their mysterious patterns."
#     },
#     {
#         "title": "Linear Algebra in Machine Learning",
#         "author": "Math Club Team",
#         "date": "2024-01-05",
#         "excerpt": "How linear algebra powers modern machine learning algorithms and data science applications."
#     }
# ]
#
# for post in blog_posts:
#     with st.expander(f"📄 {post['title']}"):
#         st.markdown(f"**Author:** {post['author']}")
#         st.markdown(f"**Date:** {post['date']}")
#         st.markdown(f"**Excerpt:** {post['excerpt']}")
#         st.button("Read More", key=f"read_{post['title']}")
#

footer.load()
