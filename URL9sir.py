#bsmlh
# Importing sys, socket, pyshorteners, urlparse
import sys, socket, pyshorteners
from urllib.parse import urlparse

#The help menu-------------------------------------------------------
#if the script name only is given
def HELP(): print("""_/This is the help menu for URL9sir.py

Usage: python3 URL9sir.py [options] <example1.com> <example2.com> <exampleN.com>
        
    /\\ Type the URL without the "HTTP://"
Options:
        -help | -h      Display this help menu
        -force | -f     Get the shortener link if the website is down
                  
""")
#proxy of redirections : -proxy | -p


if len(sys.argv) == 1: #if no aditional argiments are given
    HELP()
    exit()

#if a help argument is given
elif sys.argv[1].lower() in ["-help", "--help", "help", "-h", "h" ]:
        HELP()
        exit()

#the end of the help menu --------------------------------------------


#force the script to spawn the link if the website is down------------


#The script header----------------------------------------------------
print("""
      
⠀⢀⣤⡀⠀⢠⣠⡀⢠⣠⣄⣤⣠⡀⠀⣤⡀⠀⠀⠀⢀⣤⣤⣀⠀⠀⠀⠀⠀⠀⢠⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢐⣿⡇⠀⢸⣿⡂⢸⣿⣏⣉⣿⡇⠨⣿⡇⠀⠀⠀⣿⣇⢈⣿⡇⢠⣴⠦⣦⠀⢰⣵⠀⣤⣦⣦⠄⠀⠠⣴⣤⢦⣦⠀⣴⡄⠠⣴⠄⠀
⠀⠀⣿⣇⣀⣸⣿⠄⢸⣿⡏⢻⣯⡄⠐⣿⣇⣀⣀⡀⣈⣏⢋⣿⡏⣘⣛⠳⣶⡆⢸⣿⠀⢾⣗⠀⣤⡠⢐⣿⡇⢨⣿⠅⠸⣷⣸⡟⠀⠀
⠀⠀⠈⠛⠛⠋⠃⠀⠘⠙⠁⠀⠋⠋⠈⠋⠋⠛⠙⠀⠈⠋⠛⠉⠀⠈⠋⠛⠙⠁⠘⠋⠀⠙⠉⠀⠋⠋⠠⣿⡏⠛⠙⠀⣀⣽⡿⠀⠀⠀

       
      """)
#----------------------------------------------------------------------

#PROIBLEM
#spawn links for down websites(controll it, -f option for spawn, and not by default)


#Get input to choose which URL shortener service to use, or all of them
INPUT = input("Pick a service :> clckru[1]  isgd[2] tinyurl[3] dagd[4] ALL[0]: ")

SAVE = input("Do you want to save it [Y/n]? (press ENTER to skip) ")


def SHORTS():    
            #Pass more than one URL at once
        def REPEAT(A):
            
            # Get input(the URL link) from STDIN and pass it as an argument to the function
            URL = sys.argv[A]

            #FIRST we need to check the validity of the URLs by setting up a TCP connection
            
            #parse the URL
            HOST = urlparse(URL).netloc
            if HOST == "":
                HOST = urlparse(URL).path
            else:
                HOST

            PORT = 80


            #Error handling 
            try:
                #create a socket object    
                ###                           IPv4   |        TCP client
                CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                #Connect the client
                CLIENT.connect((HOST,PORT))

                #Send some data
                CLIENT.send(b"GET / HTTP/1.1\r\nHost: bleh bleh ugh ugh\r\n\r\n")
                
                #receive some data
                #RESPONSE = CLIENT.recv(4096)

                print(f"{URL} is up!")
            
            #If target is down dont spawn the shortened link
            except socket.gaierror:
                print(f"{URL} is down :c")        
                return
            CLIENT.close()        
            


            #Shorten the shortener function in S varuable
            S = pyshorteners.Shortener()

            #Handle the INPUT
            if INPUT == "1":
                # use tinyurl
                print(f"{URL} => {S.clckru.short(URL)}")
            elif INPUT == "2":
                #use isgd
                print(f"{URL} => {S.isgd.short(URL)}")

            elif INPUT == "3":
                #use clckru
                print(f"{URL} => {S.tinyurl.short(URL)}")

            elif INPUT == "4":
                #use dagd
                print(f"{URL} => {S.dagd.short(URL)}")

            else:
                #if the INPUT is something ELSE, use all of the URL shortener services
                print(f"{URL} => {S.clckru.short(URL)}")
                print(f"{URL} => {S.isgd.short(URL)}")
                print(f"{URL} => {S.tinyurl.short(URL)}")
                print(f"{URL} => {S.dagd.short(URL)}")


        for ARG in range(1,1000):
            try:
                    if sys.argv[ARG].lower() in ["--force", "-force", "-f"]:
                                    
                        # Get input(the URL link) from STDIN and pass it as an argument to the function
                        for ARG in range(2,1000):       
                                URL = sys.argv[ARG]

                                #FIRST we need to check the validity of the URLs by setting up a TCP connection
                                
                                #parse the URL
                                HOST = urlparse(URL).netloc
                                if HOST == "":
                                    HOST = urlparse(URL).path
                                else:
                                    HOST

                                PORT = 80


                                #Error handling 
                                try:
                                    #create a socket object    
                                    ###                           IPv4   |        TCP client
                                    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                                    #Connect the client
                                    CLIENT.connect((HOST,PORT))

                                    #Send some data
                                    CLIENT.send(b"GET / HTTP/1.1\r\nHost: bleh bleh ugh ugh\r\n\r\n")
                                    
                                    #receive some data
                                    #RESPONSE = CLIENT.recv(4096)

                                    print(f"{URL} is up!")
                                
                                #If target is down dont spawn the shortened link
                                except socket.gaierror:
                                    print(f"{URL} is down :c")        
                                    
                                CLIENT.close()        
                                


                                #Shorten the shortener function in S varuable
                                S = pyshorteners.Shortener()

                                #Handle the INPUT
                                if INPUT == "1":
                                    # use tinyurl
                                    print(f"{URL} => {S.clckru.short(URL)}")
                                elif INPUT == "2":
                                    #use isgd
                                    print(f"{URL} => {S.isgd.short(URL)}")

                                elif INPUT == "3":
                                    #use clckru
                                    print(f"{URL} => {S.tinyurl.short(URL)}")

                                elif INPUT == "4":
                                    #use dagd
                                    print(f"{URL} => {S.dagd.short(URL)}")

                                else:
                                    #if the INPUT is something ELSE, use all of the URL shortener services
                                    print(f"{URL} => {S.clckru.short(URL)}")
                                    print(f"{URL} => {S.isgd.short(URL)}")
                                    print(f"{URL} => {S.tinyurl.short(URL)}")
                                    print(f"{URL} => {S.dagd.short(URL)}")

                    else:
                        REPEAT(ARG)                       
                        print("... .. .")
                    
            except:
                break



#SAVE INPUT, IF STATEMEENT 
#NO no N n 
if SAVE.lower() in ["no", "n", ""]:   
    SHORTS()


# yes y Y ye YA YES YS MHM
elif SAVE.lower() in ["yes", "ye", "y"]:
    FILENAME = input("File name: ")
    print(" WAIT Wait..")
    #Redirect the output to a file
    with open(FILENAME or "URL9sir.txt", 'a') as FILE:
        sys.stdout = FILE
        SHORTS()


