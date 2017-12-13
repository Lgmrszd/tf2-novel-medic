# BACKGROUNDS

image spawn1 = "bg/spawn1.png"
image spawnhall1 = "bg/spawnhall1.png"

image middle1 = "bg/middle1.png"
image middle2 = "bg/middle2.png"
image middle3 = "bg/middle3.png"

image intells1 = "bg/intells1.png"
image intells2 = "bg/intells2.png"
image intells3 = "bg/intells3.png"
image intells4 = "bg/intells4.png"

image tflogo = "tflogo.png"

image movie = Movie(size=(1920,1280),  xpos=0, ypos=0, xanchor=0, yanchor=100)

# CHARACTERS

image medic0 = "chars/medic0.png"
image medic0f = im.Flip("chars/medic0.png", horizontal=True)
image demoman0 = "chars/demoman0.png"
image heavy0 = "chars/heavy0.png"
image heavygibus = "chars/heavygibus.png"
image spy0 = "chars/spy0.png"
image pyro0 = "chars/pyro0.png"

define admin = Character("Administrator")
define med = Character("Medic")
define spy = Character("Sneaky french man")

# SCREENS

screen spawnhall1:
    imagemap:
        ground "bg/spawnhall1_nav.png"
        hover "bg/spawnhall1_navh.png"
        hotspot(110, 479, 68, 61) clicked Jump("act_middle1")
        # hotspot (1547, 507, 69, 62) clicked Jump("act_intells1")

screen middle1:
    imagemap:
        ground "bg/middle1_nav.png"
        hover "bg/middle1_navh.png"
        hotspot(425, 236, 65, 65) clicked Jump("act_middle2")
        hotspot(606, 475, 60, 64) clicked Jump("act_middle3")

# LABELS

label start:
    stop music
    scene black
    show text "Loading \"Turbine\"":
        ypos 800
    show tflogo at truecenter:
        subpixel True
        rotate 0
        linear 5.0 rotate 360
        ease 20
        repeat
    $ renpy.pause(5.0)
    jump act_spawn


label act_spawn:
    play music "music/act1_engineer_theme.mp3"
    scene spawn1 with dissolve
    # play movie "videos/Turbine0.ogv" loop
    # show movie with fade

    admin "Alert! The Enemy Has Taken Our Intelligence!"
    show medic0 at left with moveinleft
    med "Dummkopfs!"
    med "Again? Okay, let's do it again!"

    show spy0 at right with moveinright
    play sound "sfx/spy_medic01.wav"
    spy "Doctor!"
    $ renpy.pause(.8)
    play sound "sfx/spy_activatecharge01.wav"
    spy "Charge me, doctor!"

    # med "I'll not uber you, dumbass! Why? 'Cause you're the freakin' spy!"
    med "Are you serious?"
    med "I will not give the uber!"

    spy "Okay. But now i'll not to destroy sentries and other shit!"

    med "That's your job!"
    hide spy0 with dissolve
    $ renpy.pause(1.0)
    med "**Uber for the spy... LOL**"
    hide medic0 with dissolve
    stop movie


label act_spawnhall1:
    scene spawnhall1 with dissolve
    show medic0 at left with moveinright
    call screen spawnhall1
    
    
label act_middle1:
    play music "music/act2_rocket_jump_waltz.mp3"
    scene middle1 with dissolve
    # play movie "videos/middle1.ogv" loop
    # show movie with fade

    show medic0 at left with moveinright
    show heavy0 at right with moveinleft
    play sound "sfx/heavy_medicfollow01.wav"

    med "Finally! Heavy!"
    med "We need to defende our intels!"

    play sound "sfx/heavy_yes02.wav"
    $ renpy.pause(1.0)
    play sound "sfx/medic_go01.wav"
    med "Go! Go! Go!"
    
    call screen middle1

    hide heavy0 with dissolve
    hide medic0 with dissolve


label act_middle2:
    scene black
    play movie "videos/middle2.ogv" loop
    show movie with fade

    show heavy0 at left with moveinright
    show medic0f at right with moveinright

    med "Heavy, beware!"
    play sound "sfx/csgo_awp_shoot_crit.wav"
    $ renpy.pause(1.0)
    play sound "sfx/heavy_paincrticialdeath01.wav"
    hide heavy0 with dissolve

    med "Oh shit!"

    return
