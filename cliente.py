import socket
import threading

# Endereço IP e porta do servidor
host = "127.0.0.1"
porta = 2345

# Cria um objeto socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Função para receber mensagens do servidor
def receber_mensagens():
    while True:
        mensagem, endereco_servidor = cliente_socket.recvfrom(1024)
        print(
            f"Recebido do servidor ({endereco_servidor[0]}:{endereco_servidor[1]}): {mensagem.decode('utf-8')}"
        )


# Inicializa uma thread para receber mensagens
thread_recebimento = threading.Thread(target=receber_mensagens)
thread_recebimento.daemon = True
thread_recebimento.start()


# Função para enviar mensagens ao servidor
def enviar_mensagens():
    while True:
        mensagem = input("Digite a mensagem: ")
        if mensagem == ".contatos":
            # Solicita a lista de contatos ao servidor
            cliente_socket.sendto(mensagem.encode("utf-8"), (host, porta))
        elif mensagem.startswith("."):
            # Envie mensagens para um contato específico
            cliente_socket.sendto(mensagem.encode("utf-8"), (host, porta))
        else:
            print(
                "Comando inválido. Use '.contatos' para listar contatos ou '.<nome_do_contato>_<mensagem>' para enviar uma mensagem."
            )


# Inicializa uma thread para enviar mensagens
thread_envio = threading.Thread(target=enviar_mensagens)
thread_envio.start()

# Aguarda as threads finalizarem
thread_envio.join()
thread_recebimento.join()
