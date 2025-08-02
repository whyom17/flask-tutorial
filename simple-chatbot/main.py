# About this project :
# Here we are using ChatterBot - Conversational AI Chatbot Engine
# -  Machine Learning-Based: Learns from conversations and improves over time
# -  Language Independent: Can be trained in multiple languages
# -  Simple API: Easy to set up with just a few lines of code
# -  Corpus Training: Comes with built-in training data for greetings, conversations, etc.

from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
# Flask - the main class present inside 'flask' package to create a web app.
# calling it creates a new app instance/ object called app from the Flask class
# Instance: Specifically an object that was created from a particular class.


# module vs package:
# Python file itself is a module.
# When we group all the modules in a directory, it becomes a package.

# What is __init__.py?
# It’s a special Python file that lives inside a package directory.
# It tells Python that this directory should be treated as a package.
# First we import all the modules we want to use in __init__.py which is present in the same directory.
# After that we can access any functions or classes from those modules using the package name.

english_bot= ChatBot("Chatterbot", storage_adapter='chatterbot.storage.SQLStorageAdapter')  # 'Chatterbot' is the name of the chatbot instance and storage_adapter is used to specify how the data will be stored.
trainer=ChatterBotCorpusTrainer(english_bot) # ChatterBotCorpusTrainer is used to train the chatbot with a predefined set of data
trainer.train("chatterbot.corpus.english")  # This line trains the chatbot using the English corpus provided by ChatterBot.
trainer.train("data/data.yml") # This line trains the chatbot using a custom data from 'data.yml'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

# 👇 used to control script execution
if __name__ == '__main__':   # executes this python file only when it is run directly, it is not going to run if it used as a module
    app.run(debug=True)      
