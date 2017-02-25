'''
A program that will make studing kanji easier.
William Ray Johnson
'''

from readKanjiFile import *
from random import choice, shuffle, randint

KANJI_FILE = 'genkiKanji.txt'
CHAP_RANGS = [(0,0), (0,0), (0,0), (0,15), (15,29), (29,43), (43,58), (58,72),
        (72,86), (86,101), (101,115), (115,131), (131,145), (145,161),
        (161,177), (177,193), (193,209)]

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
        randKanji = randint(0, len(kanjiSet))
        while kanjiSet[randKanji] in randKanjiSet:
            randKanji = randint(0, len(kanjiSet))
        randKanjiSet.append(kanjiSet[randKanji])

    return randKanjiSet


def main():
    kanjiDict = readKanjiFile(KANJI_FILE)
    isStudying = True

    while(isStudying):
        print('There are {} kanji available to study.'.format(len(kanjiDict)))
        studySetType = input("Would you like to study by (c)hapter or a (r)andom amount?")
        if studySetType == 'c':
            chapter = input('Which chapter would you like to study? ')
            chapRang = CHAP_RANGS[int(chapter)]
            studySet = list(kanjiDict.items())[chapRang[0]:chapRang[1]]
            shuffle(studySet)
        elif studySetType == 'r':
            kanAmt = input("How many kanji would you like to study? ")
            studySet = genRandKanjiSet(int(kanAmt), list(kanjiDict.items()))
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
