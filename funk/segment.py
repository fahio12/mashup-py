import csv
import librosa
import numpy as np

class segment:
    def __init__(self,startTime,endTime,times):
        self.startTime = startTime
        self.endTime = endTime
        self.startIndex = times.index(startTime)
        self.endIndex = times.index(endTime)
        self.frames = self.endIndex - self.startIndex

def getFrames(song):
    """Gets onset frames and times

    Parameters:
    song (string): name of the song

    Output:
    .wav song with the clicks for developing purposes
    .csv file with timesptamps of the clicks

    Returns:
    frames_time: list with all the times with onset
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
    return frames_time

def getSegment(mode,seconds = 15,frames_time):
    """Gets Fastest/Slowest segments of the song

    Parameters:
    mode (string): "fast"/"slow"
    seconds (int): seconds for the segments
    frames_time (list): list with all the onsets times (getFrames(song))

    Returns:
    object with details about the segments
    (startTime,startIndex,endTime,endIndex,frames)
    """
    # round times list to 3 decimal places so its easier to work withs
    times = []
    for time in frameTimes:
        times.append(round(time,3))
    # algorithm to get the most/least amount of frames in the time(seconds)
    fastest = segment(times[0],times[0],times) #sets the fastest temp var (most amount of frames)
    slowest = segment(times[0],times[len(times)-1],times) #sets the slowest temp var (least amount of frames)
    for i in range(len(times)):
        dinamicTimes = times[i:]
        for j in range(len(dinamicTimes)):
            time = dinamicTimes[j] - times[i]
            if time >= seconds:
                seg = segment(times[i],dinamicTimes[j],times)
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
