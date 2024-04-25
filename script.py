import time

def introduction():
    print("Welcome to the Haunted Mansion Adventure!")
    print("You find yourself standing in front of a dark and eerie mansion, surrounded by mist.")
    print("The mansion seems abandoned, but strange noises emanate from within.")
    print("Do you dare to enter and uncover its secrets?")
    print("What will you do?")
    time.sleep(2)
    print("1. Enter the mansion through the front door.")
    print("2. Look for another way inside.")
    print("3. Turn back and leave.")
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_front_door()
    elif choice == "2":
        print("You decide to look for another way inside.")
        # Add function call for another way inside
    elif choice == "3":
        print("You decide to turn back and leave. The mystery of the mansion remains unsolved.")
def enter_front_door():
    print("You gather your courage and push open the creaky front door, stepping into the mansion's foyer.")
    print("The air feels heavy, and the silence is deafening.")
    print("What will you do next?")
    time.sleep(2)
    print("1. Explore the ground floor.")
    print("2. Head upstairs to the upper floors.")
    print("3. Check the basement for clues.")
    choice = input("Enter your choice: ")
    if choice == "1":
        explore_ground_floor()
    elif choice == "2":
        print("You decide to head upstairs to explore the upper floors.")
        # Add function call for exploring upper floors
    elif choice == "3":
        print("You decide to check the basement for clues.")
def explore_ground_floor():
    print("You begin to explore the ground floor of the mansion.")
    print("Each room is filled with dusty furniture and cobwebs.")
    print("Suddenly, you hear footsteps coming from the next room.")
    print("What will you do?")
    time.sleep(2)
    print("1. Investigate the source of the footsteps.")
    print("2. Hide and observe from a safe distance.")
    print("3. Retreat back to the foyer.")
    choice = input("Enter your choice: ")
    if choice == "1":
        investigate_source_of_footsteps()
    elif choice == "2":
        retreat_quietly()
    elif choice == "3":
        print("You decide to retreat back to the foyer.")
        enter_front_door()
def investigate_source_of_footsteps():
    print("You cautiously approach the room where you heard the footsteps.")
    print("Peering inside, you see a shadowy figure lurking in the darkness.")
    print("What will you do?")
    time.sleep(2)
    print("1. Confront the figure and demand answers.")
    print("2. Retreat quietly and avoid being noticed.")
    print("3. Call out to ask the figure who they are.")
    choice = input("Enter your choice: ")
    if choice == "1":
        confront_the_figure()
    elif choice == "2":
        retreat_quietly()
    elif choice == "3":
        ask_the_figure_who_they_are()
def confront_the_figure():
    print("You summon your courage and step forward, confronting the shadowy figure.")
    print("As you draw closer, the figure's form shifts and twists,")
    print("revealing itself to be a malevolent spirit, its eyes gleaming with malice.")
    time.sleep(2)
    print("You bravely confront the shadowy figure, but as you draw near, it lunges at you with supernatural speed, enveloping you in darkness.")
    print("Your vision fades as chilling whispers surround you, marking the end of your journey in the haunted mansion.")
    print("GAME OVER")
    #This is a death

def retreat_quietly():
    print("As you choose to retreat quietly you notice the door behind you has closed and locked")
    print("This causes you to be very nervous and frightened")
    time.sleep(2)
    print("1. Whimper out for help")
    print("2. Continue to look around for clues")
#This will result in a win

def whimper():
    print("You can't help but let out a whimper, hoping someone will come to your aid.")
    print("Suddenly, you hear footsteps approaching from the other side of the door.")
    time.sleep(2)
    print("1. Call out for help.")
    print("2. Stay silent and listen.")
    choice = input("Enter your choice: ")
    if choice == "1":
        call_out_for_help()
    elif choice == "2":
        stay_silent_and_listen()
def call_out_for_help():
    print("You call out for help to the voices outside, your voice echoing through the empty halls.")
    print("But as time passes with no response, desperation sets in.")
    print("You begin to imagine voices and noises, seeking comfort in illusions of rescue.")
    print("Tragically, no help arrives, and you're left to confront the terrifying reality alone.")
    print("You've met a grim fate within the confines of the haunted mansion.")
    print("GAME OVER")

def stay_silent_and_listen():
    print("You decide to stay silent and listen.")
    print("As you strain your ears, you hear faint whispers echoing through the corridors of the mansion.")
    print("The whispers seem to be guiding you, leading you deeper into the heart of the mansion.")
    time.sleep(2)
    print("You follow the whispers, your heart pounding with each step, until you reach a hidden chamber.")
    print("Inside the chamber, you find an old diary, its pages filled with cryptic writings and mysterious symbols.")
    print("As you leaf through the pages, you feel a chill run down your spine, as if the diary itself holds some dark power.")
    time.sleep(2)
    print("What will you do next?")
    print("1. Take the diary with you and continue exploring.")
    print("2. Leave the diary and search for another way out.")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You decide to take the diary with you, feeling that it may hold the key to unlocking the mansion's secrets.")
        print("With the diary in hand, you venture further into the mansion, following the whispers.")
        time.sleep(2)
        print("As you explore, you come across a locked door with strange symbols etched into its surface.")
        print("The symbols seem to match those in the diary.")
        print("What will you do?")
        print("1. Use the diary to decipher the symbols and unlock the door.")
        print("2. Leave the door and search for another path.")
        door_choice = input("Enter your choice: ")

        if door_choice == "1":
            print("You carefully study the symbols in the diary and manage to decipher the code.")
            print("With a satisfying click, the door unlocks, revealing a hidden passage.")
            time.sleep(2)
            print("What will you do next?")
            print("1. Walk down the hidden passage.")
            print("2. Try and find another way.")
            passage_choice = input("Enter your choice: ")

            if passage_choice == "1":
                print("You bravely step into the hidden passage, determined to uncover its secrets.")
                print("The passage twists and turns, leading you deeper into the depths of the mansion.")
                time.sleep(2)
                print("After what feels like an eternity of winding corridors and hidden chambers,")
                print("you finally come across a door bathed in an eerie glow.")
                print(
                    "As you approach the door, you feel a sense of foreboding, as if something dark awaits on the other side.")
                time.sleep(2)
                print("What will you do?")
                print("1. Open the door and confront whatever lies beyond.")
                print("2. Turn back and search for another path.")
                door_choice = input("Enter your choice: ")
                if door_choice == "1":
                    print("With a deep breath, you summon your courage and push open the door.")
                    # Add continuation of the story or ending based on what lies beyond the door
                elif door_choice == "2":
                    print("You decide to turn back, unwilling to face whatever awaits beyond the glowing door.")
                    # Add continuation of the story or ending


            elif passage_choice == "2":
                print("You decide to search for another way, leaving the hidden passage behind for now.")
                # Add continuation of the story or ending

        elif door_choice == "2":
            print("You decide to leave the door for now and continue exploring.")
            time.sleep(2)
            print("What will you do?")
            print("1. Try to find more clues.")
            print("2. Head back to the foyer")
            exploration_choice = input("Enter your choice: ")

            if exploration_choice == "1":
                print("You search for more clues, hoping to uncover a way out of the mansion.")
                # Add continuation of the story or ending

            elif exploration_choice == "2":
                print("You decide to head back to the foyer, feeling that you may have missed something.")
                time.sleep(2)
                print("On the way back to the foyer, you notice something different.")
                print("As you round a corner, you come face to face with a ghastly apparition, its eyes glowing with malice.")
                time.sleep(2)
                print("You freeze in terror as the apparition reaches out towards you, its chilling touch draining the warmth from your body.")
                print("In a panic, you try to flee, but it's too late.")
                print("Your vision fades as darkness envelops you, marking the end of your journey in the haunted mansion.")
                print("Game Over")

    elif choice == "2":
        print("You leave the diary behind, not wanting to risk the dangers it may hold.")
        # Add continuation of the story or ending


def ask_the_figure_who_they_are():
    print("Summoning all your courage, you call out to the shadowy figure,")
    print("demanding to know who they are and what they seek.")
    print("The figure turns slowly towards you, its eyes gleaming with malice,")
    print("and a chilling voice whispers, 'I am the keeper of this mansion's darkest secrets.'")
    time.sleep(2)
    print("What will you do next?")
    print("1. Ask for a trade for more information.")
    print("2. Retreat cautiously and try to find another way out.")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask_for_a_trade()
    elif choice == "2":
        retreat_cautiously()

#This will lead to a win

def retreat_cautiously():
    print("Feeling overwhelmed by the eerie atmosphere and the unknown dangers lurking in the mansion,")
    print("you decide to retreat cautiously, step by step, back towards the foyer.")
    print("Every creak of the floorboards sends shivers down your spine as you navigate the dimly lit corridors.")
    print("You're keenly aware of the eerie silence, broken only by the occasional unsettling noise.")

    print("As you inch your way back, a sudden gust of wind extinguishes your only source of light, plunging you into darkness.")
    print("Panic sets in as you realize you've lost your sense of direction, and the mansion seems to have come alive around you.")

    print("In your disoriented state, you stumble and fall into a hidden pit trap, your screams echoing through the mansion's halls as darkness consumes you.")

    print("You've met a tragic end, another victim claimed by the haunted mansion's sinister secrets.")
#This is a death make the game end

def ask_for_a_trade():
    print("You decide to take a risk and propose a trade to the ghostly figure,")
    print("offering something of value in exchange for information on how to escape the mansion.")
    print("You offer to exchange your soul for the information.")
    time.sleep(2)
    print("The ghostly figure considers your offer, its ethereal form wavering slightly.")
    print("After what feels like an eternity, it finally speaks, its voice echoing in the darkness.")
    print("Your soul is a tempting offer, it says, but I seek something more tangible.")
    while True:
        print("You rack your brain for something else to offer, realizing that your soul might not be enough.")
        print("You could:")
        print("1. Offer a cherished possession instead.")
        print("2. Offer to perform a task for the ghostly figure.")
        choice = input("Enter your choice: ")
        if choice == "1":
         print("You try to offer your gold locket with a picture of your family in it.")
         print("The ghost is not interested in your locket. ")
        # Add continuation of the story or ending
        elif choice == "2":
            perform_task()
def perform_task():
    print("The ghostly figure nods.")
    print("Deep within these walls lies an ancient locket, a token of my past life.")
    print("Retrieve it, and I shall grant you the knowledge to escape.")
    print("You could:")
    print("1. Accept the task and begin your search.")
    print("2. Refuse and seek another way out.")
    choice = input("Enter your choice: ")
    if choice == "1":
        accept_the_task()
    elif choice == "2":
        refuse_and_seek()
def refuse_and_seek():
    print("You refuse the task, determined to find another way out.")
    print("But as you stand alone in the darkness,")
    print("you realize the enormity of your decision.")
    print("Without the ghost's guidance, you're lost.")
    print("Trapped forever within these haunted walls.")
    print("GAME OVER")

def accept_the_task():
    print("You accept the task, determined to find the ancient locket and earn your freedom.")
    print("With a nod of determination, you set off into the depths of the mansion.")
    print("After what feels like hours of searching, you finally discover the ancient locket, hidden away in a forgotten chamber.")
    print("With the locket in hand, you return to the ghostly figure.")
    print("As you offer the locket, the figure's form begins to shimmer,")
    print("and with a soft glow, it imparts the knowledge you seek.")
    print("With gratitude, the ghostly figure gestures towards the exit.")
    print("You step out of the mansion, finally free from its haunting confines.")
    print("Congratulations! You have successfully escaped the haunted mansion.")

introduction()
