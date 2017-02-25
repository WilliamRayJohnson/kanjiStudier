'''
A set of functions that will read in a file containing kanji and its readings
for use in a studier.
William Ray Johnson
'''

from collections import OrderedDict

def constructKanjiDictEntry(kanji, words, wordReadings):
    wordsAndReadings = {}

    for word in range(len(words)):
        wordsAndReadings.update({words[word]:wordReadings[word]})
    
    return {kanji : wordsAndReadings}


def readKanjiFile(filename):
    kanjiDictionary = []
    chapEntry = OrderedDict()
    kanji = ''
    words = []
    wordReadings = []
    kanjiFile = open(filename, 'r')

    #process first line which should be #1 kanji label
    kanjiFile.readline()

    for line in kanjiFile:
        line = line.rstrip()

        if line != '':
            if line[0] != '@':
                if line[0] != '#':
                    lineElements = line.split(' ')

                    if lineElements[0] == 'kanji:':
                        kanji = lineElements[1]
                    elif lineElements[0] == 'words:':
                        words = lineElements[1:]
                    elif lineElements[0] == 'wordReadings:':
                        wordReadings = lineElements[1:]
                    else:
                        raise NameError('Label not found')
                else:
                    entry = constructKanjiDictEntry(kanji, words, wordReadings)
                    chapEntry.update(entry)
            else:
                kanjiDictionary.append(chapEntry)
                chapEntry = OrderedDict()

    kanjiFile.close()
    entry = constructKanjiDictEntry(kanji, words, wordReadings)
    chapEntry.update(entry)
    kanjiDictionary.append(chapEntry)
    return kanjiDictionary
