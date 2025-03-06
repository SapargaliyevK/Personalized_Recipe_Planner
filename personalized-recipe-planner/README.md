# Personalized Recipe Planner

## Overview
The Personalized Recipe Planner is a Flask web application designed to help users manage their cooking preferences and recipes. Users can input their dietary restrictions, favorite cuisines, and desired meal plans to receive personalized recipe suggestions.

## Features
- User-friendly interface for managing preferences and recipes.
- Input forms for dietary restrictions, favorite cuisines, and recipes.
- Dynamic recipe planning based on user preferences.

## Project Structure
```
personalized-recipe-planner
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── preferences.html
│   │   ├── recipes.html
│   │   └── manage.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd personalized-recipe-planner
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app/__init__.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.