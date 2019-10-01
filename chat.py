from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Meu Bot")

conv = (
   "Quais são os custos para abertura de conta ? ",
   "Pioneira em taxa zero no mercado de títulos públicos e renda fixa privada, a Easynvest disponibiliza também outros investimentos com taxas diferenciadas. Confira abaixo nossos custos. Renda Variável: Na Easynvest não cobramos taxa de custódia, somente é cobrada a taxa de corretagem, que é de R$ 4,99 por ordem executada, e R$ 2,49 para lote fracionário."
)

trainer = ListTrainer(bot)

trainer.train(conv)

quest = ""
while (quest != "exit"):
    quest = input("Você: ")

    response = bot.get_response(quest)

    print("Bot: ", response)