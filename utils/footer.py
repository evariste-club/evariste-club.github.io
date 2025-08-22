import streamlit as st





def load():

    st.markdown("---")

    st.markdown("_Contact Us_")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        [Email](mailto:evariste@iiitd.ac.in)

        [WhatsApp Group](https://chat.whatsapp.com/Gw1a1ARhVMsEIDGdo0DjRw)
        """)

    with col2:
        st.markdown("""
        [Instagram](https://www.instagram.com/evariste.iiitd/)

        [Telegram](https://t.me/joinchat/Da8m6kMPZmX7g93YWxlnKw)
        """)

    with col3:
        st.markdown("""
        [Reddit](http://bit.ly/EvaristeClub)
        """)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 2rem 0;">
        <p>© 2025 Évariste Math Club, IIIT-D. Built with ❤️</p>
    </div>
    """, unsafe_allow_html=True)

