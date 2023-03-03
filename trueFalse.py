print('Do you want to play the game  if yes(y) if no Quit(q)') 
playing = input('')
if(playing.lower() !='y'):
    quit()                    # this is to quit from the programme 
print('Press true(t) or false(f)')
score =0                              # the variable is used to show your score at the end of the game 

# 1
answer = input('1)Sharks are mammals.')
if(answer.lower() == 'f'):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT(Shark are classified as fish )')

#2
answer = input('2)The blue whale is the biggest animal to have ever lived')
if(answer.lower() == 't'):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT (yes it is one of the biggest animal to live around the time of dinasours)')

#3
answer = input('3)Bats are blind.')
if(answer.lower() == 'f'):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT (bats use ultrasound to navigate but they also have eye which can partially see So technically they are not blind)')

#4
answer = input('4)The goat is the national animal of Scotland')
if(answer.lower() == 'f'):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT(unicorn is the national animal of the Scothland )')

#5
answer = input('5)Does Sun rise from the East ')
if(answer.lower() == 't'):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT(Due to rotation of the earth the sun always rise form the east and sets at west)')  

#5
answer = input('6)Where was the G20 summit held in 2023')
if(answer.lower() == "india"):
    print('CORRECT')
    score +=1
else:
    print('IN-CORRECT(G20 summit was held in India in the year 2023)')      

print(f'Total score{score}')
print('<---------------THE END------------------->')
