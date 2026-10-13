import time
print("\033[1mVENDY WICANNY: The Game\033[0m")
time.sleep(5)
print()
print("It's another day in the year 2000.")
time.sleep(1.5)
print("13 year old best friends are at Anna's house, but all of a sudden they hear Anna's parents arguing.")
time.sleep(2)
print("They have decided to turn to witchcraft to cope with their private battles.")
time.sleep(2)
print("Collect all the items to complete their spells and meet at the greenhouse when all is gathered!")
time.sleep(2)

state = "Anna's House"
vicanny_wiccany_card = False
herbs = False
hoodie = False
hair = False
clipped_nail = False
prepped_ritual = False
twisted_hair = False

while True:
    if state == "Anna's House":
        print("LOCATION: ANNA's ROOM")
        print(r"""Maya and Anna are watching a movie at Anna's house until they hear arguing coming from another area of the house.
        Going to the where her parent's are arguing, they both get overwhelmed and run outside.

        Option 1: Run to the Forest nearby Anna's house
        Option 2: Stay""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "option 1" or action == "run":
            state = "Forest"
        elif action == "option 2" or action == "2" or action == "stay":
            print("They just kept hearing the arguing, so they ran to the forest anyway")
            state = "Forest"
        pass
    elif state == "Forest":
        print(r"""Maya and Anna start acting like witches at the forest and they are climbing a tree.""")
        if not vicanny_wiccany_card:
            print(r"""Anna spots a paper in the tree while climbing. They both freak out.
            Maya: "Why is there fricking paper in the tree?!"
            Anna: "Because paper comes from trees you nut."
            Option 1: Inspect the paper
            Option 2: Go to Anna's front yard""")
        else:
            print(r"""
            Option 1: Go to Anna's front yard""")
        action = input("What are you going to do? ").lower()
        if not vicanny_wiccany_card:
            if action == "1" or action == "option 1" or action == "inspect":
                print(r"""It's a buiness card for a woman named 'Wendy Rochelle Vicanny'.
            Anna says how in Germany they sa W's instead of V's.
            They both come to the conclusion that Mother Witch 'Wicanny' left this card as a sign that witchcraft is real.""")
                vicanny_wiccany_card = True
            elif action == "2" or action == "option 2" or action == "anna's front yard" or action == "yard" or action == "front yard":
                state = "Anna's front Yard"
        else:
            if action == "1" or action == "option 1" or action == "anna's front yard" or action == "yard" or action == "front yard" or action == "go to anna's front yard":
                state = "Anna's front Yard"
        pass
    elif state == "Anna's front Yard":
        print("LOCATION: ANNA's FRONT YARD")
        print("In class, Anna had decided to do an 'I never loved him' spell on Alex.")
        if not herbs:
            print(r"""Anna's spellbook specified for FIVE different herbs: lovage, rose petal, rosemary, violet, and yarrow.

            SOLVE THIS PUZZLE TO OBTAIN THE HERBS

            Type the 5 herbs in a certain order, separated by a double space between each herb (hint: alphabetical) """)
            puzzle = input("Your Answer:").lower()
            if puzzle == "lovage  rose petal  rosemary  violet  yarrow":
                print("You solved the puzzle. You obtained the five herbs for the spell.")
                herbs = True
            else:
                print("Wrong. Try again.")
                continue
        print(r"""
                Option 1: Go to English class
                Option 2: Go back to the forest""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "english" or action == "option 1" or action == "class" or action == "english class":
            state = "English Class"
        elif action == "2" or action == "option 2" or action == "forest":
            state = "Forest"
        pass
    elif state == "English Class":
        print("LOCATION: ENGLISH CLASS")
        print(r"""In class, a kid calls Maya and Anna something inappropriate, Maya tries casting a spell, but Anna catches it with her bare hands.
            Anna warns Maya that they have a limited amount of spells, then Alex and Brandt walk into the class.""")
        if not hair:
            print("Option 1 (for Maya): Secretly pluck hair from Brandt's head while sitting behind him")
        if not hoodie:
            print("Option 2 (for Anna): Wait for Alex to leave his seat and swipe his hoodie off his chair")
        print("Option 3: Go to School Hallway")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "pluck" or action == "pluck hair" or action == "option 1" and not hair:
            print("Maya plucks hair from her own head and quietly plucks a strand from Brandt's head.")
            hair = True
        elif action == "2" or action == "hoodie" or action == "option 2" or action == "swipe hoodie" and not hoodie:
            print("Alex gets up from his desk. Anna quickly swipes his hoodie off the back of his chair.")
            hoodie = True
        elif action == "3" or action == "hallway" or action == "option 3" or action == "go to school hallway":
            state = "School Hallway"
        pass
    elif state == "School Hallway":
        print("LOCATION: SCHOOL HALLWAY")
        print("Maya is at the lockers in the school hallway")
        if not twisted_hair:
            print(r"""
                  Option 1: Put it into the locker
                  Option 2: Go to English Class
                  Option 3: Go to School Stairway""")
        else:
            print(r"""
                  Option 2: Go to English Class
                  Option 3: Go to School Stairway""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "locker" or action == "option 1" and not twisted_hair:
            if hair:
                print("Maya licks the strands, twists them tightly together, and shoves them inside Brandt's locker")
                twisted_hair = True
            else:
                print("Maya needs to pluck hair from Brandt in English Class first")
        elif action == "2" or action == "english" or action == "option 2":
            state = "English Class"
        elif action == "3" or action == "stairway" or action == "option 3":
            state = "School Stairway"
        pass
    elif state == "School Stairway":
        print("LOCATION: SCHOOL STAIRWAY")
        print(r"""Maya ties a lover's lace in a devil's knot beside the stairwell in a corner.
        As a girl walks by, Maya aggressively hisses at her"
        Option 1: Go to Social Class to clip a virgin's fingernail
        Option 2: Go back to English Class""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "option 1"or action == "social" or action == "social class":
            state = "Social Class"
        elif action == "2" or action == "option 2" or action == "english" or action == "english class":
            state = "English Class"
        pass
    elif state == "Social Class":
        print("LOCATION: SOCIAL CLASS")
        print("Anna needs the fingernails of a weak virgin for her spell. Terra is sitting beside her.")
        if not clipped_nail:
            print(r"""
            Option 1: Ask Terra to clip her nails
            Option 2: Go to Maya's room
            Option 3: Go back to School Stairway""")
        else:
            print(r"""
            Option 2: Go to Maya's room
            Option 3: Go back to School Stairway""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "option 1" or action == "clip" or action == "ask terra" and not clipped_nail:
            print("Terra says no, So under the table, Anna quietly clips her own fingernails instead :P")
            clipped_nail = True
        elif action == "2" or action == "option 2" or action == "maya's room" or action == "mayas room":
            state = "Maya's room"
        elif action == "3" or action == "option 3" or action == "stairway" or action == "school stairway":
            state = "School Stairway"
        pass
    elif state == "Maya's room":
        print("LOCATION: MAYA'S ROOM")
        print(r"""Maya calls Anna asking if Vendy Wiccany requires a Brandt doll. Anna says no.
        Maya rips a chunk of her own hair off anyway, attaches it to her Brandt doll, and plays house in her fort.
        Option 1: Go to School Greenhouse
        Option 2: Go back to Social Class""")
        action = input("What are you going to do? ").lower()
        if action == "1" or action == "option 1" or action == "greenhouse" or action == "school greenhouse":
            state = "School Greenhouse"
        elif action == "2" or action == "option 2" or action == "social" or action == "social class":
            state = "Social Class"
        pass
    elif state == "School Greenhouse":
        print("LOCATION: GREENHOUSE")
        print("The sun is at 176 degrees North and it's almost high noon. meaning they have got to start now.")
        if vicanny_wiccany_card and herbs and hoodie and twisted_hair and clipped_nail:
            print(r"""Anna whispers: 'She's here...'
            Maya and Anna begin chanting 'Vendy Rochelle Wiccany' around their ritual/spell items.
            Some kids peek through the opening of the greenhouse, get creeped out, and go call the principal.
            Maya sees them and shouts 'STAY OUT WEAKLINGS' and Anna threatens to hex them.
            Maya screams 'SHILAYLAY PUMPANO' like a crazy woman right as the principal walks in"
            Option 1: Go to Front of School""")
            prepped_ritual = True
            action = input("What are you going to do? ").lower()
            if action == "1" or action == "option 1" or action == "front of school":
                state = "School Front"
        else:
            print("Maya and Anna can't complete their ritual because they are missing items. Go back and collect all items first.")
            print("Option 1: Return to Maya's room")
            action = input("What are you going to do? ").lower()
            if action == "1" or action == "option 1" or action == "return" or action == "maya's room":
                state = "Maya's room"
        pass
    elif state == "School Front":
        print("LOCATION: FRONT OF SCHOOL (pick up/drop off area)")
        print(r"""Maya and Anna sit on the stairs with their stuff. Alex walks by.
        Anna says she loves Alex less, but it still hurts.
        Brandt rides by on his bike. Maya goes up to him and says wazzup.
        Brandt scoffs and tells Maya to stop following him, stop talking to him, and stop putting her hair in his locker.""")
        time.sleep(1.5)
        print(r"""Later that evening, Anna's parents officially break up. Maya sneaks out of her house after her brother Shuji calls her a brat.
        Maya meets Anna in the forest at night for one last ritual with all their spell items.
        Anna cries in Maya's lap. Maya holds her and comforts her, letting her know that Anna is her family and she will always love her.""")
        time.sleep(1.5)
        print("GAME COMPLETED.")
        break