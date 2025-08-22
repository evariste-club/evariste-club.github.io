"""
ProSort Streamlit Application
Basic mathematical competition system interface
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


class ProSortStreamlitApp:
    """Basic ProSort Streamlit application"""
    
    def __init__(self):
        self.engine = ProSortEngine()
        self._initialize_engine()
        self._setup_session_state()
    
    def _initialize_engine(self):
        """Initialize the ProSort engine with problems"""
        # Add all problems from the problem bank
        for problem in problem_bank.get_all_problems():
            self.engine.add_problem(problem)
        
        # Create sample users
        self._create_sample_users()
    
    def _create_sample_users(self):
        """Create sample users for demonstration"""
        # Create sample users if they don't exist
        sample_users = [
            User(id="user1", username="math_wizard", email="wizard@math.com", 
                 full_name="Math Wizard", institution="IIIT-D", created_at=datetime.now()),
            User(id="user2", username="problem_solver", email="solver@math.com", 
                 full_name="Problem Solver", institution="IIIT-D", created_at=datetime.now()),
            User(id="user3", username="calculus_master", email="master@math.com", 
                 full_name="Calculus Master", institution="IIIT-D", created_at=datetime.now())
        ]
        
        for user in sample_users:
            if not any(u.username == user.username for u in self.engine.users.values()):
                self.engine.add_user(user)
    
    def _setup_session_state(self):
        """Setup Streamlit session state variables"""
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'dashboard'
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
        </style>
        """, unsafe_allow_html=True)
    
    def _render_main_navigation(self):
        """Render the main navigation"""
        # Sidebar navigation
        st.sidebar.markdown("## 🧮 ProSort System")
        
        page = st.sidebar.selectbox(
            "Navigate to:",
            ["🏠 Dashboard", "📚 Practice Problems", "🏆 Competitions", "📊 Leaderboard", "👤 Profile", "⚙️ Settings"]
        )
        
        st.session_state.current_page = page
    
    def _render_main_content(self):
        """Render the main content based on selected page"""
        page = st.session_state.get('current_page', '🏠 Dashboard')
        
        if page == "🏠 Dashboard":
            self._render_dashboard()
        elif page == "📚 Practice Problems":
            self._render_practice_problems()
        elif page == "🏆 Competitions":
            self._render_competitions()
        elif page == "📊 Leaderboard":
            self._render_leaderboard()
        elif page == "👤 Profile":
            self._render_profile()
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
            st.metric("Active Users", len(self.engine.users))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.metric("Total Submissions", len(self.engine.submissions))
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
        if self.engine.submissions:
            recent_submissions = list(self.engine.submissions.values())[-5:]
            for submission in reversed(recent_submissions):
                user = self.engine.users.get(submission.user_id)
                if user:
                    status_emoji = "✅" if submission.is_correct else "❌"
                    st.info(f"{status_emoji} {user.username} solved Problem {submission.problem_id} - {submission.submitted_at.strftime('%H:%M')}")
        else:
            st.info("No submissions yet. Be the first to solve a problem!")
    
    def _render_practice_problems(self):
        """Render the practice problems page"""
        st.markdown('<h2 class="section-header">📚 Practice Problems</h2>', unsafe_allow_html=True)
        
        # Problem selection filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            selected_difficulty = st.selectbox(
                "Difficulty",
                ["All"] + [d.value for d in ProblemDifficulty]
            )
        
        with col2:
            selected_type = st.selectbox(
                "Problem Type",
                ["All"] + [t.value for t in ProblemType]
            )
        
        with col3:
            if st.button("🎲 Random Problem", use_container_width=True):
                difficulty = None
                problem_type = None
                
                if selected_difficulty != "All":
                    difficulty = ProblemDifficulty(selected_difficulty)
                if selected_type != "All":
                    problem_type = ProblemType(selected_type)
                
                random_problem = problem_bank.get_random_problem(difficulty, problem_type)
                if random_problem:
                    st.session_state.current_problem = random_problem
                    st.rerun()
                else:
                    st.warning("No problems found with the selected criteria.")
        
        # Display filtered problems
        st.subheader("🔍 Available Problems")
        
        all_problems = problem_bank.get_all_problems()
        filtered_problems = all_problems
        
        if selected_difficulty != "All":
            difficulty_enum = ProblemDifficulty(selected_difficulty)
            filtered_problems = [p for p in filtered_problems if p.difficulty == difficulty_enum]
        
        if selected_type != "All":
            type_enum = ProblemType(selected_type)
            filtered_problems = [p for p in filtered_problems if p.problem_type == type_enum]
        
        if not filtered_problems:
            st.info("No problems found with the selected criteria.")
            return
        
        # Display problems in a grid
        for i in range(0, len(filtered_problems), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(filtered_problems):
                    problem = filtered_problems[i + j]
                    with cols[j]:
                        self._render_problem_card(problem)
    
    def _render_problem_card(self, problem: Problem):
        """Render a problem card"""
        difficulty_colors = {
            ProblemDifficulty.EASY: "#27ae60",
            ProblemDifficulty.MEDIUM: "#f39c12",
            ProblemDifficulty.HARD: "#e74c3c",
            ProblemDifficulty.EXPERT: "#8e44ad"
        }
        
        color = difficulty_colors.get(problem.difficulty, "#6c757d")
        
        st.markdown(f"""
        <div style="border: 2px solid {color}; border-radius: 10px; padding: 1rem; margin: 1rem 0;">
            <h4>{problem.title}</h4>
            <p><strong>Type:</strong> {problem.problem_type.value}</p>
            <p><strong>Difficulty:</strong> <span style="color: {color};">{problem.difficulty.value}</span></p>
            <p><strong>Points:</strong> {problem.points}</p>
            <p><strong>Time Limit:</strong> {problem.time_limit} seconds</p>
            <p><strong>Tags:</strong> {', '.join(problem.tags)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🧮 Solve Problem", key=f"solve_{problem.id}"):
            st.session_state.current_problem = problem
            st.rerun()
    
    def _render_competitions(self):
        """Render the competitions page"""
        st.markdown('<h2 class="section-header">🏆 Competitions</h2>', unsafe_allow_html=True)
        
        # Create new competition
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
    
    def _render_leaderboard(self):
        """Render the leaderboard page"""
        st.markdown('<h2 class="section-header">📊 Leaderboard</h2>', unsafe_allow_html=True)
        
        # Overall leaderboard
        st.subheader("🏆 Overall Leaderboard")
        
        # Get all users with their statistics
        leaderboard_data = []
        for user in self.engine.users.values():
            total_score = sum(s.score for s in self.engine.submissions.values() if s.user_id == user.id)
            problems_solved = len([s for s in self.engine.submissions.values() if s.user_id == user.id and s.is_correct])
            
            leaderboard_data.append({
                "Username": user.username,
                "Full Name": user.full_name,
                "Institution": user.institution,
                "Total Score": total_score,
                "Problems Solved": problems_solved
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
        """Render the profile page"""
        st.markdown('<h2 class="section-header">👤 Profile</h2>', unsafe_allow_html=True)
        st.info("Profile functionality would be implemented here!")
    
    def _render_settings(self):
        """Render the settings page"""
        st.markdown('<h2 class="section-header">⚙️ Settings</h2>', unsafe_allow_html=True)
        st.info("Settings functionality would be implemented here!")


def main():
    """Main function to run the ProSort Streamlit app"""
    app = ProSortStreamlitApp()
    app.run()


if __name__ == "__main__":
    main()
