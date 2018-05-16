from chatterbot import ChatBot
from chatterbot.filters import Filter

#Stores SQLite  Database and specifies input and output parameter 
bot = ChatBot(
    'Jarvis',

    trainer='chatterbot.trainers.ListTrainer',

     logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],


    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    input_adapter='chatterbot.input.TerminalAdapter',

    output_adapter='chatterbot.output.TerminalAdapter',

    filters=["chatterbot.filters.RepetitiveResponseFilter"]


    

    #database='./database.sqlite3'
)

while(True):
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

    bot.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',

])

    

    