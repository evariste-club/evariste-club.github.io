import numpy as np
import pandas as pd
from scipy import linalg, optimize
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Tuple, Optional

class MathTools:
    """Collection of mathematical tools and utilities for the Évariste Math Club app."""
    
    @staticmethod
    def solve_linear_system(coefficients: np.ndarray, constants: np.ndarray) -> Tuple[np.ndarray, str]:
        """Solve a system of linear equations Ax = b."""
        try:
            solution = np.linalg.solve(coefficients, constants)
            return solution, "Unique solution found"
        except np.linalg.LinAlgError:
            return None, "No unique solution (system may be singular or inconsistent)"
    
    @staticmethod
    def find_eigenvalues(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Find eigenvalues and eigenvectors of a matrix."""
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
    
    @staticmethod
    def matrix_rank(matrix: np.ndarray) -> int:
        """Find the rank of a matrix."""
        return np.linalg.matrix_rank(matrix)
    
    @staticmethod
    def matrix_determinant(matrix: np.ndarray) -> float:
        """Find the determinant of a matrix."""
        return np.linalg.det(matrix)
    
    @staticmethod
    def prime_factorization(n: int) -> List[int]:
        """Find prime factorization of a number."""
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
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def generate_primes(n: int) -> List[int]:
        """Generate first n prime numbers using Sieve of Eratosthenes."""
        if n <= 0:
            return []
        
        # Estimate upper bound for nth prime
        upper_bound = max(100, int(n * np.log(n) + n * np.log(np.log(n))))
        
        sieve = [True] * upper_bound
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(upper_bound**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, upper_bound, i):
                    sieve[j] = False
        
        primes = [i for i in range(upper_bound) if sieve[i]]
        return primes[:n]
    
    @staticmethod
    def fibonacci_sequence(n: int) -> List[int]:
        """Generate first n Fibonacci numbers."""
        if n <= 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    @staticmethod
    def plot_function(func_str: str, x_range: Tuple[float, float], points: int = 1000) -> go.Figure:
        """Plot a mathematical function."""
        try:
            x = np.linspace(x_range[0], x_range[1], points)
            # Safe evaluation of mathematical expressions
            y = eval(func_str, {"__builtins__": {}}, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, 
                                                     "tan": np.tan, "exp": np.exp, "log": np.log, 
                                                     "sqrt": np.sqrt, "pi": np.pi, "e": np.e})
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=func_str))
            fig.update_layout(
                title=f"Graph of {func_str}",
                xaxis_title="x",
                yaxis_title="y",
                template="plotly_white"
            )
            return fig
        except Exception as e:
            # Return error figure
            fig = go.Figure()
            fig.add_annotation(text=f"Error plotting function: {str(e)}", 
                             xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False)
            return fig
    
    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> Tuple[List[complex], str]:
        """Solve quadratic equation ax² + bx + c = 0."""
        if a == 0:
            return None, "Not a quadratic equation (a = 0)"
        
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + np.sqrt(discriminant)) / (2*a)
            x2 = (-b - np.sqrt(discriminant)) / (2*a)
            return [x1, x2], "Two real roots"
        elif discriminant == 0:
            x = -b / (2*a)
            return [x], "One real root (repeated)"
        else:
            x1 = (-b + 1j * np.sqrt(-discriminant)) / (2*a)
            x2 = (-b - 1j * np.sqrt(-discriminant)) / (2*a)
            return [x1, x2], "Two complex roots"
    
    @staticmethod
    def matrix_visualization(matrix: np.ndarray) -> go.Figure:
        """Create a heatmap visualization of a matrix."""
        fig = px.imshow(matrix, 
                       text_auto=True, 
                       aspect="auto",
                       color_continuous_scale="RdBu_r")
        fig.update_layout(
            title="Matrix Visualization",
            xaxis_title="Columns",
            yaxis_title="Rows"
        )
        return fig
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Find greatest common divisor using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Find least common multiple."""
        return abs(a * b) // MathTools.gcd(a, b)
    
    @staticmethod
    def modular_inverse(a: int, m: int) -> Optional[int]:
        """Find modular multiplicative inverse of a modulo m."""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        g, x, _ = extended_gcd(a, m)
        if g != 1:
            return None  # No inverse exists
        return (x % m + m) % m

# Example usage and testing
if __name__ == "__main__":
    # Test the MathTools class
    tools = MathTools()
    
    # Test prime generation
    print("First 10 primes:", tools.generate_primes(10))
    
    # Test Fibonacci
    print("First 15 Fibonacci numbers:", tools.fibonacci_sequence(15))
    
    # Test matrix operations
    matrix = np.array([[2, 1], [1, 3]])
    print("Matrix:", matrix)
    print("Determinant:", tools.matrix_determinant(matrix))
    print("Rank:", tools.matrix_rank(matrix))
    
    eigenvalues, eigenvectors = tools.find_eigenvalues(matrix)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
