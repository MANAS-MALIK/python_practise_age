<<<<<<< HEAD
# Import Flask - a web framework for Python that helps us create web applications
from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)

# Define a route for the home page
# When someone visits the root URL (/), this function will run
@app.route('/')
def index():
    # render_template looks for a file called 'index.html' in a 'templates' folder
    # and sends it to the user's browser
    return render_template('index.html')

# Define a route for checking voting eligibility
# This route accepts POST requests (data sent from the frontend)
@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    # Get the JSON data sent from the frontend
    # request.json contains the data sent in the request body
    data = request.json
    
    # Extract the 'age' value from the received data
    # If 'age' is not provided, it will be None
    age = data.get('age')
    
    # Check if age was provided
    if age is None:
        # Return an error response if age is missing
        return jsonify({
            'success': False,
            'message': 'Age is required'
        }), 400  # 400 is HTTP status code for Bad Request
    
    # Try to convert age to an integer
    try:
        age = int(age)
    except (ValueError, TypeError):
        # If conversion fails (e.g., user entered text), return an error
        return jsonify({
            'success': False,
            'message': 'Age must be a valid number'
        }), 400
     

    # Check if age is greater than 18
    if age > 18:
        # If eligible, return success response with eligibility status
        return jsonify({
            'success': True,
            'eligible': True,
            'message': f'You are {age} years old. You are ELIGIBLE to vote! 🗳️'
        })
    else:
        # If not eligible, return success response with ineligibility status
        return jsonify({
            'success': True,
            'eligible': False,
            'message': f'You are {age} years old. You are NOT ELIGIBLE to vote. You need to be 18 or older.'
        })

# This block runs only when the script is executed directly (not imported)
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables auto-reload when code changes and shows detailed error messages
    # host='0.0.0.0' makes the server accessible from any network interface
    # port=5000 sets the server to run on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)

=======
# Import Flask - a web framework for Python that helps us create web applications
from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)

# Define a route for the home page
# When someone visits the root URL (/), this function will run
@app.route('/')
def index():
    # render_template looks for a file called 'index.html' in a 'templates' folder
    # and sends it to the user's browser
    return render_template('index.html')

# Define a route for checking voting eligibility
# This route accepts POST requests (data sent from the frontend)
@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    # Get the JSON data sent from the frontend
    # request.json contains the data sent in the request body
    data = request.json
    
    # Extract the 'age' value from the received data
    # If 'age' is not provided, it will be None
    age = data.get('age')
    
    # Check if age was provided
    if age is None:
        # Return an error response if age is missing
        return jsonify({
            'success': False,
            'message': 'Age is required'
        }), 400  # 400 is HTTP status code for Bad Request
    
    # Try to convert age to an integer
    try:
        age = int(age)
    except (ValueError, TypeError):
        # If conversion fails (e.g., user entered text), return an error
        return jsonify({
            'success': False,
            'message': 'Age must be a valid number'
        }), 400
     

    # Check if age is greater than 18
    if age > 18:
        # If eligible, return success response with eligibility status
        return jsonify({
            'success': True,
            'eligible': True,
            'message': f'You are {age} years old. You are ELIGIBLE to vote! 🗳️'
        })
    else:
        # If not eligible, return success response with ineligibility status
        return jsonify({
            'success': True,
            'eligible': False,
            'message': f'You are {age} years old. You are NOT ELIGIBLE to vote. You need to be 18 or older.'
        })

# This block runs only when the script is executed directly (not imported)
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables auto-reload when code changes and shows detailed error messages
    # host='0.0.0.0' makes the server accessible from any network interface
    # port=5000 sets the server to run on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)

>>>>>>> 581c87001915fe80ff646810ca9f72b0ffb2fec8
