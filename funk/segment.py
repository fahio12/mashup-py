import csv

class segment:
    def __init__(self,startTime,endTime,times):
        self.startTime = startTime
        self.endTime = endTime
        self.startIndex = times.index(startTime)
        self.endIndex = times.index(endTime)
        self.frames = self.endIndex - self.startIndex

def getFastSegment(frameTimes,seconds = 15):
    # round times list to 3 decimal places so its easier to work with
    times = []
    for time in frameTimes:
        times.append(round(time,3))

    # algorithm to get the most amount of frames in the time(seconds)
    fastest = segment(times[0],times[0],times) #sets the fastest temp var (most amount of frames)
    slowest = segment(times[0],times[len(times)-1],times) #sets the slowest temp var (least amount of frames)
    for i in range(len(times)):
        dinamicTimes = times[i:]
        for j in range(len(dinamicTimes)):
            time = dinamicTimes[j] - times[i]
            if time >= seconds:
                seg = segment(times[i],dinamicTimes[j],times)
                if seg.frames > fastest.frames: #same concept for slowest segment jusut change the sign and vars
                    fastest = seg
                break
    print(f"{fastest.startTime} - {fastest.endTime} = {fastest.frames}")
