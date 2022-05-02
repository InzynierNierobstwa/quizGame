print('Welcome to my computer quiz')

playing = input('Do you want to play a game? ')

if playing.lower() != 'yes':
    quit()

print('Ok. Let\'s play a game' )
score = 0

answer = input('What doe\'s CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct')
    score += 1
else:
    print('inccorect')

answer = input('What doe\'s GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('correct')
    score += 1
else:
    print('inccorect')

answer = input('What doe\'s RAM stand for? ')
if answer.lower() == 'random access memory':
    print('correct')
    score += 1
else:
    print('inccorect')

answer = input('What doe\'s PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('correct')
    score += 1
else:
    print('inccorect')

print(f'You got {score} questions correct!')
percent = (score / 4) * 100
print(f'You got {percent}%!')