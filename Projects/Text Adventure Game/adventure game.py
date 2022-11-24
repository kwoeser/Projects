###
# Karma Woeser
# ADVENTURE GAME
###

#imports
import cards 
import random
import time

doors = ["Door 1","Door 2", "Door 3"]#list

print("You're stuck in a forest and need to escape")
print("You also have no service and lost your phone and friends")
print("You're friends are in the forest, find them and escape")
print("Becareful of monsters and there are a total of 3 friends in the forest")
print()

'''
THERE'S ONLY ONE ROUTE TO ESCAPE, YOU HAVE TO GO
STRAIGHT TO TO ESCAPE BUT I CAN'T TELL YOU THE REST
'''
def story():#function
    answer=input("Would you like to play y/n? ")

    

    if answer.lower().strip() == "y":
        answer = input("You a road that spilts into 3 ways, would you like to go straight, left, or right ").lower().strip()
        print()





        '''
        While the answer is atraight many different things could happen
        like you finding your friend or dying to another monster or you
        fighting a monster with your friend and killing the monster.
        this is the only possible way for you to escape the entrance.
        '''
        
        while answer == "straight":
            friend_1=input("You head down a long dark path and see a shadowy figure, do you want to approch it y/n ")
            print()
            
            if friend_1.lower() == "y":
                print("You have found one of your friends Tim, you and him team up to find the rest of your friends")
                print()
                
                friend=input("You try and retrace your footsteps with Tim and try to find your friend and you run into a bridge and there are 2 guards with 2 huge cards in there hands, in one guard's hand there is a King and in one hand there is a Joker, guard 1 has a king in his hand and guard 2 has a joker in his hand which one do you want to choose 1/2 ")             
                if friend.lower() == "1":
                    print()
                    print("You chose King and the guards let you pass across the bridge")
                    print("At the other side of bridge you encounter a monster and you and your friend attack him")
                    print()
                    print("The monster attacks...")
                    time.sleep(2)#makes it feel more like a game
                    print("You and your friend attack...")
                    time.sleep(2)
                    print("The monster attacks...")
                    time.sleep(2)
                    print()
                    print("The monster dies")
                    print("Inside of the monster you find your other friend's corspe in his belly and you run away in fear")
                    print("As you and your friend are running away you run into a huge tree")
                    '''
                    THE EXIT, THE WAY OUT
                    '''
                    exit=input("Do you climb it or keep walking forward y to climb/n to keep forward ")
                    if exit.lower() == "y":
                        print("You and your friend climb the tree and see an exit if you keep walking forward, but right as you and your friend spot it you slip and fall onto your friend and both of you fall to your death")
                        print()
                        story()
                        break

                    
                    elif exit.lower() == "n":
                        print()
                        print("You keep on walking forward and see an huge monster appears in front of you")
                        print("The monster lunges at you...")
                        time.sleep(1.5)#makes it feel more like a game
                        print("You and your friend dogde...")
                        time.sleep(1.5)
                        print("You both attack the monster...")
                        time.sleep(1.5)
                        print("The monster attacks your friend..")
                        time.sleep(1.5)
                        print("You jump and attack the monster and finally...")
                        time.sleep(2)
                        print()
                        print("The monster dies and you carry your friend out of the forest")
                        print("GAME OVER, YOU WIN!")
                        myfile = open("win.txt", "w")#FILE
                        myfile.write("Hopefully I still get points for this")
                        myfile.close()
                        break
                        

                        

                if friend.lower() == "2":
                        print("You chose Joker and the guards kill both you and your friend")
                        print()
                        story()
                        break
                        
            if friend_1 == "n":
                print("You head back to the road")
                answer = input("You a road that spilts into 3 ways, would you like to go straight, left, or right ")
                print()








        '''
        While the answer is left the following will happening
        and it will ask you many different questions thing like
        attacking the monster and dying or you running away
        and playing the game with the person in the cabin
        '''


        while answer == "left":
            friend_2= input("You head down a dark road and head to a cabin, do you want to go in y/n ")
            print()

            if friend_2.lower() == "n":
                print("You head back to the road")
                answer = input("You a road that spilts into 3 ways, would you like to go straight, left, or right ").lower().strip()
                print()
                

            elif friend_2.lower() == "y":
                attack=input("You enter the cabin just to see an monster inside, do you want to attack y/n ")

                if attack.lower() == "y":
                    print("You attack...")
                    time.sleep(2)
                    print("The monster attacks...")
                    time.sleep(2)
                    print("You attack...")
                    time.sleep(2)
                    print("The monster attacks...")
                    time.sleep(2)
                    print()
                    print("You died")
                    print()
                    story()
                    break

                elif attack.lower() == "n":
                    print("You run...")
                    time.sleep(2)
                    print("The monster chases you...")
                    time.sleep(2)
                    print("You finally make it out...")
                    time.sleep(2)
                    print()
                    print("You're tired but then you see a person playing cards at the table ")
                    print("You approach him outta curiosity, and he asks you to play with him")
                    print("You play just because you're kinda scared of him")
                    print("He says that if you win he will tell you the way out of the forest")

                    play=input("Do you want to play a game with him y/n ")#PLAY A GAME
                    
                    if play.lower() == "y":
                        print()
                        print("He tells you whoever gets higher number cards they will win, then you two play")
                        cards.your_cards()#MODULE PLACEMENT
                        cards.player_cards()
                        print("After you two play he says that he didn't even know the way out and kills you")
                        story()
                        break
                            
                        
                    elif play.lower() == "n":
                        print("He says you have to play, but you argue with him and try to run but he kills you with a swift throw of a card")
                        story()
                        break




                        
                    


        '''
        While the answer is right the following happens
        so you first attack the monster and then monster
        spawn in front of you but you get saved by your
        friend but that if you go this route
        '''

        
        while answer == "right":
            print("As your walking down the road you run into a monster he attacks you and you have no choice but to fight")
            print("The monster attacks...")
            time.sleep(2)
            print("You attack...")
            time.sleep(2)
            print("The monster attacks...")
            time.sleep(2)
            print("You dogde then attack...")
            time.sleep(2)
            print()
            print("The monster dies")
            print()
            print("Inside the monster a person comes out but it's not one of your friends, he tells to chose a number between 1 and 6")
            print("At first you attack him outta fear but you can instantly tell he is way stronger then you but then you ask him what's gonna happen if I choose a number")
            print("He says that if you choose the correct answer you will escape the forest")
            
            monster_inside=input("You believe him and choose an number between 2 and 10, what number do you choose: ")
            print()
            print("The person inside of the monster spawns",monster_inside,"monsters in front of you and you try to run away but the monsters and too fast and they corner you")
            print()

            print("Then out of no where your friend appears with a huge group of people and they all recuse you and take down the monsters")
            friend_again=input("You look back at the person that spawned the monster but to your suprise you find out that he has disappeared. Then your friend asks for you to come with him y/n ")
            if friend_again == "y":
                print()
                print("You follow your friend and find out that he acutally isn't even your friend he's a random imposter that somehow looks like your friend")
                print("You figure this out but you try and act like you don't know then you try to run but get killed in a instant")
                print()
                story()
                break
                
            elif friend_again == "n":
                print()
                print("Your friend argue with you on why you don't want to do with him but you tell him that you know the way out")
                print("Then your friend says the he knows the way out too and they should do find your other friend")
                print("You can tell that something is fishy and you try not to act too suspect, and when you look at your friend's face more you can tell that he wasn't even your friend at all he was someone else that looked like him")
                print("Then you say your going to leave and your 'friend' lets you go")
                print("While you try to find the exit by yourself you run into a small cabin")
                cabin=input("Do you want to enter the cabin y/n ")

                if cabin == "n":
                    print()
                    print("You don't enter the cabin and walk down a path and see someone come outta the cabin")
                    print("You instantly get scared and run away in fear and trip on a tree branch and fall into a trap")
                    print()
                    story()
                    break
            
                elif cabin == "y":
                    print()
                    print("You open the door for the cabin you find a person inside")
                    print("In the cabin is a person and there is 3 doors behing him")
                    print("He tells you to that one of the doors will lead to an exit, but the others don't")
                    print()
                    for i in doors:#for loop
                        print(i)
                    door=input("Which door would you like to choose outta the 3, enter 1,2 or 3: ")

                    if door.lower() == "1":
                        print("You open the first door and he pushes you in and the door close behind you")
                        print("Then you fall down a deep dark hole and fall into a endless pit and never hit the floor")
                        break

                    elif door.lower() == "2":
                        print("When you go to open the door it doesn't work and then he tells you that was never a option and kills you")
                        print() 
                        story()
                        break
                        

                    elif door.lower() == "3":
                        print("You enter the room and see a long hallway")
                        print("You start walking down and look back to see the door shut")
                        print("Then you see a ladder, it takes you on the roof then on the roof you see a exit")
                        leave=input("Do you want to head back down the ladder or just jump or the roof, enter l for ladder or j for jump ")

                        if leave.lower() == "l":
                            print("You head back down the ladder and the person inside the cabin awaits you and kills you")
                            print()
                            story()
                            break
                        
                        elif leave.lower() == "j":
                            print("You jump off and right at the porch of the cabin there is a monster and he attacks you and kills you before you even notice")
                            print()
                            story()
                            break
                            
                    else:
                        print("He tells you that not a opition and kills you")
                        story()
                        break







story()





        

