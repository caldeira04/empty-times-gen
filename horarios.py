#!/usr/bin/python3

import datetime
import locale

def abrir_mensagens():
    # Obtendo as mensagens dentro do arquivo de mensagens
    try:
        with open("mensagens.txt", "r", encoding="utf-8") as lista_mensagem:
            mensagens = lista_mensagem.readlines()
    except FileNotFoundError:
        # Caso o arquivo não exista ele é criado
        with open("mensagens.txt", "w") as lista_mensagem:
            return

    # Mostrando todas opções de mensagem
    while True:
        print("Selecione uma mensagem para utilizar agora:")
        for i, mensagem in enumerate(mensagens):
            print(f"{i+1}: {mensagem.strip()}")
        print("0: Escrever uma nova mensagem")
        try:
        # Aqui definirá que para adicionar uma mensagem nova se usa 0, para utilizar já existentes, os números atribuídos
            n = int(input("Digite o número da mensagem: "))
            if 0 < n <= len(mensagens):
                mensagem_obtida = mensagens[n - 1].strip() # n - 1 acertam o número da mensagem, strip remove os colchetes
                print(mensagem_obtida)
                break

            elif n == 0:
                mensagem_nova = input("Escreva sua nova mensagem: ")
                mensagens.append(mensagem_nova + "\n")
                with open("mensagens.txt", "a", encoding="utf-8") as f:
                    f.write(mensagem_nova + "\n") # \n serve para quebrar a linha para que as mensagens não entrem todas na mesma
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    return mensagem_obtida

# Variável curta para minimizar o trabalho
motd = abrir_mensagens()

def obter_abertura_mensagem():
    now = datetime.datetime.now()
    current_hour = now.hour

    if current_hour < 12:
        return f"Bom dia pessoal!\n\n{motd}\n\nHorários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A-feira*')}):"
    elif current_hour < 18:
        return f"Boa tarde pessoal!\n\n{motd}\n\nÚltimos horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A-feira*')}):"
    else:
        tomorrow = now + datetime.timedelta(days=1)
        return f"Boa noite pessoal!\n\n{motd}\n\nHorários nobres vagos para AMANHÃ ({tomorrow.strftime('%d/%m')}, {tomorrow.strftime('*%A-feira*')}):"

def obter_lista_horarios(esporte):
    horarios = []
    while True:
        horario = input(f"Insira um horário disponível para {esporte} (ou 'fim' para encerrar): ")
        if horario.lower() == 'fim':
            break
        try:
            hora = int(horario)
            if int(horario) > 22:
                raise ValueError
            else:
                horarios.append(hora)
        except ValueError:
            print("Horário inválido. Insira um número inteiro.")

    if horarios:
        horarios.sort()
        horarios_formatados = [f"{hora:02d}h" for hora in horarios]
        lista_horarios = ", ".join(horarios_formatados)
        return f"\n\n{esporte}: *{lista_horarios}*"
    else:
        return f"\n\nNão há quadras disponíveis para {esporte}."

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Exemplo de uso:
esporte = ("Pádel", "Beach")
final = "\n\nConsulte disponibilidade para os demais horários."
abertura_mensagem = obter_abertura_mensagem()
lista_horarios = (obter_lista_horarios(esporte[0]), obter_lista_horarios(esporte[1]))


# Fazendo a mensagem com promoção ou sem

promo = (" (promocional, joga até 23h30)", " (promocional, joga até 23h)")

for i in lista_horarios[0]:

    if "22" in lista_horarios[0]:
        mensagem1 = f"{abertura_mensagem}{lista_horarios[0]}{promo[0]}{final}\n\n"
    else:
        mensagem1 = f"{abertura_mensagem}{lista_horarios[0]}{final}\n\n"

    if "21" in lista_horarios[1]:
        mensagem2 = f"{abertura_mensagem}{lista_horarios[1]}{promo[1]}{final}"
    else:
        mensagem2 = f"{abertura_mensagem}{lista_horarios[1]}{final}"

# Criar arquivo de saída para os horários de pádel
nome_arquivo1 = f"horarios_{esporte[0].lower()}.txt"
with open(nome_arquivo1, 'w') as arquivo1:
    arquivo1.write(mensagem1)

# Criar arquivo de saída para os horários de beach
nome_arquivo2 = f"horarios_{esporte[1].lower()}.txt"
with open(nome_arquivo2, 'w') as arquivo2:
    arquivo2.write(mensagem2)

print(f"Arquivos de horários foram criados: {nome_arquivo1}, {nome_arquivo2}")
