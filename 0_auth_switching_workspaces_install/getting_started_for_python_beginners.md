# Getting Started with Prefect for Python Beginners

Welcome to the world of Python and Prefect! This guide is designed to help beginners set up a Python environment, install Prefect, and log into Prefect Cloud. Let's get started.
## Prerequisites

Before you begin, ensure you have:
- Basic understanding of using a terminal or command prompt.
- Access to the internet for downloading necessary software.
## Step 1: Install Python

Prefect requires Python. If you don’t have Python installed, download and install Python 3.10 or an earlier version from [python.org]().
## Step 2: Set Up a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It's a best practice to use a virtual environment for each Python project to manage dependencies more effectively. 
1. **Open your terminal or command prompt.** 
2. **Create a new directory for your project and navigate into it:** 

    ```bash
    mkdir my_prefect_project
    cd my_prefect_project
    ``` 
3. **Create a virtual environment:**  
    On Windows:

    ```bash
    python -m venv env
    ``` 
    On macOS and Linux:

    ```bash
    python3 -m venv env
    ``` 
4. **Activate the virtual environment:**  
    On Windows:

    ```bash
    .\env\Scripts\activate
    ``` 
    On macOS and Linux:

    ```bash
    source env/bin/activate
    ```

Your command prompt should now indicate that you are in the virtual environment.
## Step 3: Install Prefect and Prefect Docker

With your virtual environment activated, install Prefect and Prefect Docker using pip, Python's package installer.

```bash
pip install prefect prefect-docker
```


## Step 4: Log into Prefect Cloud from Your Browser 

1. **and log in**  You can sign up for a free account or accept an invitation from your organization. 
2. to avoid creating a duplicate account, IF your company has already set up SSO, try signing up with SSO first. 
<img src="images/sso_login_button.png" width="300"/>
## Step 5: Log into Prefect Cloud from Your Terminal 
**In your terminal, enter the following command:** 

```bash
prefect cloud login
``` 

*.*<img src="images/get_api_key.png" width="300"/>
## Step 6: Set Your Workspace

Set your workspace to the one you want to work in:

```bash
prefect cloud workspace set
```



Choose the desired workspace from the list that appears.
## Step 7: Start Coding!

Now that you're all set up, you'll want to start writing Python scripts to define your Prefect flows. If you're new to coding, consider using a code editor like Visual Studio Code or PyCharm. These editors offer helpful features like syntax highlighting and code completion that can make your coding experience much easier.---

Remember, learning to code takes time and practice, so don't get discouraged if things seem tricky at first. You're now on your way to becoming a Python and Prefect pro!