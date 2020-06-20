import csv

def getFastSegment(frameTimes,seconds = 7):
    # round times list to 3 decimal places so its easier to work with
    times = []
    for time in frameTimes:
        times.append(round(time,3))
    # algorithm to get the most amount of frames in the time(seconds)
    for i in range(len(times)):
        dinamicTimes = times[i:]
        print("--------new--------")
        for j in range(len(dinamicTimes)):
            time =  dinamicTimes[j] - times[i]
            if time >= seconds:
                indexJ = times.index(dinamicTimes[j])
                print(f"{dinamicTimes[j]} [{indexJ}] - {times[i]} [{i}] = {time}") #modify later
                break
    """
    the algo gets all 7 second segments of the song with the starting
    index and the ending index and the starting second and ending second
    and lastly the time of the segment(around 7 seconds)
    TODO: CALCULATE THE AMOUNT OF FRAMES OF EACH SEGMENT USING THE INDEXES OF
    THE LIST AND RETURN THE SECONDS
    """
