import time

def introduction():
    print("Welcome to the Haunted Mansion Adventure!")
    print("You find yourself standing in front of a dark and eerie mansion, surrounded by mist.")
    print("The mansion seems abandoned, but strange noises emanate from within.")
    print("Do you dare to enter and uncover its secrets?")
    print("What will you do?")
    time.sleep(2)
    print("\n1. Enter the mansion through the front door.")
    print("2. Look for another way inside.")
    print("3. Turn back and leave.")
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_front_door()
    elif choice == "2":
        look_for_another_way_in()
    elif choice == "3":
        print("\nYou decide to turn back and leave. The mystery of the mansion remains unsolved.")


def look_for_another_way_in():
    time.sleep(2)
    print("\nYou decide to look for another way inside the mansion.")
    print("As you search the perimeter, you notice two possible paths.")
    time.sleep(2)
    print("\n1. Explore the overgrown garden path on the left side of the mansion.")
    print("2. Venture into the dark alley on the right side of the mansion.")
    choice = input("Enter your choice: ")
    if choice == "1":
        explore_garden_path()
    elif choice == "2":
        venture_into_dark_alley()

def explore_garden_path():
    time.sleep(2)
    print("\nYou choose to explore the overgrown garden path.")
    print("The garden is filled with tangled vines and eerie statues covered in moss.")
    time.sleep(2)
    print("\n1. Investigate the old well hidden in the corner of the garden.")
    print("2. Follow the winding path deeper into the heart of the garden.")
    choice = input("Enter your choice: ")
    if choice == "1":
        investigate_old_well()
    elif choice == "2":
        follow_winding_path()

def follow_winding_path():
    time.sleep(2)
    print("\nYou decide to follow the winding path deeper into the garden.")
    print("The path twists and turns, leading you deeper into the heart of the overgrown garden.")
    print("Suddenly, you feel the ground give way beneath your feet, and you plummet into a hidden pit.")
    print("The fall knocks the wind out of you, and you realize too late that it's a trap set by the mansion's dark forces.")
    print("As darkness consumes you, you realize you've become another victim of the mansion's sinister secrets.")
    print("\nGame Over.")
    restart_game()

def investigate_old_well():
    time.sleep(2)
    print("\nYou approach the old well with caution.")
    print("Peering into its depths, you catch a glimpse of something glimmering at the bottom.")
    time.sleep(2)
    print("\n1. Lower a rope into the well to retrieve the object.")
    print("2. Leave the well alone and continue exploring the garden.")
    choice = input("Enter your choice: ")
    if choice == "1":
        lower_rope_into_well()
    elif choice == "2":
        continue_exploring_garden()

def continue_exploring_garden():
    time.sleep(2)
    print("\nYou decide to leave the well alone and continue exploring the garden.")
    print("As you wander deeper into the garden, you stumble upon a hidden path obscured by thick foliage.")
    time.sleep(2)
    print("Intrigued, you follow the path and discover a forgotten mausoleum nestled among the trees.")
    print("\n1. Enter the mausoleum and search for clues.")
    print("2. Explore the area surrounding the mausoleum.")
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_mausoleum()
def enter_mausoleum():
    time.sleep(2)
    print("\nYou cautiously push open the heavy doors of the mausoleum and step inside.")
    print("The air is thick with dust, and the scent of decay fills your nostrils.")
    print("You illuminate the darkness with your flashlight and search for any signs of significance.")
    time.sleep(2)
    print("In the dim light, you spot an ancient sarcophagus adorned with strange markings.")
    print("\n1. Investigate the sarcophagus.")
    print("2. Search the rest of the mausoleum.")
    choice = input("Enter your choice: ")
    if choice == "1":
        investigate_sarcophagus()
    elif choice == "2":
        search_the_rest_of_mausoleum()

def investigate_sarcophagus():
    time.sleep(2)
    print("\nYou approach the sarcophagus with trepidation, intrigued by its mysterious markings.")
    print("As you cautiously examine it, you notice a hidden compartment.")
    print("Inside, you find a rare artifact that holds the key to unlocking the mansion's secrets.")
    print("With the artifact in hand, you feel a sense of triumph and accomplishment.")
    time.sleep(2)
    print("However, as you try to leave, you hear a sinister laughter echoing through the mausoleum.")
    print("Suddenly, the lid of the sarcophagus slams shut, trapping you inside.")
    print("\n1. Use the artifact to escape the sarcophagus.")
    print("2. Try to force the lid open.")
    choice = input("Enter your choice: ")
    if choice == "1":
        use_artifact_to_escape()
    elif choice == "2":
        force_lid_open()


def use_artifact_to_escape():
    time.sleep(2)
    print("\nYou quickly use the artifact to unlock the sarcophagus, and the lid swings open.")
    print("You escape just in time, narrowly avoiding a deadly trap set by the mansion's dark forces.")
    time.sleep(2)
    print("As you step out of the mausoleum, you're faced with two paths:")
    print("\n1. Follow the map's instructions to the hidden chamber.")
    print("2. Leave the mansion grounds, feeling fortunate to have escaped alive.")
    choice = input("Enter your choice: ")
    if choice == "1":
        follow_map_to_hidden_chamber()
    elif choice == "2":
        leave_mansion_grounds()

def leave_mansion_grounds():
    time.sleep(2)
    print("\nYou choose to leave the mansion grounds, feeling fortunate to have escaped alive.")
    print("As you walk away, you can't shake the feeling that the mansion's dark secrets still linger.")
    print("As you reach the edge of the property, you're suddenly overcome by a sense of dread.")
    time.sleep(2)
    print("Without warning, the ground beneath you gives way, and you fall into a hidden pit.")
    print("The fall is long and merciless, and you hit the bottom with a bone-crushing impact.")
    print("You lie helpless in the darkness, realizing too late that leaving the mansion was a fatal mistake.")
    print("\nGame Over.")
    restart_game()
def follow_map_to_hidden_chamber():
    time.sleep(2)
    print("\nYou decide to follow the map's instructions to the hidden chamber.")
    print("With the artifact in hand, you navigate through the mansion's corridors.")
    time.sleep(2)
    print("Eventually, you reach the hidden chamber and uncover the mansion's darkest secret.")
    print("\nCongratulations! You've uncovered the truth and won the game.")
    restart_game()
def force_lid_open():
    time.sleep(2)
    print("\nYou try to force the lid open with all your strength, but it refuses to budge.")
    print("In a last desperate attempt, you kick the lid, triggering a hidden mechanism.")
    time.sleep(2)
    print("Spikes shoot out from the walls, impaling you from all sides.")
    print("With your last breath, you realize the true horror of the mansion's traps.")
    print("\nGame Over.")
    restart_game()
def search_the_rest_of_mausoleum():
    time.sleep(2)
    print("\nYou decide to search the rest of the mausoleum for clues.")
    print("Among the dusty shelves and ancient relics, you find a hidden compartment containing a cryptic journal.")
    time.sleep(2)
    print("The journal seems to detail the history of the mansion and its dark secrets.")
    print("As you reach for the journal, you hear a faint click beneath your feet.")
    time.sleep(2)
    print("Suddenly, the floor gives way, and you plummet into a hidden pit trap.")
    print("You land with a thud, and darkness engulfs you as the pit seals shut above you.")
    print("\nGame Over.")
    restart_game()

def lower_rope_into_well():
    time.sleep(2)
    print("\nYou carefully lower a rope into the well and feel the weight of the object at the bottom.")
    print("With a strong tug, you pull up a dusty old chest, covered in cobwebs.")
    print("Excitement courses through you as you eagerly open the chest to reveal its contents.")
    time.sleep(2)
    print("Inside, you find a collection of ancient artifacts, each radiating a mysterious energy.")
    print("Among the artifacts, you notice a map with cryptic symbols.")
    time.sleep(2)
    print("\n1. Study the map closely to decipher its meaning.")
    print("2. Take the artifacts and explore further into the mansion.")
    choice = input("Enter your choice: ")
    if choice == "1":
        study_map()
    elif choice == "2":
        explore_further()

def study_map():
    time.sleep(2)
    print("\nYou carefully study the map, trying to make sense of its cryptic symbols.")
    print("After deciphering the symbols, the map leads you to a hidden passage behind a bookshelf.")
    print("Following the map's guidance, you push aside the bookshelf and enter the hidden passage.")
    print("As you venture deeper, the passage twists and turns, leading you to the mansion's catacombs.")
    time.sleep(2)
    print("You've successfully followed the map's guidance and are closer to uncovering the mansion's secrets.")
    print("However, as you proceed, you notice three branching paths:")
    time.sleep(2)
    print("\n1. Follow the path illuminated by torches.")
    print("2. Take the narrow path that leads downwards.")
    print("3. Investigate the dark corridor with faint whispers.")
    choice = input("Enter your choice: ")
    if choice == "1":
        follow_torches_path()
    elif choice == "2":
        take_narrow_path()
    elif choice == "3":
        investigate_dark_corridor()

def follow_torches_path():
    time.sleep(2)
    print("\nYou choose to follow the path illuminated by torches, feeling it's the safest option.")
    print("As you walk along the well-lit corridor, you come across an ancient altar.")
    print("Upon the altar rests a relic of great power, shining with an otherworldly glow.")
    print("You cautiously approach the relic and claim it as your own, feeling its power coursing through you.")
    print("\nCongratulations! You've found the relic and won the game.")
    restart_game()
def take_narrow_path():
    time.sleep(2)
    print("\nYou opt for the narrow path that leads downwards, intrigued by its mysterious allure.")
    print("The path descends deeper into the darkness, becoming increasingly treacherous.")
    print("Suddenly, the ground gives way beneath you, and you plummet into a bottomless pit.")
    print("As you fall, you realize the map led you to your demise.")
    print("\nGame Over.")
    restart_game()
def investigate_dark_corridor():
    time.sleep(2)
    print("\nYou decide to investigate the dark corridor with faint whispers, despite the ominous signs.")
    print("As you walk down the corridor, the whispers grow louder and more sinister.")
    print("Before you can react, shadowy figures emerge from the darkness, surrounding you.")
    print("Their icy grip tightens around you, pulling you into the depths of the mansion.")
    print("You become another victim of the mansion's dark forces.")
    print("\nGame Over.")
    restart_game()
def explore_further():
    time.sleep(2)
    print("\nYou decide to take the artifacts and explore further into the mansion.")
    print("As you delve deeper into the mansion's corridors, you come across a locked door.")
    time.sleep(2)
    print("The artifacts seem to resonate with the door, hinting at a connection.")
    print("You carefully study the symbols in the diary and manage to decipher the code.")
    print("With a satisfying click, the door unlocks, revealing a hidden passage.")
    time.sleep(2)
    print("What will you do next?")
    print("\n1. Walk down the hidden passage.")
    print("2. Run away screaming")
    passage_choice = input("Enter your choice: ")

    if passage_choice == "1":
        time.sleep(2)
        print("\nYou bravely step into the hidden passage, determined to uncover its secrets.")
        print("The passage twists and turns, leading you deeper into the depths of the mansion.")
        time.sleep(2)
        print("After what feels like an eternity of winding corridors and hidden chambers,")
        print("you finally come across a door bathed in an eerie glow.")
        print("As you approach the door, you feel a sense of foreboding, as if something dark awaits on the other side.")
        time.sleep(2)
        print("With a deep breath, you summon your courage and push open the door.")
        print("To your surprise, you find yourself standing in a moonlit garden, surrounded by fragrant flowers and serene beauty.")
        time.sleep(2)
        print("The ghostly whispers that led you here fade away, replaced by the gentle rustle of leaves.")
        print("You realize that you've found the way out of the mansion, and with a grateful heart")
        print("you step into the garden, free at last.")
        time.sleep(2)
        print("\nCongratulations")
        restart_game()

    elif passage_choice == "2":
        time.sleep(2)
        print("\nAs you run away screaming the darkness swallows you.")
        time.sleep(2)
        print("Some still say they can hear you even today.")
        print("\nGAME OVER")
        restart_game()





def venture_into_dark_alley():
    time.sleep(2)
    print("\nYou decide to venture into the dark alley.")
    print("The alley is narrow and shadowy, with ominous whispers echoing off the walls.")
    time.sleep(2)
    print("\n1. Proceed cautiously down the alley.")
    print("2. Retreat and reconsider your options.")
    choice = input("Enter your choice: ")
    if choice == "1":
        proceed_down_alley()
    elif choice == "2":
        reconsider_options()

def proceed_down_alley():
    time.sleep(2)
    print("\nYou steel yourself and proceed cautiously down the alley.")
    print("The darkness seems to close in around you as you move deeper into the unknown.")
    print("Suddenly, you feel a cold hand grasp your shoulder, freezing you in place.")
    time.sleep(2)
    print("Before you can react, a shadowy figure emerges from the darkness and drags you into the abyss.")
    print("Your screams are swallowed by the darkness as you meet your untimely demise.")
    print("\nGAME OVER")
    restart_game()
def reconsider_options():
    time.sleep(2)
    print("You have chosen to reconsider your options.")
    time.sleep(2)
    print("\n1. Enter the mansion through the front door.")
    print("2. Look for another way inside.")
    print("3. Turn back and leave.")
    time.sleep(2)
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_front_door()
    elif choice == "2":
        print("\nYou decide to look for another way inside.")
        look_for_another_way_in()
    elif choice == "3":
        print("\nYou decide to turn back and leave. The mystery of the mansion remains unsolved.")






def enter_front_door():
    time.sleep(2)
    print("\nYou gather your courage and push open the creaky front door, stepping into the mansion's foyer.")
    print("The air feels heavy, and the silence is deafening.")
    print("What will you do next?")
    time.sleep(2)
    print("\n1. Explore the ground floor.")
    print("2. Head upstairs to the upper floors.")
    print("3. Check the basement for clues.")
    choice = input("Enter your choice: ")
    if choice == "1":
        explore_ground_floor()
    elif choice == "2":
        print("You decide to head upstairs to explore the upper floors.")
        head_upstairs()
        time.sleep(2)
    elif choice == "3":
        check_the_basement()
        time.sleep(2)


def check_the_basement():
    time.sleep(2)
    print("\nYou decide to check the basement, hoping to uncover any secrets or clues that may lie hidden below.")
    time.sleep(2)
    print("Descending down the creaky stairs, you enter the dimly lit basement, shrouded in shadows.")
    time.sleep(2)
    print("The air feels heavy with the weight of the mansion's history, sending shivers down your spine.")
    time.sleep(2)
    print("As you explore the basement, you come across various old furniture, dusty crates, and cobweb-covered objects.")
    time.sleep(2)
    print("What will you do next?")
    print("\n1. Search through the crates and objects for any useful items or information.")
    print("2. Retreat back to the foyer.")
    choice = input("Enter your choice: ")
    if choice == "1":
        search_basement()
    elif choice == "2":
        print("You decide to retreat back to the foyer.")
        enter_front_door()


def search_basement():
    time.sleep(2)
    print("\nDetermined to uncover more secrets, you continue searching the basement for hidden treasures.")
    time.sleep(2)
    print("As you explore further, you stumble upon a concealed doorway hidden behind a pile of crates.")
    time.sleep(2)
    print("Intrigued by the discovery, you cautiously approach the doorway and push it open.")
    time.sleep(2)
    print("To your astonishment, the doorway leads to a hidden chamber filled with ancient artifacts and mysterious symbols.")
    time.sleep(2)
    print("As you delve deeper into the chamber, you uncover even more secrets about the mansion's enigmatic past.")
    print("You noice you may need a book to decypher and a noise coming from the foyer. ")
    time.sleep(2)
    retreat_quietly()


def head_upstairs():
    time.sleep(2)
    print("\nYou decide to head upstairs, where you find two bedrooms.")
    time.sleep(2)
    print("As you peek into the rooms, you notice that they are decorated as children's bedrooms.")
    time.sleep(2)
    print("To your surprise, you catch a glimpse of two ghostly figures playing in the rooms.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Approach the ghostly figures and try to communicate with them.")
    print("2. Retreat back to the foyer.")
    choice = input("Enter your choice: ")
    if choice == "1":
        communicate_with_ghosts()
    elif choice == "2":
        print("You decide to retreat back to the foyer.")  # FIX ALL RETREAT BACK TO FOYER MESSGAES
        enter_front_door()


def communicate_with_ghosts():
    time.sleep(2)
    print("\nYou cautiously approach the ghostly figures, your heart racing with trepidation.")
    time.sleep(2)
    print("As you draw near, the ghostly children turn towards you, their translucent forms shimmering in the dim light.")
    time.sleep(2)
    print("One of the children extends a hand towards you, a silent invitation to join their spectral game.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Decline the invitation and search for a way out of the mansion.")
    print("2. Accept the invitation and play with the ghostly children.")
    choice = input("Enter your choice: ")
    if choice == "1":
        decline_invitation()
    elif choice == "2":
        play_with_ghosts()


def play_with_ghosts():
    time.sleep(2)
    print("\nYou accept the invitation and decide to play with the ghostly children, intrigued by the supernatural encounter.")
    time.sleep(2)
    print("As you join their spectral game, the atmosphere lightens, and the ghostly children giggle with delight.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Engage in a game of hide-and-seek with the ghostly children.")
    print("2. Participate in a spectral tea party with the ghostly children.")
    choice = input("Enter your choice: ")
    if choice == "1":
        play_hide_and_seek()
    elif choice == "2":
        have_tea_party()


def play_hide_and_seek():
    time.sleep(2)
    print("\nYou decide to suggest playing hide-and-seek, a childhood favorite, with the ghostly children.")
    time.sleep(2)
    print("Excited by the idea, the ghostly children eagerly agree, their translucent forms shimmering with anticipation.")
    time.sleep(2)
    print("You begin to count while the ghostly children vanish into the shadows, their giggles echoing faintly in the eerie silence.")
    time.sleep(2)
    print("As you search for the hidden children, the mansion's corridors seem to twist and warp around you, disorienting your senses.")
    time.sleep(2)
    print("You hear whispers in the darkness, teasing and taunting you as you navigate the haunted halls.")
    time.sleep(2)
    print("Suddenly, you catch a glimpse of movement out of the corner of your eye.")
    time.sleep(2)
    print("Your heart races as you inch closer to the source of the movement, anticipation and fear intertwining.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Continue searching for the ghostly children.")
    print("2. Retreat and try to find another way out of the mansion.")
    choice = input("Enter your choice: ")
    if choice == "1":
        continue_searching()
    elif choice == "2":
        retreat_from_hide_and_seek()


def continue_searching():
    time.sleep(2)
    print("\nYou steel yourself against the whispers and press on, determined to find the ghostly children.")
    time.sleep(2)
    print("As you navigate the twisting corridors, the mansion's malevolent presence seems to grow stronger.")
    time.sleep(2)
    print("You catch glimpses of the ghostly children darting through the shadows, their laughter echoing in the darkness.")
    time.sleep(2)
    print("Finally, after what feels like an eternity, you manage to find all the ghostly children, ending the game of hide-and-seek.")
    time.sleep(2)
    print("As a way of thanking you for playing, the ghostly children gather around you, their translucent forms shimmering in the dim light.")
    time.sleep(2)
    print("They tell you a haunting tale of how they were once like you, but they got trapped in the mansion and are now condemned to live here as ghosts.")
    time.sleep(2)
    print("You feel a chill run down your spine as their story sinks in, leaving you feeling unsettled.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Offer to help the ghostly children find peace and move on from the mansion.")
    print("2. Try to find a way to leave the mansion and forget about the ghostly encounter.")
    choice = input("Enter your choice: ")
    if choice == "1":
        offer_to_help()
    elif choice == "2":
        try_to_leave()


def offer_to_help():
    time.sleep(2)
    print("\nYou offer your help to the ghostly children, hoping to assist them in finding peace and moving on from the mansion.")
    time.sleep(2)
    print("However, the ghostly children solemnly explain that this mansion is now their home and their afterlife.")
    time.sleep(2)
    print("They express that they've come to accept their fate and do not wish for anything different.")
    time.sleep(2)
    print("Despite their refusal, the ghostly children offer you information that might help you escape from the mansion.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Force the children to accept your help, insisting that it's for their own good.")
    print("2. Accept the children's help with the hope of finding a way out of the mansion.")
    choice = input("Enter your choice: ")
    if choice == "1":
        force_help()
    elif choice == "2":
        accept_help()


def force_help():
    time.sleep(2)
    print("\nYou insist on helping the ghostly children, despite their protests, believing that it's for their own good.")
    time.sleep(2)
    print("However, your attempts to force your help upon them only worsen the atmosphere in the mansion.")
    time.sleep(2)
    print("The ghostly children's anger grows, and their once playful demeanor turns hostile.")
    time.sleep(2)
    print("In a fit of rage, they unleash their supernatural powers, trapping you within the mansion's walls forever.")
    print("\nGAME OVER")
    restart_game()

def accept_help():
    time.sleep(2)
    print("\nRecognizing the futility of forcing your help upon the ghostly children, you accept their offer of information to help you escape.")
    time.sleep(2)
    print("Grateful for their assistance, you listen attentively as they provide you with the knowledge you seek.")
    time.sleep(2)
    print("Armed with this newfound information, you embark on a journey to find the way out of the mansion.")
    time.sleep(2)
    print("With determination in your heart, you follow their guidance, inching closer to freedom with each step.")
    print("\nCongratulations! You have successfully accepted the ghostly children's help and found your way out of the haunted mansion!")
    restart_game()

def try_to_leave():
    time.sleep(2)
    print("\nFeeling unsettled by the ghostly encounter, you resolve to find a way to leave the mansion and forget about the haunting.")
    time.sleep(2)
    print("You make your way back to the mansion's entrance, your heart heavy with the weight of the encounter.")
    time.sleep(2)
    print("As you step out into the moonlit night, you try to push the memories of the ghostly children to the back of your mind.")
    time.sleep(2)
    print("But no matter how hard you try, you can't shake the feeling of unease that lingers.")
    print("\nGAME OVER")
    restart_game()

def retreat_from_hide_and_seek():
    time.sleep(2)
    print("\nFeeling overwhelmed by the whispers and the twisted corridors, you decide to retreat from the game of hide-and-seek.")
    time.sleep(2)
    print("You attempt to sneak away, your heart pounding with each cautious step.")
    time.sleep(2)
    print("But just as you turn a corner, a ghostly voice rings out behind you, 'Where are you going?'")
    time.sleep(2)
    print("You freeze in terror, realizing that the ghostly children have caught you trying to escape.")
    time.sleep(2)
    print("With a sinking feeling, you realize that there's no way out, and the darkness engulfs you.")
    print("\nGAME OVER")
    restart_game()

def have_tea_party():
    time.sleep(2)
    print("\nYou opt to have a spectral tea party with the ghostly children, intrigued by the surreal experience.")
    time.sleep(2)
    print("The ghostly children clap their hands in delight as you join them at the makeshift table.")
    time.sleep(2)
    print("As you sip imaginary tea and nibble on ethereal treats, the mansion around you fades away, replaced by a dreamlike scene.")
    time.sleep(2)
    print("You find yourself lost in a whimsical trance, the laughter of the ghostly children echoing in your ears.")
    time.sleep(2)
    print("However, as the tea party continues, you begin to feel a strange drowsiness creeping over you.")
    time.sleep(2)
    print("The world around you starts to blur, and you struggle to keep your eyes open.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Fight against the drowsiness and try to break free from the trance.")
    print("2. Surrender to the drowsiness and let the tea party consume you.")
    choice = input("Enter your choice: ")
    if choice == "1":
        fight_drowsiness()
    elif choice == "2":
        surrender_to_drowsiness()


def surrender_to_drowsiness():
    time.sleep(2)
    print("\nOverwhelmed by the drowsiness, you surrender to the trance, allowing the tea party to consume you completely.")
    time.sleep(2)
    print("As you drift into unconsciousness, the ghostly children's laughter echoes in your mind, fading into darkness.")
    time.sleep(2)
    print("You become trapped in an eternal slumber, lost to the haunting embrace of the mansion's supernatural forces.")
    print("\nGAME OVER")
    restart_game()


def fight_drowsiness():
    time.sleep(2)
    print("\nYou fight against the drowsiness, summoning all of your willpower to break free from the trance.")
    time.sleep(2)
    print("As you struggle, the ghostly children's laughter turns into sinister whispers, urging you to give in.")
    time.sleep(2)
    print("With a final burst of effort, you manage to shake off the drowsiness, breaking free from the tea party's spell.")
    time.sleep(2)
    print("You find yourself back in the mansion's main hallway, shaken but alive.")
    print("What will you do next?")
    print("\n1. Confront the ghostly children and demand answers about the mansion.")
    print("2. Search for a way to leave the mansion and escape the supernatural influences.")
    choice = input("Enter your choice: ")
    if choice == "1":
        confront_children()
    elif choice == "2":
        search_for_exit()


def confront_children():
    time.sleep(2)
    print("\nYou confront the ghostly children, demanding answers about the mansion and their haunting presence.")
    time.sleep(2)
    print("The ghostly children exchange knowing glances before revealing cryptic details about the mansion's dark history.")
    time.sleep(2)
    print("Their words chill you to the bone as they speak of ancient curses and restless spirits.")
    time.sleep(2)
    print("Determined to uncover the truth, you press them for more information, ignoring the growing sense of unease.")
    print("\nGAME OVER")
    restart_game()

def search_for_exit():
    time.sleep(2)
    print("\nFighting the drowsiness you manage to get down the hall to a bookshelf.")
    print("You notice one in particular that looks out of the ordinary.")
    print("\nIts a lever!")
    time.sleep(3)
    pull_lever()


def decline_invitation():
    time.sleep(2)
    print("\nYou decline the invitation, feeling uneasy about playing with ghostly apparitions.")
    time.sleep(2)
    print("As you turn to leave, a sudden chill fills the air, and the room darkens around you.")
    time.sleep(2)
    print("The ghostly children's playful demeanor shifts, their translucent forms contorting with anger.")
    time.sleep(2)
    print("You sense their displeasure at your refusal, and the atmosphere grows tense.")
    time.sleep(2)
    print("Before you can react, the room begins to spin, and you feel a cold grip around your wrist.")
    time.sleep(2)
    print("The ghostly children pull you into their spectral realm, their anger palpable.")
    time.sleep(2)
    print("Trapped in their otherworldly grasp, your fate becomes entwined with theirs.")
    print("\nGAME OVER")
    restart_game()

def explore_ground_floor():
    time.sleep(2)
    print("\nYou begin to explore the ground floor of the mansion.")
    print("Each room is filled with dusty furniture and cobwebs.")
    print("Suddenly, you hear footsteps coming from the next room.")
    print("What will you do?")
    time.sleep(2)
    print("\n1. Investigate the source of the footsteps.")
    print("2. Retreat back to the foyer.")
    choice = input("Enter your choice: ")
    if choice == "1":
        investigate_source_of_footsteps()
    elif choice == "2":
        print("You decide to retreat back to the foyer.")
        enter_front_door()


def investigate_source_of_footsteps():
    time.sleep(2)
    print("\nYou cautiously approach the room where you heard the footsteps.")
    print("Peering inside, you see a shadowy figure lurking in the darkness.")
    print("What will you do?")
    time.sleep(2)
    print("\n1. Confront the figure and demand answers.")
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
    time.sleep(2)
    print("\nYou summon your courage and step forward, confronting the shadowy figure.")
    print("As you draw closer, the figure's form shifts and twists,")
    print("revealing itself to be a malevolent spirit, its eyes gleaming with malice.")
    time.sleep(2)
    print("You bravely confront the shadowy figure, but as you draw near, it lunges at you with supernatural speed, enveloping you in darkness.")
    print("Your vision fades as chilling whispers surround you, marking the end of your journey in the haunted mansion.")
    print("\nGAME OVER")
    restart_game()


def retreat_quietly():
    time.sleep(2)
    print("\nAs you choose to retreat quietly you notice the door behind you has closed and locked")
    print("This causes you to be very nervous and frightened")
    time.sleep(2)
    print("\n1. Whimper out for help")
    print("2. Continue to look around for clues")
    choice = input("Enter your choice: ")
    if choice == "1":
        whimper()
    elif choice == "2":
        continue_to_look()


def continue_to_look():
    time.sleep(2)
    print("\nYou steel yourself against the rising fear and resolve to press on, searching for any sign of a way out.")
    time.sleep(2)
    print("You scour the dimly lit corridors, your footsteps echoing in the oppressive silence of the mansion.")
    time.sleep(2)
    print("After what feels like an eternity of fruitless searching, you stumble upon a dusty old bookshelf.")
    time.sleep(2)
    print("Upon closer inspection, you notice a small lever hidden amongst the books.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Pull the lever and see what happens.")
    print("2. Leave the bookshelf and continue exploring.")
    choice = input("Enter your choice: ")
    if choice == "1":
        pull_lever()
    elif choice == "2":
        continue_exploring()


def continue_exploring():
    time.sleep(2)
    print("\nYou decide to leave the bookshelf for now and continue your exploration of the mansion.")
    time.sleep(2)
    print("As you navigate the labyrinthine halls, you come across a decrepit staircase leading downwards.")
    print("Despite the ominous aura surrounding it, you're drawn to explore further, eager to uncover the mansion's secrets.")
    time.sleep(2)
    print("As you descend the stairs, the air grows colder, and a sense of dread settles over you.")
    time.sleep(2)
    print("Suddenly, the staircase gives way beneath your weight, sending you tumbling into darkness.")
    print("You land with a bone-jarring thud, your surroundings shrouded in pitch-blackness.")
    time.sleep(2)
    print("Panic sets in as you realize you're trapped in a hidden cellar, with no means of escape.")
    time.sleep(2)
    print("Your screams for help go unanswered, lost amidst the mansion's malevolent whispers.")
    print("\nGAME OVER")
    restart_game()

def pull_lever():
    time.sleep(2)
    print("\nYou cautiously reach out and pull the lever, unsure of what it might trigger.")
    time.sleep(2)
    print("To your surprise, the bookshelf creaks open, revealing a secret passage concealed behind it.")
    time.sleep(2)
    print("What will you do?")
    print("\n1. Venture into the secret passage.")
    print("2. Opt to explore elsewhere before venturing into the unknown.")
    choice = input("Enter your choice: ")
    if choice == "1":
        enter_secret_passage() #This will loop o one of the other original options
    elif choice == "2":
        continue_exploring()


def enter_secret_passage():
    time.sleep(2)
    print("\nSummoning your resolve, you step into the concealed passage, the air heavy with anticipation.")
    time.sleep(2)
    print("The passage winds its way deeper into the mansion's depths, leading you through twists and turns.")
    time.sleep(2)
    print("Emerging into a dimly illuminated chamber, you're greeted by a sight that steals your breath away.")
    time.sleep(2)
    print("Before you lies a hidden treasure trove, glittering with riches beyond imagination.")
    time.sleep(2)
    print("With a triumphant smile, you gather the treasure and make your way back to the mansion's entrance.")
    time.sleep(2)
    print("Stepping into the moonlit night, you watch as the mansion crumbles behind you, its secrets lost forever.")
    time.sleep(2)
    print("You emerge as the sole survivor, having conquered the mansion's challenges and claimed your reward.")
    print("\nCongratulations! You have successfully completed your quest and escaped the haunted mansion!")
    restart_game()

def whimper():
    time.sleep(2)
    print("\nYou can't help but let out a whimper, hoping someone will come to your aid.")
    print("Suddenly, you hear footsteps approaching from the other side of the door.")
    time.sleep(2)
    print("\n1. Call out for help.")
    print("2. Stay silent and listen.")
    choice = input("Enter your choice: ")
    if choice == "1":
        call_out_for_help()
    elif choice == "2":
        stay_silent_and_listen()


def call_out_for_help():
    time.sleep(2)
    print("\nYou call out for help to the voices outside, your voice echoing through the empty halls.")
    print("But as time passes with no response, desperation sets in.")
    time.sleep(2)
    print("You begin to imagine voices and noises, seeking comfort in illusions of rescue.")
    print("Tragically, no help arrives, and you're left to confront the terrifying reality alone.")
    time.sleep(2)
    print("You've met a grim fate within the confines of the haunted mansion.")
    print("\nGAME OVER")
    restart_game()

def stay_silent_and_listen():
    time.sleep(2)
    print("\nYou decide to stay silent and listen.")
    print("As you strain your ears, you hear faint whispers echoing through the corridors of the mansion.")
    print("The whispers seem to be guiding you, leading you deeper into the heart of the mansion.")
    time.sleep(2)
    print("You follow the whispers, your heart pounding with each step, until you reach a hidden chamber.")
    print("Inside the chamber, you find an old diary, its pages filled with cryptic writings and mysterious symbols.")
    print("As you leaf through the pages, you feel a chill run down your spine, as if the diary itself holds some dark power.")
    time.sleep(2)
    print("What will you do next?")
    print("\n1. Take the diary with you and continue exploring.")
    print("2. Leave the diary and search for another way out.")
    diary_choice = input("Enter your choice: ")
    if diary_choice == "1":
        time.sleep(2)
        print("\nYou decide to take the diary with you, feeling that it may hold the key to unlocking the mansion's secrets.")
        print("With the diary in hand, you venture further into the mansion, following the whispers.")
        time.sleep(2)
        print("As you explore, you come across a locked door with strange symbols etched into its surface.")
        print("The symbols seem to match those in the diary.")
        print("What will you do?")
        print("\n1. Use the diary to decipher the symbols and unlock the door.")
        print("2. Leave the door and search for another path.")
        door_choice = input("Enter your choice: ")

        if door_choice == "1":
            time.sleep(2)
            print("\nYou carefully study the symbols in the diary and manage to decipher the code.")
            print("With a satisfying click, the door unlocks, revealing a hidden passage.")
            time.sleep(2)
            print("What will you do next?")
            print("\n1. Walk down the hidden passage.")
            print("2. Run away screaming")
            passage_choice = input("Enter your choice: ")

            if passage_choice == "1":
                time.sleep(2)
                print("\nYou bravely step into the hidden passage, determined to uncover its secrets.")
                print("The passage twists and turns, leading you deeper into the depths of the mansion.")
                time.sleep(2)
                print("After what feels like an eternity of winding corridors and hidden chambers,")
                print("you finally come across a door bathed in an eerie glow.")
                print("As you approach the door, you feel a sense of foreboding, as if something dark awaits on the other side.")
                time.sleep(2)
                print("With a deep breath, you summon your courage and push open the door.")
                print("To your surprise, you find yourself standing in a moonlit garden, surrounded by fragrant flowers and serene beauty.")
                time.sleep(2)
                print("The ghostly whispers that led you here fade away, replaced by the gentle rustle of leaves and the distant chirping of crickets.")
                print("You realize that you've found the way out of the mansion, and with a grateful heart, you step into the garden, free at last.")
                print("\nCongratulations")
                restart_game()

            elif passage_choice == "2":
                time.sleep(2)
                print("\nAs you run away screaming the darkness swallows you.")
                time.sleep(2)
                print("Some still say they can hear you even today.")
                print("\nGAME OVER")
                restart_game()
        elif door_choice == "2":
            time.sleep(2)
            print("\nYou decide to leave the door for now and continue exploring.")
            time.sleep(2)
            print("What will you do?")
            print("\n1. Try to find more clues.")
            print("2. Head back to the foyer")
            exploration_choice = input("Enter your choice: ")

            if exploration_choice == "1":
                time.sleep(2)
                print("\nYou search for more clues, hoping to uncover a way out of the mansion.")
                print("You find that you cant seem to find your away around the place anymore")
                time.sleep(2)
                print("After on your hands and knees to find any sort of direction in the darkness")
                print("You crawl into the feet of the ghost hoping it will be over quick.")
                print("\nGAME OVER")
                restart_game()

            elif exploration_choice == "2":
                time.sleep(2)
                print("\nYou decide to head back to the foyer, feeling that you may have missed something.")
                time.sleep(2)
                print("On the way back to the foyer, you notice something different.")
                print("As you round a corner, you come face to face with a ghastly apparition, its eyes glowing with malice.")
                time.sleep(2)
                print("You freeze in terror as the apparition reaches out towards you, its chilling touch draining the warmth from your body.")
                print("In a panic, you try to flee, but it's too late.")
                print("Your vision fades as darkness envelops you, marking the end of your journey in the haunted mansion.")
                print("\nGAME OVER")
                restart_game()
    elif diary_choice == "2":
        time.sleep(2)
        print("\nYou opt to leave the diary behind, unwilling to risk the perils it may conceal.")
        time.sleep(2)
        print("But as you venture deeper into the mansion, uncertainty gnaws at you, and dread begins to take hold.")
        time.sleep(2)
        print("Suddenly, you find yourself standing before a fork in the path, unsure of which way to proceed.")
        time.sleep(2)
        print("Your sense of direction falters, and the mansion's ominous atmosphere closes in around you.")
        time.sleep(2)
        print("Trapped within its walls, your fate becomes entwined with the mansion's dark legacy.")
        print("\nGAME OVER")
        restart_game()


def ask_the_figure_who_they_are():
    time.sleep(2)
    print("\nSummoning all your courage, you call out to the shadowy figure,")
    print("demanding to know who they are and what they seek.")
    print("The figure turns slowly towards you, its eyes gleaming with malice,")
    print("and a chilling voice whispers, 'I am the keeper of this mansion's darkest secrets.'")
    time.sleep(2)
    print("What will you do next?")
    print("\n1. Ask for a trade for more information.")
    print("2. Retreat cautiously and try to find another way out.")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask_for_a_trade()
    elif choice == "2":
        retreat_cautiously()


def retreat_cautiously():
    time.sleep(2)
    print("\nFeeling overwhelmed by the eerie atmosphere and the unknown dangers lurking in the mansion,")
    print("you decide to retreat cautiously, step by step, back towards the foyer.")
    print("Every creak of the floorboards sends shivers down your spine as you navigate the dimly lit corridors.")
    print("You're keenly aware of the eerie silence, broken only by the occasional unsettling noise.")
    time.sleep(2)
    print("As you inch your way back, a sudden gust of wind extinguishes your only source of light, plunging you into darkness.")
    print("Panic sets in as you realize you've lost your sense of direction, and the mansion seems to have come alive around you.")
    time.sleep(2)
    print("In your disoriented state, you stumble and fall into a hidden pit trap, your screams echoing through the mansion's halls as darkness consumes you.")
    time.sleep(2)
    print("You've met a tragic end, another victim claimed by the haunted mansion's sinister secrets.")
    print("\nGAME OVER")
    restart_game()


def ask_for_a_trade():
    time.sleep(2)
    print("\nYou decide to take a risk and propose a trade to the ghostly figure,")
    print("offering something of value in exchange for information on how to escape the mansion.")
    print("You offer to exchange your soul for the information.")
    time.sleep(2)
    print("The ghostly figure considers your offer, its ethereal form wavering slightly.")
    print("After what feels like an eternity, it finally speaks, its voice echoing in the darkness.")
    print("Your soul is a tempting offer, it says, but I seek something more tangible.")
    print("You rack your brain for something else to offer, realizing that your soul might not be enough.")
    time.sleep(2)
    print("You could:")
    time.sleep(2)
    print("\n1. Offer a cherished possession instead.")
    print("2. Offer to perform a task for the ghostly figure.")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You try to offer your gold locket with a picture of your family in it.")
            print("The ghost is not interested in your locket. ")
            print("You could:")
            print("\n1. Offer to perform a task for the ghostly figure.")
            choice = input("Enter your choice: ")
        if choice == "1":
            perform_task()
        elif choice == "2":
            perform_task()


def perform_task():
    time.sleep(2)
    print("\nThe ghostly figure nods.")
    time.sleep(2)
    print("Deep within these walls lies an ancient locket, a token of my past life.")
    print("Retrieve it, and I shall grant you the knowledge to escape.")
    print("You could:")
    print("\n1. Accept the task and begin your search.")
    print("2. Refuse and seek another way out.")
    choice = input("Enter your choice: ")
    if choice == "1":
        accept_the_task()
    elif choice == "2":
        refuse_and_seek()


def refuse_and_seek():
    time.sleep(2)
    print("\nYou refuse the task, determined to find another way out.")
    print("But as you stand alone in the darkness,")
    print("you realize the enormity of your decision.")
    print("Without the ghost's guidance, you're lost.")
    print("Trapped forever within these haunted walls.")
    print("\nGAME OVER")
    restart_game()


def accept_the_task():
    time.sleep(2)
    print("\nYou accept the task, determined to find the ancient locket and earn your freedom.")
    print("With a nod of determination, you set off into the depths of the mansion.")
    print("After what feels like hours of searching, you finally discover the ancient locket, hidden away in a forgotten chamber.")
    time.sleep(2)
    print("With the locket in hand, you return to the ghostly figure.")
    print("As you offer the locket, the figure's form begins to shimmer,")
    time.sleep(2)
    print("and with a soft glow, it imparts the knowledge you seek.")
    print("With gratitude, the ghostly figure gestures towards the exit.")
    time.sleep(2)
    print("You step out of the mansion, finally free from its haunting confines.")
    print("\nCongratulations! You have successfully escaped the haunted mansion.")
    restart_game()



def restart_game():
    print("\nWould you like to play again?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        introduction()  # Start the game again
    elif choice == "2":
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter 1 to play again or 2 to exit.")
        restart_game()
introduction()
