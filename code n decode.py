# CODE N DECODE

ans = input("\nDo you wish to code or decode? ") 
num = int(input("\nEnter the number of words to be coded or decoded: "))
print("\nNow you must enter one word of your sentence at a time")
for i in range(0,num):
    if(ans.lower() == "code"):
        word = input("\nEnter the word to be coded: ")
        a = len(word)
        if(a>=3):
            nword = f"wrd{word[1:]}{word[0]}hsc"
            print(f"The coded word for {word} is {nword}")        
        else:
            nword = f"{word[1:]}{word[0]}"
            print(f"The coded word for {word} is {nword}")
    else:
        word = input("\nEnter the code to be decoded: ")
        a = len(word)
        nword = f"{word[3:(a-3)]}"
        b = len(nword)
        tword = f"{nword[b-1]}{nword[0:(b-1)]}"
        print(f"The decoded word for {word} is {tword}")        
              

# a new code
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
