# SCHOOL MANAGEMENT PROJECT ( MCQ GENERATOR )




from cryptography.fernet import Fernet

key = Fernet.generate_key()
 
fernet = Fernet(key)

admin=[{'username': 'krushank', 'password': '12'}]
user=[{'Uusername': 'krushank', 'Upassword': '123456'}]
question=[{'questions': 'what is your ', 'wrong': ['ds', 'sj', 'js', 'jsj'], 'right': 'krushank'},
          {'questions': 'how are you', 'wrong': ['23', 'ds', 'sd', 'sd'], 'right': 'nice'},
          {'questions': 'Which clss you are in ', 'wrong': ['2', '3', '4', '12'], 'right': 'college'},
          {'questions': 'What is your age ', 'wrong': ['12', '16', '13', '15'], 'right': '20'},
          {'questions': 'What is your gf name ', 'wrong': ['ds', 'sj', 'js', 'jsj'], 'right': 'I dont know'}]
d={}
# ques={""}

while(True):
    print("1.ADMIN")
    print("2.USER")
    print("0.EXIT")

    choice =int(input("Enter your choice = "))


    if(choice==1):
        print("----------------------------------------------------------")
        print("          YOU ARE DIRECTED TO ADMIN PANEL")
        print("----------------------------------------------------------")
        print("1.Register")
        print("1.Login")
        print("----------------------------------------------------------")
        
        choice1 = int(input("Enter your choice = "))
        
        if(choice1==1):
            Nusername = input("Enter your new username = ")
            Npassword = input("Enter your new password = ")
            print("----------------------------------------------------------")
            
            
            print("Registration Done Successfully")
            
            encMessage = fernet.encrypt(Npassword.encode())
            
            d={}
            d["username"]=Nusername
            d["password"]=Npassword
            print(d)
            admin.append(d)
            
        elif(choice1==2):
            flag=0
            Lusername =input("Enter your username = ")
            Lpassword =input("Enter your password = ")
            print("----------------------------------------------------------")
            
            
            for i in admin:
                if(Lusername==i["username"] and Lpassword==i["password"]):
                    print("")
                    print("Log in sucessful")
                    flag=1
                    
                    while(True):
                        print("==========================================================================================================================")
                        print("1. INSERT")
                        print("2. POP")
                        print("3. DISPLAY")
                        print("4. UPDATE")
                        print("0. EXIT")
                        print("==========================================================================================================================")
                        
                        
                        adminch=int(input("Enter the choice = "))
                        
                        if(adminch==1):
                            print("----------------------------------------------------------")
                            print("YOU  SELECTED INSERT FUNCTION")      
                            print("----------------------------------------------------------")
                            question1=input("Enter your question = ")
                            wop1=input("Enter option 1 = ")
                            wop2=input("Enter option 2 = ")
                            wop3=input("Enter option 3 = ")
                            wop4=input("Enter option 4 = ")
                            rop5=input("Enter option 5 = ")
                            print("________________________________________________________________________________")
                            
                            ques={}
                            ques["questions"]=question1
                            ques["wrong"]=[wop1,wop2,wop3,wop4]
                            ques["right"]=rop5
                            print(ques)
                            question.append(ques)
                            print(question)
                            
                        
                        elif(adminch==2):
                            flag=0
                            print("----------------------------------------------------------")
                            print("YOU SELECTED POP FUNCTION")
                            print("----------------------------------------------------------") 
                            questionmatch=input("Enter your question = ")
                            
                            c=0
                            
                            for i in question:

                                if(questionmatch==i["questions"]):
                                    question.pop(c) 
                                    flag=1
                                    print(question)
                                    c=c+1;    
                            if(flag==0):
                                print("------------------------------------------------------")
                                print("QUESTION NOT FOUND")  
                                print("------------------------------------------------------")                                
                                
                        elif(adminch==3):
                            print("----------------------------------------------------------")
                            print("YOU SELECTED DISPLAY FUCNTION")
                            print("----------------------------------------------------------")
                            
                            for i in question:  
                                print(i)
                            
                        elif(adminch==4):
                            flag=0
                            print("----------------------------------------------------------")
                            print("YOU SELECTED UPDATE FUCNTION")
                            print("----------------------------------------------------------")
                            
                            questionmatch1=input("Enter your question to change = ")
                            c=0
                            for i in question:
                                if(questionmatch1==i["questions"]):
                                    flag=1
                                    newquestion=input("Enter new question = ")
                                    print("----------------------------------------------------------")
                                    newwop1=input("Enter option = ")
                                    newwop2=input("Enter option = ")
                                    newwop3=input("Enter option = ")
                                    newwop4=input("Enter option = ")
                                    newrop5=input("Enter option = ")

                                    i["questions"]=question1
                                    i["wrong"]=[newwop1,newwop2,newwop3,newwop4]
                                    i["right"]=newrop5
                                    
                                    break
                                c=c+1
                                
                                
                        elif(adminch==0):
                            break
                        
                        else:
                            print("----------------------------------------------------------")
                            print("ENTER VALID NUMBER")
                            print("----------------------------------------------------------")
            
            if(flag==0):
                print("Check your entered username or password")
        
        elif(choice1==0):
            break    
        
    
    elif(choice==2):
        flag=0
    
        print("------------------------------------------------------------------")
        print("         YOU ARE DIRECTED TO USER PANEL")
        print("------------------------------------------------------------------")
        while(True):
            print("===========================================================================")
            print("1. REGISTER")
            print("2. LOGIN")
            print("0. EXIT")
            print("===========================================================================")
        
            choice2=int(input("Enter your choice = "))
            
            if(choice2==1):
                NUusername = input("Enter your new username = ")
                NUpassword = input("Enter your new password = ")
                print("----------------------------------------------------------")        
                print("Registration Done Successfully")
                print("----------------------------------------------------------")        
                
                encMessage = fernet.encrypt(NUpassword.encode())
                
                use={}
                use["Uusername"]=NUusername
                use["Upassword"]=NUpassword
                user.append(use)
                print(use)
                
                #print(user)
                
            elif(choice2==2):
                LUusername =input("Enter your username = ")
                LUpassword =input("Enter your password = ")
                print("----------------------------------------------------------")
                
                
                for i in user:
                    if(LUusername==i["Uusername"] and LUpassword==i["Upassword"]):
                        print("")
                        print("Log in successful")
                        flag=1
                        print("_________________________________________________________________________________________________________")
                        print("                               Solve the following questions ")
                        print("_________________________________________________________________________________________________________")
                        c=0
                        for i in question:
                            # print(i["questions"])
                            # print(i["wrong"])
                            # print(i["right"])
                            print("-----------------------------------------------------------------------------")
                            print("Question :-  ",i["questions"])
                            print("Option 1 :-  ",i["wrong"][0])
                            print("Option 2 :-  ",i["wrong"][1])
                            # print("Option 3 :-  ",i["right"])
                            print("Option 3:-  ",i["right"])
                            print("Option 4 :-  ",i["wrong"][3])
                            print()
                            youranswer=input("Enter your answer option number = ")
                            print()
                            
                            if(youranswer==i["right"]):
                                c=c+1
                                
                        print("YOUR SCORE IS ",c,"/",len(question))                        
                            
                        
                if(flag==0):
                    print("Check your username or password")
                    
            elif(choice2==0):
                break
            
            else:
                print("Enter valid choice")