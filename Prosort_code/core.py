"""
Core ProSort System
Handles problem management, scoring, and competition logic
"""

import json
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
import random


class ProblemDifficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


class ProblemType(Enum):
    ALGEBRA = "algebra"
    GEOMETRY = "geometry"
    CALCULUS = "calculus"
    NUMBER_THEORY = "number_theory"
    COMBINATORICS = "combinatorics"
    PROBABILITY = "probability"
    ALGORITHMS = "algorithms"
    OPTIMIZATION = "optimization"


@dataclass
class Problem:
    """Represents a mathematical problem in the ProSort system"""
    id: str
    title: str
    statement: str
    difficulty: ProblemDifficulty
    problem_type: ProblemType
    points: int
    time_limit: int  # in minutes
    hints: List[str]
    solution: str
    test_cases: List[Dict[str, Any]]
    tags: List[str]
    created_at: datetime
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert problem to dictionary for storage"""
        data = asdict(self)
        data['difficulty'] = self.difficulty.value
        data['problem_type'] = self.problem_type.value
        data['created_at'] = self.created_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Problem':
        """Create problem from dictionary"""
        data['difficulty'] = ProblemDifficulty(data['difficulty'])
        data['problem_type'] = ProblemType(data['problem_type'])
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)


@dataclass
class Submission:
    """Represents a user's submission for a problem"""
    id: str
    user_id: str
    problem_id: str
    answer: str
    code: Optional[str]
    language: Optional[str]
    submitted_at: datetime
    execution_time: Optional[float]
    memory_used: Optional[float]
    status: str  # "correct", "incorrect", "timeout", "error"
    score: float
    feedback: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert submission to dictionary for storage"""
        data = asdict(self)
        data['submitted_at'] = self.submitted_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Submission':
        """Create submission from dictionary"""
        data['submitted_at'] = datetime.fromisoformat(data['submitted_at'])
        return cls(**data)


@dataclass
class User:
    """Represents a user in the ProSort system"""
    id: str
    username: str
    email: str
    total_score: float
    problems_solved: int
    rank: int
    join_date: datetime
    last_active: datetime
    preferences: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for storage"""
        data = asdict(self)
        data['join_date'] = self.join_date.isoformat()
        data['last_active'] = self.last_active.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create user from dictionary"""
        data['join_date'] = datetime.fromisoformat(data['join_date'])
        data['last_active'] = datetime.fromisoformat(data['last_active'])
        return cls(**data)


@dataclass
class Competition:
    """Represents a ProSort competition"""
    id: str
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    problems: List[str]  # List of problem IDs
    participants: List[str]  # List of user IDs
    leaderboard: List[Dict[str, Any]]
    rules: Dict[str, Any]
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert competition to dictionary for storage"""
        data = asdict(self)
        data['start_time'] = self.start_time.isoformat()
        data['end_time'] = self.end_time.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Competition':
        """Create competition from dictionary"""
        data['start_time'] = datetime.fromisoformat(data['start_time'])
        data['end_time'] = datetime.fromisoformat(data['end_time'])
        return cls(**data)


class ProSortEngine:
    """Main ProSort engine for managing competitions and problems"""
    
    def __init__(self):
        self.problems: Dict[str, Problem] = {}
        self.users: Dict[str, User] = {}
        self.submissions: Dict[str, Submission] = {}
        self.competitions: Dict[str, Competition] = {}
        self.problem_bank: List[Problem] = []
        
    def add_problem(self, problem: Problem) -> bool:
        """Add a new problem to the system"""
        if problem.id in self.problems:
            return False
        
        self.problems[problem.id] = problem
        self.problem_bank.append(problem)
        return True
    
    def get_problem(self, problem_id: str) -> Optional[Problem]:
        """Retrieve a problem by ID"""
        return self.problems.get(problem_id)
    
    def get_problems_by_difficulty(self, difficulty: ProblemDifficulty) -> List[Problem]:
        """Get all problems of a specific difficulty"""
        return [p for p in self.problem_bank if p.difficulty == difficulty and p.is_active]
    
    def get_problems_by_type(self, problem_type: ProblemType) -> List[Problem]:
        """Get all problems of a specific type"""
        return [p for p in self.problem_bank if p.problem_type == problem_type and p.is_active]
    
    def submit_answer(self, user_id: str, problem_id: str, answer: str, 
                     code: Optional[str] = None, language: Optional[str] = None) -> Submission:
        """Submit an answer to a problem"""
        problem = self.get_problem(problem_id)
        if not problem:
            raise ValueError(f"Problem {problem_id} not found")
        
        # Generate submission ID
        submission_id = hashlib.md5(f"{user_id}_{problem_id}_{time.time()}".encode()).hexdigest()
        
        # Check if answer is correct
        is_correct = self._check_answer(problem, answer)
        status = "correct" if is_correct else "incorrect"
        score = problem.points if is_correct else 0
        
        # Create submission
        submission = Submission(
            id=submission_id,
            user_id=user_id,
            problem_id=problem_id,
            answer=answer,
            code=code,
            language=language,
            submitted_at=datetime.now(),
            execution_time=None,
            memory_used=None,
            status=status,
            score=score,
            feedback=self._generate_feedback(problem, answer, is_correct)
        )
        
        self.submissions[submission_id] = submission
        
        # Update user stats if correct
        if is_correct:
            self._update_user_stats(user_id, problem.points)
        
        return submission
    
    def _check_answer(self, problem: Problem, answer: str) -> bool:
        """Check if the submitted answer is correct"""
        # Simple string comparison for now
        # In a real system, this would be more sophisticated
        return answer.strip().lower() == problem.solution.strip().lower()
    
    def _generate_feedback(self, problem: Problem, answer: str, is_correct: bool) -> str:
        """Generate feedback for the submission"""
        if is_correct:
            return "Correct! Well done!"
        else:
            return f"Incorrect. The correct answer is: {problem.solution}"
    
    def _update_user_stats(self, user_id: str, points: int):
        """Update user statistics after solving a problem"""
        if user_id in self.users:
            user = self.users[user_id]
            user.total_score += points
            user.problems_solved += 1
            user.last_active = datetime.now()
    
    def create_competition(self, name: str, description: str, start_time: datetime, 
                          end_time: datetime, problem_ids: List[str], rules: Dict[str, Any]) -> Competition:
        """Create a new competition"""
        competition_id = hashlib.md5(f"{name}_{start_time.isoformat()}".encode()).hexdigest()
        
        competition = Competition(
            id=competition_id,
            name=name,
            description=description,
            start_time=start_time,
            end_time=end_time,
            problems=problem_ids,
            participants=[],
            leaderboard=[],
            rules=rules
        )
        
        self.competitions[competition_id] = competition
        return competition
    
    def get_leaderboard(self, competition_id: str) -> List[Dict[str, Any]]:
        """Get the leaderboard for a competition"""
        competition = self.competitions.get(competition_id)
        if not competition:
            return []
        
        # Calculate scores for all participants
        scores = {}
        for user_id in competition.participants:
            user = self.users.get(user_id)
            if user:
                scores[user_id] = {
                    'username': user.username,
                    'total_score': user.total_score,
                    'problems_solved': user.problems_solved
                }
        
        # Sort by score (descending)
        sorted_scores = sorted(scores.items(), key=lambda x: x[1]['total_score'], reverse=True)
        
        # Format leaderboard
        leaderboard = []
        for rank, (user_id, user_data) in enumerate(sorted_scores, 1):
            leaderboard.append({
                'rank': rank,
                'user_id': user_id,
                'username': user_data['username'],
                'total_score': user_data['total_score'],
                'problems_solved': user_data['problems_solved']
            })
        
        return leaderboard
    
    def get_user_progress(self, user_id: str) -> Dict[str, Any]:
        """Get detailed progress information for a user"""
        user = self.users.get(user_id)
        if not user:
            return {}
        
        # Get user's submissions
        user_submissions = [s for s in self.submissions.values() if s.user_id == user_id]
        
        # Calculate statistics
        total_submissions = len(user_submissions)
        correct_submissions = len([s for s in user_submissions if s.status == "correct"])
        accuracy = (correct_submissions / total_submissions * 100) if total_submissions > 0 else 0
        
        # Get problem types solved
        problem_types_solved = {}
        for submission in user_submissions:
            if submission.status == "correct":
                problem = self.problems.get(submission.problem_id)
                if problem:
                    problem_type = problem.problem_type.value
                    problem_types_solved[problem_type] = problem_types_solved.get(problem_type, 0) + 1
        
        return {
            'user_info': user.to_dict(),
            'total_submissions': total_submissions,
            'correct_submissions': correct_submissions,
            'accuracy': accuracy,
            'problem_types_solved': problem_types_solved,
            'recent_submissions': [s.to_dict() for s in user_submissions[-5:]]  # Last 5 submissions
        }
    
    def generate_problem_set(self, difficulty: ProblemDifficulty, count: int, 
                           problem_types: Optional[List[ProblemType]] = None) -> List[Problem]:
        """Generate a set of problems for a competition or practice session"""
        available_problems = [p for p in self.problem_bank 
                            if p.difficulty == difficulty and p.is_active]
        
        if problem_types:
            available_problems = [p for p in available_problems 
                               if p.problem_type in problem_types]
        
        # Randomly select problems
        selected_problems = random.sample(available_problems, min(count, len(available_problems)))
        return selected_problems
    
    def export_data(self) -> Dict[str, Any]:
        """Export all data for backup or analysis"""
        return {
            'problems': {pid: p.to_dict() for pid, p in self.problems.items()},
            'users': {uid: u.to_dict() for uid, u in self.users.items()},
            'submissions': {sid: s.to_dict() for sid, s in self.submissions.items()},
            'competitions': {cid: c.to_dict() for cid, c in self.competitions.items()}
        }
    
    def import_data(self, data: Dict[str, Any]):
        """Import data from backup"""
        # Clear existing data
        self.problems.clear()
        self.users.clear()
        self.submissions.clear()
        self.competitions.clear()
        self.problem_bank.clear()
        
        # Import problems
        for pid, p_data in data.get('problems', {}).items():
            problem = Problem.from_dict(p_data)
            self.problems[pid] = problem
            self.problem_bank.append(problem)
        
        # Import users
        for uid, u_data in data.get('users', {}).items():
            user = User.from_dict(u_data)
            self.users[uid] = user
        
        # Import submissions
        for sid, s_data in data.get('submissions', {}).items():
            submission = Submission.from_dict(s_data)
            self.submissions[sid] = submission
        
        # Import competitions
        for cid, c_data in data.get('competitions', {}).items():
            competition = Competition.from_dict(c_data)
            self.competitions[cid] = competition
