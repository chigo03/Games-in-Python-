# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
random_no = 0
secret_no = 0
count = 7
high =1000
low = 0

print "GUESS THE NUMBER \n"
# helper function to start and restart the game
def new_game():
    global count
    count = 7
    global random_no
    random_no = 0
    global secret_no
    secret_no = 0
    global high 
    high =1000
    global low
    low = 0
    range100()   
    
    
# define event handlers for control panel
def range100():
    global secret_no
    secret_no = random.randrange(0, 100)
    print 'New game. Range is from 0 to 100'
    print 'Number of remaining guesses is '+ str(count)+"\n"
        
    
def range1000():
    global count
    global secret_no
    count = 10
    secret_no = random.randrange(0, 1000)
    print '\nNew game. Range is from 0 to 1000'
    print 'Number of remaining guesses is '+ str(count)+"\n"
    

def input_guess(guess):
    global high
    global low
    global count
    count = count - 1
    random_no = int(guess)
    print "\nGuess was "+ str(random_no)
    print "Number of remaining guesses is "+ str(count)
    if random_no > secret_no:
        print "Higher!"
        high = random_no - 1
    elif random_no < secret_no:
        print "Lower!"
        low = random_no + 1
    elif random_no == secret_no:
        print "Correct!!!!\n"
        new_game()
    if count == 0:
        print "You ran out of guesses.  The number was "+ str(secret_no)+"\n"
        new_game()
        
  
# create frame
f = simplegui.create_frame("Guess the Number", 300, 300)


# register event handlers for control elements
f.add_button("Number range: 0 - 100", range100, 200)
f.add_button("Number range: 0 - 1000", range1000, 200)
f.add_input("Enter the guess", input_guess, 200)


# call new_game and start frame
new_game()
f.start()
