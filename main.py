from guizero import App, Picture, Box, PushButton, Text, Combo
from fruits import fruit_data
from random import choice

def reset(fruits, guesses, guessNr, statIndicator):
    fruits.options.clear()
    # fruits.options.extend(['AppleGreen', 'AppleRed', 'Banana', 'Orange', 'Raspberry', 'Blueberry', 'Strawberry', 'Pear'])
    fruits.insert(0, 'AppleGreen')
    fruits.insert(1, 'AppleRed')
    fruits.insert(2, 'Banana')
    fruits.insert(3, 'Orange')
    fruits.insert(4, 'Raspberry')
    fruits.insert(5, 'Blueberry')
    fruits.insert(6, 'Strawberry')
    fruits.insert(7, 'Pear')
    for child in guesses.children[3:]:
        child.destroy()
    guessNr[0] = 0
    stateIndicator.children[0].destroy()
    indicatorPicture = Picture(stateIndicator, image='red-big.png')
    global targetFruit
    targetFruit = choice(list(fruit_data.items()))
    print(targetFruit)

def guess(fruits, guesses, guessNr, stateIndicator):
    guessNr[0] += 1
    guess = fruits.value
    if(fruit_data[guess] == targetFruit[1]):
        stateIndicator.children[0].destroy()
        indicatorPicture = Picture(stateIndicator, image='green-big.png')
        print('WIN')
    for i in range(3):
        if (fruit_data[guess][i] == targetFruit[1][i]):
            img = 'green.png'
        else:
            img = 'red.png'
        picture = Picture(guesses, image=img, grid=[i, 1])
    for entry in guesses.children[3:-3]:
        entry.grid = [entry.grid[0], entry.grid[1]+1]
    fruits.remove(fruits.value)


def do_endless_shit():
    print(2)

app = App(title='Feed the Picosaur', height=800, width=1280, bg='#212121', layout='grid')
app.set_full_screen()
app.icon = 'icon.png'
topPadding = Box(app, height=20, width='fill', grid=[1, 0])
titleImage = Picture(app, image='title.png', grid=[1, 1])
fruits = Combo(app, options=['AppleGreen', 'AppleRed', 'Banana', 'Orange', 'Raspberry', 'Blueberry', 'Strawberry', 'Pear'], grid=[1, 2])
fruits.text_color = '#FFFFFF'

guesses = Box(app, layout='grid', height=500, width=400, align='top', grid=[0, 3])
categorys = [Text(guesses, text='COLOR ', color='#FFFFFF', font='Ubuntu', size=32, grid=[0, 0]), Text(guesses, text=' SIZE ', color='#FFFFFF', font='Ubuntu', size=32, grid=[1, 0]), Text(guesses, text=' SHAPE', color='#FFFFFF', font='Ubuntu', size=32, grid=[2, 0])]

stateIndicator = Box(app, height=500, width=400, align='top', grid=[1, 3])
indicatorPicture = Picture(stateIndicator, image='red-big.png')

cameraView = Picture(app, height=500, width=400, align='top', grid=[2, 3], image='camera-view.jpg')

guessNr = [0]
resetButton = PushButton(app, command=reset, image='reset.png', args=[fruits, guesses, guessNr, stateIndicator], grid=[0, 4])
paddingButtons = Box(app, width=500, grid=[1, 4])
guessButton = PushButton(app, command=guess, image='guess.png', args=[fruits, guesses, guessNr, stateIndicator], grid=[2, 4])


# repeat()
# update()
targetFruit = choice(list(fruit_data.items()))
print(targetFruit)

# app.repeat(100, do_endless_shit)
app.display()