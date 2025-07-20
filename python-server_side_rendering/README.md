Flask Project
This is a simple Flask web application that demonstrates how to render templates and handle routes.

Requirements
Python 3.x

Flask

To install the required dependencies, run:

bash
Copy code
pip install -r requirements.txt
Folder Structure
plaintext
Copy code
your_project/
│
├── app.py              # Main application file
├── templates/          # Folder containing HTML templates
│   └── index.html      # Sample HTML template
└── requirements.txt    # Python dependencies
Project Setup
Clone the repository:

bash
Copy code
git clone https://your-repository-url.git
Navigate to the project directory:

bash
Copy code
cd your_project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
Templates Folder
Flask uses the templates folder to store HTML files that will be rendered by the application. In the example project, we have the index.html file inside the templates folder.

templates/index.html - This file is rendered when you visit the root route (/). The render_template() function in Flask will automatically look for templates inside the templates folder.

If you create any additional HTML files, they should be placed inside the templates folder, and you can render them similarly using render_template().

Example Usage
app.py
python
Copy code
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Leoos")

if __name__ == '__main__':
    app.run(debug=True)
templates/index.html
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Example</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
</body>
</html>
