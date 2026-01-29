import pgzrun, random, pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="catch the black one game"
message ="catch the black one" 
person=Actor("person.png")
person.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
player=Actor("player.png")
player.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
actor=Actor("actor.png")
actor.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
def draw():
    screen.fill("white")
    screen.draw.text(message,(50,50),color="black")
    person.draw() 
    player.draw() 
    actor.draw()
def update():
    global message
    if keyboard.left:
        actor.x=actor.x-10
    if keyboard.right:
        actor.x=actor.x+10
    if keyboard.up:
      actor.y=actor.y-10
    if keyboard.down:
      actor.y=actor.y+10
    if actor.colliderect(person):
       message="you got the balck one"
    elif actor.colliderect(player): 
        message="oops you got the brown one try again"
    else:
       message="catch the black one"    
pgzrun.go()        
