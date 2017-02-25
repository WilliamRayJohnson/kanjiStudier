'''
A program that will make studing kanji easier.
William Ray Johnson
'''

from readKanjiFile import *
from random import choice, shuffle, randint

KANJI_FILE = 'genkiKanji.txt'

def studyReading(studySet):
    for entry in studySet:
        word, reading = choice(list(entry[1].items()))
        input(word)
        input('It is read {}'.format(reading))
        print()

def studyWritting(studySet):
    for entry in studySet:
        word, reading = choice(list(entry[1].items()))
        input(reading)
        input('It is written {}'.format(word))
        print()

def genRandKanjiSet(size, kanjiSet):
    randKanjiSet = []

    for kanjiNum in range(size):
        randKanji = choice(kanjiSet)
        while randKanji in randKanjiSet:
            randKanji = choice(kanjiSet)
        randKanjiSet.append(randKanji)

    return randKanjiSet


def main():
    kanjiDict = readKanjiFile(KANJI_FILE)
    isStudying = True

    while(isStudying):
        print('There are {} chapters available to study.'.format(len(kanjiDict)))
        studySetType = input("Would you like to study by (c)hapter or a (r)andom amount?")
        if studySetType == 'c':
            chapter = input('Which chapter would you like to study? ')
            studySet = list(kanjiDict[int(chapter)].items())
            shuffle(studySet)
        elif studySetType == 'r':
            kanAmt = input("How many kanji would you like to study? ")
            newDict = OrderedDict()
            for chap in kanjiDict:
                for kan, wor in chap.items():
                    newDict.update({kan:wor})
            studySet = genRandKanjiSet(int(kanAmt), list(newDict.items()))
        studyType = input('Would you like to study (r)eading or (w)riting?: ')
        if studyType == 'r':
            studyReading(studySet)
        elif studyType == 'w':
            studyWritting(studySet)
        willCont = input('Would you like to continue studying? (y)es (n)o: ')
        if willCont == 'n':
            isStudying = False


if __name__ == '__main__':
    main()
