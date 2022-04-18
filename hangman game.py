import random
def hangman():
    list_of_words=["random","rock","apple","cattel","school","education","complete","software"]
    word=random.choice(list_of_words)
    turns=10
    guessmade=""
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word=""
        missed=0

        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"

        if main_word==word:
            print(main_word)
            print("you won!!!")
            break

        print("guess the words",main_word)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid characters")
            guess=input()

        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left!!")
                print("------------------------")
            if turns==8:
                print("8 turns left!!")
                print("------------------------")
                print("           O            ")
            if turns==7:
                print("7 turns left!!")
                print("------------------------")
                print("                        ")
                print("           O            ")
                print("           I            ")
            if turns==6:
                print("6 turns left!!")
                print("------------------------")
                print("                        ")
                print("           O            ")
                print("           I            ")
                print("          /             ")
            if turns==6:
                print("6 turns left!!")
                print("------------------------")
                print("                        ")
                print("           O            ")
                print("           I            ")
                print("          / \            ")
            if turns==5:
                print("5 turns left!!")
                print("------------------------")
                print("                        ")
                print("          \O            ")
                print("           I            ")
                print("          / \           ")
            if turns==4:
                print("4 turns left!!")
                print("------------------------")
                print("                        ")
                print("          \O/           ")
                print("           I            ")
                print("          / \           ")
            if turns==3:
                print("3 turns left!!")
                print("------------------------")
                print("               |        ")
                print("          \O/           ")
                print("           I            ")
                print("          / \           ")
            if turns==2:
                print("2 turns left!!")
                print("------------------------")
                print("               |        ")
                print("          \O/  |        ")
                print("           I            ")
                print("          / \           ")
            if turns==1:
                print("only 1 turn left!! Hangman on his last breath.")
                print("------------------------")
                print("               |        ")
                print("          \O/__|        ")
                print("           I            ")
                print("          / \           ")
            if turns==1:
                print("you loose!!")
                print("you let a good man die..")
                print("------------------------")
                print("               |        ")
                print("           O __|        ")
                print("          /I\           ")
                print("          / \           ")

                break
                
    
name=input("enter your name:")
print("welcome",name,"!")
print("________________")
print("try to guess the word in less thn 8 attampts:")
hangman()