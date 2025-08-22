"""
ProSort Enhanced Streamlit Application
Integrated authentication and enhanced problem solving with participation tracking
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import hashlib
import time
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import ProSortEngine, ProblemDifficulty, ProblemType, User, Problem
from problems import problem_bank
from user_management import user_manager
from auth_interface import auth_interface
from enhanced_problem_solver import enhanced_solver


class EnhancedProSortApp:
    """Enhanced ProSort application with authentication and participation tracking"""
    
    def __init__(self):
        self.engine = ProSortEngine()
        self._initialize_engine()
        self._setup_session_state()
    
    def _initialize_engine(self):
        """Initialize the ProSort engine with problems and sample users"""
        # Add all problems from the problem bank
        for problem in problem_bank.get_all_problems():
            self.engine.add_problem(problem)
        
        # Create sample users if none exist
        if not user_manager.users:
            self._create_sample_users()
    
    def _create_sample_users(self):
        """Create sample users for demonstration"""
        sample_users_data = [
            {
                'username': 'math_wizard',
                'email': 'wizard@mathclub.com',
                'full_name': 'Math Wizard',
                'institution': 'IIIT-D',
                'student_id': 'STU001',
                'phone': '+91-9876543210',
                'date_of_birth': '1995-01-15',
                'grade_level': 'Graduate',
                'mathematical_background': ['Algebra', 'Calculus', 'Number Theory'],
                'interests': ['Problem Solving', 'Competitions', 'Research'],
                'password': 'password123'
            },
            {
                'username': 'problem_solver',
                'email': 'solver@mathclub.com',
                'full_name': 'Problem Solver',
                'institution': 'IIIT-D',
                'student_id': 'STU002',
                'phone': '+91-9876543211',
                'date_of_birth': '1996-03-20',
                'grade_level': 'Undergraduate',
                'mathematical_background': ['Geometry', 'Probability'],
                'interests': ['Problem Solving', 'Competitions'],
                'password': 'password123'
            },
            {
                'username': 'calculus_master',
                'email': 'master@mathclub.com',
                'full_name': 'Calculus Master',
                'institution': 'IIIT-D',
                'student_id': 'STU003',
                'phone': '+91-9876543212',
                'date_of_birth': '1994-07-10',
                'grade_level': 'Graduate',
                'mathematical_background': ['Calculus', 'Linear Algebra', 'Optimization'],
                'interests': ['Research', 'Teaching', 'Applied Math'],
                'password': 'password123'
            }
        ]
        
        for user_data in sample_users_data:
            success, message, user_id = user_manager.register_user(user_data)
            if success:
                print(f"Created sample user: {user_data['username']}")
            else:
                print(f"Failed to create sample user {user_data['username']}: {message}")
    
    def _setup_session_state(self):
        """Setup Streamlit session state variables"""
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'auth'
        if 'current_problem' not in st.session_state:
            st.session_state.current_problem = None
    
    def run(self):
        """Main application runner"""
        st.set_page_config(
            page_title="ProSort - Mathematical Competition System",
            page_icon="🧮",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS
        self._load_custom_css()
        
        # Main navigation
        self._render_main_navigation()
        
        # Main content based on current page
        self._render_main_content()
    
    def _load_custom_css(self):
        """Load custom CSS styling"""
        st.markdown("""
        <style>
        .prosort-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }
        .problem-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 5px solid #3498db;
        }
        .difficulty-easy { border-left-color: #27ae60; }
        .difficulty-medium { border-left-color: #f39c12; }
        .difficulty-hard { border-left-color: #e74c3c; }
        .difficulty-expert { border-left-color: #8e44ad; }
        .stats-card {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            margin: 1rem 0;
        }
        .leaderboard-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border: 2px solid #e9ecef;
        }
        .auth-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
    
    def _render_main_navigation(self):
        """Render the main navigation"""
        # Check if user is logged in
        if auth_interface.is_user_logged_in():
            user_info = st.session_state.user_info
            
            # Sidebar navigation
            st.sidebar.markdown("## 🧮 ProSort System")
            st.sidebar.markdown(f"### 👤 {user_info['username']}")
            st.sidebar.markdown(f"**Name:** {user_info['full_name']}")
            st.sidebar.markdown(f"**Institution:** {user_info['institution']}")
            st.sidebar.markdown("---")
            
            # Navigation menu
            page = st.sidebar.selectbox(
                "Navigate to:",
                ["🏠 Dashboard", "📚 Practice Problems", "🔍 Browse Problems", "🧮 Problem Solver", 
                 "🏆 Competitions", "📊 Leaderboard", "👤 My Profile", "📈 Statistics", "⚙️ Settings"]
            )
            
            st.session_state.current_page = page
            
            # Logout button
            if st.sidebar.button("🚪 Logout"):
                auth_interface.handle_logout()
        else:
            # Show authentication interface
            auth_interface.render_auth_interface()
    
    def _render_main_content(self):
        """Render the main content based on selected page"""
        if not auth_interface.is_user_logged_in():
            return  # Auth interface is handled in sidebar
        
        page = st.session_state.get('current_page', '🏠 Dashboard')
        
        if page == "🏠 Dashboard":
            self._render_dashboard()
        elif page == "📚 Practice Problems":
            self._render_practice_problems()
        elif page == "🔍 Browse Problems":
            self._render_browse_problems()
        elif page == "🧮 Problem Solver":
            self._render_problem_solver()
        elif page == "🏆 Competitions":
            self._render_competitions()
        elif page == "📊 Leaderboard":
            self._render_leaderboard()
        elif page == "👤 My Profile":
            self._render_profile()
        elif page == "📈 Statistics":
            self._render_statistics()
        elif page == "⚙️ Settings":
            self._render_settings()
    
    def _render_dashboard(self):
        """Render the main dashboard"""
        st.markdown('<div class="prosort-header">', unsafe_allow_html=True)
        st.markdown("""
        <h1>🧮 ProSort</h1>
        <h3>Mathematical Competition System</h3>
        <p>Challenge yourself with mathematical problems and compete with others!</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.metric("Total Problems", problem_bank.get_problem_count())
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.metric("Active Users", len(user_manager.users))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.metric("Total Participations", len(user_manager.participations))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.metric("Active Competitions", len([c for c in self.engine.competitions.values() if c.is_active]))
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Problem distribution charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Problems by Difficulty")
            difficulty_counts = problem_bank.get_problem_count_by_difficulty()
            fig = px.pie(
                values=list(difficulty_counts.values()),
                names=list(difficulty_counts.keys()),
                title="Problem Distribution by Difficulty"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Problems by Type")
            type_counts = problem_bank.get_problem_count_by_type()
            fig = px.bar(
                x=list(type_counts.keys()),
                y=list(type_counts.values()),
                title="Problem Distribution by Type"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Recent activity
        st.subheader("🕒 Recent Activity")
        if user_manager.participations:
            recent_participations = list(user_manager.participations.values())[-5:]
            for participation in reversed(recent_participations):
                user = user_manager.users.get(participation.user_id)
                if user:
                    status_emoji = "✅" if participation.is_correct else "❌"
                    st.info(f"{status_emoji} {user.username} solved Problem {participation.problem_id} - {participation.created_at.strftime('%H:%M')}")
        else:
            st.info("No participations yet. Be the first to solve a problem!")
    
    def _render_practice_problems(self):
        """Render the practice problems dashboard"""
        enhanced_solver.render_practice_dashboard()
    
    def _render_browse_problems(self):
        """Render the problem browsing interface"""
        enhanced_solver.render_problem_selection()
    
    def _render_problem_solver(self):
        """Render the enhanced problem solver"""
        if st.session_state.get('current_problem_id'):
            # User is working on a problem
            enhanced_solver.render_problem_solver()
        else:
            st.info("Please select a problem from the Browse Problems page to start solving!")
    
    def _render_competitions(self):
        """Render the competitions page"""
        st.markdown('<h2 class="section-header">🏆 Competitions</h2>', unsafe_allow_html=True)
        
        # Create new competition (admin only)
        current_user = st.session_state.user_info
        if current_user and current_user['username'] == "math_wizard":
            with st.expander("➕ Create New Competition"):
                self._render_create_competition()
        
        # Active competitions
        st.subheader("🔥 Active Competitions")
        active_competitions = [c for c in self.engine.competitions.values() if c.is_active]
        
        if not active_competitions:
            st.info("No active competitions at the moment.")
        else:
            for competition in active_competitions:
                self._render_competition_card(competition)
        
        # Past competitions
        st.subheader("📚 Past Competitions")
        past_competitions = [c for c in self.engine.competitions.values() if not c.is_active]
        
        if not past_competitions:
            st.info("No past competitions.")
        else:
            for competition in past_competitions:
                self._render_competition_card(competition, is_past=True)
    
    def _render_create_competition(self):
        """Render the create competition form"""
        name = st.text_input("Competition Name")
        description = st.text_area("Description")
        
        col1, col2 = st.columns(2)
        with col1:
            start_time = st.date_input("Start Date")
        with col2:
            end_time = st.date_input("End Date")
        
        # Problem selection
        st.subheader("Select Problems")
        all_problems = problem_bank.get_all_problems()
        selected_problems = st.multiselect(
            "Choose problems:",
            options=[(p.id, p.title) for p in all_problems],
            format_func=lambda x: x[1]
        )
        
        if st.button("Create Competition"):
            if name and description and selected_problems:
                problem_ids = [pid for pid, _ in selected_problems]
                start_dt = datetime.combine(start_time, datetime.min.time())
                end_dt = datetime.combine(end_time, datetime.min.time())
                
                competition = self.engine.create_competition(
                    name=name,
                    description=description,
                    start_time=start_dt,
                    end_time=end_dt,
                    problem_ids=problem_ids,
                    rules={"time_limit": "3 hours", "scoring": "points based"}
                )
                
                st.success(f"Competition '{name}' created successfully!")
                st.rerun()
            else:
                st.error("Please fill all fields!")
    
    def _render_competition_card(self, competition, is_past=False):
        """Render a competition card"""
        status_color = "#e74c3c" if is_past else "#27ae60"
        status_text = "Ended" if is_past else "Active"
        
        st.markdown(f"""
        <div style="border: 2px solid {status_color}; border-radius: 10px; padding: 1rem; margin: 1rem 0;">
            <h4>{competition.name}</h4>
            <p>{competition.description}</p>
            <p><strong>Status:</strong> <span style="color: {status_color};">{status_text}</span></p>
            <p><strong>Problems:</strong> {len(competition.problems)}</p>
            <p><strong>Participants:</strong> {len(competition.participants)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not is_past and st.session_state.user_info:
            if st.button(f"Join Competition", key=f"join_{competition.id}"):
                if st.session_state.user_info['user_id'] not in competition.participants:
                    competition.participants.append(st.session_state.user_info['user_id'])
                    st.success("Joined competition successfully!")
                    st.rerun()
                else:
                    st.info("You're already in this competition!")
    
    def _render_leaderboard(self):
        """Render the leaderboard page"""
        st.markdown('<h2 class="section-header">📊 Leaderboard</h2>', unsafe_allow_html=True)
        
        # Overall leaderboard
        st.subheader("🏆 Overall Leaderboard")
        
        # Get all users with their statistics
        leaderboard_data = []
        for user in user_manager.users.values():
            stats = user_manager.get_user_statistics(user.user_id)
            if stats:
                leaderboard_data.append({
                    "Username": user.username,
                    "Full Name": user.full_name,
                    "Institution": user.institution,
                    "Total Score": stats['participation_stats']['total_score'],
                    "Problems Solved": stats['participation_stats']['correct_answers'],
                    "Total Participations": stats['participation_stats']['total_participations'],
                    "Accuracy": f"{stats['participation_stats']['accuracy']:.1f}%"
                })
        
        # Sort by total score
        leaderboard_data.sort(key=lambda x: x['Total Score'], reverse=True)
        
        if leaderboard_data:
            df = pd.DataFrame(leaderboard_data)
            st.dataframe(df, use_container_width=True)
            
            # Top 10 chart
            top_10 = df.head(10)
            fig = px.bar(
                top_10,
                x="Username",
                y="Total Score",
                title="Top 10 Users by Score",
                color="Total Score",
                color_continuous_scale="viridis"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No leaderboard data available yet.")
    
    def _render_profile(self):
        """Render the user profile page"""
        auth_interface.render_user_profile()
    
    def _render_statistics(self):
        """Render the detailed statistics page"""
        enhanced_solver.render_detailed_statistics()
    
    def _render_settings(self):
        """Render the settings page"""
        if not auth_interface.require_login():
            return
        
        st.markdown('<h2 class="section-header">⚙️ Settings</h2>', unsafe_allow_html=True)
        
        user_info = st.session_state.user_info
        
        st.subheader("👤 Account Settings")
        
        # Password change
        with st.expander("🔐 Change Password"):
            with st.form("password_change_form"):
                current_password = st.text_input("Current Password", type="password")
                new_password = st.text_input("New Password", type="password")
                confirm_password = st.text_input("Confirm New Password", type="password")
                
                if st.form_submit_button("Change Password"):
                    if new_password != confirm_password:
                        st.error("New passwords do not match!")
                    elif len(new_password) < 6:
                        st.error("Password must be at least 6 characters long!")
                    else:
                        st.success("Password change functionality would be implemented here!")
        
        # Data export
        st.subheader("📊 Data Export")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Export My Data (JSON)"):
                user_id = auth_interface.get_current_user_id()
                success, message, data = user_manager.export_user_data(user_id, 'json')
                if success:
                    st.download_button(
                        label="Download JSON",
                        data=data,
                        file_name=f"prosort_data_{user_info['username']}.json",
                        mime="application/json"
                    )
                else:
                    st.error(f"Export failed: {message}")
        
        with col2:
            if st.button("Export Participation History (CSV)"):
                user_id = auth_interface.get_current_user_id()
                history = user_manager.get_user_participation_history(user_id)
                
                if history:
                    df = pd.DataFrame(history)
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name=f"participation_history_{user_info['username']}.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("No participation history to export!")
        
        # Account deletion
        st.subheader("🗑️ Account Management")
        
        with st.expander("⚠️ Delete Account"):
            st.warning("This action cannot be undone!")
            if st.button("Delete My Account", type="secondary"):
                st.error("Account deletion functionality would be implemented here!")


def main():
    """Main function to run the enhanced ProSort Streamlit app"""
    app = EnhancedProSortApp()
    app.run()


if __name__ == "__main__":
    main()
