"""
ProSort Enhanced Problem Solver
Provides enhanced problem solving interface with detailed participation tracking
"""

import streamlit as st
from datetime import datetime
from typing import Dict, Any, Optional
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import Problem, ProblemDifficulty, ProblemType
from problems import problem_bank
from user_management import user_manager
from auth_interface import auth_interface


class EnhancedProblemSolver:
    """Enhanced problem solver with participation tracking"""
    
    def __init__(self):
        self.setup_session_state()
    
    def setup_session_state(self):
        """Setup session state for problem solving"""
        if 'current_problem_id' not in st.session_state:
            st.session_state.current_problem_id = None
        if 'problem_start_time' not in st.session_state:
            st.session_state.problem_start_time = None
        if 'current_hints_used' not in st.session_state:
            st.session_state.current_hints_used = []
    
    def render_practice_dashboard(self):
        """Render the practice problems dashboard"""
        if not auth_interface.require_login():
            return
        
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
                    st.session_state.current_problem_id = random_problem.id
                    st.session_state.problem_start_time = datetime.now()
                    st.session_state.current_hints_used = []
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
    
    def render_problem_selection(self):
        """Render the problem browsing interface"""
        if not auth_interface.require_login():
            return
        
        st.markdown('<h2 class="section-header">🔍 Browse Problems</h2>', unsafe_allow_html=True)
        
        # Search and filters
        search_query = st.text_input("🔍 Search problems by title or tags")
        
        col1, col2 = st.columns(2)
        with col1:
            difficulty_filter = st.multiselect(
                "Difficulty",
                [d.value for d in ProblemDifficulty],
                default=[d.value for d in ProblemDifficulty]
            )
        
        with col2:
            type_filter = st.multiselect(
                "Problem Type",
                [t.value for t in ProblemType],
                default=[t.value for t in ProblemType]
            )
        
        # Apply filters
        all_problems = problem_bank.get_all_problems()
        filtered_problems = all_problems
        
        # Search filter
        if search_query:
            search_lower = search_query.lower()
            filtered_problems = [
                p for p in filtered_problems
                if (search_lower in p.title.lower() or 
                    any(search_lower in tag.lower() for tag in p.tags))
            ]
        
        # Difficulty filter
        if difficulty_filter:
            difficulty_enums = [ProblemDifficulty(d) for d in difficulty_filter]
            filtered_problems = [p for p in filtered_problems if p.difficulty in difficulty_enums]
        
        # Type filter
        if type_filter:
            type_enums = [ProblemType(t) for t in type_filter]
            filtered_problems = [p for p in filtered_problems if p.problem_type in type_enums]
        
        # Display results
        st.subheader(f"📊 Found {len(filtered_problems)} Problems")
        
        if not filtered_problems:
            st.info("No problems match your search criteria.")
            return
        
        # Sort options
        sort_by = st.selectbox(
            "Sort by",
            ["Difficulty", "Type", "Points", "Title"]
        )
        
        if sort_by == "Difficulty":
            filtered_problems.sort(key=lambda x: x.difficulty.value)
        elif sort_by == "Type":
            filtered_problems.sort(key=lambda x: x.problem_type.value)
        elif sort_by == "Points":
            filtered_problems.sort(key=lambda x: x.points, reverse=True)
        elif sort_by == "Title":
            filtered_problems.sort(key=lambda x: x.title)
        
        # Display problems
        for problem in filtered_problems:
            self._render_problem_card(problem, show_select_button=True)
    
    def _render_problem_card(self, problem: Problem, show_select_button: bool = False):
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
        
        if show_select_button:
            if st.button(f"🧮 Solve Problem", key=f"solve_{problem.id}"):
                st.session_state.current_problem_id = problem.id
                st.session_state.problem_start_time = datetime.now()
                st.session_state.current_hints_used = []
                st.rerun()
    
    def render_problem_solver(self):
        """Render the enhanced problem solver interface"""
        if not auth_interface.require_login():
            return
        
        if not st.session_state.get('current_problem_id'):
            st.info("Please select a problem to start solving!")
            return
        
        problem = problem_bank.get_problem_by_id(st.session_state.current_problem_id)
        if not problem:
            st.error("Problem not found!")
            return
        
        # Problem header
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
            <h2>🧮 {problem.title}</h2>
            <p><strong>Type:</strong> {problem.problem_type.value} | 
               <strong>Difficulty:</strong> {problem.difficulty.value} | 
               <strong>Points:</strong> {problem.points}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Timer
        if st.session_state.problem_start_time:
            elapsed = (datetime.now() - st.session_state.problem_start_time).seconds
            remaining = max(0, problem.time_limit - elapsed)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Time Elapsed", f"{elapsed}s")
            with col2:
                st.metric("Time Remaining", f"{remaining}s")
                
                if remaining <= 0:
                    st.warning("⏰ Time's up! Please submit your solution.")
        
        # Problem statement
        st.subheader("📝 Problem Statement")
        st.markdown(problem.statement)
        
        # Problem choice
        st.subheader("🎯 Your Approach")
        problem_choice = st.selectbox(
            "What do you want to do with this problem?",
            ["selected", "skipped", "attempted"],
            format_func=lambda x: {
                "selected": "I want to solve this problem",
                "skipped": "I want to skip this problem",
                "attempted": "I attempted but couldn't solve"
            }[x]
        )
        
        # Hints section
        st.subheader("💡 Hints")
        if problem.hints:
            for i, hint in enumerate(problem.hints):
                hint_key = f"hint_{problem.id}_{i}"
                if st.button(f"Show Hint {i+1}", key=hint_key):
                    st.info(f"**Hint {i+1}:** {hint}")
                    if hint not in st.session_state.current_hints_used:
                        st.session_state.current_hints_used.append(hint)
        else:
            st.info("No hints available for this problem.")
        
        # Written solution
        st.subheader("✍️ Your Solution")
        written_solution = st.text_area(
            "Write your step-by-step solution here:",
            height=200,
            placeholder="Show your work step by step..."
        )
        
        # Code solution (optional)
        st.subheader("💻 Code Solution (Optional)")
        use_code = st.checkbox("I want to submit a programming solution")
        
        code_solution = ""
        programming_language = ""
        
        if use_code:
            col1, col2 = st.columns(2)
            with col1:
                programming_language = st.selectbox(
                    "Programming Language",
                    ["Python", "Java", "C++", "JavaScript", "Other"]
                )
            with col2:
                code_solution = st.text_area(
                    "Your code:",
                    height=150,
                    placeholder="Write your code here..."
                )
        
        # Final answer
        st.subheader("🎯 Final Answer")
        final_answer = st.text_input("Enter your final answer:")
        
        # Personal notes
        st.subheader("📝 Personal Notes")
        notes = st.text_area(
            "Any additional thoughts or approach notes:",
            height=100,
            placeholder="What was your approach? What did you learn?"
        )
        
        # Submit solution
        if st.button("🚀 Submit Solution", type="primary", use_container_width=True):
            if not written_solution.strip():
                st.error("Please provide a written solution!")
                return
            
            if not final_answer.strip():
                st.error("Please provide a final answer!")
                return
            
            self.submit_solution(
                problem=problem,
                problem_choice=problem_choice,
                written_solution=written_solution,
                code_solution=code_solution,
                programming_language=programming_language,
                final_answer=final_answer,
                notes=notes
            )
        
        # Back to problems
        if st.button("← Back to Problems"):
            st.session_state.current_problem_id = None
            st.session_state.problem_start_time = None
            st.session_state.current_hints_used = []
            st.rerun()
    
    def submit_solution(self, problem: Problem, problem_choice: str, written_solution: str,
                       code_solution: str, programming_language: str, final_answer: str, notes: str):
        """Submit the user's solution and record participation"""
        try:
            # Calculate time spent
            time_spent = None
            if st.session_state.problem_start_time:
                time_spent = int((datetime.now() - st.session_state.problem_start_time).total_seconds())
            
            # Determine if answer is correct (simplified - in real system, this would be more sophisticated)
            is_correct = self._check_answer(problem, final_answer)
            
            # Calculate score
            score_earned = self._calculate_score(problem, is_correct, time_spent, len(st.session_state.current_hints_used))
            
            # Record participation
            participation_data = {
                'user_id': auth_interface.get_current_user_id(),
                'problem_id': problem.id,
                'problem_choice': problem_choice,
                'written_solution': written_solution,
                'code_solution': code_solution if code_solution.strip() else None,
                'programming_language': programming_language if code_solution.strip() else None,
                'hints_used': st.session_state.current_hints_used.copy(),
                'attempts_made': 1,  # For now, assume single attempt
                'final_answer': final_answer,
                'is_correct': is_correct,
                'score_earned': score_earned,
                'notes': notes,
                'start_time': st.session_state.problem_start_time or datetime.now(),
                'end_time': datetime.now(),
                'time_spent': time_spent
            }
            
            success, message, participation_id = user_manager.record_participation(participation_data)
            
            if success:
                # Show results
                st.success("✅ Solution submitted successfully!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Correct", "✅" if is_correct else "❌")
                with col2:
                    st.metric("Score Earned", f"{score_earned:.1f}")
                with col3:
                    st.metric("Time Spent", f"{time_spent}s" if time_spent else "N/A")
                
                # Show solution if incorrect
                if not is_correct:
                    with st.expander("📖 View Correct Solution"):
                        st.markdown(problem.solution)
                
                # Reset problem state
                st.session_state.current_problem_id = None
                st.session_state.problem_start_time = None
                st.session_state.current_hints_used = []
                
                st.info("🎉 Problem completed! You can now select another problem.")
                
            else:
                st.error(f"Failed to submit solution: {message}")
                
        except Exception as e:
            st.error(f"Error submitting solution: {str(e)}")
    
    def _check_answer(self, problem: Problem, user_answer: str) -> bool:
        """Check if user's answer is correct (simplified implementation)"""
        # This is a simplified answer checker
        # In a real system, you'd have more sophisticated answer validation
        
        # For now, just check if the answer contains key elements
        user_answer_lower = user_answer.lower()
        
        # Check against test cases
        for test_case in problem.test_cases:
            expected = str(test_case['output']).lower()
            if expected in user_answer_lower or user_answer_lower in expected:
                return True
        
        # Check against solution keywords
        solution_lower = problem.solution.lower()
        key_terms = [term.lower() for term in problem.tags]
        
        # If user answer contains key terms from solution, consider it correct
        for term in key_terms:
            if term in user_answer_lower and term in solution_lower:
                return True
        
        return False
    
    def _calculate_score(self, problem: Problem, is_correct: bool, time_spent: Optional[int], hints_used: int) -> float:
        """Calculate score based on correctness, time, and hints used"""
        base_score = problem.points if is_correct else 0
        
        if not is_correct:
            return 0.0
        
        # Time bonus/penalty
        time_bonus = 0
        if time_spent is not None:
            if time_spent <= problem.time_limit * 0.5:  # Solved in first half of time
                time_bonus = base_score * 0.1
            elif time_spent > problem.time_limit * 0.8:  # Took most of the time
                time_bonus = base_score * -0.1
        
        # Hint penalty
        hint_penalty = base_score * 0.05 * hints_used
        
        final_score = base_score + time_bonus - hint_penalty
        return max(0.0, final_score)  # Score cannot be negative
    
    def render_detailed_statistics(self):
        """Render detailed user statistics"""
        if not auth_interface.require_login():
            return
        
        user_id = auth_interface.get_current_user_id()
        stats = user_manager.get_user_statistics(user_id)
        
        if not stats:
            st.info("No statistics available yet. Start solving problems!")
            return
        
        st.markdown('<h2 class="section-header">📈 Detailed Statistics</h2>', unsafe_allow_html=True)
        
        # Overall performance
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Score", stats['participation_stats']['total_score'])
        
        with col2:
            st.metric("Problems Solved", stats['participation_stats']['correct_answers'])
        
        with col3:
            st.metric("Total Participations", stats['participation_stats']['total_participations'])
        
        with col4:
            st.metric("Accuracy", f"{stats['participation_stats']['accuracy']:.1f}%")
        
        # Problem choice analysis
        st.subheader("🎯 Problem Choice Analysis")
        choice_data = stats['choice_analysis']['problem_choice_distribution']
        
        if choice_data:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Problem Choice Distribution**")
                for choice, count in choice_data.items():
                    st.info(f"{choice}: {count}")
            
            with col2:
                st.markdown("**Programming Language Usage**")
                lang_data = stats['choice_analysis']['programming_language_usage']
                if lang_data:
                    for lang, count in lang_data.items():
                        st.info(f"{lang}: {count}")
                else:
                    st.info("No programming solutions submitted yet.")
        
        # Time analysis
        st.subheader("⏱️ Time Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            total_time = stats['choice_analysis']['total_time_spent']
            avg_time = stats['choice_analysis']['avg_time_per_problem']
            
            st.metric("Total Time Spent", f"{total_time//60}m {total_time%60}s")
            st.metric("Average Time per Problem", f"{avg_time//60}m {avg_time%60}s")
        
        with col2:
            st.markdown("**Time Efficiency Tips:**")
            if avg_time > 600:  # More than 10 minutes average
                st.warning("Consider spending less time per problem to improve efficiency.")
            elif avg_time < 300:  # Less than 5 minutes average
                st.success("Great time management! You're solving problems efficiently.")
            else:
                st.info("Good time management. Keep up the balanced approach!")
        
        # Recent activity
        st.subheader("🕒 Recent Activity")
        recent_activity = stats['recent_activity']
        
        if recent_activity:
            for activity in recent_activity:
                status_emoji = "✅" if activity['is_correct'] else "❌"
                st.info(f"{status_emoji} {activity['problem_id']} - Score: {activity['score_earned']} - {activity['date']}")
        else:
            st.info("No recent activity to display.")


# Global enhanced solver instance
enhanced_solver = EnhancedProblemSolver()
