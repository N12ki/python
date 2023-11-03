day = input("Enter day name of the : ")
if day == "monday" or day == "Monday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \tPrise")
    display = '''    1] Aalu Pratha      Ru:-70
    2] Dal-Rice         Ru:-120
    3] Momos           Ru:-90
    4] Black Chana      Ru:-90
    5] Rasgula          Ru:-50'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+70
            elif x==2:
                c=c+120
            elif x==3:
                c=c+60
            elif x==4:
                c=c+90
            elif x==5:
                c=c+50
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Tuseday" or day == "tuseday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \t\tPrise")
    display = '''    1] French Fries              Ru:-60
    2] Gulab Jamun	        Ru:-130
    3] Spicy Pasta              Ru:-60
    4] Dal Makhani              Ru:-100
    5] Laccha Parantha          Ru:-110'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+60
            elif x==2:
                c=c+130
            elif x==3:
                c=c+60
            elif x==4:
                c=c+100
            elif x==5:
                c=c+110
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Wednesday" or day == "wednesday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \t\tPrise")
    display = '''    1] Roomali Roti             Ru:-60
    2] Tandoori Paneer Tikka    Ru:-130
    3] Jeera Raita              Ru:-60
    4] Spring Roll              Ru:-100
    5] Papad                    Ru:-15'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+60
            elif x==2:
                c=c+130
            elif x==3:
                c=c+60
            elif x==4:
                c=c+100
            elif x==5:
                c=c+15
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Thursday" or day == "thursday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \t\tPrise")
    display = '''    1] Tomato, Onion Pizza	Ru:-150
    2] Dosa (Butter)            Ru:-60
    3] Halwa (Seasonal)         Ru:-50
    4] Tomato Uttapam           Ru:-105
    5] Gol Gappa                Ru:-62'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+150
            elif x==2:
                c=c+60
            elif x==3:
                c=c+50
            elif x==4:
                c=c+105
            elif x==5:
                c=c+62
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Friday" or day == "friday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \t\tPrise")
    display = '''    1] Dahi Bhalla Papri        Ru:-90
    2] Gulab Jamun	          Ru:-60
    3] Jeera Raita              Ru:-70
    4] Plain Raita              Ru:-127
    5] Chutney                  Ru:-25'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+90
            elif x==2:
                c=c+60
            elif x==3:
                c=c+70
            elif x==4:
                c=c+127
            elif x==5:
                c=c+25
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Saturday" or day == "saturday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print("\t items  \t\tPrise")
    display = '''    1] Plain Cheese Pizza	Ru:-170
    2] Pav Bhaji	        Ru:-135
    3] Coffee Mocachino         Ru:-50
    4] Gravy Noodles            Ru:-109
    5] Sambhar                  Ru:-75'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+170
            elif x==2:
                c=c+135
            elif x==3:
                c=c+50
            elif x==4:
                c=c+109
            elif x==5:
                c=c+75
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)

elif day == "Sunday" or day == "sunday":
    print("Good morning what would you like to Odder Sir/Mam : \n")
    print(" \t items   \t \t\tPrise")
    display = '''    1] Chilly Garlic Rice	        Ru:-160
    2] Rawa Dosa	                Ru:-155
    3] Fresh Juices Seasonal/Mix	Ru:-60
    4] Veg Hakka Noodles                Ru:-145
    5] Fruit Punch                      Ru:-75'''
    print(display)
    print("enter done when you done with your odder")
    x = 0
    c = 0
    while True:
        x = input("Select an number of dish wich you want to odder (or Done) : ") 
        if x == "Done":
            break
        else:
            x = int(x)
            if x==1:
                c=c+160
            elif x==2:
                c=c+155
            elif x==3:
                c=c+60
            elif x==4:
                c=c+145
            elif x==5:
                c=c+75
            else:
                print("Invalid item number. Please select a valid item.")
    print("Totle Bill :- ",c)
