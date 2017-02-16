'''
A program that will make studing kanji easier.
William Ray Johnson
'''

from readKanjiFile import *
from random import choice, shuffle

KANJI_FILE = 'kanjiTestFile.txt'
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

def main():
    kanjiDict = readKanjiFile(KANJI_FILE)
    isStudying = True

    while(isStudying):
        print('There are {} kanji available to study.'.format(len(kanjiDict)))
        chapter = input('Which chapter would you like to study? ')
        chapRang = CHAP_RANGS[int(chapter)]
        studySet = list(kanjiDict.items())[chapRang[0]:chapRang[1]]
        shuffle(studySet)
        studyType = input('Would you like to study (r)eading or (w)riting?: ')
        if studyType == 'r':
            studyReading(studySet)
        elif studyType == 'w':
            studyWritting(studySet)
        willCont = input('Would you like to continue studying? (y)es (n)o: ')
        if willCont[0] == 'n':
            isStudying = False


if __name__ == '__main__':
    main()
