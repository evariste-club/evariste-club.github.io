"""
ProSort Problem Bank
Contains a collection of mathematical problems for competitions and practice
"""

import random
from datetime import datetime
from typing import List, Optional
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import Problem, ProblemDifficulty, ProblemType


class ProblemBank:
    """Manages a collection of mathematical problems"""
    
    def __init__(self):
        self.problems: List[Problem] = []
        self._initialize_problems()
    
    def _initialize_problems(self):
        """Initialize the problem bank with sample problems"""
        self._add_algebra_problems()
        self._add_geometry_problems()
        self._add_calculus_problems()
        self._add_number_theory_problems()
        self._add_combinatorics_problems()
        self._add_probability_problems()
        self._add_algorithms_problems()
        self._add_optimization_problems()
    
    def _add_algebra_problems(self):
        """Add algebra problems"""
        problems = [
            Problem(
                id="alg_001",
                title="Quadratic Equation Roots",
                statement="Find all real roots of the equation: x² - 5x + 6 = 0",
                difficulty=ProblemDifficulty.EASY,
                problem_type=ProblemType.ALGEBRA,
                points=10,
                time_limit=300,
                hints=["Try factoring the quadratic", "Look for factors of 6 that add to -5"],
                solution="x² - 5x + 6 = (x - 2)(x - 3) = 0\nTherefore, x = 2 or x = 3",
                test_cases=[{"input": "x² - 5x + 6 = 0", "output": "x = 2, x = 3"}],
                tags=["quadratic", "factoring", "roots"],
                created_at=datetime.now()
            ),
            Problem(
                id="alg_002",
                title="System of Linear Equations",
                statement="Solve the system:\n2x + y = 5\nx - 3y = -7",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.ALGEBRA,
                points=15,
                time_limit=600,
                hints=["Use substitution or elimination", "Solve for one variable first"],
                solution="From first equation: y = 5 - 2x\nSubstitute into second: x - 3(5-2x) = -7\nx - 15 + 6x = -7\n7x = 8\nx = 8/7\ny = 5 - 2(8/7) = 19/7",
                test_cases=[{"input": "2x + y = 5, x - 3y = -7", "output": "x = 8/7, y = 19/7"}],
                tags=["linear equations", "system", "substitution"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_geometry_problems(self):
        """Add geometry problems"""
        problems = [
            Problem(
                id="geo_001",
                title="Pythagorean Theorem",
                statement="In a right triangle, if the legs are 3 and 4 units long, what is the length of the hypotenuse?",
                difficulty=ProblemDifficulty.EASY,
                problem_type=ProblemType.GEOMETRY,
                points=10,
                time_limit=300,
                hints=["Use a² + b² = c²", "c is the hypotenuse"],
                solution="Using Pythagorean theorem: a² + b² = c²\n3² + 4² = c²\n9 + 16 = c²\n25 = c²\nc = 5",
                test_cases=[{"input": "a=3, b=4", "output": "c=5"}],
                tags=["right triangle", "pythagorean theorem", "hypotenuse"],
                created_at=datetime.now()
            ),
            Problem(
                id="geo_002",
                title="Area of Circle",
                statement="Find the area of a circle with radius 7 units. Use π ≈ 3.14159",
                difficulty=ProblemDifficulty.EASY,
                problem_type=ProblemType.GEOMETRY,
                points=10,
                time_limit=300,
                hints=["Area = πr²", "r = 7"],
                solution="Area = πr² = π × 7² = π × 49 ≈ 3.14159 × 49 ≈ 153.938",
                test_cases=[{"input": "r=7", "output": "≈153.938"}],
                tags=["circle", "area", "radius"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_calculus_problems(self):
        """Add calculus problems"""
        problems = [
            Problem(
                id="calc_001",
                title="Derivative of Polynomial",
                statement="Find the derivative of f(x) = 3x³ - 2x² + 5x - 1",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.CALCULUS,
                points=15,
                time_limit=600,
                hints=["Use power rule: d/dx(xⁿ) = nxⁿ⁻¹", "Derivative of constant is 0"],
                solution="f'(x) = d/dx(3x³) - d/dx(2x²) + d/dx(5x) - d/dx(1)\nf'(x) = 9x² - 4x + 5",
                test_cases=[{"input": "3x³ - 2x² + 5x - 1", "output": "9x² - 4x + 5"}],
                tags=["derivative", "polynomial", "power rule"],
                created_at=datetime.now()
            ),
            Problem(
                id="calc_002",
                title="Definite Integral",
                statement="Evaluate ∫₀¹ (2x + 1) dx",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.CALCULUS,
                points=15,
                time_limit=600,
                hints=["Find antiderivative first", "Then evaluate at limits"],
                solution="∫(2x + 1) dx = x² + x + C\n∫₀¹ (2x + 1) dx = [x² + x]₀¹ = (1² + 1) - (0² + 0) = 2",
                test_cases=[{"input": "∫₀¹ (2x + 1) dx", "output": "2"}],
                tags=["integral", "definite integral", "antiderivative"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_number_theory_problems(self):
        """Add number theory problems"""
        problems = [
            Problem(
                id="nt_001",
                title="Prime Factorization",
                statement="Find the prime factorization of 84",
                difficulty=ProblemDifficulty.EASY,
                problem_type=ProblemType.NUMBER_THEORY,
                points=10,
                time_limit=300,
                hints=["Start with smallest prime", "Divide repeatedly"],
                solution="84 = 2 × 42 = 2 × 2 × 21 = 2 × 2 × 3 × 7 = 2² × 3 × 7",
                test_cases=[{"input": "84", "output": "2² × 3 × 7"}],
                tags=["prime factorization", "divisibility"],
                created_at=datetime.now()
            ),
            Problem(
                id="nt_002",
                title="GCD and LCM",
                statement="Find the GCD and LCM of 48 and 60",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.NUMBER_THEORY,
                points=15,
                time_limit=600,
                hints=["Use prime factorization", "GCD: common factors with lowest exponents", "LCM: all factors with highest exponents"],
                solution="48 = 2⁴ × 3\n60 = 2² × 3 × 5\nGCD = 2² × 3 = 12\nLCM = 2⁴ × 3 × 5 = 240",
                test_cases=[{"input": "48, 60", "output": "GCD=12, LCM=240"}],
                tags=["gcd", "lcm", "prime factorization"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_combinatorics_problems(self):
        """Add combinatorics problems"""
        problems = [
            Problem(
                id="comb_001",
                title="Permutations",
                statement="How many different ways can 5 people sit in 5 chairs?",
                difficulty=ProblemDifficulty.EASY,
                problem_type=ProblemType.COMBINATORICS,
                points=10,
                time_limit=300,
                hints=["Use factorial", "n! = n × (n-1) × ... × 1"],
                solution="5! = 5 × 4 × 3 × 2 × 1 = 120",
                test_cases=[{"input": "5 people, 5 chairs", "output": "120"}],
                tags=["permutations", "factorial"],
                created_at=datetime.now()
            ),
            Problem(
                id="comb_002",
                title="Combinations",
                statement="How many ways can you choose 3 students from a class of 10?",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.COMBINATORICS,
                points=15,
                time_limit=600,
                hints=["Use combination formula", "C(n,r) = n!/(r!(n-r)!)"],
                solution="C(10,3) = 10!/(3! × 7!) = (10×9×8)/(3×2×1) = 120",
                test_cases=[{"input": "10 students, choose 3", "output": "120"}],
                tags=["combinations", "binomial coefficient"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_probability_problems(self):
        """Add probability problems"""
        problems = [
            Problem(
                id="prob_001",
                title="Coin Toss Probability",
                statement="What is the probability of getting exactly 2 heads in 3 coin tosses?",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.PROBABILITY,
                points=15,
                time_limit=600,
                hints=["Use binomial probability", "P(X=k) = C(n,k) × p^k × (1-p)^(n-k)"],
                solution="P(X=2) = C(3,2) × (1/2)² × (1/2)¹ = 3 × (1/4) × (1/2) = 3/8",
                test_cases=[{"input": "3 tosses, 2 heads", "output": "3/8"}],
                tags=["probability", "binomial", "coin toss"],
                created_at=datetime.now()
            ),
            Problem(
                id="prob_002",
                title="Dice Probability",
                statement="What is the probability of rolling a sum of 7 with two dice?",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.PROBABILITY,
                points=15,
                time_limit=600,
                hints=["Count favorable outcomes", "Total outcomes = 36"],
                solution="Favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\nTotal outcomes = 36\nProbability = 6/36 = 1/6",
                test_cases=[{"input": "sum of 7, two dice", "output": "1/6"}],
                tags=["probability", "dice", "counting"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_algorithms_problems(self):
        """Add algorithms problems"""
        problems = [
            Problem(
                id="algo_001",
                title="Fibonacci Sequence",
                statement="Write an algorithm to find the nth Fibonacci number. F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.ALGORITHMS,
                points=20,
                time_limit=900,
                hints=["Consider recursive vs iterative approach", "Think about time complexity"],
                solution="Iterative approach:\nF(0) = 0, F(1) = 1\nFor i from 2 to n:\n  F(i) = F(i-1) + F(i-2)\nReturn F(n)",
                test_cases=[{"input": "n=5", "output": "5"}, {"input": "n=10", "output": "55"}],
                tags=["fibonacci", "recursion", "dynamic programming"],
                created_at=datetime.now()
            ),
            Problem(
                id="algo_002",
                title="Sorting Algorithm",
                statement="Implement bubble sort and analyze its time complexity",
                difficulty=ProblemDifficulty.HARD,
                problem_type=ProblemType.ALGORITHMS,
                points=25,
                time_limit=1200,
                hints=["Compare adjacent elements", "Bubble largest to end", "Consider worst case"],
                solution="Bubble Sort:\nFor i from 0 to n-1:\n  For j from 0 to n-i-1:\n    If A[j] > A[j+1]:\n      Swap A[j] and A[j+1]\nTime Complexity: O(n²)",
                test_cases=[{"input": "[5,2,4,1,3]", "output": "[1,2,3,4,5]"}],
                tags=["sorting", "bubble sort", "time complexity"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def _add_optimization_problems(self):
        """Add optimization problems"""
        problems = [
            Problem(
                id="opt_001",
                title="Linear Programming",
                statement="Maximize f(x,y) = 3x + 2y subject to:\nx + y ≤ 4\n2x + y ≤ 6\nx, y ≥ 0",
                difficulty=ProblemDifficulty.HARD,
                problem_type=ProblemType.OPTIMIZATION,
                points=25,
                time_limit=1200,
                hints=["Graph the constraints", "Find corner points", "Evaluate objective function at corners"],
                solution="Corner points: (0,0), (0,4), (2,2), (3,0)\nf(0,0) = 0, f(0,4) = 8, f(2,2) = 10, f(3,0) = 9\nMaximum is 10 at (2,2)",
                test_cases=[{"input": "constraints given", "output": "max=10 at (2,2)"}],
                tags=["linear programming", "optimization", "constraints"],
                created_at=datetime.now()
            ),
            Problem(
                id="opt_002",
                title="Function Optimization",
                statement="Find the minimum value of f(x) = x² - 4x + 3",
                difficulty=ProblemDifficulty.MEDIUM,
                problem_type=ProblemType.OPTIMIZATION,
                points=20,
                time_limit=900,
                hints=["Find critical points", "Use derivative", "Check second derivative"],
                solution="f'(x) = 2x - 4\nSet f'(x) = 0: 2x - 4 = 0\nx = 2\nf(2) = 2² - 4(2) + 3 = 4 - 8 + 3 = -1\nMinimum value is -1 at x = 2",
                test_cases=[{"input": "x² - 4x + 3", "output": "min=-1 at x=2"}],
                tags=["optimization", "derivative", "critical points"],
                created_at=datetime.now()
            )
        ]
        self.problems.extend(problems)
    
    def get_problem_by_id(self, problem_id: str) -> Optional[Problem]:
        """Get a problem by its ID"""
        for problem in self.problems:
            if problem.id == problem_id:
                return problem
        return None
    
    def get_problems_by_difficulty(self, difficulty: ProblemDifficulty) -> List[Problem]:
        """Get all problems of a specific difficulty"""
        return [p for p in self.problems if p.difficulty == difficulty]
    
    def get_problems_by_type(self, problem_type: ProblemType) -> List[Problem]:
        """Get all problems of a specific type"""
        return [p for p in self.problems if p.problem_type == problem_type]
    
    def get_random_problem(self, difficulty: Optional[ProblemDifficulty] = None, 
                          problem_type: Optional[ProblemType] = None) -> Optional[Problem]:
        """Get a random problem, optionally filtered by difficulty and/or type"""
        filtered_problems = self.problems
        
        if difficulty:
            filtered_problems = [p for p in filtered_problems if p.difficulty == difficulty]
        
        if problem_type:
            filtered_problems = [p for p in filtered_problems if p.problem_type == problem_type]
        
        if filtered_problems:
            return random.choice(filtered_problems)
        return None
    
    def get_all_problems(self) -> List[Problem]:
        """Get all problems"""
        return self.problems.copy()
    
    def get_problem_count(self) -> int:
        """Get total number of problems"""
        return len(self.problems)
    
    def get_problem_count_by_difficulty(self) -> dict:
        """Get count of problems by difficulty"""
        counts = {}
        for difficulty in ProblemDifficulty:
            counts[difficulty.value] = len(self.get_problems_by_difficulty(difficulty))
        return counts
    
    def get_problem_count_by_type(self) -> dict:
        """Get count of problems by type"""
        counts = {}
        for problem_type in ProblemType:
            counts[problem_type.value] = len(self.get_problems_by_type(problem_type))
        return counts


# Global problem bank instance
problem_bank = ProblemBank()
