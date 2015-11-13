# -*- coding: utf-8 -*-
# CC by 4.0 Hiram Ring, October 2015, www.hiramring.com, hiram1@e.ntu.edu.sg
# http://creativecommons.org/licenses/by/4.0/
# designed for making Toolbox .txt files into .srt
# for usage refer to the accompanying README.txt file
import glob
import datetime
import re

config = open('txt2srt.cfg', 'r') # open the config file located in the same directory

ref = '' # create a blank string to store the 'ref' tag from the config file for processing
tbeg = '' # create a blank string to store the 'tbeg' tag from the config file for processing
tend = '' # create a blank string to store the 'tend' tag from the config file for processing
ver = '' # create a blank string to store the 'text' tag from the config file for processing
trans = '' # create a blank string to store the 'trans' tag from the config file for processing

for line in config: # read all the lines and look for the correct tags
    if line[0:18] == 'reference number: ': # read the reference number tag
        ref += line[18:-1]+' ' # append it to the 'ref' string
    if line[0:20] == 'timecode beginning: ': # read the tag that identifies the beginning of a timecode
        tbeg += line[20:-1]+' ' # append it to the 'tbeg' string
    if line[0:17] == 'timecode ending: ': # read the tag that identifies the end of a timecode
        tend += line[17:-1]+' ' # append it to the 'tend' string
    if line[0:29] == 'text for language subtitles: ': # read the tag that identifies the subtitles in the vernacular language
        ver += line[29:-1]+' ' # append it to the 'text' string
    if line[0:22] == 'text for translation: ': # read the tag that identifies the translation subtitles
        trans += line[22:-1]+' ' # append it to the 'trans' string
    
filenames = [] # create an empty list called 'filenames' to keep track of the .txt files in the directory

for index, file in enumerate(glob.glob("*.txt")): # use glob to create an enumerated list of the .txt files in the directory
    filenames.append(file) # append the names of the .txt files in the directory to a list

for infile in filenames: # create a 'for' loop to iterate through all the .txt files in the directory as listed in the 'filenames' list
    textfile = open(infile,'r') # Open each .txt file in 'read' mode

    srtfile = open(str(infile[0:-3])+'srt','w') # create a corresponding .srt file in 'write' mode to store the values we want from the .txt file
    
    for line in textfile: # get all the lines we want from the .txt file and write them into a corresponding (new) .srt file
        if line[0:len(ref)] == ref: # identify the line headed by 'ref' (where the first characters correspond to 'ref '
            srtfile.write(str(line[-4:-1]).lstrip('0')+'\n') # get the reference number from the end of the 'ref' line and strip the zeros, then add a newline character
        if line[0:len(tbeg)] == tbeg: #'\\ELANBegin ': # identify the line headed by 'tbeg'
            templine = str(datetime.timedelta(seconds=float(line[len(tbeg):-1]))).rstrip('0')+' --> ' # append it to the 'temp' list, converting the timecode from raw seconds to a more standard DD:MM:SS format, stripping the trailing zeros and adding the dashed arrow
            srtfile.write(templine.replace('0:00: ', '0:00:00.0 ')) # replace the initial start string - without the final '0.0' this was causing issues on loading the subtitle using a Mac
        if line[0:len(tend)] == tend: # identify the line headed by 'tend'
            templine = str(datetime.timedelta(seconds=float(line[len(tend):-1]))).rstrip('.0')
            srtfile.write(templine+'\n') # append it to the file, converting the timecode from raw seconds to a more standard DD:MM:SS format
        if line[0:len(ver)] == ver: # identify the line headed by 'ver'
            templine = re.sub("  +", " ", line[len(ver):-1]) # get the vernacular text lines
            srtfile.write(templine+' ') # write each of the vernacular text lines with a trailing space in case there are multiple
        if line[0:len(trans)] == trans: # identify the line headed by 'trans'
            templine = line[len(trans):-1] # get the translation line
            templine2 = '\n'+templine+'\n\n' # add new line characters for formatting
            srtfile.write(templine2) # append it to the file
            
    textfile.close() # close the textfile now that all the data has been written to the 'srtfile'
    srtfile.close() # close the srtfile as well
    
# return to the head of the for loop and continue as long as there is a .txt file in the 'filenames' list
