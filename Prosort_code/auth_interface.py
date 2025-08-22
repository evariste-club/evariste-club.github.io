"""
ProSort Authentication Interface
Provides Streamlit UI for user authentication and profile management
"""

import streamlit as st
from datetime import datetime
from typing import Dict, Any, Optional
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from user_management import user_manager


class AuthInterface:
    """Handles user authentication interface"""
    
    def __init__(self):
        self.setup_session_state()
    
    def setup_session_state(self):
        """Setup authentication session state variables"""
        if 'user_info' not in st.session_state:
            st.session_state.user_info = None
        if 'auth_page' not in st.session_state:
            st.session_state.auth_page = 'login'
    
    def render_auth_interface(self):
        """Render the main authentication interface"""
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        
        # Page selection
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔐 Login", use_container_width=True):
                st.session_state.auth_page = 'login'
        
        with col2:
            if st.button("📝 Register", use_container_width=True):
                st.session_state.auth_page = 'register'
        
        with col3:
            if st.button("🔑 Forgot Password", use_container_width=True):
                st.session_state.auth_page = 'forgot_password'
        
        st.markdown("---")
        
        # Render appropriate page
        if st.session_state.auth_page == 'login':
            self._render_login_page()
        elif st.session_state.auth_page == 'register':
            self._render_register_page()
        elif st.session_state.auth_page == 'forgot_password':
            self._render_forgot_password_page()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    def _render_login_page(self):
        """Render the login page"""
        st.subheader("🔐 Login to ProSort")
        
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.form_submit_button("Login", use_container_width=True):
                    self.handle_login(username, password)
            
            with col2:
                if st.form_submit_button("Demo Login", use_container_width=True):
                    self.handle_demo_login()
        
        # Show sample accounts
        with st.expander("📋 Sample Accounts"):
            st.markdown("""
            **For testing purposes, you can use these accounts:**
            
            | Username | Password | Role |
            |----------|----------|------|
            | `math_wizard` | `password123` | Admin |
            | `problem_solver` | `password123` | User |
            | `calculus_master` | `password123` | User |
            """)
    
    def _render_register_page(self):
        """Render the registration page"""
        st.subheader("📝 Create New Account")
        
        with st.form("register_form"):
            # Personal Information
            st.markdown("**Personal Information**")
            col1, col2 = st.columns(2)
            
            with col1:
                full_name = st.text_input("Full Name")
                username = st.text_input("Username")
                email = st.text_input("Email")
                phone = st.text_input("Phone Number")
            
            with col2:
                date_of_birth = st.date_input("Date of Birth")
                grade_level = st.selectbox("Grade Level", 
                                         ["High School", "Undergraduate", "Graduate", "Professional"])
            
            # Academic Information
            st.markdown("**Academic Information**")
            col1, col2 = st.columns(2)
            
            with col1:
                institution = st.text_input("Institution/School")
                student_id = st.text_input("Student ID (optional)")
            
            with col2:
                mathematical_background = st.multiselect(
                    "Mathematical Background",
                    ["Algebra", "Geometry", "Calculus", "Number Theory", "Combinatorics", 
                     "Probability", "Statistics", "Linear Algebra", "Analysis", "Topology"]
                )
            
            interests = st.multiselect(
                "Interests",
                ["Problem Solving", "Competitions", "Research", "Teaching", "Applied Math", 
                 "Pure Math", "Computer Science", "Physics", "Engineering"]
            )
            
            # Account Security
            st.markdown("**Account Security**")
            col1, col2 = st.columns(2)
            
            with col1:
                password = st.text_input("Password", type="password")
            
            with col2:
                confirm_password = st.text_input("Confirm Password", type="password")
            
            agree_terms = st.checkbox("I agree to the Terms and Conditions")
            
            if st.form_submit_button("Create Account", use_container_width=True):
                if password != confirm_password:
                    st.error("Passwords do not match!")
                elif len(password) < 6:
                    st.error("Password must be at least 6 characters long!")
                elif not agree_terms:
                    st.error("You must agree to the Terms and Conditions!")
                else:
                    self.handle_registration({
                        'full_name': full_name,
                        'username': username,
                        'email': email,
                        'phone': phone,
                        'date_of_birth': date_of_birth.strftime('%Y-%m-%d') if date_of_birth else '',
                        'grade_level': grade_level,
                        'institution': institution,
                        'student_id': student_id,
                        'mathematical_background': mathematical_background,
                        'interests': interests,
                        'password': password
                    })
    
    def _render_forgot_password_page(self):
        """Render the forgot password page"""
        st.subheader("🔑 Forgot Password")
        st.info("This feature is not yet implemented. Please contact an administrator.")
        
        if st.button("Back to Login"):
            st.session_state.auth_page = 'login'
    
    def handle_login(self, username: str, password: str):
        """Handle user login"""
        if not username or not password:
            st.error("Please enter both username and password!")
            return
        
        # Get client info for session tracking
        client_info = self._get_client_info()
        
        success, message, user_info = user_manager.authenticate_user(
            username, password, client_info['ip'], client_info['user_agent']
        )
        
        if success:
            st.session_state.user_info = user_info
            st.success(f"Welcome back, {user_info['full_name']}!")
            st.rerun()
        else:
            st.error(f"Login failed: {message}")
    
    def handle_demo_login(self):
        """Handle demo login for quick testing"""
        # Use the first available sample user
        demo_username = "math_wizard"
        demo_password = "password123"
        
        client_info = self._get_client_info()
        
        success, message, user_info = user_manager.authenticate_user(
            demo_username, demo_password, client_info['ip'], client_info['user_agent']
        )
        
        if success:
            st.session_state.user_info = user_info
            st.success(f"Demo login successful! Welcome, {user_info['full_name']}!")
            st.rerun()
        else:
            st.error(f"Demo login failed: {message}")
    
    def handle_registration(self, data: Dict[str, Any]):
        """Handle user registration"""
        success, message, user_id = user_manager.register_user(data)
        
        if success:
            st.success("Account created successfully! You can now login.")
            st.session_state.auth_page = 'login'
            st.rerun()
        else:
            st.error(f"Registration failed: {message}")
    
    def handle_logout(self):
        """Handle user logout"""
        if st.session_state.user_info and 'token' in st.session_state.user_info:
            user_manager.logout_user(st.session_state.user_info['token'])
        
        st.session_state.user_info = None
        st.session_state.auth_page = 'login'
        st.success("Logged out successfully!")
        st.rerun()
    
    def is_user_logged_in(self) -> bool:
        """Check if user is currently logged in"""
        return st.session_state.user_info is not None
    
    def require_login(self) -> bool:
        """Require user to be logged in, return False if not"""
        if not self.is_user_logged_in():
            st.warning("Please login to access this feature.")
            return False
        return True
    
    def get_current_user_id(self) -> Optional[str]:
        """Get the current user's ID"""
        if self.is_user_logged_in():
            return st.session_state.user_info.get('user_id')
        return None
    
    def _get_client_info(self) -> Dict[str, str]:
        """Get client information for session tracking"""
        # In a real application, you'd get this from the request
        # For Streamlit, we'll use placeholder values
        return {
            'ip': '127.0.0.1',
            'user_agent': 'Streamlit-Client'
        }
    
    def render_user_profile(self):
        """Render the user profile page"""
        if not self.require_login():
            return
        
        user_info = st.session_state.user_info
        
        st.markdown('<h2 class="section-header">👤 My Profile</h2>', unsafe_allow_html=True)
        
        # Profile information
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Personal Information")
            st.info(f"**Username:** {user_info['username']}")
            st.info(f"**Full Name:** {user_info['full_name']}")
            st.info(f"**Email:** {user_info['email']}")
            st.info(f"**Institution:** {user_info['institution']}")
        
        with col2:
            st.subheader("📊 Account Statistics")
            stats = user_manager.get_user_statistics(user_info['user_id'])
            
            if stats:
                participation_stats = stats.get('participation_stats', {})
                st.metric("Total Score", participation_stats.get('total_score', 0))
                st.metric("Problems Solved", participation_stats.get('correct_answers', 0))
                st.metric("Accuracy", f"{participation_stats.get('accuracy', 0):.1f}%")
                st.metric("Total Participations", participation_stats.get('total_participations', 0))
            else:
                st.info("No statistics available yet.")
        
        # Recent activity
        st.subheader("🕒 Recent Activity")
        history = user_manager.get_user_participation_history(user_info['user_id'])
        
        if history:
            # Show last 5 participations
            recent = history[:5]
            for participation in recent:
                status_emoji = "✅" if participation['is_correct'] else "❌"
                st.info(f"{status_emoji} {participation['problem_title']} - {participation['created_at']}")
        else:
            st.info("No participation history yet. Start solving problems!")
        
        # Profile editing
        with st.expander("✏️ Edit Profile"):
            st.info("Profile editing functionality would be implemented here!")
            if st.button("Update Profile"):
                st.success("Profile update functionality would be implemented here!")


# Global auth interface instance
auth_interface = AuthInterface()
