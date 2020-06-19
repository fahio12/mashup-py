from spleeter.separator import Separator
import librosa
import numpy as np

def split(song,stems=2):
    """Separates instruments from the song

    Parameters:
    song (string): name of the song
    stems (int): number of instruments to split the song into

    Output:
    .wav files inside a folder named after the song. Files are named after the
    instrument. Does not return anything

    """
    separator = Separator(f'spleeter:{stems}stems')
    separator.separate_to_file(f'./songs/{song}.mp3', './output/instruments')

def getFrames(song):
    """Gets onset frames and times

    Parameters:
    song (string): name of the song

    Output:
    .wav song with the clicks for developing purposes
    .csv file with timesptamps of the clicks
    """
    y, sr = librosa.load(f'./songs/{song}.mp3')
    # #get frames
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    # #turn frames into time
    frames_time = librosa.frames_to_time(onset_frames, sr=sr)
    # #create clicks
    clicks = librosa.clicks(frames_time, sr=sr, length=len(y))
    #output
    librosa.output.write_wav(f'./output/{song}-onset.wav', y + clicks, sr)
    librosa.output.times_csv(f'./output/{song}-onsetimes.csv',frames_time)
