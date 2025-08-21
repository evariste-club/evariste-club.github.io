# Évariste Math Club - Streamlit Application

A modern, interactive web application for IIIT-D's Évariste Mathematics Club, built with Streamlit.

## 🚀 Features

### 🏠 **Home Page**
- Welcome message and club introduction
- Interactive statistics dashboard
- Featured content showcase
- Real-time mathematical visualizations

### 📚 **Study Materials**
- Comprehensive subject coverage (Linear Algebra, Calculus, Number Theory, etc.)
- Interactive calculators and tools
- Recommended books and resources
- Practice problem sets

### 🎯 **ProSort Euler**
- Event information and details
- Interactive problem solver
- Mathematical exercises and hints
- Competition preparation tools

### 🔐 **PWNHUB CTF**
- Capture The Flag challenge information
- CTF box details (Ellie & Benjamin)
- Progress tracking system
- Hints and solutions

### 📝 **Blog Section**
- Mathematical articles and insights
- Club updates and announcements
- Educational content sharing

### 📅 **Events Calendar**
- Upcoming events and workshops
- Registration system
- Event details and locations

### 🧮 **Advanced Math Tools**
- Matrix operations and calculations
- Equation solvers (Linear, Quadratic, Systems)
- Function plotting capabilities
- Number theory utilities
- Interactive mathematical visualizations

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone or download the project files**
   ```bash
   # If you have the files locally, navigate to the project directory
   cd /path/to/evariste-club.github.io
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   # Option 1: Use the launcher script
   python run_app.py
   
   # Option 2: Run directly with Streamlit
   streamlit run app_enhanced.py
   
   # Option 3: Run the basic version
   streamlit run app.py
   ```

4. **Access the application**
   - The app will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

## 📁 File Structure

```
evariste-club.github.io/
├── app.py                    # Basic Streamlit application
├── app_enhanced.py          # Enhanced version with advanced math tools
├── math_tools.py            # Mathematical utilities and calculations
├── run_app.py               # Launcher script
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── README_STREAMLIT.md      # This file
└── README.md                # Original project README
```

## 🧮 Mathematical Tools Available

### Matrix Operations
- Determinant calculation
- Rank computation
- Eigenvalue and eigenvector finding
- Matrix visualization

### Equation Solvers
- Linear equations: `ax + b = c`
- Quadratic equations: `ax² + bx + c = 0`
- System of linear equations

### Function Plotting
- Mathematical function visualization
- Customizable x-axis range
- Support for trigonometric, exponential, and polynomial functions

### Number Theory
- Prime number generation
- Prime factorization
- GCD and LCM calculation
- Modular arithmetic

### Interactive Visualizations
- Fibonacci sequence plotting
- Prime number distribution
- Matrix heatmaps
- Real-time mathematical graphs

## 🎨 Customization

### Themes and Styling
The application uses custom CSS for a modern, professional appearance:
- Gradient backgrounds
- Card-based layouts
- Responsive design
- Mathematical typography

### Configuration
Modify `.streamlit/config.toml` to customize:
- Color schemes
- Server settings
- Browser behavior

## 🔧 Development

### Adding New Features
1. **New Pages**: Add to the navigation menu in the main app
2. **Mathematical Tools**: Extend the `MathTools` class in `math_tools.py`
3. **Styling**: Modify the CSS in the main application files

### Testing
```bash
# Test the math tools module
python math_tools.py

# Run with specific port
streamlit run app_enhanced.py --server.port 8502
```

## 🌐 Deployment

### Local Development
- Perfect for development and testing
- Real-time updates with Streamlit's hot-reload

### Production Deployment
- Deploy to Streamlit Cloud
- Use Docker containers
- Deploy to cloud platforms (AWS, GCP, Azure)

## 📊 Performance Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Updates**: Live mathematical calculations
- **Interactive Elements**: Dynamic charts and visualizations
- **Efficient Algorithms**: Optimized mathematical computations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📚 Educational Value

This application serves as both a club website and an educational platform:
- **Interactive Learning**: Hands-on mathematical exploration
- **Visual Understanding**: Graphical representation of concepts
- **Practical Application**: Real-world problem-solving tools
- **Community Building**: Centralized resource for club members

## 🔗 External Links

- **Original Website**: [GitHub Repository](https://github.com/evariste-club/evariste-club.github.io)
- **Streamlit Documentation**: [streamlit.io](https://docs.streamlit.io)
- **IIIT-D**: [iiitd.ac.in](https://iiitd.ac.in)

## 📄 License

This project maintains the same license as the original Évariste Math Club repository.

## 🆘 Support

For issues or questions:
- Check the original project documentation
- Review Streamlit documentation
- Contact the Évariste Math Club team

---

**Built with ❤️ by the Évariste Math Club Team using Streamlit**

*Transforming mathematical education through interactive technology*
