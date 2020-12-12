#/////////////////////////////////DICTIONARIES

hotel = {
  
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
    '102': None,
    '103': None,
  },

  '2': {
    '201': ['Jack Torrance', 'Wendy Torrance'],
    '202': None,
    '203': None,
  },

  '3': {
    '301': ['Neo', 'Trinity', 'Morpheus'],
    '302': None,
    '303': None,
  }
}

#/////////////////////////////////END DICTIONARIES





#/////////////////////////////////FUNKTIONS

def check_floor_availability(f):
    if f == 1:
        
        if hotel['1']['101'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['1']['101'] = [person1]
                 
            if checking_status == "in" and group_size == 2:
                hotel['1']['101'] = [person1, person2]
                    
            if checking_status == "in" and group_size == 3:
                hotel['1']['101'] = [person1, person2, person3]
                   
            if checking_status == "in" and group_size == 4:
                hotel['1']['101'] = [person1, person2, person3, person4]
                   
            if checking_status == "in" and group_size == 5:
                hotel['1']['101'] = [person1, person2, person3, person4, person5]
                    
            if checking_status == "in" and group_size == 6:
                hotel['1']['101'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 101. Here is your key. Have a nice stay!")

          
        elif hotel['1']['102'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['1']['102'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['1']['102'] = [person1, person2]
            
            if checking_status == "in" and group_size == 3:
                hotel['1']['102'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['1']['102'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['1']['102'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['1']['102'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 102. Here is your key. Have a nice stay!")
            
           
        elif hotel['1']['103'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['1']['103'] = [person1]
            
            if checking_status == "in" and group_size == 2:
                hotel['1']['103'] = [person1, person2]
            
            if checking_status == "in" and group_size == 3:
                hotel['1']['103'] = [person1, person2, person3]
            
            if checking_status == "in" and group_size == 4:
                hotel['1']['103'] = [person1, person2, person3, person4]
           
            if checking_status == "in" and group_size == 5:
                hotel['1']['103'] = [person1, person2, person3, person4, person5]
           
            if checking_status == "in" and group_size == 6:
                hotel['1']['103'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 103. Here is your key. Have a nice stay!")
            
        
        else:
            print("OOOPS! I'm sorry. We do not have any availability on the first floor.")
    
    
    if f == 2:

        if hotel['2']['201'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['2']['201'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['2']['201'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['2']['201'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['2']['201'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['2']['201'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['2']['201'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 201. Here is your key. Have a nice stay!")

        elif hotel['2']['202'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['2']['202'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['2']['202'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['2']['202'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['2']['202'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['2']['202'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['2']['202'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 202. Here is your key. Have a nice stay!")

        elif hotel['2']['203'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['2']['203'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['2']['203'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['2']['203'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['2']['203'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['2']['203'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['2']['203'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 203. Here is your key. Have a nice day!")

        else:
            print("Oops. I'm sorry. We do not have any availability on the second floor.")
    
    
    if f == 3:

        if hotel['3']['301'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['3']['301'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['3']['301'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['3']['301'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['3']['301'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['3']['301'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['3']['301'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 301. Here is your key. Have a nice stay!")

        elif hotel['3']['302'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['3']['302'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['3']['302'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['3']['302'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['3']['302'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['3']['302'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['3']['302'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 302. Here is your key. Have a nice stay!")

        elif hotel['3']['303'] == None:
            if checking_status == "in" and group_size == 1:
                hotel['3']['303'] = [person1]
                
            if checking_status == "in" and group_size == 2:
                hotel['3']['303'] = [person1, person2]
               
            if checking_status == "in" and group_size == 3:
                hotel['3']['303'] = [person1, person2, person3]
              
            if checking_status == "in" and group_size == 4:
                hotel['3']['303'] = [person1, person2, person3, person4]
             
            if checking_status == "in" and group_size == 5:
                hotel['3']['303'] = [person1, person2, person3, person4, person5]
            
            if checking_status == "in" and group_size == 6:
                hotel['3']['303'] = [person1, person2, person3, person4, person5, person6]
            print("I\'m checking you in to Room 303. Here is your key. Have a nice stay!")

        else:
            print("Oops. I'm sorry. We do not have any availability on the third floor.")

#/////////////////////////////////END FUNKTIONS





checking_status = input("Are you checking \"in\" or \"out?\" ")
group_size = int(input("How many people are in your group? "))

if checking_status == "in":
    if group_size > 6:
        print("I'm sorry. We have no rooms that can accommodate more than 6 people. Kick rocks!")
    elif group_size == 6:
        person1 = input("What is your name? ")
        person2 = input("What is the name of the second person in your group? ")
        person3 = input("What is the name of the third person in your group? ")
        person4 = input("What is the name of the fourth person in your group? ")
        person5 = input("What is the name of the fifth person in your group? ")
        person6 = input("What is the name of the sixth person in your group? ")
    elif group_size == 5:
        person1 = input("What is your name? ")
        person2 = input("What is the name of the second person in your group? ")
        person3 = input("What is the name of the third person in your group? ")
        person4 = input("What is the name of the fourth person in your group? ")
        person5 = input("What is the name of the fifth person in your group? ")
    elif group_size == 4:
        person1 = input("What is your name? ")
        person2 = input("What is the name of the second person in your group? ")
        person3 = input("What is the name of the third person in your group? ")
        person4 = input("What is the name of the fourth person in your group? ")
    elif group_size == 3:
        person1 = input("What is your name? ")
        person2 = input("What is the name of the second person in your group? ")
        person3 = input("What is the name of the third person in your group? ")
    elif group_size == 2:
        person1 = input("What is your name? ")
        person2 = input("What is the name of the second person in your group? ")
    elif group_size == 1:
        person1 = input("What is your name? ")
    else:
        print("Kick rocks.")
    
    chosen_floor = input("Which floor would you like to be on? Choose \"1\" , \"2\" , or \"3\" : ")

if chosen_floor == "1":
    print(check_floor_availability(1))

if chosen_floor == "2":
    print(check_floor_availability(2))

if chosen_floor == "3":
    print(check_floor_availability(3))
        
        
   
print("Hotel\'s current occupancy: %s" %hotel)