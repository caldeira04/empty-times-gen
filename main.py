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
        return f"Bom dia pessoal!" #Good morning everyone!

    elif currentHour < 18:
        return f"Boa tarde pessoal!" #Good afternoon everyone!
    
    else:
        return f"Boa noite pessoal!" #Good evening everyone!

sportsMessages = (padel.generateMessage(), beach.generateMessage()) 
sportsList = (padel.obtainAvailableTimes(), beach.obtainAvailableTimes())

print(sportsMessages[0, 1])
print(sportsList[0, 1])



