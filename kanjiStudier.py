'''
A program that will make studing kanji easier.
William Ray Johnson
'''

from readKanjiFile.py import *

KANJI_FILE = 'kanjiTestFile.txt'

def main():
    kanjiDict = readKanjiFile(KANJI_FILE)

    print('There are {} kanji available to study.'.format(len(kanjiDict)))
    studyType = input('Would you like to study (r)eading or (w)riting?: ')
    if studyType == 'r':
        studyReading()
    elif studyType == 'w':
        studyWritting()


if __name__ == '__main__':
    main()
