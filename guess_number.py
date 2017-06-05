
import random

num = random.randint(1, 100)
print num

attempts = 1
prompt = "pick a number from 1 to 100: "
guess = int(raw_input(prompt + " within 10 guesses"))
print guess

while guess != num :
	
    attempts_remain = 10 - attempts
    prompt_2 = prompt + ' with attempts_remain guesses remaining'

    if attempts_remain > 10:
        print "game over : you have used up the attempts guesses"
    elif guess > num:
        print "wrong guess and you have " + str(attempts_remain) + " remaining"
        print "guess is > then number"
        guess = int(raw_input( prompt_2 ) )
    elif guess < num:
        print "wrong guess and you have " + str(attempts_remain) + " remaining"
        print "guess is < number"
        guess = int( raw_input( prompt_2 ) )
    else:
        print "correct: your guess = num"
        break

    attempts += 1
