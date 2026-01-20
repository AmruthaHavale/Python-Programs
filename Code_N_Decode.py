# a new code
print("---Welcome to Code And Decode.---")
print("If you wanna covert a text into a code then type code.:)\nIf you wanna decode a code then type decode.:)")
cnd = input("Do you wish to code or decode? ")
if(cnd.lower() == "code"):
    msg = input("Enter your message: ")   
    words = msg.split(" ")
    newword = []
    for i in words:
        if(len(i)>=3):
            nword = "akj" + i[1:] + i[0] + "hje"
            newword.append(nword)
        elif(len(i) == 2):
            nword = i[1] + i[0]
            newword.append(nword)
        else:
            nword = i
            newword.append(nword)
    print(" ".join(newword))
else:
    msg = input("Enter the code: ")
    words = msg.split(" ")
    newword = []
    for i in words:
        if(len(i)>=3):
            nword = i[-4] + i[3:-4]
            newword.append(nword)
        elif(len(i) == 2):
            nword = i[1] + i[0]
            newword.append(nword)
        else:
            nword = i
            newword.append(nword)
    print(" ".join(newword))