README for 'txt2srt' script and executable
Version 1.0
CC by 4.0 Hiram Ring, October 2015, www.hiramring.com, hiram1@e.ntu.edu.sg
http://creativecommons.org/licenses/by/4.0/
Freely available for use, distribution, and modification

This README.txt file is intended to be copied along with the 'txt2srt' script.
This folder contains the following files:

README.txt (this readme file)
txt2srt.cfg (the configuration file for the executable and python script)
txt2srt.exe (the executable script file)
txt2srt.py (the Python script from which the executable is built)

The script is designed for making Toolbox .txt files (http://www-01.sil.org/computing/toolbox/) into .srt for subtitles in programs such as VLC, Aimersoft, or Premier Pro. It uses the 'txt2srt.cfg' file to determine the markers in your Toolbox files. The time-alignments read from the Toolbox files are assumed to have been created by Transcriber 1.5.1 (http://sourceforge.net/projects/trans/files/transcriber/1.5.1/) and converted using 'trs2txt' (https://github.com/themadafrican/trs2txt) or a similar program. Edit the 'txt2srt.cfg' file in a standard Text Editor, and replace the following markers with those that refer to the same fields in your own Toolbox texts:
 \ref (line name and number)
 \ELANBegin (timecode beginning)
 \ELANEnd (timecode ending)
 \t (vernacular text - Toolbox default is \tx)
 \f (free translation - Toolbox default is \ft)

To use the script, run it in a directory that contains your Toolbox .txt files and the edited 'txt2srt.cfg' file. You may need to ensure that your files are in Unicode format. To ensure that separate .srt files are created for separate records (texts) you may need to export each record from your Toolbox project. The script/executable will create a corresponding .srt file for each .txt file in the directory, using the configuration file as a guide. Existing .srt files will be overwritten.

Things to note:
1) not all programs will import the .srt files produced.
2) vernacular text lines that split over several lines (i.e. have line breaks) will be combined, so if you have an extremely long sentence this may result in too much text on the screen.
3) free translations which split over several lines will not be combined, so if this happens you will need to edit the texts manually.
4) unicode/non-unicode conversions may not work exactly as expected, depending on the user's individual software. Hopefully it does.
5) if the resulting .srt file only contains numbers, the markers in the .cfg file are incorrect - you may need to pay closer attention to extra spaces, etc.
