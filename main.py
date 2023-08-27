import beach
import padel
import locale
import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

#Starts a system to get the greetings message

def initMessage():
    now = datetime.datetime.now()
    currentHour = now.hour

    #Checks what time it is to see what message use
    if currentHour < 12:
        return f"Bom dia pessoal!\n\n" #Good morning everyone!

    elif currentHour < 18:
        return f"Boa tarde pessoal!\n\n" #Good afternoon everyone!
    
    else:
        return f"Boa noite pessoal!\n\n" #Good evening everyone!

#Defines the middle message, that goes between the sportsMessages and sportsList

def middleMessage():
    now = datetime.datetime.now()
    currentHour = now.hour

    if currentHour < 12:
        return f"Horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):\n\n" #Best vacant times for today

    elif currentHour < 18:
        return f"Últimos horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):\n\n" #Last vacant times for today

    else:
        tomorrow = now + datetime.timedelta(days=1)
        return f"Horários nobres vagos para AMANHÃ ({tomorrow.strftime('%d/%m')}, {tomorrow.strftime('*%A*')})\n\n:" #Best vacant times for tomorrow

#Creating every message as vars
greetings = initMessage()
middle = middleMessage()
sportsMessages = [padel.actualMessage, beach.actualMessage] 
sportsList = [padel.times, beach.times]
sportsPromo = [padel.promo, beach.promo]
final = "\n\nConsulte disponibilidade para os demais horários"

padelMessage = f"{greetings}{sportsMessages[0]}\n\n{middle}{sportsList[0]}{sportsPromo[0]}{final}"

beachMessage = f"{greetings}{sportsMessages[1]}\n\n{middle}{sportsList[1]}{sportsPromo[1]}{final}"

#Creating output files

#Padel
padelFile = f"output_{padel.sport}.txt"
with open(padelFile, 'w', encoding='utf8') as filePadel:
    filePadel.write(padelMessage)

#Beach
beachFile = f"output_{beach.sport}.txt"
with open(beachFile, 'w', encoding='utf8') as fileBeach:
    fileBeach.write(beachMessage)

print("Arquivos foram criados com os horários.")