'''
A program that will make studing kanji easier.
William Ray Johnson
'''

from readKanjiFile import *

KANJI_FILE = 'kanjiTestFile.txt'
CHAP_RANGS = [(0,0), (0,0), (0,0), (0,15), (15,29), (29,43), (43,58), (58,72),
        (72,86), (86,101), (101,115), (115,131), (131,145), (145,161),
        (161,177), (177,193), (193,209)]

def studyReading(studySet):
    print("You are going to be reading these kanji: ")
    for entry in studySet:
        print(entry[0])

def studyWritting(studySet):
    print("You are going to be writting these kanji: ")
    for entry in studySet:
        print(entry[0])

def main():
    kanjiDict = readKanjiFile(KANJI_FILE)

    print('There are {} kanji available to study.'.format(len(kanjiDict)))
    chapter = input('Which chapter would you like to study? ')
    chapRang = CHAP_RANGS[int(chapter)]
    studySet = list(kanjiDict.items())[chapRang[0]:chapRang[1]]
    studyType = input('Would you like to study (r)eading or (w)riting?: ')
    if studyType == 'r':
        studyReading(studySet)
    elif studyType == 'w':
        studyWritting(studySet)


if __name__ == '__main__':
    main()
