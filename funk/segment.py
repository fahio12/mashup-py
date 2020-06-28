import csv
import librosa
from pydub import AudioSegment
import numpy as np

class segment:
    def __init__(self,startTime,endTime,times,length):
        self.startTime = startTime
        self.endTime = endTime
        self.length = length
        self.startIndex = times.index(startTime)
        self.endIndex = times.index(endTime)
        self.frames = self.endIndex - self.startIndex

def getFrames(path):
    """Gets onset frames and times

    Parameters:
    song (string): name of the song

    Output:
    .wav song with the clicks for developing purposes
    .csv file with timesptamps of the clicks

    Returns:
    frames_time: list with all the times with onset
    """
    y, sr = librosa.load(path)
    # #get frames
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    # #turn frames into time
    frames_time = librosa.frames_to_time(onset_frames, sr=sr)
    # #create clicks
    clicks = librosa.clicks(frames_time, sr=sr, length=len(y))
    #output
    librosa.output.write_wav(f'./output/audio-onset.wav', y + clicks, sr)
    librosa.output.times_csv(f'./output/audio-onsetimes.csv',frames_time)
    return frames_time

def getSegment(mode,frames_time,seconds = 15):
    """Gets Fastest/Slowest segments of the song

    Parameters:
    mode (string): "fast"/"slow"
    seconds (int): seconds for the segments
    frames_time (list): list with all the onsets times (getFrames(song))

    Returns:
    object with details about the segments
    (startTime,startIndex,endTime,endIndex,frames,lengths=# of secs)
    """
    # round times list to 3 decimal places so its easier to work withs
    times = []
    for time in frames_time:
        times.append(round(time,3))
    # algorithm to get the most/least amount of frames in the time(seconds)
    fastest = segment(times[0],times[0],times,seconds) #sets the fastest temp var (most amount of frames)
    slowest = segment(times[0],times[len(times)-1],times,seconds) #sets the slowest temp var (least amount of frames)
    for i in range(len(times)):
        dinamicTimes = times[i:]
        for j in range(len(dinamicTimes)):
            time = dinamicTimes[j] - times[i]
            if time >= seconds:
                seg = segment(times[i],dinamicTimes[j],times,seconds)
                if mode == "fast":
                    if seg.frames > fastest.frames:
                        fastest = seg
                    break
                else:
                    if seg.frames < slowest.frames:
                        slowest = seg
                    break
    if mode == "fast":
        return fastest
    else:
        return slowest

def export(path,seg,slice = 0,move = 0):
    """Exports a segment and lets you do some changes to it
    like adjusting the length and moving it

    Parameters:
    song (string): name of the song
    seg (segment): segment object with details about the segment
    slice (int): adjust the length of the segment (use negatives to decrease)
    move (int): move the segment (use negatives to decrease)

    Output:
    .mp3 file with the segment

    """
    song_file = AudioSegment.from_mp3(path)
    time = ((seg.startTime+move)*1000)+(seg.length*1000)
    audio = song_file[:time]
    time = (seg.length+slice) * 1000
    audio = audio[-time:]
    audio.export("segment.mp3", format="mp3")
