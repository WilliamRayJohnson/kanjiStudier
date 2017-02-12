from readKanjiFile import *

def main():
    testDict = readKanjiFile('kanjiTestFile.txt')

    print('There are {} entries in this dictionary.'.format(len(testDict)))
    for entry in testDict:
        print(entry)

if __name__ == '__main__':
    main()
