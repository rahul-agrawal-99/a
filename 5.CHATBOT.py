import datetime


print("  Welcome to the CHATBOT  ")
name = input("Hey What's your name? ")
print("\n\n  What can i do for you  " , name , "\n")



def chatbot(st):
    if st in ["hi","hello","hey" , "hii"]:
        return "Hello " + name
    if st in ["Bye","bye" , "by"]:
        return "Bye have a nice day"
    if st in ["time","time is","time now"]:
        return "It is " + str(datetime.datetime.now().strftime("%H:%M:%S"))
    if st in ["Joke","joke","Joke me" , "laugh"]:
        return "I am not a joke like you  \n Just Kidding ^_^"
    if st in ["thanks","thank you" , "thank"]:
        return "You are welcome !"
    if st in ["loan" , "money"]:
        return "You mean Loan , i Would advise you to check offers Kotak bank"
    if st in ["invest" , "investment"]:
        return "That's great plan , why dont you go for IPO's"
    
    
    return False




while(True):
    query = input(f"\nAsk me anything {name}  \n")
    
    for q in query.split():
        ans = chatbot(q)
        if ans != False:
            break
    
    
    
    if ans == "Bye have a nice day":
        print(ans)
        break
    
    if not ans:
        print(" I Cant understand you ! \n Please try again ")
    else:   
        print(ans)
    
    
    
    