import random
import time

def displayIntro():
    print (
        '''Вы находитесь в пещере
        у вас на выбор две пещеры
        в одной злой дракон в ругой добрый
        Выберете в какую пещеру вы войдете'''
    )
    print()
def chooseCave():
    cave = ''
    while cave !='1' and cave !='2':
        print('В какую пещеру вы войдете?( нажмите клавишу 1 или 2)')
        cave = input()
        return cave
def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами')

    else:
        print('...моментально вас сьесдает!')

playAgain = 'да'
while playAgain == 'да' or playAgain =='y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Попытаете удачу еще раз?(да или нет)')
    playAgain = input()