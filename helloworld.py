# Juan Marcos Mendez
# Ok I dont know what happened but this is becomeing a pain to upload
# I had to delete and redo the fork and download just to try and submit it.

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!
name = ''                             #User can put anything.
print('Hey you what your name?')      #Asks for name
name = input()                        #Waiting for imput of name
print('Thnak you ' + name)            #Me adding a thanks plus name
print('Can you now pick a launguge?') #Asking the user to pick a languge
print('Press 1 for English')          #display option 
print('Press 2 for Spanish')          #display option
print('Press 3 for Klingon')          #display option
number = input()                      #Waiting for number input
if number == '1':                     #if its 1 then say it in english
    print('Hello ' + name)            #saying it in english
elif number == '2':                   #if its 2 then say it in spanish
    print('Hola ' + name)             #saying it in spanish
elif number == '3':                   #If its 3 then your a nerd just like me lol
    print('nuqneH ' + name)           #Klingon hello
elif number == '':                    #for the person who doesnt pick one
    print('Silly billy that is not a number')   #no languge picked
print('Are you done here? y/n ')                #just an addon to practice
done = input()                                  #everything past this point
if done == 'y':                                 #extra credit :) 
    print('Goodbye ' + name)
elif done == 'n':
    print('To bad, bye ' + name)
elif done == '':
    print('Okay be that way. bye ' + name)
    
    


