# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image shadow_overlay = "images/shadow_overlay.png"
transform yandere:
    # Define the animation: move to a zoom level of 5.0 (500%) over 2 seconds with easing
    ease 20 zoom 3.0
    linear 0.1 xoffset -30 yoffset 30 # Move left and up
    linear 0.1 xoffset 30 yoffset -30 # Move right and down
    linear 0.1 xoffset -30 yoffset -30 # Move left and down
    linear 0.1 xoffset 30 yoffset 30 # Move right and up
    repeat 

transform normal_size:
    ease 2.0 zoom 1.0
screen disable_input():
    # Makes it impossible to click through
        key "dismiss" action NullAction() 
    # Optional: Block right click/menu
        key "game_menu" action NullAction() 
    # Makes the whole screen an invisible button
        button:
            xfill True
            yfill True
            action NullAction()
transform shake_eyes:
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset 2 yoffset 2
    repeat 3 # Shakes for a few cycles
    xoffset 0 yoffset 0 # Returns to normal
#image character_eyes_shaking:
    #"images/eyes_open.png"
    #pause 0.5
    #shake_eyes
    #"images/eyes_closed.png"
    #pause 0.2
    #repeat
define p = Character("[povname]")
transform small_sprite:
    zoom 0.4 # Reduces 2000x3000 to 800x1200
    xalign 0.5
    yalign 0.2

transform continuous_shake:
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 3 yoffset -3
    linear 0.05 xoffset 2 yoffset -2
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat
define f = Character("Fai")
define n = Character("???")
define g = Character ("Gwi-Chan")
default fai_points = 0
default affection_points = 0
define config.menu_include_disabled = True


# The game starts here.

label start:
    stop music
    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "[povname]"
    p "My name is [povname]."
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    play music someonesvoicebgm loop

    "..."

    "Whats.. happening..,?"

    "It feels like im falling."

    show floating eyes at continuous_shake

    "I feel watched, like i'm the prey being glared at by a hungry wolf pack."

    "And i dont know why."

    "Yesterday was just a normal day, and now i think im...."

    "I think i'm dead."

    "Is this really the end for me? Is there a way out now from death?"

    "But why... What did i do to deserve this?"

    "I think this isn't so bad... Its quite relaxing..."

    n "Yahoo~ is anyone alive? Any heartbeat? Knock Knock!"

    "!!"

    n "There you are! Fai had been wondering until when you would wake up. Fai has been worried sick. Kekeke~"

    stop music

    play sound wake 

    scene bg white

    with fade

    show fai normal at small_sprite

    "You awoke in a strange, eye blinding void of some sorts, with a happy peculiar looking Jester in front of you"

    "He appeared to be eating... pancakes?"

    play music goofy_clown

    n "Welcome, welcome, we-lcome~"

    "He happily greeted you as if you've known him your whole life."

    f "Long story short: you're dead! POOF! Gone! stuck with me, your favourite handsome jester, Fai, forever and ever and ever! Kekeke~"

    show fai normal4 with dissolve

    f "Fufufu~ Gosh, aren't you excited?? No more boring repetitive human life, just me and you together eternally~"

    show fai glad with dissolve

    "Is this guy crazy? What the fuck is happening?!"

    menu:
        "Are you holding pancakes? Those look delicious!":
            $ affection_points += 5

            show fai crazylove2 with dissolve

            f "WOWW!! Human, do you love pancakes too?!"

            show fai gladopen with dissolve

            f "Nobody loves pancakes more than the magnificent Fai!"

            show fai glad with dissolve

            "He feeds you a little bit of his pancakes"

            show fai normal3 with dissolve

            f "Hum hum! You are really worth keeping, human~"


        "M-monster! W-what are you!?":
            $ fai_points += 3

            show fai pout
            "He rolls his eyes at you, unamused."

            f "Rude. Youre no fun, little human."

            f "Fai is no monster, Fai is your entertainment!"

        "Fai? Is that your name? I like your name, weird jester.":
            $ affection_points += 2

            show fai suprised with dissolve

            "Fai's eyes lit up as you spoke. He seemed to like that."

            show fai glad with dissolve
            
            f "Wow! You like my name?! Fai feels so... tingly inside~"

            show fai gladopen with dissolve

            f "Like something is about to pop... like a balloon!"

            show fai normal1 with dissolve

            f "Well anyways, Human!"

            jump introduction

label introduction:
    stop music

    "He finishes his pancakes, and stood dramatically posing to you."

    show screen disable_input

    play audio drumroll

    "{cps=10} Drumroll pleaaasee....{w=5.0}{nw}"

    scene bg black

    play music astrangeclownappearsbgm loop fadein 2.0

    scene fai_intro

    play audio partyhorn

    hide screen disable_input

    "A odd stage randomly appeared before you, with a unknown source of light coming from above."

    p "Wait where did that light come fro- {nw}"

    f "Greetings little human!"

    f "Youre in the presence of my fantastic void, where anything i want to happen, will happen!"

    f "No more same-same boring expendable human mortal life... Now you belong to FAI!!!, the greatest jester to ever exist~"

    "Well he's not wrong. Life did suck working a minimum wage."

    play audio clapping

    ""
    f "Yes!!! Thank you, thank you~"

    p "WHERE DID THE CLAPPING COME FROM-{nw}"

    scene bg white

    show fai pout at small_sprite

    f "AHEEEMMMM!!! YOU DO NOT QUESTION THE WAYS OF THE JESTER."

    p "Yes sir..."

    show fai normal with dissolve

    "Even though this crazy jester took me here i still think..."

    "..Maybe this wont be so bad after all?"

    show fai gladopen with dissolve

    "He helped you up, twirling you around happily."

    "That made you feel..a little dizzy..."

    "?"

    show fai glad with dissolve

    "How weird... It doesn't look like he wants to kill me..."

    "Why did this weird jester take me here? I have.. so many questions..."

    "Hmmm... why not ask him a few?"

    show fai suprised with dissolve

    p "Sir Fai, why do you stay in this void?"

    show fai offended with dissolve

    "He frowns a little, looking quite uncomfortable to awnser such a question."

    f "You dont need to know."

    p "..."

    p "...."

    "I really shouldnt get into Fai's business..."

    show fai normal1 with dissolve

    f "Well, ahem! anyway little human, its time for a proper introduction at last!"

    show fai gladopen with dissolve

    f "My name is Fai! As you can tell, Fai is a cute jester demon~"

    show fai crazylove2

    f "your jester demon <3 {nw}"

    show fai normal4
    
    f "The cutest and most handsome demon jester you'll ever witness~"

    "He snaps his fingers, and a cute ghost blob appears"

    show gwi gwi at right

    "The ghost looks at you curiously, happy to see you for some reason"
    
    f "This is Fai's companion, Gwi gwi!"

    p "Oh, hello there little ghost."

    play audio gwi

    g "Gwi!!"

    hide gwi gwi with fade

    show fai dissapointed1 with dissolve

    p "Well.. um.. my name is- {nw}"

    show fai gladopen with dissolve

    f "Oh, Fai already know everything about you, [povname]. Dont even bother introducing yourself, Kekeke."

    p "Wait- how do you know my name?!"

    show fai cheeky with dissolve

    f "Fai know's everything about anything around here. "

    show fai crazylove with dissolve

    f "I especially know everything about you, fleshy human~"

    show fai cheeky3 with dissolve

    "Is this guy insane?! How is he playing that off like thats normal?!"

    p "Well Fai,"

    menu:
        "How do you look so artificial? You look really cool.":
            $ affection_points += 2

            show fai suprised with dissolve

            "Fai seemed amused with that awnser, his tail starting to wag slightly"

            show fai normal1 with dissolve

            f "Wow human~ Fai cannot keep up with your nice words~"

            show fai suprised with dissolve

            f "My form is made up of my shadows, you see~"

            f "Shadows cannot have colors, isn't that right?"

            p "Interesting..."

        "This isnt funny, I want to see my family again.":
            $ fai_points += 2

            show fai pout with dissolve

            "Fai scoffs, clearly annoyed at your response. He didnt seem to like that one bit."

            f "Family!! Family!! What a LOOAD of bullcrap!"

            show fai gladopen with dissolve

            f "After all, my dear"

            show fai cheeky with dissolve

            f "Why have a family when you have Fai?~"

            show fai normal3 with dissolve

            f "Don't expect to ever see them again~"

label badend:
    if fai_points >= 5:
        stop music
        show fai dissapointed with dissolve
        f "..."

        f "You know what? Youre really pissing me off now."

        play audio grab

        "He grabs you with his tail and holds tight onto your body."

        play music tension

        show fai cheeky with dissolve

        f "What should i do to you now, hm?"

        show fai crazylove with dissolve

        f "Hmmm... I know! I know exactly how to fix your fragile, little rotten soul."

        "You start to try to flee from Fai's grasp."

        p "What- What is this?! Let me go!-"

        show fai cheeky with dissolve

        f "I can make you better for me."
        
        "You struggle and struggle. He looks at you, enjoying the view."

        show fai crazylove2 with dissolve

        f "Its so delicious to see you try and try to escape your fate."

        show fai cheeky2 with dissolve

        f "How selfish is it... To choose this path, yet try to hard to escape it?"

        show fai cheeky with dissolve
        
        "Fai waits and waits until you are completely exausted."

        show fai normal3 with dissolve

        p "Haa... Haa..."

        show fai pensiveopen with dissolve

        f "You done? Good~"

        show fai shy4 with dissolve

        "Fai uses mystical unknown powers on your body"

        "You are too powerless to do anything."

        "Fai turns you into a porcelain doll, and all you could do was watch him do that, bit by bit."

        "Your soul is trapped inside it forever."

        show fai pensive with dissolve

        "He picks your body up unempathetically."

        f "What a pity."

        f "I almost fell for it, didn't i?"

        stop music

        show fai cheeky with dissolve

        f "But alas,"

        f "{cps=30}You were the one that chose your fate~" 

        "BAD END - Doomed From the Start"

        return
    
label choice:

    show fai pensive with dissolve
    "Fai thinks for a moment. Then looks at you, crossing his arms."

    stop music

    show fai gladopen with dissolve

    f "Fine! I believe Fai can propose a compromise to human."

    scene fai_choice with fade

    "He holds three cards before you out of thin air, one a king, one a queen and one a jack."

    f "Fai wants to entertain human, so Fai will bless human with Fai's magnificence!"

    f "Fai also understands human, human needs to get used to your new life here in the afterlife~"

    f "I'll let you pick a card~ Choose wisely, human."

    "I really shouldnt get on his bad side."

    "I think i should choose carefully..."

    menu:

            "NOT AVAILABLE King (Carnival)" if False:
                pass

            "NOT AVAILABLE Queen (Restaurant)" if False:
                pass

            "Jack (Stargazing)":

                jump stargazing

label carnival:

    f "Wonderful choice! Fai will create a wonderful carnival for you~"

label restaurant:

    f "Wonderful choice! Fai will make a restaurant for you~"

label stargazing:

    scene bg white with fade

    show fai gladopen at small_sprite

    f "Wonderful choice~ Fai will create a beautiful scene of stars for you~"

    stop music

    scene stargazing

    play music stargazing fadein 3.0

    with fade

    show fai suprised at small_sprite

    show shadow_overlay zorder 100

    "The enviroment around you changes, youre on top of a big mountain in the clouds with no bottom in sight."

    "The sky is beautiful, its filled with thousands of different types of constellations and stars."
    
    p "Wow, Fai.. This is.."
    
    show fai normal4 with dissolve

    f "I know right? Fai knows what humans enjoy~"

    show fai normal with dissolve

    "Fai spawns a picnic infront of you two, and offers you a sandwich."

    show fai gladopen with dissolve

    f "Fai prepared this delicious human tasting sandwich! Try it~"

    show fai glad with dissolve

    "Should i really trust this guy? We just met..."

    "I think im going to..."

    menu:
        "Accept the sandwich":
            $ affection_points += 1

            "You took the sandwich, still uneasy about it having something bad inside of it or something."

            p "Thank you, Fai."

        "Sorry, im not hungry...":
            $ fai_points += 2

            show fai offended with dissolve

            "For a moment, he looked genuinely upset at your refusal, then put the sandwich down on the picnic towel."

            show fai pout with dissolve

            f "It's not like Fai wanted you to eat it.. i guess..."

        "Feed me the sandwitch!":
            $ affection_points += 2

            show fai dissapointed1 with dissolve

            f "You want Fai to.. Place this food in your mouth?"

            "You nodded happily"

            show fai shy with dissolve

            "Fai blushed, a little taken aback from your proposal"

            show fai gladopen with dissolve

            f "Well, sure then human, if thats what you want from Fai, i will grant your wish~"

            show fai shy3 with dissolve

            "Fai places the sandwitch in your mouth, admiring your looks for a moment as you chew on it."

            show fai gladopen with dissolve

            f "Youre so interesting, little human."
    show fai suprised with dissolve
    
    "Fai paused for a minute then looks up to the sky."

    f "Wooowwza~ Look, [povname]!"

    scene meteors

    "You looked up too, and you couldnt believe your eyes."

    "It was a beautiful meteor shower, right up in the sky."

    p "Its.. beautiful."

    "You two lay together on the ground, admiring what you see."

    "Maybe Fai isn't so bad..."

    scene stargazing

    show fai glad at small_sprite

    show shadow_overlay zorder 100



    menu:
        "Hold Fai's hand":
            $ affection_points += 3
            show fai shy2 with dissolve

            f "[povname]? What are you.."
            "He instintively looked at you confused at your move."

            show fai glad with dissolve

            "Fai chuckled nervously, but doesnt dare to pull away from you."

            show fai gladopen with dissolve

            f "Kekeke.. Youre funny, human."

            show fai shy3 with dissolve

            "Fai tightens his grip onto your hand, smiling at you."
            

            if affection_points >= 8:

                show fai shy3 with dissolve 

                f "Fai has never met such a interesting human such as you, my dear."

                p "Oh, wow.. i.. um-"

                show fai shy with dissolve

                "Your face went tomato red without noticing."

                show fai gladopen with dissolve

                "He chuckled at your flustered face."

                f "Haha! Just look at your face!"

                show fai pensiveopen with dissolve

                f "I just love that about you."

                show fai crazylove2 with dissolve

                f "Your face, your body..."

                f "Your eyes."

                show fai cheeky3 with dissolve

                "Hes.. Not talking in third person..?"

                show fai shy3 with dissolve

                "Fai started staring deeply into your eyes, captivated by you."
                
                "He held your hand firmly, confident about what he had said."

                show fai normal4 with dissolve

                f "It feels like you were made for me."

                show fai gladopen with dissolve

                "He laughs, circuling his thumb on yours"

                show fai shy with dissolve

                play audio shy

                f "!!"

                show fai shy2 with dissolve

                f "Ahhhh. Sorry, its rude to stare, isn't it?"

                "He looked away, blushing pretty hard."

                show fai shy3 with dissolve

                f "Ahem well, anyway my dear..."

        "Stay still":  
            show fai pensive with dissolve

            "You stood there, gazing at the sky."

            show fai shy3 with dissolve

            "You also noticed Fai staring at you, almost creepily."

            "Its freaking you out. I think he noticed."

            show fai pensivecheeky with dissolve

            "Fai freakishly gave you a wide grin."

            show fai pensiveopen with dissolve 

            f "Fai loves that face you make when you're scared~"
    
    show fai suprised with dissolve

    "A big meteor passed through the sky."

    show fai gladopen with dissolve

    f "Make a wish, [povname]!"

    show fai shy3 with dissolve

    "Fai looks at you curiously"

    "You decide to play along, wishing for your dreams to come true."

    show fai pensiveopen with dissolve

    f "Fai made his wish already~"

    p "Really? What did you wish for?"

    show fai gladopen with dissolve

    f "Of course Fai cannot tell you his wish! That would be cheating~"

    p "Fair enough."

    show fai glad with dissolve

    if affection_points >= 7:

        show fai crazylove2 with dissolve

        f "...But my wish does involve you."

        show fai shy3 with dissolve

        "You felt a pink tint around your cheeks and you felt a little shy."

        p "Wait- Really?"

        show fai shy with dissolve

        p "But i just met you, Fai..."

        show fai pensiveopen with dissolve

        "He looks at you, then chuckles."

        show fai shy3 with dissolve

        f "So what?? I love my little human so much."

label newroom:

    show fai suprised with dissolve

    "The last meteors fade into the vast night sky."

    show fai glad with dissolve
    
    "Fai took a deep breath, he looks pretty happy."

    f "Ahh~ refreshing, isn't it?~"

    f "Time to go back, my dear."

    f "Dont be upset it ended, Fai can take you to watch the stars again anytime you desire!"

    "Fai sits up, stretching his body lazily, then suddenly the whole scene changes."

    stop music

    "That beautiful scenery you just saw melted away, just like that."

    "You're back in the void, where you were before."

    scene bg white

    with fade

    show fai gladopen at small_sprite

    f "Ah! That was great, wasn't it, [povname]?~"

    menu:
        "Yeah! It was pretty good, Fai.":
            show fai crazylove2 with dissolve
            "He seemed pretty happy."
            show fai shy3 with dissolve
            f "Fai agrees with you, my dear~."
        "Yeah, but i think you were the best part.":
            $ affection_points += 3

            show fai shy with dissolve
            "Fai visibly seemed shy, but then transformed his feelings into something more.. freaky?"

            show fai pensiveopen with dissolve

            f "Hmmm~ Well i am pretty magnificent~"

            show fai pensivecheeky with dissolve

            f "Though Fai must admit, your hair smelled pretty good back there, [povname]~"

            show fai glad with dissolve

            "!!"
            "Maybe a little.. TOO freaky.."

        "It was.. okay.":
            $ fai_points += 4

            show fai pout with dissolve

            "He pouts like a child, annoyed at your words."

            show fai offended with dissolve

            f "Psh, as if i wasn't the best jester around..."
    
    show fai suprised with dissolve

    f "Thats right, Fai forgot to show you something!"

    scene portal

    "Fai opens a portal to a peculiar room of sorts."

    scene room_lightson

    with fade

    show fai gladopen at small_sprite
    transform add_blend:
        blend "add"
        alpha 0.6

    f "This is your room from now on! What does my cute human think, hmm hmm?"

    "Its very cute.. Fai really does know what i like."

    show fai normal with dissolve

    p "Thank you Fai, you must've put a lot of effort in this, right?"

    show fai pensiveopen with dissolve

    f "Hahah~ Yes, Fai took lots of time making it to your tastes~ you love it don't you, my dear?~"

    menu:
        "Its great, just how i like it!":
            f "Thats great to hear, my little human~"
        "Wow, its nice, i guess.":
            f "Thats great to hear, my little human~"
        "Its creepy. Why are you so creepy...":
            $ fai_points += 3
            show fai offended with dissolve

            f "Me? Im not creepy. You just dont have good taste, hmph."

            show fai pout with dissolve

            f "Human is so ungrateful for what Fai does for you~"

    show fai glad with dissolve

    "Fai holds you up, then plops you gently on your new bed."

    show fai normal3 with dissolve

    f "Sleeping isnt necessary in this void, but its good to have some rest from time to time, isnt it my cute fleshy human?~"

    show fai normal with dissolve

    "Fai kisses your forehead, then tucks you into bed, making sure you're okay."

    show fai gladopen with dissolve

    f "Sweet dreams, my love~"

    menu:
        "Wait, Im scared to go to sleep alone, Could you sleep with me...?":
            show fai suprised with dissolve
            f "Oh? Human wants to sleep with little old me?"
            show fai pensive with dissolve
            "He contemplates it, thinking of a response, pretty stunned."
            if affection_points >= 10:
                jump bedtogether
            else:
                show fai shy3 with dissolve
                f "Mmmm~ Its really tempting but not today, my dear~"
                show fai gladopen with dissolve
                f "Maybe if you sweeter earlier i would have reconsidered~ Have good dreams now little human~"
                jump sleepingending

        "Good night, Fai.":
            jump sleepingending
        "...":
            jump sleepingending
label sleepingending:
    scene bg black
    "He pets you one last time, then leaves you to rest."
    "..."
    "...."
    play audio door
    "Fai opened the door.{w=5.0}"
    show fai dissapointed at small_sprite
    if fai_points >=10:
        f "I've decided i dont want to keep you."
        f "Filthy rotten human."
        f "Nighty night~"
        "Fai decided he has had enough of you."
        "He goes up to your bed menacingly."
        f "I'll show you what happens when you mess with me."
        "He made you slumber for all eternity against your will."
        "You dont mean anything to Fai anymore, and so he found someone better than you."
        "Maybe you shouldn't try pissing him off next time?"
        "BAD END 2 - Eternal Slumber"
        return
    transform multiply_blend:
        blend "multiply"
    scene bg room1
    show screen disable_input
    play music horror_bgm fadein 5.0
    play sound slow_heartbeat
    show fai crazylove at small_sprite
    show shadow_overlay1 at multiply_blend
    f "{cps=10}Oh... my dear~ {w=5.0}{nw}" 
    f "{cps=10}You look so beautiful when you sleep~ {w=5.0}{nw}" 
    stop sound
    play sound normal_heartbeat
    show fai cheeky with dissolve
    f "{cps=10}So vulnerable... Like i could kill you right now and you would still wouldnt know~ {w=5.0}{nw}"  
    f "{cps=10}Oh~ im just so EXCITED to see what awaits us, little human~ {w=5.0}{nw}" 
    show fai gladopen with dissolve
    f "{cps=10}I love you. {w=1.0}{nw}" 
    stop sound
    play sound fast_heartbeat
    show fai crazylove2 at yandere
    f "{cps=10}I love you I love you I love you I love you {cps=20}I love you I love you {cps=70} I love you I love you {cps=90}I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you{w=8.0}{nw}" 
    window hide
    scene static
    play audio static volume 1.0
    image yandere cutscene = Movie(play="images/cutscene.webm", side_mask=False)
    show yandere cutscene
    f "{cps=10}LOVE ME {nw}{w=0.8}"
    stop sound8
    stop music
    $ renpy.quit()
label bedtogether:
    show fai glad with dissolve

    f "Sure~ Fai would love to lay a while with [povname]~"



    "He removes his jester clothes, changing into very comfortable-looking pajamas."
    
    "Fai then puts himself in the covers with you, snuggling up to you gleefully, purring like a little cat."

    f "Human's bed is so comfy~"

    "Hmm.. what should i do now..."
    menu:
        "Could i pet your hair?":
            $ affection_points += 2
            show fai shy
            "He looks at you, blushing at your request."
    
            f "My hair..? Mmmhh.."
    
            f "Go ahead human, why not~"
    
            "His hair is exceptionally soft and smooth, like he had just washed it."

            "Fai whimpers slightly the moment your hand meets his cotton-candy like hair."

            p "How did you make your hair so soft and fluffy? It feels amazing to touch!"

            "Fai looked at you, grinning with his menacing smile."

            f "I keep it nice and tidy for little cute humans who want to touch it~ Kekeke~"

            "Fai puts his head into your hands, leaning into your touch."

            "You stopped petting him, then he smiles at you."

            f "It did feel reaally good though~ Thanks, human~"

        "Could i touch your horns? (Suggestive)":
            $ affection_points += 10
            show fai shy2 with dissolve
            f "My... Horns?"
            show fai shy with dissolve
            "His face, for a moment, started blushing a slight gray."
            show fai shy4 with dissolve

            f "You dont understand demon anatomy, do you?"

            "You didnt understand what Fai meant, in fact, you were quite curious to know."

            p "What do you mean, Fai?"

            "He nervously chuckled, then dismissed your question."
            
            f "Ahh.. dont worry about it, little human. Just touch them."

            show fai heat3 with dissolve

            "You gently touched his fairly small triangular stubby horns."

            f "Mm..-"

            show fai heat1 with dissolve

            "He instantly put his face cuddled into your chest as you touched them."

            p "Wow... This really gets you going, huh?"

            show fai heat with dissolve

            "He doesnt awnser, all he does in response is make a few sounds and purr into your chest, clearly content with your horn rubbing."

            f "Go for... as long as you want, human..."

            show fai heat1 with dissolve

            "Is Fai drooling on me...?"

            "You think you felt something wet pool onto your chest, but you are not sure."

            "After a few minutes, you decide to stop touching his horns."

            "He looks almost breathless, wow."

            show fai heat3 with dissolve

            f "Dont worry about Fai- Hah..."

            "Fai did drool on me. Sigh."

            "He looks at the stain, then he exclaims:"
 
            show fai shy2 with dissolve

            f "A-ah- Fai didnt mean to.. um..."

            f "Fai can fix that for you later! Fai promises you!"

            show fai pout with dissolve

            "I wonder what its like for demons horns to get touched... I didnt realize it was THIS sensitive..."

    # Max affection points: 3 + 2 + 2 + 3 + 3 + 4 = 17

    if affection_points >= 20:
        show fai heat1 with dissolve
        "Fai looks uneasy, like he has been holding something back this whole time."
        show fai heat with dissolve
        f "Human..."
        f "Mmh..."
        f "Mmmh..Fai..cannot take it anymore..~"
        show fai heat3 with dissolve
        f "Fai needs you. Fai needs to breathe you from the inside out."
        show fai shy3 with dissolve
        "Fai put his arm on top of your thigh."
        p "?!"
        p "(What do i do...)"
        menu:
            "Allow Fai to escalate further (Not available currently...)." if False:
                "Which genitalia do you desire?"
                menu:
                    "Female genitals.":
                        jump nsfwscenefaidick
                    "Male genitals.":
                        jump nsfwscenefaipussy
            "Maybe we should take it easy...":
                show fai pout with dissolve
                "He whines at you, annoyed."
                f "Humf, i guess its too fast. Fai will listen to your command i suppose..."
                jump fluffscene

    else:
        jump fluffscene

label nsfwscenefaidick:
    "Fai desperately went on top of you, hungry and thirsty."
    p "Fai...?"
    f "You have no idea what you have done to me, my darling...~"
    "He keeps his eyes half lidded and panting above you."
    "Fai slowly put his hands underneath your shirt, tracing your skin carefully."
    f "You have no idea what you do to me."
    f "You made me so... tingly inside earlier..."
    f "It makes me want to... do things to you."
    f "Just let me do it to you.. please~"
label nsfwscenefaipussy:
    "Fai desperately went on top of you, hungry and thirsty."
    p "Fai...?"
    f "You have no idea what you have done to me, my darling...~"
    "He keeps his eyes half lidded and panting above you."
    "Fai slowly put his hands underneath your shirt, cupping your boobs and tracing your skin carefully."
    f "You have no idea what you do to me."
    f "You made me so... tingly inside earlier..."
    f "It makes me want you to... do things to me."
    f "Just do it to me.. please~"



label fluffscene:
    show fai gladopen with dissolve
    "Fai cuddled up to you happily, he's really close to you now."
    f "Haha! You are so funny to tease, little human~"
    show fai normal with dissolve
    p "You really like me that much, huh?"
    show fai normal1 with dissolve
    f "Of course Fai does, Fai love loves you a lot."
    show fai glad with dissolve
    "He hugged your arm, nuzzling it and glorifying it"
    show fai shy4 with dissolve
    f "Oh human~ I'm so glad i can never ever lose you~"
    show fai crazylove2 with dissolve
    f "You want to stay together forever with me too, don't you?"
    menu:
        "I love you.":
            pass
        "I love you.":
            pass
        "I love you.":
            pass
    "?"
    "What? When did i say that? My mouth moved on its own..."
    show fai shy4 with dissolve
    f "Fai loves you too~ hehe~"
    show fai gladopen with dissolve
    f "Now lets sleep, my dear~"
    "You 'live' to see another day with the demon jester."
    play music distortedbgm fadein 0.5
    scene bg black
    "To be continiued - Normal ending"

label begging:
    "Hi! I am the solo dev creator kingcrib, and If you enjoyed this VN PLEEEEASE consider sharing it to your friends!"
    "I took a lot of time making it, and i will prob only update this VN once it gets some traction (doesnt have to be much, maybe 100 downloads!)"
    "Read the itch.io description for my game to know whats planned if i reach my goal :33333"
    "Thank you sm for playing."
    stop music fadeout 5
    "{w=10}"
    scene bg black






    # This ends the game.

    return
