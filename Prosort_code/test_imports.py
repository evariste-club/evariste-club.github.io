#!/usr/bin/env python3
"""
Test script to verify all ProSort modules can be imported without Streamlit
"""

def test_imports():
    """Test importing all core modules"""
    try:
        print("Testing imports...")
        
        # Test core modules
        import core
        print("✅ core module imported")
        
        import problems
        print("✅ problems module imported")
        
        import utils
        print("✅ utils module imported")
        
        import user_management
        print("✅ user_management module imported")
        
        # Test that we can create instances
        from core import ProSortEngine, ProblemDifficulty, ProblemType
        print("✅ Core classes imported")
        
        from problems import problem_bank
        print("✅ Problem bank imported")
        
        from user_management import user_manager
        print("✅ User manager imported")
        
        # Test basic functionality
        engine = ProSortEngine()
        print("✅ ProSort engine created")
        
        problem_count = problem_bank.get_problem_count()
        print(f"✅ Problem bank has {problem_count} problems")
        
        print("\n🎉 All imports successful! The relative import issue has been resolved.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Other error: {e}")
        return False

if __name__ == "__main__":
    test_imports()
