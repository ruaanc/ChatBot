from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Meu Bot")

conv = (
)

trainer = ListTrainer(bot)

trainer.train(conv)

quest = ""
while (quest != "exit"):
    quest = input("Você: ")

    response = bot.get_response(quest)

    print("Bot: ", response)