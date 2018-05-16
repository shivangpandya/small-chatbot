from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Jarvis")


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

while(True):
	request = input('You: ')
	response = chatbot.get_response(request)
	print('Bot:' ,response)




