"""
ProSort Integration Layer
Provides functions to embed ProSort widgets into external applications
"""

import streamlit as st
from typing import Dict, Any, Optional, List
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import ProSortEngine, Problem, User, Competition
from problems import problem_bank


class ProSortIntegration:
    """Integration layer for embedding ProSort into external applications"""
    
    def __init__(self):
        self.engine = ProSortEngine()
        self._initialize_engine()
    
    def _initialize_engine(self):
        """Initialize the ProSort engine with problems"""
        for problem in problem_bank.get_all_problems():
            self.engine.add_problem(problem)
    
    def get_problem_by_id(self, problem_id: str) -> Optional[Problem]:
        """Get a problem by its ID"""
        return self.engine.get_problem(problem_id)
    
    def get_problems_by_difficulty(self, difficulty: str) -> List[Problem]:
        """Get problems by difficulty level"""
        from core import ProblemDifficulty
        try:
            difficulty_enum = ProblemDifficulty(difficulty)
            return problem_bank.get_problems_by_difficulty(difficulty_enum)
        except ValueError:
            return []
    
    def get_problems_by_type(self, problem_type: str) -> List[Problem]:
        """Get problems by problem type"""
        from core import ProblemType
        try:
            type_enum = ProblemType(problem_type)
            return problem_bank.get_problems_by_type(type_enum)
        except ValueError:
            return []
    
    def submit_answer_external(self, user_id: str, problem_id: str, answer: str, 
                              code: Optional[str] = None, language: Optional[str] = None) -> Dict[str, Any]:
        """Submit an answer from an external system"""
        try:
            submission = self.engine.submit_answer(
                user_id=user_id,
                problem_id=problem_id,
                answer=answer,
                code=code,
                language=language
            )
            
            return {
                'success': True,
                'submission_id': submission.id,
                'is_correct': submission.is_correct,
                'score': submission.score,
                'feedback': submission.feedback
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def create_competition_external(self, name: str, description: str, start_time: str, 
                                   end_time: str, problem_ids: List[str], rules: Dict[str, Any]) -> Dict[str, Any]:
        """Create a competition from an external system"""
        try:
            from datetime import datetime
            start_dt = datetime.fromisoformat(start_time)
            end_dt = datetime.fromisoformat(end_time)
            
            competition = self.engine.create_competition(
                name=name,
                description=description,
                start_time=start_dt,
                end_time=end_dt,
                problem_ids=problem_ids,
                rules=rules
            )
            
            return {
                'success': True,
                'competition_id': competition.id,
                'competition': competition.to_dict()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_leaderboard_external(self, competition_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get leaderboard data for external use"""
        try:
            if competition_id:
                leaderboard = self.engine.get_leaderboard(competition_id)
            else:
                leaderboard = self.engine.get_leaderboard()
            
            return leaderboard
        except Exception as e:
            return []
    
    def render_prosort_widget(self, widget_type: str, **kwargs):
        """Render a ProSort widget based on type"""
        if widget_type == "problem_display":
            self._render_problem_display_widget(**kwargs)
        elif widget_type == "leaderboard":
            self._render_leaderboard_widget(**kwargs)
        elif widget_type == "competition_info":
            self._render_competition_info_widget(**kwargs)
        elif widget_type == "user_stats":
            self._render_user_stats_widget(**kwargs)
        else:
            st.error(f"Unknown widget type: {widget_type}")
    
    def _render_problem_display_widget(self, problem_id: str, show_solution: bool = False):
        """Render a problem display widget"""
        problem = self.get_problem_by_id(problem_id)
        if not problem:
            st.error("Problem not found!")
            return
        
        st.markdown(f"### {problem.title}")
        st.markdown(f"**Difficulty:** {problem.difficulty.value}")
        st.markdown(f"**Type:** {problem.problem_type.value}")
        st.markdown(f"**Points:** {problem.points}")
        
        st.markdown("**Statement:**")
        st.markdown(problem.statement)
        
        if show_solution:
            st.markdown("**Solution:**")
            st.markdown(problem.solution)
    
    def _render_leaderboard_widget(self, competition_id: Optional[str] = None, limit: int = 10):
        """Render a leaderboard widget"""
        leaderboard = self.get_leaderboard_external(competition_id)
        
        if not leaderboard:
            st.info("No leaderboard data available.")
            return
        
        # Limit the number of entries
        leaderboard = leaderboard[:limit]
        
        st.markdown("### 🏆 Leaderboard")
        
        # Create a simple table
        for i, entry in enumerate(leaderboard, 1):
            col1, col2, col3 = st.columns([1, 3, 2])
            with col1:
                st.markdown(f"**#{i}**")
            with col2:
                st.markdown(f"**{entry.get('username', 'Unknown')}**")
            with col3:
                st.markdown(f"**{entry.get('score', 0)} pts**")
    
    def _render_competition_info_widget(self, competition_id: str):
        """Render a competition information widget"""
        competition = self.engine.competitions.get(competition_id)
        if not competition:
            st.error("Competition not found!")
            return
        
        st.markdown(f"### 🏆 {competition.name}")
        st.markdown(competition.description)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Problems", len(competition.problems))
        with col2:
            st.metric("Participants", len(competition.participants))
        with col3:
            status = "Active" if competition.is_active else "Ended"
            st.metric("Status", status)
    
    def _render_user_stats_widget(self, user_id: str):
        """Render a user statistics widget"""
        user = self.engine.users.get(user_id)
        if not user:
            st.error("User not found!")
            return
        
        st.markdown(f"### 👤 {user.username}")
        
        # Calculate basic stats
        user_submissions = [s for s in self.engine.submissions.values() if s.user_id == user_id]
        total_score = sum(s.score for s in user_submissions)
        problems_solved = len([s for s in user_submissions if s.is_correct])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Score", total_score)
        with col2:
            st.metric("Problems Solved", problems_solved)
        with col3:
            st.metric("Total Submissions", len(user_submissions))
    
    def export_data(self, data_type: str, filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Export data for external use"""
        try:
            if data_type == "problems":
                data = [p.to_dict() for p in problem_bank.get_all_problems()]
            elif data_type == "users":
                data = [u.to_dict() for u in self.engine.users.values()]
            elif data_type == "submissions":
                data = [s.to_dict() for s in self.engine.submissions.values()]
            elif data_type == "competitions":
                data = [c.to_dict() for c in self.engine.competitions.values()]
            else:
                return {'success': False, 'error': f'Unknown data type: {data_type}'}
            
            # Apply filters if provided
            if filters:
                # Simple filtering - in a real system, this would be more sophisticated
                filtered_data = []
                for item in data:
                    include = True
                    for key, value in filters.items():
                        if key in item and item[key] != value:
                            include = False
                            break
                    if include:
                        filtered_data.append(item)
                data = filtered_data
            
            return {
                'success': True,
                'data_type': data_type,
                'count': len(data),
                'data': data
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


# Global integration instance
prosort_integration = ProSortIntegration()


def get_prosort_widget(widget_type: str, **kwargs):
    """Convenience function to get a ProSort widget"""
    return prosort_integration.render_prosort_widget(widget_type, **kwargs)


def submit_prosort_answer(user_id: str, problem_id: str, answer: str, 
                         code: Optional[str] = None, language: Optional[str] = None) -> Dict[str, Any]:
    """Convenience function to submit an answer"""
    return prosort_integration.submit_answer_external(user_id, problem_id, answer, code, language)


def get_prosort_leaderboard(competition_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """Convenience function to get leaderboard data"""
    return prosort_integration.get_leaderboard_external(competition_id)
