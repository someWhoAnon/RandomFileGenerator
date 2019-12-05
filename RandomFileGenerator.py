import os
from threading import Thread
import random
import datetime
import time

# This we will use name our files
listOfExtensions = ['.txt', '.docx', '.xlsx', '.jpeg', '.png', '.mp3', '.zip', '.c', '.rar', '.jar']
listOfNameParts1 = ['some', 'default', 'simple', 'random', 'any', 'great', 'pretty', 'glorious']
listOfNameParts2 = ['data', 'info', 'test', 'file']

# Define global vars
wantedNumOfFiles = 0
count = 0
filename = ''

# define place for our files
folder = os.path.expanduser("~/Desktop/GeneratedTestingData/")
if not os.path.exists(folder):
    os.makedirs(folder)


# function for generating names + path of files
def generateName():
    global filename
    filename = random.choice(listOfNameParts1) + '_' + random.choice(listOfNameParts2) + '_' + \
               datetime.datetime.now().strftime("%Y-%m-%d_") + str(random.randint(0, 5465465)) + random.choice(
        listOfExtensions)
    full_path = folder + filename
    return full_path


# function that will write data into the file
def prescript(file, num):
    with open(file, 'w') as f:
        for i in range(num):
            f.write('Randomakldsjflkajsdfasjdflajsdklfjkalsjdflkjaskdljflkajsdklfjlaksjdflkjaskdjflkasjdlkfjaskdjfa\n')


# function that will work with user input
def userInput():
    global wantedNumOfFiles
    wantedNumOfFiles = int(input("Please input number of files: "))
    if 0 < wantedNumOfFiles <= 100:
        print('Ok, hold on...')
    elif 100 < wantedNumOfFiles <= 300:
        print('Hey man, easier!')
    elif wantedNumOfFiles > 300:
        print('Freaky bastard...')
    print('Files will be placed at your desktop in the folder GeneratedTestingData')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)


def loop():
    global count
    while count < wantedNumOfFiles:
        try:
            # defining var for thread
            t1 = Thread(target=prescript, args=(generateName(), random.randint(10, 99999)))  # random.randint(min, max)
            print('Generated: ' + filename)
        except IOError:
            print('Error during init of thread 1')
        try:
            t1.start()
        except:
            print('IOError during starting of thread')
        try:
            t1.join()
        except:
            print('IOError during stopping of thread')
        count = count + 1


#######################################################################################################################


userInput()
loop()
