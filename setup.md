# Project Setup Guide

## Prerequisites
- Make sure you have Python 3 installed on your system.
- You'll need `pip`, the Python package installer, which usually comes with Python.

## Setup Instructions

1. **Clone the project repository**
   ```bash
   git clone <your-repo-url>
   cd <project-repo>
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   - On **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application**
   ```bash
   python3 app.py
   ```

## Additional Information
- To deactivate the virtual environment, simply run:
  ```bash
  deactivate
  ```
  
