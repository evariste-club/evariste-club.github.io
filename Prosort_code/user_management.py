"""
ProSort User Management System
Handles user registration, authentication, and participation tracking
"""

import hashlib
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import uuid
import re
import sys

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import DataValidator, SecurityUtils, DataPersistence


@dataclass
class UserProfile:
    """Extended user profile with additional information"""
    user_id: str
    username: str
    email: str
    full_name: str
    institution: str
    student_id: str
    phone: str
    date_of_birth: str
    grade_level: str
    mathematical_background: List[str]
    interests: List[str]
    created_at: datetime
    last_login: datetime
    is_active: bool = True
    is_verified: bool = False
    profile_complete: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert profile to dictionary"""
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['last_login'] = self.last_login.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserProfile':
        """Create profile from dictionary"""
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        data['last_login'] = datetime.fromisoformat(data['last_login'])
        return cls(**data)


@dataclass
class UserParticipation:
    """Tracks user participation in competitions and problems"""
    participation_id: str
    user_id: str
    competition_id: Optional[str]
    problem_id: str
    start_time: datetime
    end_time: Optional[datetime]
    time_spent: Optional[int]  # in seconds
    problem_choice: str  # "selected", "skipped", "attempted"
    written_solution: str
    code_solution: Optional[str]
    programming_language: Optional[str]
    hints_used: List[str]
    attempts_made: int
    final_answer: str
    is_correct: bool
    score_earned: float
    notes: str
    created_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert participation to dictionary"""
        data = asdict(self)
        data['start_time'] = self.start_time.isoformat()
        data['end_time'] = self.end_time.isoformat() if self.end_time else None
        data['created_at'] = self.created_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserParticipation':
        """Create participation from dictionary"""
        data['start_time'] = datetime.fromisoformat(data['start_time'])
        if data['end_time']:
            data['end_time'] = datetime.fromisoformat(data['end_time'])
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)


@dataclass
class UserSession:
    """Manages user login sessions"""
    session_id: str
    user_id: str
    token: str
    created_at: datetime
    expires_at: datetime
    ip_address: str
    user_agent: str
    is_active: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary"""
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['expires_at'] = self.expires_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserSession':
        """Create session from dictionary"""
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        data['expires_at'] = datetime.fromisoformat(data['expires_at'])
        return cls(**data)


class UserManager:
    """Manages user accounts, authentication, and participation"""
    
    def __init__(self, data_dir: str = "user_data"):
        self.data_dir = data_dir
        self.persistence = DataPersistence(data_dir)
        self.users: Dict[str, UserProfile] = {}
        self.participations: Dict[str, UserParticipation] = {}
        self.sessions: Dict[str, UserSession] = {}
        self.secret_key = os.environ.get('PROSORT_SECRET_KEY', 'default_secret_key_change_in_production')
        
        self._load_data()
    
    def _load_data(self):
        """Load existing user data"""
        # Load users
        users_data = self.persistence.load_data("users", compress=False)
        if users_data:
            for user_id, user_data in users_data.items():
                self.users[user_id] = UserProfile.from_dict(user_data)
        
        # Load participations
        participations_data = self.persistence.load_data("participations", compress=False)
        if participations_data:
            for part_id, part_data in participations_data.items():
                self.participations[part_id] = UserParticipation.from_dict(part_data)
        
        # Load sessions
        sessions_data = self.persistence.load_data("sessions", compress=False)
        if sessions_data:
            for session_id, session_data in sessions_data.items():
                self.sessions[session_id] = UserSession.from_dict(session_data)
    
    def _save_data(self):
        """Save all user data"""
        # Save users
        users_data = {uid: user.to_dict() for uid, user in self.users.items()}
        self.persistence.save_data(users_data, "users", compress=False)
        
        # Save participations
        participations_data = {pid: part.to_dict() for pid, part in self.participations.items()}
        self.persistence.save_data(participations_data, "participations", compress=False)
        
        # Save sessions
        sessions_data = {sid: session.to_dict() for sid, session in self.sessions.items()}
        self.persistence.save_data(sessions_data, "sessions", compress=False)
    
    def register_user(self, registration_data: Dict[str, Any]) -> Tuple[bool, str, Optional[str]]:
        """Register a new user"""
        try:
            # Validate required fields
            required_fields = ['username', 'email', 'full_name', 'password']
            for field in required_fields:
                if field not in registration_data or not registration_data[field]:
                    return False, f"Missing required field: {field}", None
            
            # Validate email format
            if not DataValidator.validate_email(registration_data['email']):
                return False, "Invalid email format", None
            
            # Validate username format
            if not DataValidator.validate_username(registration_data['username']):
                return False, "Username must be 3-20 characters, alphanumeric and underscores only", None
            
            # Check if username already exists
            for user in self.users.values():
                if user.username == registration_data['username']:
                    return False, "Username already exists", None
                if user.email == registration_data['email']:
                    return False, "Email already registered", None
            
            # Create user ID
            user_id = str(uuid.uuid4())
            
            # Hash password
            hashed_password, salt = SecurityUtils.hash_password(registration_data['password'])
            
            # Create user profile
            user_profile = UserProfile(
                user_id=user_id,
                username=registration_data['username'],
                email=registration_data['email'],
                full_name=registration_data['full_name'],
                institution=registration_data.get('institution', ''),
                student_id=registration_data.get('student_id', ''),
                phone=registration_data.get('phone', ''),
                date_of_birth=registration_data.get('date_of_birth', ''),
                grade_level=registration_data.get('grade_level', ''),
                mathematical_background=registration_data.get('mathematical_background', []),
                interests=registration_data.get('interests', []),
                created_at=datetime.now(),
                last_login=datetime.now()
            )
            
            # Store user with hashed password
            user_data = user_profile.to_dict()
            user_data['hashed_password'] = hashed_password
            user_data['salt'] = salt
            
            self.users[user_id] = user_profile
            self._save_data()
            
            return True, "User registered successfully", user_id
            
        except Exception as e:
            return False, f"Registration error: {str(e)}", None
    
    def authenticate_user(self, username: str, password: str, ip_address: str = "", user_agent: str = "") -> Tuple[bool, str, Optional[Dict[str, Any]]]:
        """Authenticate user and create session"""
        try:
            # Find user by username
            user = None
            for u in self.users.values():
                if u.username == username:
                    user = u
                    break
            
            if not user:
                return False, "Invalid username or password", None
            
            if not user.is_active:
                return False, "Account is deactivated", None
            
            # Load user data to get password hash
            users_data = self.persistence.load_data("users", compress=False)
            if not users_data or user.user_id not in users_data:
                return False, "Authentication error", None
            
            user_data = users_data[user.user_id]
            hashed_password = user_data.get('hashed_password')
            salt = user_data.get('salt')
            
            if not hashed_password or not salt:
                return False, "Authentication error", None
            
            # Verify password
            if not SecurityUtils.verify_password(password, hashed_password, salt):
                return False, "Invalid username or password", None
            
            # Update last login
            user.last_login = datetime.now()
            
            # Create session
            session_id = str(uuid.uuid4())
            token = SecurityUtils.generate_token(user.user_id, self.secret_key)
            
            session = UserSession(
                session_id=session_id,
                user_id=user.user_id,
                token=token,
                created_at=datetime.now(),
                expires_at=datetime.now() + timedelta(hours=24),
                ip_address=ip_address,
                user_agent=user_agent
            )
            
            self.sessions[session_id] = session
            self._save_data()
            
            # Return user info (without sensitive data)
            user_info = {
                'user_id': user.user_id,
                'username': user.username,
                'full_name': user.full_name,
                'email': user.email,
                'institution': user.institution,
                'session_id': session_id,
                'token': token
            }
            
            return True, "Authentication successful", user_info
            
        except Exception as e:
            return False, f"Authentication error: {str(e)}", None
    
    def validate_session(self, token: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """Validate user session token"""
        try:
            # Find active session with token
            active_session = None
            for session in self.sessions.values():
                if session.token == token and session.is_active and session.expires_at > datetime.now():
                    active_session = session
                    break
            
            if not active_session:
                return False, None
            
            # Get user info
            user = self.users.get(active_session.user_id)
            if not user or not user.is_active:
                return False, None
            
            user_info = {
                'user_id': user.user_id,
                'username': user.username,
                'full_name': user.full_name,
                'email': user.email,
                'institution': user.institution,
                'session_id': active_session.session_id
            }
            
            return True, user_info
            
        except Exception as e:
            return False, None
    
    def logout_user(self, token: str) -> bool:
        """Logout user by invalidating session"""
        try:
            for session in self.sessions.values():
                if session.token == token:
                    session.is_active = False
                    self._save_data()
                    return True
            return False
        except Exception:
            return False
    
    def update_user_profile(self, user_id: str, profile_data: Dict[str, Any]) -> Tuple[bool, str]:
        """Update user profile information"""
        try:
            if user_id not in self.users:
                return False, "User not found"
            
            user = self.users[user_id]
            
            # Update allowed fields
            allowed_fields = ['full_name', 'institution', 'student_id', 'phone', 
                            'date_of_birth', 'grade_level', 'mathematical_background', 'interests']
            
            for field in allowed_fields:
                if field in profile_data:
                    setattr(user, field, profile_data[field])
            
            # Mark profile as complete
            user.profile_complete = True
            
            self._save_data()
            return True, "Profile updated successfully"
            
        except Exception as e:
            return False, f"Profile update error: {str(e)}"
    
    def record_participation(self, participation_data: Dict[str, Any]) -> Tuple[bool, str, Optional[str]]:
        """Record user participation in a problem or competition"""
        try:
            # Validate required fields
            required_fields = ['user_id', 'problem_id', 'problem_choice', 'written_solution']
            for field in required_fields:
                if field not in participation_data or not participation_data[field]:
                    return False, f"Missing required field: {field}", None
            
            # Check if user exists
            if participation_data['user_id'] not in self.users:
                return False, "User not found", None
            
            # Create participation record
            participation_id = str(uuid.uuid4())
            
            participation = UserParticipation(
                participation_id=participation_id,
                user_id=participation_data['user_id'],
                competition_id=participation_data.get('competition_id'),
                problem_id=participation_data['problem_id'],
                start_time=participation_data.get('start_time', datetime.now()),
                end_time=participation_data.get('end_time'),
                time_spent=participation_data.get('time_spent'),
                problem_choice=participation_data['problem_choice'],
                written_solution=participation_data['written_solution'],
                code_solution=participation_data.get('code_solution'),
                programming_language=participation_data.get('programming_language'),
                hints_used=participation_data.get('hints_used', []),
                attempts_made=participation_data.get('attempts_made', 1),
                final_answer=participation_data.get('final_answer', ''),
                is_correct=participation_data.get('is_correct', False),
                score_earned=participation_data.get('score_earned', 0.0),
                notes=participation_data.get('notes', ''),
                created_at=datetime.now()
            )
            
            self.participations[participation_id] = participation
            self._save_data()
            
            return True, "Participation recorded successfully", participation_id
            
        except Exception as e:
            return False, f"Participation recording error: {str(e)}", None
    
    def get_user_participation_history(self, user_id: str) -> List[Dict[str, Any]]:
        """Get participation history for a user"""
        try:
            user_participations = [p for p in self.participations.values() if p.user_id == user_id]
            
            # Sort by creation date (newest first)
            user_participations.sort(key=lambda x: x.created_at, reverse=True)
            
            # Convert to dictionaries
            history = []
            for participation in user_participations:
                part_dict = participation.to_dict()
                # Add problem title if available
                part_dict['problem_title'] = f"Problem {participation.problem_id}"
                history.append(part_dict)
            
            return history
            
        except Exception as e:
            print(f"Error getting participation history: {e}")
            return []
    
    def get_user_statistics(self, user_id: str) -> Dict[str, Any]:
        """Get comprehensive statistics for a user"""
        try:
            if user_id not in self.users:
                return {}
            
            user = self.users[user_id]
            user_participations = [p for p in self.participations.values() if p.user_id == user_id]
            
            # Calculate statistics
            total_participations = len(user_participations)
            correct_answers = len([p for p in user_participations if p.is_correct])
            total_score = sum(p.score_earned for p in user_participations)
            
            # Problem choice distribution
            choice_distribution = {}
            for participation in user_participations:
                choice = participation.problem_choice
                choice_distribution[choice] = choice_distribution.get(choice, 0) + 1
            
            # Time analysis
            total_time_spent = sum(p.time_spent or 0 for p in user_participations)
            avg_time_per_problem = total_time_spent / total_participations if total_participations > 0 else 0
            
            # Programming language usage
            language_usage = {}
            for participation in user_participations:
                if participation.programming_language:
                    lang = participation.programming_language
                    language_usage[lang] = language_usage.get(lang, 0) + 1
            
            stats = {
                'user_info': {
                    'username': user.username,
                    'full_name': user.full_name,
                    'institution': user.institution,
                    'join_date': user.created_at.strftime('%Y-%m-%d'),
                    'last_active': user.last_login.strftime('%Y-%m-%d %H:%M')
                },
                'participation_stats': {
                    'total_participations': total_participations,
                    'correct_answers': correct_answers,
                    'accuracy': (correct_answers / total_participations * 100) if total_participations > 0 else 0,
                    'total_score': total_score,
                    'avg_score_per_problem': total_score / total_participations if total_participations > 0 else 0
                },
                'choice_analysis': {
                    'problem_choice_distribution': choice_distribution,
                    'total_time_spent': total_time_spent,
                    'avg_time_per_problem': avg_time_per_problem,
                    'programming_language_usage': language_usage
                },
                'recent_activity': [
                    {
                        'problem_id': p.problem_id,
                        'problem_choice': p.problem_choice,
                        'is_correct': p.is_correct,
                        'score_earned': p.score_earned,
                        'date': p.created_at.strftime('%Y-%m-%d %H:%M')
                    }
                    for p in user_participations[-5:]  # Last 5 participations
                ]
            }
            
            return stats
            
        except Exception as e:
            print(f"Error getting user statistics: {e}")
            return {}
    
    def search_users(self, query: str) -> List[Dict[str, Any]]:
        """Search users by name, username, or institution"""
        try:
            query = query.lower()
            results = []
            
            for user in self.users.values():
                if (query in user.username.lower() or 
                    query in user.full_name.lower() or 
                    query in user.institution.lower()):
                    
                    # Get basic stats for this user
                    stats = self.get_user_statistics(user.user_id)
                    
                    user_info = {
                        'user_id': user.user_id,
                        'username': user.username,
                        'full_name': user.full_name,
                        'institution': user.institution,
                        'join_date': user.created_at.strftime('%Y-%m-%d'),
                        'total_participations': stats.get('participation_stats', {}).get('total_participations', 0),
                        'total_score': stats.get('participation_stats', {}).get('total_score', 0)
                    }
                    results.append(user_info)
            
            return results
            
        except Exception as e:
            print(f"Error searching users: {e}")
            return []
    
    def export_user_data(self, user_id: str, format_type: str = 'json') -> Tuple[bool, str, Optional[str]]:
        """Export user data in various formats"""
        try:
            if user_id not in self.users:
                return False, "User not found", None
            
            user = self.users[user_id]
            stats = self.get_user_statistics(user_id)
            participation_history = self.get_user_participation_history(user_id)
            
            export_data = {
                'user_profile': user.to_dict(),
                'statistics': stats,
                'participation_history': participation_history,
                'export_timestamp': datetime.now().isoformat()
            }
            
            if format_type == 'json':
                import json
                data_str = json.dumps(export_data, indent=2, default=str)
                return True, "Data exported successfully", data_str
            else:
                return False, f"Unsupported format: {format_type}", None
                
        except Exception as e:
            return False, f"Export error: {str(e)}", None
    
    def cleanup_expired_sessions(self):
        """Remove expired user sessions"""
        try:
            current_time = datetime.now()
            expired_sessions = []
            
            for session_id, session in self.sessions.items():
                if session.expires_at < current_time:
                    expired_sessions.append(session_id)
            
            for session_id in expired_sessions:
                del self.sessions[session_id]
            
            if expired_sessions:
                self._save_data()
                print(f"Cleaned up {len(expired_sessions)} expired sessions")
                
        except Exception as e:
            print(f"Error cleaning up sessions: {e}")


# Global user manager instance
user_manager = UserManager()
