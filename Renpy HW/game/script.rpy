# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Detective")
define d2 = Character("Detective 2")
define p = Character("Player")

image bg gray = "gray background.png"
image bg brown = "brown background.png"

image detective = "detective.png"
image detective2 = "detective2.png"


# The game starts here.

label start:

    scene gray background

    show detective

    "You are sitting in a bare, gray room, face to face with a detective."

    "Your memory is hazy, like you just woke up in this room. You remember seeing Jake a few nights ago, before he was reported missing."

    "You are here for \"basic questioning\" but know you are suspected of something. As far as you know, nobody has seen Jake for the last few days."

    d "So how close were you to him, before he went missing? Any conflict? Any disagreements?"

    menu:
        "We were great friends. I don't remember having any conflict near that time.":

            jump no_conflict
        "We were great friends but we had a disgreement the day before.":
            jump conflict


    return
    

    
label no_conflict:

    "The detective smiles."
    

    d "Really? When we spoke to your friend they said you had a fight the night before."

    menu:
        "Seriously, why am I being interrogated right now?":
            d "So this feels like an interrogation? Why's that?"
                
            "..."

            
            
            jump start_two

        "I don't know what you're talking about.":
            d "I have text messages the prove you do."
            
            "..."
            jump start_two
            
    return

    


label conflict:

    "What was the conflict about?"

    menu:
        "It was about money stuff. Nothing important.":
            d "Money stuff can be quite important, though."

            jump start_two

        "Haven't you spoken to my friend already? He must've told you what happened.":
            "We have. We want to hear your side of the story, too."

            jump backstory



    return


label start_two:

    scene brown background

    show detective2

    "You are sitting in a lamplit, brown room, face to face with a detective."

    "You implicated yourself last time. You will be given another chance, but they are limited."

    d2 "So far we've only spoken to your friend."

    d2 "So how close were you to Jake, before he went missing? Any conflict? Any disagreements?"

    "You must piece together your story and learn when you can lie, and when you can't." 
    
    "Your memory is powerful. As you piece together your story the world around you will change, morphing to the story you discover. These changes are no coincidence, they will give you the clues necessary to get out of the interrogation free."

    menu:
        "We were great friends. I don't remember having any conflict near that time.":
            "Got it."
            jump no_conflict
        "We were great friends but had a disgreement the day before.":
            "interesting."
            jump conflict
    

    return

    # This ends the game.



label backstory_gray:
    menu:
        "Well what did my friend tell you?":
            d "I'm happy to tell you but if we share information with you, you need to share it with us."
            jump backstory_gray_continued

label backstory_gray_continued:
    menu:
        "Makes sense to me.":

            d "Your friend said they left Jake's house at 11pm, while you and Jake were having an argument about your ex-girlfriend."

        "I don't feel like cooperating.":

            d "This doesn't help you progress the story at all. I'm sending you straight to the slammer. We know what you did!"

    menu:

        "I can't speak to the exact my friend left. All I know is I left 15 minutes after they did.":
            d "You are aware that Jake hasn't been seen since then?"

            jump fifteen

        "11 pm is about right. I left right after my friend.":

            jump right_after



label fifteen:

    "I'm sorry this is incomplete. Currently trying to think of something sophisticated that engages with the mind games of an interrogation (and also how to get the player to interact)"

label right_after:









        

        


    







    
