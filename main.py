from funk import funk,segment
from tkinter.filedialog import askopenfilename

if __name__ == '__main__':
    print("Welcome to funk-py select select the mp3 file you want to use")
    path = askopenfilename(filetypes=[("MP3 files", ".mp3")])
    mode = input("Select mode (fast/slow): ")
    times = segment.getFrames(path = path)
    seg = segment.getSegment(mode = mode,frames_time = times)
    segment.export(path=path,seg=seg)
    funk.split(path)
