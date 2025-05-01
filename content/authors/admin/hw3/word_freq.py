import multiprocessing
import re
import sys

from collections import Counter
from os import cpu_count


def words_in_line(line):
    """Split a line into a list of words.

    Arguments
    ---------
    line : str
        The line to split.

    Returns
    -------
    list of str
        A list of words.
    """
    return re.compile(r"[\w]+").findall(line)


def worker(line):
    """Return a dictionary containing the frequency of words in `line`."""
    # Convert to lowercase, split into words, and count each word's frequency.
    line = line.lower()
    words = words_in_line(line)
    freq_dict = {}
    for w in words:
        freq_dict[w] = freq_dict.get(w, 0) + 1
    return freq_dict


def compute_word_frequency(input_file, nproc):
    """Find the frequency of each word in a text file.

    The file is assumed to contain multiple words per line that may be mixed
    case (i.e., both lowercase and uppercase) but no special characters or any
    punctuation.

    Arguments
    ---------
    input_file : str
        Path to an input file.
    nproc : int
        The number of processes used to count frequencies.

    Returns
    -------
    dict
        A dictionary with key-value pairs of the form `(word, frequency)`.
    """
    # TODO: Read the file into a list of lines.
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # TODO: Create a number of processes and distribute the lines among them
    #       to compute word frequencies.
    with multiprocessing.Pool(nproc) as pool:
        freq_dicts = pool.map(worker, lines)

    # TODO: Sum up word frequencies from all subprocesses into a single dict.
    global_freq = {}
    for d in freq_dicts:
        for word, freq in d.items():
            global_freq[word] = global_freq.get(word, 0) + freq

    return global_freq

if __name__ == "__main__":
    filename = sys.argv[1]
    word_freq_dict = compute_word_frequency(filename, cpu_count())
    for word in word_freq_dict:
        print(f"{word} - freq: {word_freq_dict[word]}")
