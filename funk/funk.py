from spleeter.separator import Separator


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
