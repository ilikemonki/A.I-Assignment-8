# Group 1: Meng Cha, Justin Terry
# CECS 451 A.I.
# 11/21/2019

import speech_recognition as sr
import os
import distance


class Speech:

    def __init__(self):
        self.original = []      # original sentences
        self.recognized = []    # sentences from audio file
        self.similarity = []    # Scores

    # read file
    def read_original(self, inFile):
        f = open(inFile, 'r')           # open file and read only
        line = 1
        while line:                     # loops until EOF
            line = f.readline()        # read next line
            self.original.append(line)  # add line to array
        f.close()                       # close file

    # Convert audio to text
    def conv_audio(self, inDir):        # Converts audio into list of strings
        r = sr.Recognizer()             # Recognizes speech
        for audioName in os.listdir(inDir):     # Loop through the audio files
            audio2text = sr.AudioFile(inDir + '/' + audioName)
            # Takes a while to go through all files.
            with audio2text as source:
                audio = r.record(source)
                self.recognized.append(r.recognize_google(audio))   # add recognized sentence to array

    # Compare strings
    def comp_string(self):
        for n in range(self.original.__len__() - 1):
            orig = self.original[n].lower().split()         # lowercase and split sentence into words
            recogn = self.recognized[n].lower().split()
            errors = distance.levenshtein(orig, recogn)     # Compare the two list of words
            score = len(orig) - errors                      # Get score
            self.similarity.append(score)                   # append to array
            #print(self.original[n].lower())
            #print(self.recognized[n].lower())
            #print(str(score) + '/' + str(len(orig)))


if __name__ == '__main__':
    sp = Speech()
    sp.read_original("How Speech Recognition Works.txt")
    sp.conv_audio("Audio Files")    # the parameter is the directory of the audio files
    sp.comp_string()
