from readKanjiFile import *

def main():
    testDict = readKanjiFile('genkiKanji.txt')

    for entry in list(testDict.items()):
        print(entry)
    print('There are {} entries in this dictionary.'.format(len(testDict)))

if __name__ == '__main__':
    main()
