from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"
chatbot=ChatBot('Chatbot')
trainer = ListTrainer(chatbot)

# Function to train the chatbot using a list of files
def train_chatbot_from_files(file_list):
    for file_path in file_list:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            trainer.train(lines)
            
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)
# List of files to train the chatbot
file_list = ['politics.yml', 'greetings.yml', 'movies.yml', 'computers.yml', 'food.yml', 'trivia.yml', 'sports.yml', 'ai.yml', 'psychology.yml', 'literature.yml', 'emotion.yml', 'botprofile.yml', 'health.yml', 'history.yml', 'money.yml', 'science.yml', 'humor.yml', 'gossip.yml']

# Train the chatbot using the list of files
train_chatbot_from_files(file_list)
#trainer.train(cleaned_corpus)
exit_conditions =(":q","quit","exit")

while True:
	query = input(">")
	if query in exit_conditions:
		break
	else:
		print(f"🪴 {chatbot.get_response(query)}")
