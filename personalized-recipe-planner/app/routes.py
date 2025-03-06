from flask import render_template, request, redirect, url_for
from app import app

# In-memory storage for user data
user_data = {
    "name": "",
    "preferences": {},
    "recipes": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        user_data['preferences'] = {
            "dietary_restrictions": request.form['dietary_restrictions'],
            "favorite_cuisine": request.form['favorite_cuisine'],
            "meals_per_week": request.form['meals_per_week']
        }
        return redirect(url_for('recipes'))
    return render_template('preferences.html')

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    if request.method == 'POST':
        recipe = {
            "name": request.form['recipe_name'],
            "ingredients": request.form['ingredients']
        }
        user_data['recipes'].append(recipe)
        return redirect(url_for('manage'))
    return render_template('recipes.html')

@app.route('/manage')
def manage():
    return render_template('manage.html', user_data=user_data)