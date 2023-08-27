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

def middleMessage():
    now = datetime.datetime.now()
    currentHour = now.hour

    if currentHour < 12:
        return f"Horários nobres disponíveis para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):"

    elif currentHour < 18:
        return f"Últimos horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):"

    else:
        tomorrow = now + datetime.timedelta(days=1)
        return f"Boa noite pessoal!\n\n{motd}\n\nHorários nobres vagos para AMANHÃ ({tomorrow.strftime('%d/%m')}, {tomorrow.strftime('*%A*')}):"


sportsMessages = (padel.actualMessage, beach.actualMessage) 
sportsList = (padel.times, beach.times)
sportsPromo = (padel.promo, beach.promo)

print(sportsMessages)
print(sportsList)
print(sportsPromo)