# Markovian-Improvisation-Automatic-Jam  
Automatic improvisation based on markov model, select your key and mode, input the chord number, 
6 types of piano accompaniment in 4/4 and 3/4, totally 12 kinds of piano accompaniment.

## Introduction  
    available key: C, D, E, F, G, A, B  # key C# would be C, and Db would be D
    abailable mode: major, dorian, phrygian, lydian, mixolydian, minor, locrian, major pentatonic and minor pentatonic.

    python libraries to install:  
        hmmlearn, numpy, pypianoroll, pygame, mido, musthe, PyQt5, PyQt-tools(**windows only**)  
 
core: my/all1.py  
GUI: run my/v4main.py  
GUI seems like this.  
<div align=center><img width="556" height="500" src="https://github.com/dongmie1999/Markovian-Improvisation-Automatic-Jam/blob/master/sreenshot.png"/></div>  

## Option  
Generate melody automatically base on your chord progression.<br />
**bpm**: positive integer，beats per minutes.<br />
**time_signature**: the number of beats in each bar, usually in the form of n/m.<br />
The default rhythmic accompaniment currently only supported 4/m or 3/m.<br />
**key**: char, the first note of scale，could be C D E F G A B.<br />
**mode**: string, decide the scale of impromptu, could be<br />
          major, dorian, phrygian, lydian, mixolydian, minor, locrian,<br />
          major pentatonic and minor pentatonic.<br />
          ATTENTION: mode decide only your impromptu note,<br />
          do not include the chord.<br />
**file_path**: the path and the name of midi file.<br />
**chord_progression**: a list of you chords.<br />
**intensity**: float between 0 and 1, the parameter of horizontal improvisation and vertical improvisation,<br />
               0 means totally vertical improvisation,<br />
               1 means totally horizontal improvisation.<br />
**repeat**: the times that the same chord progression will be repeated.<br />
    
reference：<br />
    1.[MusicCritique](https://github.com/josephding23/MusicCritique)<br />
    2.[mido](https://github.com/mido/mido)<br />
    3.[PyQt5-signals-slots](https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html?highlight=connectslotsbyname)<br />
