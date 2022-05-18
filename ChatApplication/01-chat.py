# hi / hello / hey / hello there...
# play music / please play music / start song / start music
# tell me date / date / what's the date
# show time
# tell me news
# wether report

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hello there":
        print("Hello User...")
    elif msg == "bye":
        print("Bye User...")
        chat = False
        break
    else:
        print("I don't Understand...")