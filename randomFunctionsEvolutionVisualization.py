# This program was made as a way of better understanding how random functions work.
# Our understanding is better when we see things instead of just imagining them.
# It just generates random values within an interval, calculates relative frequencies(probability) for each value
# and plots probability distributions for six different functions.

import pygame,os
from sys import exit
import random
from pygame.locals import *


########################################################################
###################### PROBLEM VARIABLES ###############################
########################################################################

#Amount of random numbers in each diagram
amount=100

#Total numbers generated
totalGenerated=0

#number of iterations
iterations=0

#amount of new numbers generated in each iteration (generation step)
newNumbers= 1

#Initialize lists that hold how many times each number has been generated
nRandIntGenerated    = [0] * ( amount + 1 )
nUniformGenerated    = [0] * ( amount + 1 )
nTriangularGenerated = [0] * ( amount + 1 )
nGammaGenerated      = [0] * ( amount + 1 )
nGaussGenerated      = [0] * ( amount + 1 )
nBetaGenerated       = [0] * ( amount + 1 )

#Initialize lists that hold probability (retalive frequency)
probRandInt    = [0] * ( amount + 1 )
probUniform    = [0] * ( amount + 1 )
probTriangular = [0] * ( amount + 1 )
probGamma      = [0] * ( amount + 1 )
probGauss      = [0] * ( amount + 1 )
probBeta       = [0] * ( amount + 1 )


########################################################################
###################### WINDOW VARIABLES ################################
########################################################################

#center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Spacing factor (pixel distance between vertical lines)
spacingFactor=3 #changing this will affect window width


############## HORIZONTAL PARAMETERS ##################
#Horizontal dimension of each diagram
horizontalDiagramDimension = spacingFactor * ( amount - 1 )

#Horizontal dimension of each 'sub-window'
horizontalMargin = 20
horizontalSubwindowDimension = horizontalDiagramDimension + 2*horizontalMargin


############## VERTICAL PARAMETERS ####################
#Vertical dimension of each diagram
verticalDiagramDimension = 300 # dont change this because diagrams are not width-parametrized

#Vertical dimension of each 'sum-window'
verticalMargin = 40
verticalSubwindowDimension = verticalDiagramDimension + 2*verticalMargin


############ WINDOW FINAL DIMENSIONS ###################
#Dimension of window
width  = 3*horizontalSubwindowDimension
height = 2*verticalSubwindowDimension


############ CREATING AND SHOWING WINDOW ###############
#Background colour 
background_colour=(0,0,0)
GREEN = (  0, 180,   0)

#Initialize pygame
pygame.init()

#Set the display mode
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Evolution Visualization of Pseudo-Random Generator Functions')

#Show Window and Set Background Colour
screen.fill(background_colour)
pygame.display.flip()



########################################################################
################ lOGIC CALCULATIONS AND FUNCTIONS ######################
########################################################################

############ COORDINATE FUNCTIONS FOR EACH DISTRIBUTION ################
def xRandInt():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + horizontalMargin
    return x

def yRandInt():
    y=[0]*amount
    for i in range(amount):
        y[i]=verticalSubwindowDimension - verticalMargin - probRandInt[i]
    return y
    
def xUniform():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + horizontalSubwindowDimension + horizontalMargin
    return x 

def yUniform():
    y=[0]*amount
    for i in range(amount):
        y[i]=verticalSubwindowDimension - verticalMargin - probUniform[i]
    return y

def xTriangular():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + 2*horizontalSubwindowDimension + horizontalMargin
    return x 

def yTriangular():
    y=[0]*amount
    for i in range(amount):
        y[i]=verticalSubwindowDimension - verticalMargin - probTriangular[i]
    return y

def xGamma():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + horizontalMargin
    return x 

def yGamma():
    y=[0]*amount
    for i in range(amount):
        y[i]=height-verticalMargin-probGamma[i]
    return y

def xGauss():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + horizontalSubwindowDimension + horizontalMargin
    return x 

def yGauss():
    y=[0]*amount
    for i in range(amount):
        y[i]=height-verticalMargin-probGauss[i]
    return y

def xBeta():
    x=[0]*amount
    for i in range(amount):
        x[i]=spacingFactor*i + 2*horizontalSubwindowDimension + horizontalMargin
    return x 

def yBeta():
    y=[0]*amount
    for i in range(amount):
        y[i]=height-verticalMargin-probBeta[i]
    return y


#Calculate probability for each point
def prob(nGenerated):
    return int( float(nGenerated) / float(totalGenerated) * 100*amount )


# Generating new numbers and recalculating all probabilities
def doLogic():
    
    #Adding new random values
    for i in range(newNumbers):
        #  randint
        newInt=random.randint(0,amount )
        nRandIntGenerated[newInt] += 1
        #  uniform
        newInt=int( random.uniform( 0 , amount ) )
        nUniformGenerated[newInt] += 1
        #triangular
        newInt=int( random.triangular(0,amount,amount/2) )
        nTriangularGenerated[newInt] += 1
        #gamma
        temp=random.gammavariate( 2.3 , 0.15 )
        if(temp<=1): # Gamma distribution goes from 0 to +∞
        #parameters were chosen so that most values are from 0 to 1
        #generated values are scaled to fit the interval [0,amount]
            newInt=int(temp*amount)
            nGammaGenerated[newInt] += 1
        #gauss
        temp=random.gauss( 0 , 0.33 )
        if(temp<1 and temp>-1): # Gauss distribution goes from -∞ to +∞
        #parameters were chosen so that most values are from -1 to 1
        #generated values are scaled to fit the interval [0,amount]
            newInt=int( (temp+1.0) / 2.0*amount )
            nGaussGenerated[newInt] += 1
        #beta
        #Beta distribution goes from 0 to 1
        #generated values are scaled to fit the interval [0,amount]
        newInt=int( random.betavariate( 4 , 2 )*amount )
        nBetaGenerated[newInt] += 1

    #Calculating again probalities
    for j in range(amount+1):
        probRandInt[j]=prob( nRandIntGenerated[j] )
        probUniform[j]=prob( nUniformGenerated[j] )
        probTriangular[j]=prob( nTriangularGenerated[j] )
        probGamma[j]=prob( nGammaGenerated[j] )
        probGauss[j]=prob( nGaussGenerated[j] )
        probBeta[j]=prob( nBetaGenerated[j] )


            
########################################################################
######################  DRAWING LINES TO SCREEN ########################
########################################################################

def drawDiagram(x,y,yBottom,yTop):
    #Drawing the lines to the screen
    for i in range(amount):
        bottomPoint= [ x[i] , yBottom ]
        topPoint= [ x[i] , y[i] ]
        if( topPoint[1] < yTop ):#checking if top point is higher than the upper bound
            topPoint[1]=yTop     #comparing uses 'less' instead of 'greater' because y-axis goes downwards 
        pygame.draw.line(screen, GREEN, bottomPoint ,topPoint , 1)
        if( i != 0 and i != amount ):
            firstPoint=[ x[i-1] , y[i-1] ] 
            if( firstPoint[1] < yTop ): #same as above
                firstPoint[1]=yTop
            pygame.draw.line(screen,GREEN,firstPoint,topPoint,1)
    

def drawRandIntLines():
    drawDiagram( xRandInt() , yRandInt() , verticalSubwindowDimension-verticalMargin , verticalMargin)

def drawUniformLines():
    drawDiagram( xUniform() , yUniform(), verticalSubwindowDimension-verticalMargin , verticalMargin)    

def drawTriangularLines():
    drawDiagram( xTriangular() , yTriangular() , verticalSubwindowDimension-verticalMargin , verticalMargin )
    
def drawGammaLines():
    drawDiagram( xGamma() , yGamma() , height-verticalMargin , verticalSubwindowDimension+verticalMargin )

def drawGaussLines():
    drawDiagram( xGauss() , yGauss() , height-verticalMargin , verticalSubwindowDimension+verticalMargin )

def drawBetaLines():
    drawDiagram( xBeta() , yBeta() , height-verticalMargin , verticalSubwindowDimension + verticalMargin )


def drawSubwindowsBounds():
    ## RANDINT
    topLeft=[ horizontalMargin , verticalMargin ]
    topRight=[ horizontalSubwindowDimension - horizontalMargin , verticalMargin ]
    bottomRight=[ horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension-verticalMargin  ]
    bottomLeft=[ horizontalMargin , verticalSubwindowDimension-verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)

    ## UNIFORM
    topLeft=[ horizontalSubwindowDimension + horizontalMargin , verticalMargin ]
    topRight=[ 2*horizontalSubwindowDimension - horizontalMargin , verticalMargin ]
    bottomRight=[ 2*horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension-verticalMargin  ]
    bottomLeft=[ horizontalSubwindowDimension + horizontalMargin , verticalSubwindowDimension-verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)

    ## TRIANGULAR
    topLeft=[ 2*horizontalSubwindowDimension + horizontalMargin , verticalMargin ]
    topRight=[ 3*horizontalSubwindowDimension - horizontalMargin , verticalMargin ]
    bottomRight=[ 3*horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension-verticalMargin  ]
    bottomLeft=[ 2*horizontalSubwindowDimension + horizontalMargin , verticalSubwindowDimension-verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)

    ## GAMMA
    topLeft=[ horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    topRight=[ horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    bottomRight=[ horizontalSubwindowDimension - horizontalMargin , height - verticalMargin  ]
    bottomLeft=[ horizontalMargin , height - verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)

    ## GAUSS
    topLeft=[ horizontalSubwindowDimension + horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    topRight=[ 2*horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    bottomRight=[ 2*horizontalSubwindowDimension - horizontalMargin , height - verticalMargin  ]
    bottomLeft=[ horizontalSubwindowDimension + horizontalMargin , height - verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)

    ## BETA
    topLeft=[ 2*horizontalSubwindowDimension + horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    topRight=[ 3*horizontalSubwindowDimension - horizontalMargin , verticalSubwindowDimension + verticalMargin ]
    bottomRight=[ 3*horizontalSubwindowDimension - horizontalMargin , height - verticalMargin  ]
    bottomLeft=[ 2*horizontalSubwindowDimension + horizontalMargin , height - verticalMargin ]
    shape=[ topLeft[0] , topLeft[1] , bottomRight[0]-topLeft[0] , bottomRight[1]-topLeft[1] ]
    pygame.draw.rect(screen,GREEN, shape , 2)



########################################################################
######################  DRAWING TEXT TO SCREEN #########################
########################################################################
titleSize=40

def drawText(font, text, position):
    textsurface = font.render(text , True , GREEN)
    screen.blit(textsurface,position)

def drawAllText():
    myfont = pygame.font.SysFont(None, titleSize)

    drawText(myfont ,"randint()" , ( horizontalMargin , verticalMargin-titleSize+10 ) )

    drawText(myfont , "uniform()" , ( horizontalSubwindowDimension+horizontalMargin , verticalMargin-titleSize+10 ) )

    drawText(myfont, "triangular()" , ( 2*horizontalSubwindowDimension+horizontalMargin , verticalMargin-titleSize+10 ) )

    drawText(myfont, "gamma()" , ( horizontalMargin , verticalSubwindowDimension + verticalMargin-titleSize+10 ) )

    drawText(myfont, "gauss()" , ( horizontalSubwindowDimension+horizontalMargin , verticalSubwindowDimension + verticalMargin-titleSize+10 ) )

    drawText(myfont, "beta()" , ( 2*horizontalSubwindowDimension+horizontalMargin , verticalSubwindowDimension + verticalMargin-titleSize+10 ) )

    drawText(myfont, "total numbers generated:  " + str(totalGenerated) , ( horizontalMargin , 2*verticalSubwindowDimension-titleSize+10 ) )

    drawText(myfont, "generation step: "+ str(newNumbers) , ( 2*horizontalSubwindowDimension+horizontalMargin , 2*verticalSubwindowDimension-titleSize+10 ))
    

def drawToScreen():

    drawSubwindowsBounds()

    drawRandIntLines()

    drawUniformLines()

    drawTriangularLines()

    drawGammaLines()

    drawGaussLines()

    drawBetaLines()

    drawAllText()
    
    #Update the screen
    pygame.display.update()



########################################################################
########################### 'GAME' LOOP ################################
########################################################################

print("\nuse the arrows to change generation step")
print("\nUP/DOWN arrow to increase/decrease by 1")
print("\nRIGHT/LEFT arrow to increase/decrease by 10")

running=True

while running and totalGenerated<=200000 :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keystate=pygame.key.get_pressed()

    if(keystate[K_UP] and newNumbers<50):
        newNumbers+=1
    elif( keystate[K_DOWN] and newNumbers>1 ):
        newNumbers-=1
    elif(keystate[K_RIGHT] and newNumbers<50):
        if(newNumbers<40):
            newNumbers+=10
        else:
            newNumbers=50
    elif(keystate[K_LEFT] and newNumbers>1):
        if(newNumbers>10):
            newNumbers-=10
        else:
            newNumbers=1
    elif(keystate[K_SPACE]):
        paused=not paused
        pygame.time.wait(10)

    
    iterations+=1
    totalGenerated+=newNumbers

    #Generate new numbers and update probabilities
    doLogic()
    #Clear screen and draw new state
    screen.fill(background_colour)
    drawToScreen()
    
    pygame.time.wait(80)
    
        
pygame.quit()
