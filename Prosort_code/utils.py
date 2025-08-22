"""
ProSort Utility Functions
Helper functions for data persistence, validation, and system utilities
"""

import json
import os
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union
import pickle
import gzip
import base64
import re
import math


class DataPersistence:
    """Handles data persistence for the ProSort system"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self._ensure_data_dir()
    
    def _ensure_data_dir(self):
        """Ensure the data directory exists"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def save_data(self, data: Dict[str, Any], filename: str, compress: bool = True) -> bool:
        """Save data to file with optional compression"""
        try:
            filepath = os.path.join(self.data_dir, filename)
            
            if compress:
                # Save as compressed pickle
                with gzip.open(f"{filepath}.gz", 'wb') as f:
                    pickle.dump(data, f)
            else:
                # Save as JSON
                with open(f"{filepath}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, default=str)
            
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, filename: str, compress: bool = True) -> Optional[Dict[str, Any]]:
        """Load data from file with optional compression"""
        try:
            filepath = os.path.join(self.data_dir, filename)
            
            if compress:
                # Load from compressed pickle
                with gzip.open(f"{filepath}.gz", 'rb') as f:
                    return pickle.load(f)
            else:
                # Load from JSON
                with open(f"{filepath}.json", 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def backup_data(self, data: Dict[str, Any], backup_name: str = None) -> str:
        """Create a backup of data with timestamp"""
        if backup_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"backup_{timestamp}"
        
        backup_file = f"{backup_name}.gz"
        if self.save_data(data, backup_file, compress=True):
            return backup_file
        return ""
    
    def list_backups(self) -> List[str]:
        """List all available backup files"""
        backups = []
        for file in os.listdir(self.data_dir):
            if file.startswith("backup_") and file.endswith(".gz"):
                backups.append(file)
        return sorted(backups, reverse=True)
    
    def restore_backup(self, backup_name: str) -> Optional[Dict[str, Any]]:
        """Restore data from a backup file"""
        return self.load_data(backup_name, compress=True)


class DataValidator:
    """Validates data structures and inputs for the ProSort system"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username format"""
        # Username should be 3-20 characters, alphanumeric and underscores only
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, username) is not None
    
    @staticmethod
    def validate_problem_data(problem_data: Dict[str, Any]) -> List[str]:
        """Validate problem data structure"""
        errors = []
        required_fields = ['title', 'statement', 'difficulty', 'problem_type', 'points', 'solution']
        
        for field in required_fields:
            if field not in problem_data or not problem_data[field]:
                errors.append(f"Missing or empty required field: {field}")
        
        # Validate difficulty
        if 'difficulty' in problem_data:
            valid_difficulties = ['easy', 'medium', 'hard', 'expert']
            if problem_data['difficulty'] not in valid_difficulties:
                errors.append(f"Invalid difficulty: {problem_data['difficulty']}")
        
        # Validate problem type
        if 'problem_type' in problem_data:
            valid_types = ['algebra', 'geometry', 'calculus', 'number_theory', 
                          'combinatorics', 'probability', 'algorithms', 'optimization']
            if problem_data['problem_type'] not in valid_types:
                errors.append(f"Invalid problem type: {problem_data['problem_type']}")
        
        # Validate points
        if 'points' in problem_data:
            try:
                points = int(problem_data['points'])
                if points <= 0:
                    errors.append("Points must be positive")
            except (ValueError, TypeError):
                errors.append("Points must be an integer")
        
        return errors
    
    @staticmethod
    def validate_submission_data(submission_data: Dict[str, Any]) -> List[str]:
        """Validate submission data structure"""
        errors = []
        required_fields = ['user_id', 'problem_id', 'answer']
        
        for field in required_fields:
            if field not in submission_data or not submission_data[field]:
                errors.append(f"Missing or empty required field: {field}")
        
        return errors
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Sanitize user input to prevent injection attacks"""
        # Remove potentially dangerous characters
        dangerous_chars = ['<', '>', '"', "'", '&', ';', '{', '}', '[', ']']
        for char in dangerous_chars:
            text = text.replace(char, '')
        
        # Limit length
        if len(text) > 1000:
            text = text[:1000]
        
        return text.strip()


class MathUtils:
    """Mathematical utility functions for the ProSort system"""
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Calculate greatest common divisor using Euclidean algorithm"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Calculate least common multiple"""
        return abs(a * b) // MathUtils.gcd(a, b)
    
    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Get prime factorization of a number"""
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Calculate nth Fibonacci number"""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of n"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def combinations(n: int, r: int) -> int:
        """Calculate nCr (combinations)"""
        if r > n or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        
        # Use the formula: nCr = n! / (r! * (n-r)!)
        return MathUtils.factorial(n) // (MathUtils.factorial(r) * MathUtils.factorial(n - r))
    
    @staticmethod
    def permutations(n: int, r: int) -> int:
        """Calculate nPr (permutations)"""
        if r > n or r < 0:
            return 0
        if r == 0:
            return 1
        
        # Use the formula: nPr = n! / (n-r)!
        return MathUtils.factorial(n) // MathUtils.factorial(n - r)


class TimeUtils:
    """Time-related utility functions"""
    
    @staticmethod
    def format_duration(seconds: int) -> str:
        """Format duration in seconds to human-readable string"""
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{minutes}m {remaining_seconds}s"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            remaining_seconds = seconds % 60
            return f"{hours}h {remaining_minutes}m {remaining_seconds}s"
    
    @staticmethod
    def is_competition_active(start_time: datetime, end_time: datetime) -> bool:
        """Check if a competition is currently active"""
        now = datetime.now()
        return start_time <= now <= end_time
    
    @staticmethod
    def time_until_competition(start_time: datetime) -> str:
        """Get time until competition starts"""
        now = datetime.now()
        if now >= start_time:
            return "Competition has started"
        
        time_diff = start_time - now
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        
        if days > 0:
            return f"{days}d {hours}h {minutes}m"
        elif hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    @staticmethod
    def competition_time_remaining(end_time: datetime) -> str:
        """Get remaining time in competition"""
        now = datetime.now()
        if now >= end_time:
            return "Competition has ended"
        
        time_diff = end_time - now
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return f"{hours}h {minutes}m {seconds}s"


class SecurityUtils:
    """Security-related utility functions"""
    
    @staticmethod
    def hash_password(password: str, salt: str = None) -> tuple:
        """Hash a password with salt"""
        if salt is None:
            salt = base64.b64encode(os.urandom(16)).decode('utf-8')
        
        # Combine password and salt
        combined = password + salt
        
        # Create hash
        hashed = hashlib.sha256(combined.encode()).hexdigest()
        
        return hashed, salt
    
    @staticmethod
    def verify_password(password: str, hashed: str, salt: str) -> bool:
        """Verify a password against its hash"""
        test_hash, _ = SecurityUtils.hash_password(password, salt)
        return test_hash == hashed
    
    @staticmethod
    def generate_token(user_id: str, secret: str) -> str:
        """Generate a secure token for user authentication"""
        timestamp = str(int(time.time()))
        data = f"{user_id}:{timestamp}:{secret}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def validate_token(token: str, user_id: str, secret: str, max_age: int = 3600) -> bool:
        """Validate a user authentication token"""
        try:
            # Check if token is valid
            expected_token = SecurityUtils.generate_token(user_id, secret)
            return token == expected_token
        except:
            return False


class AnalyticsUtils:
    """Analytics and statistics utility functions"""
    
    @staticmethod
    def calculate_accuracy(correct: int, total: int) -> float:
        """Calculate accuracy percentage"""
        if total == 0:
            return 0.0
        return (correct / total) * 100
    
    @staticmethod
    def calculate_average_score(scores: List[float]) -> float:
        """Calculate average score"""
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    
    @staticmethod
    def calculate_percentile(scores: List[float], percentile: float) -> float:
        """Calculate percentile of scores"""
        if not scores:
            return 0.0
        
        sorted_scores = sorted(scores)
        index = (percentile / 100) * (len(sorted_scores) - 1)
        
        if index.is_integer():
            return sorted_scores[int(index)]
        else:
            lower = sorted_scores[int(index)]
            upper = sorted_scores[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))
    
    @staticmethod
    def calculate_ranking_score(score: float, time_taken: float, difficulty_multiplier: float = 1.0) -> float:
        """Calculate ranking score based on multiple factors"""
        # Base score
        base_score = score
        
        # Time bonus (faster solutions get bonus points)
        time_bonus = max(0, 100 - time_taken) / 100
        
        # Difficulty multiplier
        final_score = (base_score + time_bonus) * difficulty_multiplier
        
        return round(final_score, 2)
    
    @staticmethod
    def generate_progress_report(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive progress report for a user"""
        report = {
            'total_problems': user_data.get('total_submissions', 0),
            'correct_answers': user_data.get('correct_submissions', 0),
            'accuracy': user_data.get('accuracy', 0.0),
            'total_score': user_data.get('user_info', {}).get('total_score', 0),
            'rank': user_data.get('user_info', {}).get('rank', 0),
            'problem_types': user_data.get('problem_types_solved', {}),
            'recent_activity': user_data.get('recent_submissions', [])
        }
        
        # Calculate improvement rate
        if len(report['recent_activity']) >= 2:
            recent_correct = sum(1 for s in report['recent_activity'][-5:] if s.get('status') == 'correct')
            recent_total = len(report['recent_activity'][-5:])
            if recent_total > 0:
                recent_accuracy = (recent_correct / recent_total) * 100
                report['improvement_rate'] = recent_accuracy - report['accuracy']
            else:
                report['improvement_rate'] = 0
        else:
            report['improvement_rate'] = 0
        
        return report


class ExportUtils:
    """Export and import utility functions"""
    
    @staticmethod
    def export_to_csv(data: List[Dict[str, Any]], filename: str) -> str:
        """Export data to CSV format"""
        try:
            import pandas as pd
            df = pd.DataFrame(data)
            filepath = f"{filename}.csv"
            df.to_csv(filepath, index=False)
            return filepath
        except ImportError:
            raise ImportError("pandas is required for CSV export")
    
    @staticmethod
    def export_to_json(data: Any, filename: str, pretty: bool = True) -> str:
        """Export data to JSON format"""
        filepath = f"{filename}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(data, f, indent=2, default=str)
            else:
                json.dump(data, f, default=str)
        return filepath
    
    @staticmethod
    def export_to_pickle(data: Any, filename: str, compress: bool = True) -> str:
        """Export data to pickle format with optional compression"""
        filepath = f"{filename}.pkl"
        if compress:
            filepath += ".gz"
            with gzip.open(filepath, 'wb') as f:
                pickle.dump(data, f)
        else:
            with open(filepath, 'wb') as f:
                pickle.dump(data, f)
        return filepath
    
    @staticmethod
    def create_backup_summary(data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a summary of backup data"""
        summary = {
            'backup_timestamp': datetime.now().isoformat(),
            'total_problems': len(data.get('problems', {})),
            'total_users': len(data.get('users', {})),
            'total_submissions': len(data.get('submissions', {})),
            'total_competitions': len(data.get('competitions', {})),
            'data_size_mb': len(str(data).encode()) / (1024 * 1024)
        }
        return summary
