string = "this is a string"
space = " "

for x in range(len(string)):
    if(string[x] == space):
        print(string[0:x])
        break
