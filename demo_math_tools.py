#!/usr/bin/env python3
"""
Demo script for the MathTools class.
Run this to see examples of all available mathematical tools.
"""

from math_tools import MathTools
import numpy as np

def demo_matrix_operations():
    """Demonstrate matrix operations."""
    print("🔢 Matrix Operations Demo")
    print("=" * 40)
    
    # Create a sample matrix
    matrix = np.array([[2, 1], [1, 3]])
    print(f"Sample Matrix:\n{matrix}")
    
    # Calculate determinant
    det = MathTools.matrix_determinant(matrix)
    print(f"Determinant: {det}")
    
    # Find rank
    rank = MathTools.matrix_rank(matrix)
    print(f"Rank: {rank}")
    
    # Find eigenvalues and eigenvectors
    eigenvalues, eigenvectors = MathTools.find_eigenvalues(matrix)
    print(f"Eigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")
    print()

def demo_equation_solver():
    """Demonstrate equation solving."""
    print("🔍 Equation Solver Demo")
    print("=" * 40)
    
    # Linear equation
    print("Linear Equation: 2x + 3 = 7")
    a, b, c = 2, 3, 7
    x = (c - b) / a
    print(f"Solution: x = {x}")
    
    # Quadratic equation
    print("\nQuadratic Equation: x² - 5x + 6 = 0")
    roots, message = MathTools.solve_quadratic(1, -5, 6)
    print(f"Result: {message}")
    print(f"Roots: {roots}")
    print()

def demo_number_theory():
    """Demonstrate number theory tools."""
    print("🔢 Number Theory Tools Demo")
    print("=" * 40)
    
    # Prime checking
    numbers = [17, 25, 29, 100]
    for n in numbers:
        is_prime = MathTools.is_prime(n)
        status = "PRIME" if is_prime else "NOT PRIME"
        print(f"{n} is {status}")
    
    # Prime factorization
    n = 100
    factors = MathTools.prime_factorization(n)
    print(f"\nPrime factors of {n}: {factors}")
    
    # Generate primes
    primes = MathTools.generate_primes(10)
    print(f"First 10 prime numbers: {primes}")
    
    # GCD and LCM
    a, b = 48, 18
    gcd_val = MathTools.gcd(a, b)
    lcm_val = MathTools.lcm(a, b)
    print(f"\nGCD({a}, {b}) = {gcd_val}")
    print(f"LCM({a}, {b}) = {lcm_val}")
    print()

def demo_sequences():
    """Demonstrate sequence generation."""
    print("📊 Sequence Generation Demo")
    print("=" * 40)
    
    # Fibonacci sequence
    n = 15
    fib_sequence = MathTools.fibonacci_sequence(n)
    print(f"First {n} Fibonacci numbers: {fib_sequence}")
    
    # Prime number distribution
    n_primes = 20
    primes = MathTools.generate_primes(n_primes)
    print(f"\nFirst {n_primes} prime numbers: {primes}")
    print()

def demo_function_plotting():
    """Demonstrate function plotting capabilities."""
    print("📈 Function Plotting Demo")
    print("=" * 40)
    
    print("Available functions for plotting:")
    print("- sin(x), cos(x), tan(x)")
    print("- exp(x), log(x), sqrt(x)")
    print("- Polynomials: x**2 + 2*x + 1")
    print("- Combinations: sin(x) * cos(x)")
    print()
    print("Note: Use the Streamlit app to see actual plots!")
    print()

def main():
    """Run all demos."""
    print("🧮 Évariste Math Club - Mathematical Tools Demo")
    print("=" * 60)
    print()
    
    try:
        demo_matrix_operations()
        demo_equation_solver()
        demo_number_theory()
        demo_sequences()
        demo_function_plotting()
        
        print("✅ All demos completed successfully!")
        print("\n🚀 To see the full interactive application, run:")
        print("   streamlit run app_enhanced.py")
        print("   or")
        print("   python run_app.py")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Make sure all dependencies are installed:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()
