import random

serve = 1 # declaring a variable to use it globally

def swap(): # this function will swap the serve if one lost a volley
    global serve # declaring globally so that it will change outside the function
    if (serve==1): serve = 2 # my opponent will serve now
    else: serve = 1  # my serve

def RaquetBall(N): # this function will give probability by simulating N number of game
    win = 0 # initially number of win is 0
    global serve # declaring globally so that it will change outside the function
    for i in range(N): #simulation running
        serve = 1 # I will start serving
        point = 0 # my initial point
        point2 = 0  # opponent's initial point
        while(point <= 21 and point2 <= 21): # this loop will run until anyone reach 21 points
            if(point == 21): 
                win += 1 # if I reached 21 first, my number of win will increase
                break # game over
            elif(point2 == 21): # I lost
                break # game over without increasing number of win
            else:
                rand = random.random() # getting a random number
                # if I am serving and if 0 < rand < 0.6, I score a point
                if(serve == 1 and rand < 0.6):
                    point += 1
                # if opponent is serving and 0.5 <= rand, he will score
                elif (serve == 2 and rand >= 0.5):
                    point2 += 1
                # else serve will be swapped
                else:
                    swap()
    print(N,'Simulation Finished') # out of the bigger loop
    print("My probability to win: ", win/N) # calculating probability
    return win/N # returning the probability