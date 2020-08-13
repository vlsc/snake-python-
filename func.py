import random


def intRand():
    return random.randint(0, 590)//10 * 10


def getScore():
    text = open('high score.txt', 'r')
    record = str(text.readlines())
    record = record.split("'")
    record = record[1]
    record = int(record)
    text.close()
    return record


def setScore(newScore):
    text = open('high score.txt', 'w')
    text.write(str(newScore))
    text.close()


def eat(element1, element2, element3):
    if element1[0][0] == element2 and element1[0][1] == element3:
        return True
    else:
        return False