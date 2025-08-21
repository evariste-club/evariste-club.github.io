import streamlit as st
import json
import os
import challenges

USERS_FILE = "users.json"

# challenges = [
#     {
#         "title": "Challenge 1: The First Step",
#         "description": "The flag is 'flag{welcome_to_ctf}'.",
#         "flag": "flag{welcome_to_ctf}"
#     },
#     {
#         "title": "Challenge 2: Simple Math",
#         "description": "What is 123 + 456? The flag is 'flag{answer}'.",
#         "flag": "flag{579}"
#     },
#     {
#         "title": "Challenge 3: Reverse It",
#         "description": "The flag is the reverse of 'gnits_esrever'.",
#         "flag": "flag{reverse_string}"
#     }
# ]

def load_users():
    """Loads user data from a JSON file. Creates a new file if it doesn't exist."""
    if not os.path.exists(USERS_FILE):
        return {
            "testuser": {
                "password": "password123", # Hashed passwords would be used in a real app
                "score": 0,
                "solved": []
            }
        }
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users_db):
    """Saves user data to a JSON file."""
    with open(USERS_FILE, "w") as f:
        json.dump(users_db, f, indent=4)

# --- Session state initialization ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# This dictionary is now loaded from the JSON file at the start of the session
if "users_db" not in st.session_state:
    st.session_state.users_db = load_users()

# --- Page functions ---

def show_login_page():
    """Displays the login form."""
    st.title("🔐 Simple CTF Platform - Login")

    with st.form("login_form"):
        st.write("Please enter your credentials to log in.")
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        if st.form_submit_button("Login"):
            if login_username in st.session_state.users_db and st.session_state.users_db[login_username]["password"] == login_password:
                st.session_state.logged_in = True
                st.session_state.username = login_username
                st.session_state.page = "ctf"
                st.success(f"Welcome back, {login_username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")
    
    st.markdown("---")
    st.subheader("Don't have an account?")
    if st.button("Sign up here"):
        st.session_state.page = "signup"
        st.rerun()

def show_signup_page():
    """Displays the signup form."""
    st.title("🔐 Simple CTF Platform - Sign Up")

    with st.form("signup_form"):
        st.write("Create a new account to get started!")
        signup_username = st.text_input("New Username", key="signup_username")
        signup_password = st.text_input("New Password", type="password", key="signup_password")
        if st.form_submit_button("Sign Up"):
            if signup_username in st.session_state.users_db:
                st.error("Username already exists. Please choose another.")
            else:
                st.session_state.users_db[signup_username] = {
                    "password": signup_password,
                    "score": 0,
                    "solved": []
                }
                save_users(st.session_state.users_db) # Save the new user
                st.success("Account created successfully! Please log in.")
                st.session_state.page = "login"
                st.rerun()
    
    st.markdown("---")
    st.subheader("Already have an account?")
    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()

def show_ctf_platform():
    """Displays the main CTF challenges page."""
    st.title("🔐 Simple CTF Platform")
    
    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.page = "login"
        st.rerun()
    
    # Get user data
    user_data = st.session_state.users_db[st.session_state.username]
    
    # Display user stats in the sidebar
    st.sidebar.header(f"Welcome, {st.session_state.username}!")
    st.sidebar.write(f"Score: {user_data['score']}")
    st.sidebar.write(f"Solved: {len(user_data['solved'])} / {len(challenges)}")

    # Find the first unsolved challenge
    unsolved_found = False
    for idx, challenge in enumerate(challenges):
        # Display challenges sequentially, stopping at the first unsolved one
        if idx not in user_data["solved"]:
            st.subheader(challenge["title"])
            st.write(challenge["description"])
            flag_input = st.text_input(f"Enter flag for {challenge['title']}", key=f"flag_{idx}")
            if st.button(f"Submit Flag for {challenge['title']}", key=f"submit_{idx}"):
                if flag_input.strip() == challenge["flag"]:
                    st.success("🎉 Correct Flag!")
                    user_data["score"] += 10
                    user_data["solved"].append(idx)
                    save_users(st.session_state.users_db)
                    st.rerun()
                else:
                    st.error("❌ Incorrect Flag. Try again.")
            unsolved_found = True
            break # Stop after displaying the first unsolved challenge
        else:
            # Display already solved challenges as completed
            st.subheader(f"{challenge['title']} (Solved)")
            st.success("✅ Already Solved!")

    if not unsolved_found:
        st.header("🎉 Congratulations!")
        st.markdown("You have completed all the challenges. You are a true hacker!")

# Main app entry point: show login, signup, or CTF based on session state
if st.session_state.logged_in:
    show_ctf_platform()
else:
    if st.session_state.page == "login":
        show_login_page()
    elif st.session_state.page == "signup":
        show_signup_page()
