with open('Capture_1.PNG','rb') as file:
    data = file.read()
    # print(data)

with open('Cap_2.png','wb') as file:
    file.write(data)
