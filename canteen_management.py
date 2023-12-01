from cryptography.fernet import Fernet

key = Fernet.generate_key()
 
fernet = Fernet(key)

admin=[{'username': 'krushank', 'password': '12'}]
user=[{'Uusername': 'krushank', 'Upassword': '123456'}]
product_list=[{'item': 'burger', 'item_rate': '20'},
{'item': 'dhosa', 'item_rate': '100'},
{'item': 'idli', 'item_rate': '40'},
{'item': 'menduvada', 'item_rate': '30'},
{'item': 'manchurian', 'item_rate': '70'},
{'item': 'vadapav', 'item_rate': '15'},
{'item': 'puffpav', 'item_rate': '20'},
{'item': 'bread pakoda', 'item_rate': '15'},
{'item': 'thumbs up', 'item_rate': '20'},
{'item': 'pluppy', 'item_rate': '20'},
{'item': 'manchau soup', 'item_rate': '60'},
{'item': 'mineral water', 'item_rate': '20'}]


while(True):
    print("1. ADMIN")
    print("2. USER")
    print("0. EXIT")
    
    choice=int(input("Enter your choice = "))
    
    if(choice==1):
        print("------------------------------------------------------------")
        print("                      ADMIN PANEL")
        print("------------------------------------------------------------")
        print()
        print("1. REGISTER")
        print("2. LOGIN")
        print("0. EXIT")
        print()
        print()
        adminuserchoice=int(input("Enter your choice = "))
        print()
        if(adminuserchoice==1):
            print()
            print("----------------------------------------")
            print("|      WELCOME ADMIN USER               |")
            print()
            print("|  You need to register first yourself  |")
            print("----------------------------------------")
            print()
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
            
        elif(adminuserchoice==2):
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
                            print("             YOU  SELECTED INSERT FUNCTION")      
                            print("----------------------------------------------------------")
                            itementry=input("Enter your item = ")
                            rate=input("Enter you item rate  = ")
                            print("________________________________________________________________________________")
                            
                            product={}
                            product["item"]=itementry
                            product["item_rate"]=rate
                            print(product)
                            product_list.append(product)
                            print(product_list)
                            
                        
                        elif(adminch==2):
                            flag=0
                            print("----------------------------------------------------------")
                            print("             YOU SELECTED POP FUNCTION")
                            print("----------------------------------------------------------") 
                            
                            itemmatch=input("Enter your item = ")
                            
                            c=0
                            
                            for i in product_list:

                                if(itemmatch==i["item"]):
                                    itemmatch.pop() 
                                    flag=1
                                    print(product_list)
                                    c=c+1;    
                            if(flag==0):
                                print("------------------------------------------------------")
                                print("          !! ITEM NOT FOUND !!")  
                                print("------------------------------------------------------")                                
                                
                        elif(adminch==3):
                            print("----------------------------------------------------------")
                            print("             YOU SELECTED DISPLAY FUCNTION")
                            print("----------------------------------------------------------")
                            
                            for i in product_list:  
                                print(i)
                            
                        elif(adminch==4):
                            flag=0
                            print("----------------------------------------------------------")
                            print("             YOU SELECTED UPDATE FUCNTION")
                            print("----------------------------------------------------------")
                            
                            itemmatch1=input("Enter your item to change = ")
                            c=0
                            for i in product_list:
                                if(itemmatch1==i["item"]):
                                    flag=1
                                    newitem=input("Enter new item  = ")
                                    newrate=input("Enter item rate = ")                                   

                                    i["item"]=newitem
                                    i["item_rate"]=newrate                                  
                                    break
                                c=c+1
                                
                            if(flag==0):
                                print("------------------------------------------------------")
                                print("          !! ITEM NOT FOUND !!")  
                                print("------------------------------------------------------") 
                        elif(adminch==0):
                            break
                        
                        else:
                            print("----------------------------------------------------------")
                            print("ENTER VALID NUMBER")
                            print("----------------------------------------------------------")
            
            if(flag==0):
                print("Check your entered username or password")
        
        elif(choice==0):
            break
        
        
    
    
    
    
    elif(choice==2):
        print()
        print("------------------------------------------------------------------")
        print("                        HELLO USER ")
        print("------------------------------------------------------------------")
        while(True):
            print("1. REGISTER")
            print("2. LOGIN")
            print("0. EXIT")
            print("------------------------------------------------------------------")
            print()
            print()
            
            userchoice=int(input("Enter your choice = "))
            print()
            
            if(userchoice==1):
                print()
                print("-----------------------------------------------------------------------------------")
                print("     HELLO USER TO USE OUR SERVICE YOU NEED TO REGISTER AND GET LOGGED IN ")
                print("-----------------------------------------------------------------------------------")
                print()
                NUusername = input("Enter your new username = ")
                NUpassword = input("Enter your new password = ")
                print()
                print("----------------------------------------------------------")        
                print("          Registration Done Successfully")
                print("----------------------------------------------------------")        
            
                encMessage = fernet.encrypt(NUpassword.encode())
            
                use={}
                use["Uusername"]=NUusername
                use["Upassword"]=NUpassword
                user.append(use)
                print(use)
                        
            elif(userchoice==2):
                print()
                print("----------------------------------------------------------------------------------------------")
                print("                                           HELLO USER ")
                print()
                print("                 PLEASE GET LOGGED IN USING YOUR REGISTERED USERNAME AND PASSWORD")
                print("----------------------------------------------------------------------------------------------")  
                print()
                LUusername =input("Enter your username = ")
                LUpassword =input("Enter your password = ")
                print("----------------------------------------------------------")
                
                for i in user:
                    if(LUusername==i["Uusername"] and LUpassword==i["Upassword"]):
                        print("")
                        print()
                        print("<<<<  Log in successful  >>>>")
                        print()
                        flag=1
                        b=0
                        print()
                        print("----------------------------------------------------------------------------------")
                        print("         Dear ",LUusername," HERE IS THE MENU PLEASE SELECT FROM BELOW")
                        print("----------------------------------------------------------------------------------")                    
                        print()    
                        while(1):                   
                            print("+-+-+-+-+-+-+-+-+-+-+-+-+-")                        
                            print("|  ITEM            RATE  |")
                            print("+-+-+-+-+-+-+-+-+-+-+-+-+-")                                              
                            for i in product_list:
                                print("---> ",i["item"],i["item_rate"])       
                            
                            print()
                            print("NOTE  :-  IF YOU WANT TO TAKE EXIT THEN WRITE 'EXIT' OR 'exit'")                                                                         
                            
                            print()
                            itemselect=input("Enter the item name = ")
                            
                            if(itemselect=='burger' or itemselect=='Burger'):
                                print()        
                                quantity1=int(input("Enter the quantity you want = "))
                                print()                    
                                print(quantity1," Burger has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity1*20)
                                
                            elif(itemselect=='dhosa' or itemselect=='Dhosa'):
                                print()
                                quantity2=int(input("Enter the quantity you want = "))
                                print(quantity2," Dhosa has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity2*100)
                                
                            elif(itemselect=='idli' or itemselect=='Idli'):
                                print()
                                quantity3=int(input("Enter the quantity you want = "))
                                print(quantity3," Idli has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity3*40)
                            
                            elif(itemselect=='menduvada' or itemselect=='Menduvada'):
                                print()
                                quantity4=int(input("Enter the quantity you want = "))
                                print(quantity4," menduvada has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity4*30)
                            
                            elif(itemselect=='manchurian' or itemselect=='Manchurian'):
                                print()
                                quantity5=int(input("Enter the quantity you want = "))
                                print(quantity5," manchurian has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity5*70)
                            
                            elif(itemselect=='vadapav' or itemselect=='Vadapav'):
                                print()
                                quantity6=int(input("Enter the quantity you want = "))
                                print(quantity6," Vadapav has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity6*15)
                            
                            elif(itemselect=='puffpav' or itemselect=='Puffpav'):
                                print()
                                quantity7=int(input("Enter the quantity you want = "))
                                print(quantity7," Puffpav has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity7*20)
                            
                            elif(itemselect=='bread pakoda' or itemselect=='Bread pakoda'  or itemselect=='Bread Pakoda'):
                                print()
                                quantity8=int(input("Enter the quantity you want = "))
                                print(quantity8," Bread Pakoda has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity8*15)
                            
                            elif(itemselect=='thumbs up' or itemselect=='Thumbs up' or itemselect=='Thumbs Up'):
                                print()
                                quantity9=int(input("Enter the quantity you want = "))
                                print(quantity9," Thumbs Up has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity9*20)
                            
                            elif(itemselect=='pluppy' or itemselect=='Pluppy'):
                                print()
                                quantity10=int(input("Enter the quantity you want = "))
                                print(quantity10," Pluppy has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity10*20)
                            
                            elif(itemselect=='manchau soup' or itemselect=='Manchau soup' or itemselect=='Manchau Soup'):
                                print()
                                quantity11=int(input("Enter the quantity you want = "))
                                print(quantity11," Manchau Soup has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity11*60)
                            
                            elif(itemselect=='mineral water' or itemselect=='Mineral water' or itemselect=='Mineral Water'):
                                print()
                                quantity12=int(input("Enter the quantity you want = "))
                                print(quantity12," Mineral Water has been added in your bill")
                                print()
                                print("----> TOTAL BILL   =  ",quantity12*20)
                            
                            elif(itemselect=='exit' or itemselect=='EXIT'):
                                print()
                                print()
                                break
                            
                            else:
                                print()
                                break
                        
                if(flag==0):
                    print("              !! ERROR !!                ")
                    print()
                    print("   PLEASE CHECK YOUR USERNAME OR PASSWORD")
                    
            elif(userchoice==0):
                break
            
            else:
                print("!! Enter a valid number !!")
            
    elif(choice==3):
        break
    
    else:
        print(" !!  Enter a valid number  !! ")