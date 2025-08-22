import streamlit as st
from utils import footer, layout

layout.load()

st.markdown('<h2 class="section-header">📚 Study Materials</h2>', unsafe_allow_html=True)

# Subject categories
subjects = ["Linear Algebra", "Calculus", "Number Theory", "Graph Theory", "Combinatorics", "Probability"]
selected_subject = st.selectbox("Select Subject:", subjects)

if selected_subject == "Linear Algebra":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ### Linear Algebra Resources
    
    **Core Topics:**
    - Vector Spaces and Subspaces
    - Linear Transformations
    - Eigenvalues and Eigenvectors
    - Matrix Decompositions
    
    **Recommended Books:**
    - Linear Algebra Done Right by Sheldon Axler
    - Introduction to Linear Algebra by Gilbert Strang
    
    **Practice Problems:** [Download PDF]
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive matrix calculator
    st.subheader("🧮 Matrix Calculator")
    st.markdown("Enter a 2x2 matrix to find its eigenvalues:")
    
    col1, col2 = st.columns(2)
    with col1:
        a11 = st.number_input("a₁₁", value=1.0, key="a11")
        a21 = st.number_input("a₂₁", value=0.0, key="a21")
    with col2:
        a12 = st.number_input("a₁₂", value=0.0, key="a12")
        a22 = st.number_input("a₂₂", value=1.0, key="a22")
    
    matrix = np.array([[a11, a12], [a21, a22]])
    eigenvalues = np.linalg.eigvals(matrix)
    
    st.markdown(f"**Matrix:**")
    st.write(matrix)
    st.markdown(f"**Eigenvalues:** {eigenvalues}")
    
elif selected_subject == "Number Theory":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ### Number Theory Resources
    
    **Core Topics:**
    - Prime Numbers and Factorization
    - Congruences and Modular Arithmetic
    - Quadratic Residues
    - Diophantine Equations
    
    **Recommended Books:**
    - Elementary Number Theory by David Burton
    - A Classical Introduction to Modern Number Theory by Ireland & Rosen
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Prime number generator
    st.subheader("🔢 Prime Number Generator")
    n = st.slider("Generate first N prime numbers", 1, 100, 10)
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    st.write(f"First {n} prime numbers: {primes}")


footer.load()
