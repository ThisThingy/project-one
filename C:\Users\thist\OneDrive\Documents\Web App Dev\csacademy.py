
#Background
app.background='black'
backgroundStars = Group(
    Star(20, 30, 3, 5, fill ='white'), 
    Star(45, 169, 3, 5, fill ='white'), 
    Star(342, 55, 3, 5, fill ='white'), 
    Star(75, 89, 3, 5, fill ='white'), 
    Star(96, 70, 3, 5, fill ='white'), 
    Star(256, 265, 3, 5, fill ='white'), 
    Star(162, 56, 3, 5, fill ='white'), 
    Star(135, 130, 3, 5, fill ='white'), 
    Star(380, 230, 3, 5, fill ='white'), 
    Star(80, 330, 3, 5, fill ='white'), 
    Star(320, 130, 3, 5, fill ='white'), 
    Star(140, 80, 3, 5, fill ='white'), 
    Star(200, 40, 3, 5, fill ='white')
    )
timeGoneBy = Label(0, 0, 0, visible=False)
app.stepsPerSecond = 0

################################################################################

# draws fuel and fuel gauge at top of the screen
fuelGauge = Group(
    Rect(0, 0, 400, 30, fill=rgb(50, 50, 50), border='silver', borderWidth=3), 
    Line(50, 0, 50, 30, fill='silver'),
    Line(100, 0, 100, 30, fill='silver'),
    Line(150, 0, 150, 30, fill='silver'),
    Line(200, 0, 200, 30, fill='silver'),
    Line(250, 0, 250, 30, fill='silver'),
    Line(300, 0, 300, 30, fill='silver'),
    Line(350, 0, 350, 30, fill='silver'),
    Line(10, 15, 390, 15, lineWidth=15))

fuel = Line(10, 15, 390, 15, lineWidth=15, fill=gradient('limeGreen', 'green'))

fuelCounter = Label(0,1,1 , visible=False)

################################################################################

# draws bottom bar, boss bar later on, and the health counter
bottomBar = Group(
    Rect(0, 370, 400, 30, fill=rgb(50, 50, 50), border='silver', borderWidth=6),
    Line(50, 370, 50, 400, fill='silver'), 
    Line(100, 370, 100, 400, fill='silver'), 
    Line(150, 370, 150, 400, fill='silver'), 
    Line(200, 370, 200, 400, fill='silver'), 
    Line(250, 370, 250, 400, fill='silver'), 
    Line(300, 370, 300, 400, fill='silver'), 
    Line(350, 370, 350, 400, fill='silver'), 
    Line(10, 385, 390, 385, lineWidth=15) 
    )

bossBar = Line(10, 385, 390, 385, lineWidth=15, fill=gradient('crimson', 'red'), visible=False)

bossHealth = Label(0, 1, 1, visible=False)

################################################################################


#Draws the bars for separate pages
controlsBar = Label('CONTROLS', 210, 200, size=30)

objectiveBar = Label('OBJECTIVE', 210, 250, size=30)

#Draws the go back arrow in the pages
goBack = Group(
    Rect(30, 40, 60, 10), 
    RegularPolygon(40, 45, 20, 3, rotateAngle=270), 
    )
goBack.visible=False

#Draws main menu
mainMenu = Group(
    Rect(0, 0, 400, 400, fill='crimson', border='black'), 
    Label('Welcome to Purgatory!', 200, 50, size=30, bold=True), 
    Label('Press "Enter" to Start', 200, 375, size=25),
    Label('Your controls and instructions are as follows:', 200, 130, size=20), 
    controlsBar, 
    objectiveBar)

#Draws controls screen
controls = Group(
    Rect(0, 0, 400, 400, border='black', fill='crimson'),
    Label('To move UP: "up" or "w"', 200, 150, size=30), 
    Label('To move DOWN: "down" or "s"', 200, 200, size=28), 
    Label('To shoot lasers: "space"', 200, 250, size=30)
    )
controls.visible=False    


#Draws objective screen
objective = Group(
    Rect(0, 0, 400, 400, fill='crimson', border='black'), 
    Label('You are to survive as long as possible', 200, 100, size=20, bold=True), 
    Label('You can destroy specific entities like:', 180, 140, size=20), 
    Oval(50, 200, 30, 55, fill=gradient('silver','dimGrey','grey', start='top'), rotateAngle=randrange(1, 359)),
    Star(150, 200, 30, 100, fill=gradient('yellow','gold','white','orange')), 
    Label('Unbreakable entities are:', 130, 250, size=20),
    Circle(150, 340, randrange(40, 60), fill=gradient(rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), 
    rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), start='top'), 
    rotateAngle=randrange(1, 359)), 
    RegularPolygon(280, 340, randrange(40, 70), randrange(8, 20), fill=gradient('silver','dimGrey','grey', start='top'))
    )    
objective.visible=False
    
    
#Draws the win and loss screen
loseScreen = Group(
    Rect(0, 100, 400, 200, fill=None, border='black', borderWidth=4), 
    Rect(0, 100, 400, 200, fill=gradient('red','grey', start = 'top-left'), opacity=50), 
    Label('You Lose...', 200, 200, size = 50))
loseScreen.visible=False

winScreen = Group(
    Rect(0, 100, 400, 200, fill=None, border='black', borderWidth=4), 
    Rect(0, 100, 400, 200, fill=gradient('green','grey',start='top-left'), opacity=50), 
    Label('WOW YOU WON!!!', 200, 200, size=50))
winScreen.visible=False    




###################################################################
    
#Draws the entities needed to destroy or avoid
deadlyStars = Group()

deadlyPlanets = Group()

deadlyMeteors = Group()

deadlyAsteroids = Group()


#Draws a fun surprise at the end
bossDaddy = Group(
    Circle(400, 200, 100, fill=rgb(240, 255, 4)), 
    Oval(345, 180, 45, 60, fill='white', border='black', borderWidth=6, rotateAngle=-10), 
    Circle(355, 170, 10), 
    Circle(430, 180, 30, fill='white', border='black', borderWidth=6), 
    Circle(445, 170, 10), 
    Polygon(382, 275, 396, 279, 419, 279, 440, 265, 441, 266, 434, 256, 425, 253, 410, 250, 400, 254, 390, 260, 387, 262, 385, 270, fill='white'), 
    Oval(398, 241, 100, 80, fill=rgb(150, 0, 141), rotateAngle=20, opacity=80), 
    Oval(398, 241, 100, 80, fill=None, rotateAngle=20, border='black', borderWidth=6), 
    Rect(315, 190, 155, 35, fill=rgb(240, 255, 4)), 
    Line(325, 190, 367, 190, lineWidth=6), 
    Line(400, 190, 460, 190, lineWidth=6), 
    Line(350, 225, 440, 225, lineWidth=6), 
    Circle(400, 200, 100, fill=None, border='black', borderWidth=10))

bossDaddy.visible=False
bossDaddy.speedY = 0
###################################################################

#Draws the guns in which the lasers come out of
playerGuns = Group(
    Line(50, 180, 70, 180, fill='red', lineWidth=5), 
    Line(30, 180, 60, 180, lineWidth=8, fill='silver'), 
    Line(50, 220, 70, 220, fill='red', lineWidth=5), 
    Line(30, 220, 60, 220, lineWidth=8, fill='silver'))

#Draws the player    
player = Group(playerGuns,
    Star(40, 200, 50, 3, fill='red', rotateAngle=90, border='dimGray'),
    Star(75, 200, 20, 3, fill='red', rotateAngle=90, border='dimGrey'),
    Oval(50, 200, 60, 20, fill = 'grey', border='black'), 
    Oval(70, 200, 20, 15, fill='lightBlue'), 
    Oval(69, 199, 5, 6, fill='yellow', rotateAngle=30), 
    Oval(30, 200, 40, 5, fill='red', border='dimGrey', borderWidth=0.9)
    )
#Group that contains the lasers 
laser = Group()
    
###################################################################

# If the mouse is hovering over the arrow, the control bar or the objective bar,
# then highlight them
# Else, make them normal
def onMouseMove(mouseX, mouseY):
    
    if controlsBar.hits(mouseX, mouseY):
        controlsBar.size = 33
        controlsBar.border='silver'
        
    elif goBack.visible==True:
        if goBack.hits(mouseX, mouseY):
            goBack.fill='green'
        else:
            goBack.fill='black'
            
    elif objectiveBar.hits(mouseX, mouseY):
        objectiveBar.size=33
        objectiveBar.border='silver'
            
    else:
        controlsBar.size = 30
        controlsBar.border=None
        
        objectiveBar.size=30
        objectiveBar.border=None
        
    
    
    
    
    
###################################################################

# If the mouse is clicked on the shapes it is hovering over,
# then take them to the respective page and make the previous page visible

def onMousePress(mouseX, mouseY):
    
    if controlsBar.hits(mouseX, mouseY):
        controls.visible=True
        mainMenu.visible=False
        player.centerY = 350
        goBack.visible=True
        goBack.toFront()
        player.toFront()

    if objectiveBar.hits(mouseX, mouseY):
        objective.visible=True
        mainMenu.visible=False
        player.centerY= 350
        goBack.visible=True
        goBack.toFront()
        player.toFront()
        
    if goBack.hits(mouseX, mouseY):
        mainMenu.visible=True
        objective.visible=False
        controls.visible=False
        player.centerY = 200
        goBack.visible=False
        player.toFront()
    
###################################################################

# Controls inputs
def onKeyPress(key):
#As long as the main menu is visible, the only pressable button is 'enter'
    if mainMenu.visible==True:
        if key =='enter':
            app.stepsPerSecond=20
            mainMenu.visible=False
            fuelGauge.toFront()
            bottomBar.toFront()

#When 'enter' is pressed and if all the other screens are not visible, 
#the player can be controlled
    if mainMenu.visible == False and controls.visible==False and objective.visible==False:
    
        if key == 'up' or key == 'w':
            if player.centerY > 50:
                player.centerY -= 30
                fuelCounter.value+=2
        
        
        if key == 'down' or key == 's':
            if player.centerY < 350:
                player.centerY += 30
                fuelCounter.value+=2
        
        
        if key == 'space':
            laser.add(
                Line(70, player.centerY - 20, player.right + 20, player.centerY - 20, fill='green', lineWidth=5), 
                Line(70, player.centerY + 20, player.right + 20, player.centerY + 20, fill='green', lineWidth=5))
            playerGuns.centerX = playerGuns.centerX + 5
            fuelCounter.value+=2
        
        fuel.toFront()
   
# Fuel bar depletion checker    
    if fuelCounter.value >= 1:
        fuel.x2 = 390 - fuelCounter.value
        
    if fuel.x2 == 10:
        loseScreen.visible=True
        loseScreen.toFront()
        app.stop()

# this is just to make the laser guns move, after shooting

def onKeyRelease(key):
    if key == 'space':
        playerGuns.centerX = playerGuns.centerX - 5


###################################################################

def onStep():
    
    #Hidden Timer for Certain cues after specific intervals
    timeGoneBy.value += 1
    
    #Laser movements
    laser.centerX += 10
    
    #Background moving, simulating moving through space
    backgroundStars.centerX -= 1
    for star in backgroundStars:
        if star.right <= 0:
            star.left = 400
    
    
    fuel.x2=390-fuelCounter.value
    
    ###################################################################
    #Everything spawning and killing process
    
    #Draws a star every few seconds
    if timeGoneBy.value%50== 0:
        deadlyStars.add(Group(
            Star(400, randrange(30, 370), randrange(10, 30), randrange(10, 50), fill=gradient('yellow', 'gold','white','orange'))))
    for star in deadlyStars:
        deadlyStars.centerX -= 1
        star.rotateAngle+=5
        if star.right < 0:
            deadlyStars.remove(star)
        
        for line in laser:    
            if laser.hitsShape(star)==True:
                deadlyStars.remove(star)
                laser.remove(line)
                 
            if line.left>400:
                laser.remove(line)
                
        if player.hitsShape(star)==True:
            loseScreen.visible=True
            loseScreen.toFront()
            app.stop()    
            
            
    # Draws a meteor(oval) of random size every few seconds
    if timeGoneBy.value % 75 == 0:
        deadlyMeteors.add(
            Oval(400, randrange(30, 370), randrange(10, 50), randrange(10, 60), 
            fill=gradient('grey', 'dimGrey', 'silver', start='top'), rotateAngle=randrange(0, 359)))
        
    for oval in deadlyMeteors:
        deadlyMeteors.centerX -= 1
        oval.rotateAngle+=3
        if deadlyMeteors.right<0:
            deadlyMeteors.remove(oval)
        
        for line in laser:    
            if laser.hitsShape(oval)==True:
                laser.remove(line)
                deadlyMeteors.remove(oval)
                
        if player.hitsShape(oval)==True:
            loseScreen.visible=True
            loseScreen.toFront
            app.stop()
            
            
    # Draws an unbreakble planet of random size every 10 - 12 seconds 
    if timeGoneBy.value % 250 == 0:
        deadlyPlanets.add(
            Circle(400, randrange(0, 400), randrange(40, 60), fill=gradient(rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), 
            rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), rgb(randrange(0, 255), randrange(0,255),randrange(0,255)), 
            start='top')))
        
    for circle in deadlyPlanets:
        deadlyPlanets.centerX -= 1
        circle.rotateAngle+=2
        if player.hitsShape(circle):
            loseScreen.visible=True
            loseScreen.toFront()
            app.stop()
        if circle.centerX < 0:
            deadlyPlanets.remove(circle)
        for line in laser:
            if line.hitsShape(circle):
                laser.remove(line)
                
                
    # Draws an unbreakable asteroid of random size every 15 seconds            
    if timeGoneBy.value % 300 == 0:
        deadlyAsteroids.add(
            RegularPolygon(400, randrange(0, 400), randrange(30, 80), randrange(9, 20), 
            fill=gradient('grey','silver','dimgrey','white', start='top')))
    
    for polygon in deadlyAsteroids:
        deadlyAsteroids.centerX-=1
        polygon.rotateAngle+=2
        if player.hitsShape(polygon)==True:
            loseScreen.visible=True
            loseScreen.toFront()
            app.stop()
        if polygon.centerX < 0:
            deadlyAsteroids.remove(polygon)
        for line in laser:
            if line.hitsShape(polygon)==True:
                laser.remove(line)
        
        
###################################################################            
    
    #Boss Battle Time :))))))))        
    #After around 1 minute has passed(irl), the boss will spawn with the health bar
    if timeGoneBy.value >= 1500:
        bossDaddy.visible=True
        
        bossBar.visible=True
        #Controls the 
        bossDaddy.centerX -= .5        
        bossDaddy.centerY += bossDaddy.speedY
        
        
        if bossDaddy.top <= 0:
            bossDaddy.speedY = randrange(1, 10)
            
        elif bossDaddy.bottom >= 400:
            bossDaddy.speedY = -randrange(1, 10)
        
        else:
            bossDaddy.centerY += 1
            
        if player.hitsShape(bossDaddy)==True:
            loseScreen.visible=True
            loseScreen.toFront()
            app.stop()
        
        for line in laser:
            if laser.hitsShape(bossDaddy)==True:
                laser.remove(line)
                bossHealth.value += 20
                bossBar.x2 = 390 - bossHealth.value
                if bossBar.x2 <= 10:
                    bossDaddy.visible=False
                    winScreen.visible=True
                    app.stop()
                

    
    ###################################################################            


    ###################################################################            
    
