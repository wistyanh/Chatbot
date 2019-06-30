#Chatbot -- P.S. the ASCII art may not work on Windows and/or Linux
import time

def intro():
    print("Hi! My name is Anh. Type something to start talking!")
    print("P.S. type 'hi', 'tell me a joke', or 'show me art' if you don't know what to say!")
    print("And say 'bye' when you're done!")

def defaultResponse():
    print("Nice!")

def tellJoke():
    response1 = input("Knock knock! (who's there) ")
    response1.lower()
    if response1 == "who's there" or response1 == "who's there?":
        response2 = input("Hatch. (hatch who) ")
        response2.lower()
        if response2 == "hatch who" or response2 == "hatch who?":
            print("Bless you!")
            print("HAHAHA")
        else:
            print("Oh no! (╯°□°)╯")
            time.sleep(1)
            print("You said it wrong:( Try again from the beginning! (Say 'tell me a joke') ")
    else:
            print("Oh no! (╯°□°)╯")
            time.sleep(1)
            print("You said it wrong:( Try again from the beginning! (Say 'tell me a joke') ")

def showArt():
    print(r"""                    \
                                   ._ o o
                                   \_`-)|_
                                ,""       \
                              ,"  ## |   ಠ ಠ.
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /

                         TA DA!

                """)

def convo(answer):
    response1 = input("Hey there! What's your name?")
    response1.lower()
    if response1 == "erin":         #dancing man ASCII art only works for MAC - tailor for your own device
        print (r"""
                    ⊂_ヽ
                    　＼＼ Hey
                    　 ＼( ͡° ͜ʖ ͡°)
                    　　　 >　⌒ヽ
                    　　　/ 　 へ＼
                    　　 /　　/　＼ cutie
                    　　 ﾚ　ノ　　 ヽ_つ
                    　　/　/
                    　 /　/|
                    　(　(ヽ
                    　|　|、 ＼
                    　| 丿 ＼ ⌒)
                    　| |　　) /
                     ノ )　　Lﾉ
                    (_/
                """)
# use this ASCII art if the first one doesn't work (Windows)
#         print (r"""
#
# ░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄
# ░░░█░░░░▄▀█▀▀▄░░▀▀▀▄░░░░▐█░░░░░░░░░▄▀█▀▀▄░░░▀█▄
# ░░█░░░░▀░▐▌░░▐▌░░░░░▀░░░▐█░░░░░░░░▀░▐▌░░▐▌░░░░█▀
# ░▐▌░░░░░░░▀▄▄▀░░░░░░░░░░▐█▄▄░░░░░░░░░▀▄▄▀░░░░░▐▌
# ░█░░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░█       Hey
# ▐█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█         Cutie:3
# ▐█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█
# ░█░░░░░░░░░░░░░░░░░░░░█▄░░░▄█░░░░░░░░░░░░░░░░░░█
# ░▐▌░░░░░░░░░░░░░░░░░░░░▀███▀░░░░░░░░░░░░░░░░░░▐▌
# ░░█░░░░░░░░░░░░░░░░░▀▄░░░░░░░░░░▄▀░░░░░░░░░░░░█
# ░░░█░░░░░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▀▀░░░░░░░░░░░░░█
#
#             """)
    elif response1 == "nae nae":
        print (r"""
                                              _
                                   .-.  .--''` )
                                _ |  |/`   .-'`
                               ( `\      /`
                               _)   _.  -'._
                             /`  .'     .-.-;
        Hey                  `).'      /  \  \
                            (`,        \_o/_o/__
                             /           .-''`  ``'-.
                             {         /` ,___.--''`
                             {   ;     '-. \ \
           _   _             {   |'-....-`'.\_\
          / './ '.           \   \          `"`
       _  \   \  |            \   \            Nae Nae:3
      ( '-.J     \_..----.._ __)   `\--..__
     .-`                    `        `\    ''--...--.
    (_,.--""`/`         .-             `\       .__ _)
            |          (                 }    .__ _)
            \_,         '.               }_  - _.'
               \_,         '.            } `'--'
                  '._.     ,_)          /
                     |    /           .'
                      \   |    _   .-'
                       \__/;--.||-'
                        _||   _||__   __
                 _ __.-` "`)(` `"  ```._)
                (_`,-   ,-'  `''-.   '-._)
               (  (    /          '.__.'
                `"`'--'
            """)
    else:
        print(r"""
                (っ◕‿◕)っ
        """)
        print("Hey " + response1 + " !")
    response1 = input("How are you? ")
    response1 = input("That's good! What did you have for lunch? ")
    response1 = input("ooo yummmm! Hey wanna hear a joke? ")
    if response1 == "no" or response1 == "No":
        print(" (ㆆ _ ㆆ) ")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Too bad! It's opposite day (‾ ⌣ ‾) ")
        tellJoke()
    else:
        print("Okay! Type 'tell me a joke' to hear one!")

def processInput(answer):
    hi = ["hi", "hello", "hey", "what's up", "sup", "hey cutie"]
    bye = ["bye", "farewell", "exit", "break"]
    cont = True

    if answer in hi:
        convo(answer)
    elif answer == "tell me a joke":
        tellJoke()
    elif answer == "show me art":
        showArt()
    elif answer in bye:
        print("Bye! See you soon!")
        print (r"""	(｡◕‿‿◕｡) """)
        cont = False
    else:
        defaultResponse()
    return cont

def main():
    cont = True
    while cont != False:
        answer = input("(What will you say?) ")
        answer.lower()
        cont = processInput(answer)

intro()
main()
