import tkinter as tk
import Chatbot as chat

main_window = tk.Tk()
main_window.title('Cleytin')
main_window.geometry('600x600')
main_window.grid()

frame = tk.Frame(main_window)
frame.grid()

label = tk.Label(
        frame, 
        text="Insira uma mensagem aqui: ", 
        foreground='#262728',   # Cor da fonte
        background='#e1f0fe',   # Cor do fundo
        font='64px'             # Tamanho da fonte
    )
label.grid(row=0, column=0)

entry = tk.Entry(frame, font='64px')
entry.grid(row=0, column=1)

chat_frame = tk.Frame(main_window)
chat_frame.grid(row=1, column=0)
v = tk.StringVar()
v.set("Qual o seu nome?")

chat_label = tk.Label(chat_frame, textvariable=v, font='64px')
chat_label.grid()

nome_chat = 'Cleytin'
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ''

def executa_chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global nome_usuario
    global historico_conversa

    if entrada_nome_usuario:
        nome_usuario = entry.get()
        saudacao = chat.saudacao(nome_chat)
        historico_conversa = nome_chat + ': ' + saudacao + '\n'
        v.set(historico_conversa)
        entrada_nome_usuario = False
    else:
        msg = entry.get()
        historico_conversa += '\n' + nome_usuario + ': ' + msg
        v.set(historico_conversa)

        retorno = chat.busca_mensagem(mensagem='Cliente: ' + msg, nome=nome_chat)
        retorno = chat.exibe_resposta(retorno, nome_chat)
        historico_conversa += '\n' + retorno
        v.set(historico_conversa)

button = tk.Button(frame, 
                   text='Enviar', 
                   command=executa_chatbot, 
                   font='64')
button.grid(row=0, column=2)

main_window.mainloop()