import main

sport = "beach"

# Functions will most likely be the same on both beach and padel files, they'll only change at main

def generateMessage():
    # Getting and creating the messages file
    try:
        with open(f"{sport}_messages.txt", "r", encoding="utf-8") as messagelist:
            messages = messagelist.readlines()
    # If the file isn't found, the program creates it
    except FileNotFoundError:
        with open(f"{sport}_messages.txt", "w", encoding="utf-8") as messagelist:
            messages = []

    # Getting all messages list
    while True:
        print(f"Selecione uma mensagem para utilizar no {sport}: ") # Select a message for this time
        for i, message in enumerate(messages):
            print(f"{i+1}. {message.strip()}")
        print("0. Escrever uma nova mensagem") #Create a new message
        try:
            n = int(input("Digite o número da mensagem correspondente: ")) #Type the message's number
            if 0 < n <= len(messages):
                obtainedMessage = messages[n - 1].strip() # Will send the message without the sq brackets and numbers
                print(obtainedMessage)
                break

            elif n == 0:
                newMessage = input("Insira a nova mensagem: ") #Type in the new message
                messages.append(newMessage + "\n")
                with open(f"{sport}_messages.txt", "w", encoding="utf-8") as f:
                    f.write(newMessage + "\n") #Breaks the line so the new message dont concatenate at the same line as an older message

            else:
                print("Opção inválida, tente novamente") # No such option, try again

        except ValueError:
            print("Entrada inválida. Digite um número.") # Invalid input, type a number
    return obtainedMessage

actualMessage = generateMessage()

#Function for obtaining the times that are available
    
def obtainAvailableTimes():
    availableTimes = []

    while True:
        times = input(f"Insira um horário disponível para {sport} ou digite 'fim' para encerrar:") #Insert a available time or type "finish" to end the loop

        if times.lower() == "fim":
            break
        try:
            time = int(times)
            if int(times) > 21:
                raise ValueError #Since 21 is the last available time, I'll end the code here

            else:
                availableTimes.append(time)
        except ValueError:
            print("Horário inválido, tente novamente") # Invalid time, try again

    if availableTimes:
        availableTimes.sort()
        sortedTimes = [f"{time:02d}h" for time in availableTimes]
        timeList = ", ".join(sortedTimes)
        return f"{sport}: *{sortedTimes}*" #This will return the sorted available times
    
    else:
        return f"Não há quadras disponíveis para {sport}"

times = obtainAvailableTimes()

# Function to analyze if the promo is valid on the day
def hasPromo():
    for i in times:

        if "21" in times:
            return " (promocional, joga até 23h)"

promo = hasPromo()