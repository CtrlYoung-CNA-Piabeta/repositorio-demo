import Chatbot

nome_chatbot = 'Cleyton'
Chatbot.saudacao(nome_chatbot)
while True:
    msg = Chatbot.recebe_mensagem()
    resposta = Chatbot.busca_mensagem(nome_chatbot, msg)
    if Chatbot.exibe_resposta(resposta, nome_chatbot) == 'Fim':
        break

# GUI -> Graphical User Interface