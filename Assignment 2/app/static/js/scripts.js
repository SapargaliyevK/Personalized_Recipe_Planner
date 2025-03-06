// This file contains JavaScript for any client-side functionality, such as form validation or dynamic content updates.

document.addEventListener('DOMContentLoaded', function() {
    // Example: Form validation for preferences
    const preferencesForm = document.getElementById('preferences-form');
    if (preferencesForm) {
        preferencesForm.addEventListener('submit', function(event) {
            const dietInput = document.getElementById('diet-restrictions').value;
            const cuisineInput = document.getElementById('favorite-cuisine').value;
            const mealsInput = document.getElementById('meals-per-week').value;

            if (!dietInput || !cuisineInput || !mealsInput) {
                event.preventDefault();
                alert('Please fill out all fields in the preferences form.');
            }
        });
    }

    // Example: Dynamic content update for recipes
    const recipeInputForm = document.getElementById('recipe-input-form');
    if (recipeInputForm) {
        recipeInputForm.addEventListener('submit', function(event) {
            const recipeName = document.getElementById('recipe-name').value;
            const ingredients = document.getElementById('ingredients').value;

            if (!recipeName || !ingredients) {
                event.preventDefault();
                alert('Please enter both recipe name and ingredients.');
            } else {
                // Optionally, you could add code here to update the recipe list dynamically
                console.log(`Recipe added: ${recipeName} with ingredients: ${ingredients}`);
            }
        });
    }
});