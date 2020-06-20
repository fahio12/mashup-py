from funk import funk,segment

if __name__ == '__main__':
    # funk.split(song="cradles")
    times = funk.getFrames(song = "army")
    segment.getFastSegment(times)
