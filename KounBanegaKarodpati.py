# a new one

question = ["1)WHICH PLANET IS CALLED THE RED PLANET?",
            "2)WHO WROTE THE NATIONAL ANTHEM 'JANA GANA MANA'?",
            "3)What is the capital of Australia?",
            "4)WHO IS THE FOUNDER OF MICROSOFT?", 
            "5)Which Indian scientist is known as the 'Missile Man of India'?",
            "6)Which is the largest desert in the world?",
            "7)What is the smallest unit of matter?",
            "8)Which Indian festival is known as the 'Festival of Lights'?",
            "9)Which is the smallest continent in the world?",
            "10)What is the boiling point of water at standard atmospheric pressure(in degree celsius?",
            "11)Which Indian state is known as the 'Land of Five Rivers'?",
            "12)What is the chemical symbol for gold?",
            "13)Which country is known as the Land of the Rising Sun?",
            "14)Which is the largest mammal in the world?",
            "15)Who is known as the 'Father of the Indian Constitution'?",
            "16)who is the father of our nation?"]

options = [["a) EARTH","b) MARS","c) JUPITER","d)saturn"],
           ["a) RABINDRANATH TAGORE","b) MAHATMA GANDHI","c) B.R.AMBEDKAR","d) SUBHASH CHANDRA BOSE"],
           ["a)syndney","b)canberra","c)ottawa","d)wellington"],
           ["a) ELON MUSK","b) SUNDER PICHAI","c) STEVE JOBS","d) BILL GATES"],
           ["a) APJ ABDUL KALAM","b)HOMI JAHANGIR BABA","c)ELON MUSK","d)CV RAMAN"],
           ["a) Antarctic polar desert","b)sahara desert","c)great australian desert","c)gobi desert"],
           ["a)cells","b) molecules","c)dust","d)atom"],
           ["a)sankranti","b)diwali","c)dasara","d)christmas"],
           ["a)India","b)europe","c)australia","d)america"],
           ["a)27","b)39","c)100","d)1000"],
           ["a)karnataka","b)rajasthan","c)punjab","d)haryana"],
           ["a)Au","b)Ag","c)o","d)Fe"],
           ["a)India","b)china","c)singapore","d)japan"],
           ["a)blue whale","b)elephant","c)hippo","d)tiger"],
           ["a)gandhiji","b)BR ambedkar","c)Bhagat singh","d)subhashchandra bose"],
           ["a)gandhiji","b)BR ambedkar","c)Bhagat singh","d)subhashchandra bose"]]           

answers = ["b","a","b","d","a","a","d","b","c","c","c","a","d","a","b","a"]

money1 = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,100000000,700000000]

# print(len(question), len(options), len(answers))

for i in range(0,len(question)):
    q = question[i]
    print("\n",q)
    option = options[i]
    print(option[0],    option[1])
    print(option[2],   option[3])
    a = input("ENTER YOUR ANSWER(A-B)(if you want to quit then write 'quit'): ")
    money = 0
    if(i == 4):
        money = 10,000
    elif(i == 9):
        money == 3,20,000
    elif(i == 14):
        money == 1,00,00,000
    if(a == "quit"):
       print(f"\nfine you can quit. your net amount is {money1[i-1]}")
       exit()
    elif(a.lower() == answers[i]):
        print(f"\ncongrats you won. you won Rs.{money1[i]}")
    else:
        print(f"\nwrong answer. you loose your net amount is {money}")
        break



# print("₹")

        
