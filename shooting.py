import pgzrun, random, pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="shooting game"
message ="shoot the black one" 
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

def on_mouse_down(pos):
  global message
  print(pos)
  if person.collidepoint(pos):
     message="you shot the right one" 
  elif  player.collidepoint(pos):
     message="oops you shot the wrong player" 
  elif actor.collidepoint(pos):
     message="you shot the mysterious one" 
  else:message="try again" 
     
  actor.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50) 
  player.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
  person.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
  
   
 


pgzrun.go()