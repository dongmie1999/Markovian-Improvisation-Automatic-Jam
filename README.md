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
key: C, D, E, F, G, A, B . In the same chord progression, key D sounds higher than C, key E sounds higher than D, and so on.  
mode: Could be major, dorian, phrygian, lydian, mixolydian, minor, locrian, major pentatonic and minor pentatonic. Each mode has its own trait, just select and find them.  
bpm: A positive integer, short of beats per minutes, 
reference：<br />
    1.[MusicCritique](https://github.com/josephding23/MusicCritique)<br />
    2.[mido](https://github.com/mido/mido)<br />
    3.[PyQt5-signals-slots](https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html?highlight=connectslotsbyname)<br />
