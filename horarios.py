#!/usr/bin/python3

import datetime
import locale

def obter_abertura_mensagem():
    now = datetime.datetime.now()
    current_hour = now.hour

    if current_hour < 12:
        return f"Bom dia pessoal!\n\nVeja os horários e marque sua quadra pelo Site/APP - https://gripo.app/reservar/padelsul-pelotas-rs\n\nHorários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A-feira*')}):"
    elif current_hour < 18:
        return f"Boa tarde pessoal!\n\nVeja os horários e marque sua quadra pelo Site/APP - https://gripo.app/reservar/padelsul-pelotas-rs\n\nÚltimos horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A-feira*')}):"
    else:
        tomorrow = now + datetime.timedelta(days=1)
        return f"Boa noite pessoal!\n\nNada melhor que jogar mais pagando menos! Conheça nossos planos de sócio e garanta desconto em todos os horários no clube!\n\nHorários nobres vagos para AMANHÃ ({tomorrow.strftime('%d/%m')}, {tomorrow.strftime('*%A-feira*')}):"

def obter_lista_horarios(esporte):
    horarios = []
    while True:
        horario = input(f"Insira um horário disponível para {esporte} (ou 'fim' para encerrar): ")
        if horario.lower() == 'fim':
            break
        try:
            hora = int(horario)
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
esporte1 = "Pádel"
esporte2 = "Beach"
final = "\n\nConsulte disponibilidade para os demais horários."

abertura_mensagem = obter_abertura_mensagem()
lista_horarios1 = obter_lista_horarios(esporte1)
lista_horarios2 = obter_lista_horarios(esporte2)

# Fazendo a mensagem com promoção ou sem
if "22" in lista_horarios1:
    promoPadel = " (promocional, joga até 23h30)"
    mensagem1 = f"{abertura_mensagem}{lista_horarios1}{promoPadel}{final}\n\n"
else:
    mensagem1 = f"{abertura_mensagem}{lista_horarios1}{final}\n\n"

if "21" in lista_horarios2:
    promoBeach = " (promocional, joga até 23h)"
    mensagem2 = f"{abertura_mensagem}{lista_horarios2}{promoBeach}{final}"
else:
    mensagem2 = f"{abertura_mensagem}{lista_horarios2}{final}"

# Criar arquivo de saída para esporte1
nome_arquivo1 = f"horarios_{esporte1.lower()}.txt"
with open(nome_arquivo1, 'w') as arquivo1:
    arquivo1.write(mensagem1)

# Criar arquivo de saída para esporte2
nome_arquivo2 = f"horarios_{esporte2.lower()}.txt"
with open(nome_arquivo2, 'w') as arquivo2:
    arquivo2.write(mensagem2)

print(f"Arquivos de horários foram criados: {nome_arquivo1}, {nome_arquivo2}")
