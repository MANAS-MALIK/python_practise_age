# Voting Eligibility Checker - Step by Step Guide

A simple web application that checks if a person is eligible to vote based on their age.

## 📋 Prerequisites

- Python 3.7 or higher installed on your computer
- Basic understanding of Python and HTML

## 🚀 How to Run

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```

3. **Open your web browser and visit:**
   ```
   http://localhost:5000
   ```

4. **Enter your age and click "Check Eligibility"**

## 📁 Project Structure

```
jan/
├── app.py              # Backend server (Flask)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend webpage
└── README.md          # This file
```

## 🔍 Code Explanation

### Backend (app.py)

The backend handles the logic and responds to requests from the frontend.

**Key Concepts:**
- **Flask**: A Python web framework that makes it easy to create web applications
- **Routes**: URLs that trigger specific functions
- **POST Request**: Used to send data from frontend to backend
- **JSON**: Data format used for communication between frontend and backend

### Frontend (index.html)

The frontend is what users see and interact with in their browser.

**Key Concepts:**
- **HTML**: Structure of the webpage
- **CSS**: Styling and appearance
- **JavaScript**: Makes the page interactive
- **Fetch API**: Used to send requests to the backend

## 🎓 Learning Points

1. **Client-Server Architecture**: Frontend (client) sends requests, backend (server) processes and responds
2. **HTTP Methods**: GET (retrieve data) and POST (send data)
3. **Asynchronous Programming**: Using `async/await` to handle server responses
4. **Event Handling**: Responding to user actions (form submission)
5. **DOM Manipulation**: Changing webpage content with JavaScript

## 🐛 Troubleshooting

- **Port already in use**: Change `port=5000` to another number (e.g., 5001) in `app.py`
- **Module not found**: Make sure you ran `pip install -r requirements.txt`
- **Page not loading**: Check that the Flask server is running and visit the correct URL

## 📚 Next Steps

Try modifying the code to:
- Add more validation (e.g., check for negative numbers)
- Add a database to store age records
- Add more styling and animations
- Create multiple pages

