# 🧮 ProSort - Mathematical Competition System

A comprehensive mathematical problem-solving competition system built with Python and Streamlit, featuring user authentication, participation tracking, and detailed analytics.

## 🌟 Features

### Core Functionality
- **Problem Management**: Create, organize, and manage mathematical problems
- **User System**: User authentication, profiles, and progress tracking
- **Competition Engine**: Create and manage mathematical competitions
- **Scoring System**: Automated scoring and leaderboard generation
- **Problem Bank**: Extensive collection of mathematical problems across various topics
- **Participation Tracking**: Complete tracking of user choices, solutions, and time spent
- **Authentication System**: Secure login/registration with user profiles

### Problem Categories
- **Algebra**: Linear equations, quadratic equations, systems of equations, complex numbers
- **Geometry**: Area, volume, Pythagorean theorem, 3D geometry
- **Calculus**: Derivatives, integration, limits, L'Hôpital's rule
- **Number Theory**: Prime factorization, GCD/LCM, modular arithmetic
- **Combinatorics**: Permutations, combinations, inclusion-exclusion principle
- **Probability**: Basic probability, conditional probability, Bayes' theorem
- **Algorithms**: Fibonacci, binary search, dynamic programming
- **Optimization**: Linear programming, calculus optimization, constrained optimization

### Difficulty Levels
- **Easy**: Basic concepts and straightforward problems
- **Medium**: Intermediate complexity requiring multiple steps
- **Hard**: Advanced problems with complex reasoning
- **Expert**: Challenging problems for advanced mathematicians

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone or navigate to the ProSort directory:**
   ```bash
   cd Prosort_code
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv prosort_env
   
   # On Windows:
   prosort_env\Scripts\activate
   
   # On macOS/Linux:
   source prosort_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the enhanced ProSort system:**
   ```bash
   python run_enhanced_prosort.py
   ```

5. **Open your browser and navigate to:**
   ```
   http://localhost:8501
   ```

## 🔐 User Accounts

### Sample Accounts (Pre-loaded)
The system comes with 3 sample accounts for testing:

| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `math_wizard` | `password123` | Admin | Can create competitions and manage the system |
| `problem_solver` | `password123` | User | Undergraduate student with geometry focus |
| `calculus_master` | `password123` | User | Graduate student with calculus expertise |

### Creating New Accounts
1. Click "Create Account" on the login page
2. Fill in all required fields:
   - Personal Information (name, username, email, phone, date of birth, grade level)
   - Academic Information (institution, student ID, mathematical background, interests)
   - Account Security (password, confirm password)
3. Agree to Terms and Conditions
4. Click "Create Account"

## 📚 Using the System

### 1. Login and Dashboard
- **Login**: Use your username and password
- **Dashboard**: View system overview, statistics, and recent activity
- **Navigation**: Use the sidebar to navigate between different sections

### 2. Practice Problems
- **Browse Problems**: Filter by difficulty and problem type
- **Select Problem**: Choose a problem to work on
- **Problem Solver Interface**:
  - Read the problem statement
  - Choose your approach (attempt, skip, mark as difficult)
  - Use hints if needed (tracked automatically)
  - Write your complete solution
  - Provide code solution (optional)
  - Submit your final answer
  - Add notes about your approach

### 3. Problem Choices and Tracking
The system tracks:
- **Problem Selection**: Which problems you choose to work on
- **Approach Decision**: Whether you attempt, skip, or mark as difficult
- **Written Solutions**: Complete step-by-step solutions
- **Code Solutions**: Programming solutions with language selection
- **Hint Usage**: Which hints you use during problem solving
- **Time Tracking**: Start time, end time, and total time spent
- **Attempts**: Number of attempts made
- **Personal Notes**: Your thoughts and approach notes

### 4. Viewing Progress
- **Practice Dashboard**: Overview of your statistics and recent activity
- **My Profile**: Personal information and participation history
- **Statistics**: Detailed analytics including:
  - Problem choice distribution
  - Time analysis
  - Programming language usage
  - Accuracy and score trends

### 5. Competitions
- **Join Competitions**: Participate in active mathematical competitions
- **View Leaderboards**: See how you rank against other participants
- **Track Performance**: Monitor your competition progress

## 🏗️ System Architecture

### Core Components

#### 1. ProSortEngine (`core.py`)
- Manages problems, users, submissions, and competitions
- Handles scoring and leaderboard calculations
- Provides data export/import functionality

#### 2. ProblemBank (`problems.py`)
- Contains a comprehensive collection of mathematical problems
- Organizes problems by type and difficulty
- Provides filtering and random problem selection

#### 3. UserManager (`user_management.py`)
- Handles user registration, authentication, and profiles
- Manages user sessions and security
- Tracks participation and generates statistics

#### 4. AuthInterface (`auth_interface.py`)
- Provides login/registration UI
- Manages user sessions and authentication flow
- Handles user profile management

#### 5. EnhancedProblemSolver (`enhanced_problem_solver.py`)
- Interactive problem solving interface
- Tracks all user choices and solutions
- Records participation data in detail

#### 6. EnhancedStreamlitApp (`enhanced_streamlit_app.py`)
- Main application integrating all components
- Provides navigation and user interface
- Manages application state and routing

### Utilities (`utils.py`)
- Data persistence and backup
- Input validation and sanitization
- Mathematical utility functions
- Security and analytics tools

## 📁 Project Structure

```
Prosort_code/
├── __init__.py                  # Package initialization
├── core.py                      # Core system classes and logic
├── problems.py                  # Problem bank and problem management
├── user_management.py           # User authentication and management
├── auth_interface.py            # Login/registration UI
├── enhanced_problem_solver.py   # Enhanced problem solver with tracking
├── enhanced_streamlit_app.py    # Main integrated application
├── streamlit_app.py             # Basic Streamlit application
├── integration.py               # Integration layer for external systems
├── utils.py                     # Utility functions and helpers
├── main.py                      # Entry point for standalone execution
├── run_prosort.py               # Basic launcher
├── run_enhanced_prosort.py      # Enhanced system launcher
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔧 Configuration

### Environment Variables
Set these environment variables for production use:
```bash
export PROSORT_SECRET_KEY="your-secure-secret-key-here"
export PROSORT_DATA_DIR="/path/to/data/directory"
```

### Data Storage
- **User Data**: Stored in `user_data/` directory
- **Problem Data**: Embedded in the application
- **Participation Records**: Automatically saved with timestamps
- **Backup System**: Automatic data backup and recovery

## 📊 Data Export and Analysis

### Export Options
1. **Individual User Data**: JSON format with complete profile and statistics
2. **Participation History**: CSV format with detailed problem-solving records
3. **System Analytics**: Comprehensive system statistics and user metrics

### Data Fields Captured
For each problem participation:
- User ID and timestamp
- Problem ID and type
- Problem choice (attempt/skip/difficult)
- Complete written solution
- Code solution and programming language
- Hints used
- Time spent
- Final answer and correctness
- Score earned
- Personal notes and thoughts

## 🚀 Running Different Versions

### Basic ProSort System
```bash
python run_prosort.py
# or
python main.py
```

### Enhanced ProSort System (Recommended)
```bash
python run_enhanced_prosort.py
```

### Direct Streamlit Launch
```bash
streamlit run enhanced_streamlit_app.py
```

## 🧪 Development and Testing

### Adding New Problems
1. Edit `problems.py`
2. Add new problem to appropriate category method
3. Include all required fields (title, statement, difficulty, type, points, solution, hints)
4. Restart the application

### Customizing Problem Types
1. Modify `ProblemType` enum in `core.py`
2. Add corresponding problem methods in `problems.py`
3. Update validation in `utils.py`

### Testing User Accounts
- Use the pre-loaded sample accounts
- Create new accounts through the registration interface
- Test different user roles and permissions

## 🔒 Security Features

### Authentication
- **Password Hashing**: SHA-256 with salt
- **Session Management**: Token-based with expiration
- **Input Validation**: Comprehensive input sanitization
- **Access Control**: Role-based permissions

### Data Protection
- **Secure Storage**: Encrypted password storage
- **Session Security**: Automatic session expiration
- **Input Sanitization**: Protection against injection attacks
- **Data Validation**: Comprehensive data integrity checks

## 📈 Performance Features

### Optimization
- **Efficient Problem Filtering**: Fast search and categorization
- **Optimized Scoring**: Real-time leaderboard updates
- **Responsive UI**: Modern Streamlit interface
- **Data Caching**: Intelligent data loading and storage

### Scalability
- **Modular Architecture**: Easy to extend and modify
- **Data Persistence**: Efficient file-based storage
- **Session Management**: Scalable user session handling
- **Export Capabilities**: Bulk data export for analysis

## 🌐 Integration Possibilities

### External Systems
- **Learning Management Systems (LMS)**: API integration
- **Mathematical Software**: Connection to Mathematica, MATLAB
- **Educational Platforms**: Integration with existing systems
- **Mobile Applications**: RESTful API endpoints

### Data Import/Export
- **CSV/Excel**: Problem and user data import
- **JSON API**: RESTful API for external access
- **Database**: PostgreSQL/MySQL backend support
- **Cloud Storage**: Integration with cloud platforms

## 🚀 Future Enhancements

### Planned Features
- **Mobile Application**: Native iOS and Android apps
- **AI Problem Generation**: Machine learning-based problem creation
- **Real-time Collaboration**: Multi-user problem solving sessions
- **Advanced Analytics**: Deep learning insights and recommendations
- **Internationalization**: Multi-language support
- **API Development**: Comprehensive RESTful API

### Technical Improvements
- **Database Integration**: PostgreSQL/MySQL backend
- **Caching System**: Redis-based performance optimization
- **Microservices Architecture**: Scalable service-based design
- **Containerization**: Docker and Kubernetes deployment
- **Real-time Updates**: WebSocket-based live updates

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Standards
- Follow PEP 8 Python style guidelines
- Add comprehensive docstrings
- Include type hints where appropriate
- Write unit tests for new features
- Update documentation for changes

### Testing
- Test user registration and authentication
- Verify problem solving and tracking
- Check data export functionality
- Validate security features

## 📝 License

This project is developed for the Évariste Math Club at IIIT-D.

## 🆘 Support and Troubleshooting

### Common Issues

#### Import Errors
```bash
# Solution: Install missing dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

#### Port Conflicts
```bash
# Change default port
streamlit run enhanced_streamlit_app.py --server.port 8502
```

#### Data Loss
- Use the backup system to restore data
- Check `user_data/` directory for data files
- Verify file permissions and disk space

#### Authentication Issues
- Clear browser cookies and cache
- Check session expiration settings
- Verify user account status

### Getting Help
1. **Check Documentation**: Review this README and code comments
2. **Review Error Logs**: Check console output for error messages
3. **Test Sample Accounts**: Use pre-loaded accounts for testing
4. **Contact Support**: Reach out to the development team

### Debug Mode
Enable debug logging for troubleshooting:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🎉 Acknowledgments

- **Évariste Math Club**: For the vision and requirements
- **Streamlit**: For the excellent web application framework
- **Mathematical Community**: For inspiration and problem ideas
- **Open Source Contributors**: For the tools and libraries used

## 📞 Contact Information

For support, questions, or contributions:
- **Project Repository**: [GitHub Repository URL]
- **Development Team**: [Team Contact Information]
- **Math Club**: [Club Contact Information]

---

## 🚀 Quick Commands Reference

### Setup Commands
```bash
# Navigate to ProSort directory
cd Prosort_code

# Create virtual environment
python -m venv prosort_env

# Activate virtual environment
source prosort_env/bin/activate  # Linux/Mac
prosort_env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run enhanced system
python run_enhanced_prosort.py
```

### Sample User Login
```
Username: math_wizard
Password: password123
URL: http://localhost:8501
```

### Data Export Commands
```bash
# Export user data (JSON)
# Use the Export button in the Settings page

# Export participation history (CSV)
# Use the Export button in the Statistics page
```

**ProSort** - Empowering mathematical minds through competitive problem-solving! 🧮✨
