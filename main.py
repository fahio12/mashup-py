from funk import funk,segment

if __name__ == '__main__':
    times = segment.getFrames(song = "army")
    fast = segment.getSegment(mode = "fast",frames_time = times)
    slow = segment.getSegment(mode = "slow",frames_time = times)
    print(f"Fast: {fast.startTime}[{fast.startIndex}] - {fast.endTime}[{fast.endIndex}] = {fast.frames}")
    print(f"Slow: {slow.startTime}[{slow.startIndex}] - {slow.endTime}[{slow.endIndex}] = {slow.frames}")
# todo slice audio and output the slow and fast part of the song
