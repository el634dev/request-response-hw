from flask import Flask
import random

# Create app to write routes
app = Flask(__name__)

@app.route('/')
def homepage():
    """
    :return: Shows a greeting to the user
    """
    return "Are you there, world? It\'s me, Ducky!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """
    :return: Display a message to the user that changes based on their favorite animal.
    """
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """
    :return: Display a message to the user that changes based on their favorite dessert.
    """
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs_story(adjective, noun):
    """
    :return: Display a work-appropriate funny story.
    I used termnial and complier
    """
    return f"There was a {adjective} in my coffee, but this {noun} worked."

@app.route('/multiply/<number1>/<number2>')
def multiply_two(number1, number2): 
    """
    :return: the result of two numbers that are multiply
    """
    if number1.isdigit() and number2.isdigit():
         return f"{number1} times {number2} is {int(number1) * int(number2)}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n): 
    if word.isalpha() and n.isdigit():
        return f"{word} " * int(n)
    else:
        return "Invalid inputs. Please try again by entering a word and one number!"

@app.route('/dicegame')
def dice_game():
    number = random.randint(1,6)
    if number < 6:
         return f"You rolled a {number}. You lost!"
    else:
        return f"You rolled a {number}. You won!"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    