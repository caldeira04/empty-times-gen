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
        return f"Horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):\n\n"

    elif currentHour < 18:
        return f"Últimos horários nobres vagos para HOJE - ({now.strftime('%d/%m')}, {now.strftime('*%A*')}):\n\n"

    else:
        tomorrow = now + datetime.timedelta(days=1)
        return f"Horários nobres vagos para AMANHÃ ({tomorrow.strftime('%d/%m')}, {tomorrow.strftime('*%A*')})\n\n:"

final = "\n\nConsulte disponibilidade para os demais horários"
greetings = initMessage()
middle = middleMessage()
sportsMessages = (padel.actualMessage, beach.actualMessage) 
sportsList = (padel.times, beach.times)
sportsPromo = (padel.promo, beach.promo)

print(greetings)
print(sportsMessages)
print(middle)
print(sportsList)
print(sportsPromo)
print(final)