# if file do not exist then it creates a new file
# if file exists then it overwrite the file
# file = open('file_2.txt','w')
# data = "Hello How are you...?"
# file.write(data)
# file.close()

# Append mode
# file = open('file_2.txt','a')
# data = "\nI am good...Thanks for asking..."
# file.write(data)
# file.close()

# 'x' mode - I will always create a new file
# if file already exists then I will raise error...
file = open('file_3.txt','x')
data = "Hello How are you...?"
file.write(data)
file.close()