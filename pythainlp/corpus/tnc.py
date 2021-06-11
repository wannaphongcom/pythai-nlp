# -*- coding: utf-8 -*-
"""
Thai National Corpus word frequency

Credit: Korakot Chaovavanich‎
https://www.facebook.com/photo.php?fbid=363640477387469&set=gm.434330506948445&type=3&permPage=1
"""

__all__ = [
    "word_freqs",
    "unigram_word_freqs",
    "bigram_word_freqs",
    "tigram_word_freqs"
]

from collections import defaultdict
from typing import List, Tuple

from pythainlp.corpus import get_corpus
from pythainlp.corpus import get_corpus_path


_FILENAME = "tnc_freq.txt"
_BIGRAM = "tnc_bigram_word_freqs"
_TIGRAM = "tnc_tigram_word_freqs"


def word_freqs() -> List[Tuple[str, int]]:
    """
    Get word frequency from Thai National Corpus (TNC)
    \n(See: `dev/pythainlp/corpus/tnc_freq.txt\
    <https://github.com/PyThaiNLP/pythainlp/blob/dev/pythainlp/corpus/tnc_freq.txt>`_)
    """
    lines = list(get_corpus(_FILENAME))
    word_freqs = []
    for line in lines:
        word_freq = line.split("\t")
        if len(word_freq) >= 2:
            word_freqs.append((word_freq[0], int(word_freq[1])))

    return word_freqs


def unigram_word_freqs() -> defaultdict:
    """
    Get unigram word frequency from Thai National Corpus (TNC)
    """
    lines = list(get_corpus(_FILENAME))
    _word_freqs = defaultdict(int)
    for i in lines:
        _temp = i.strip().split("	")
        if len(_temp) >= 2:
            _word_freqs[(_temp[0], _temp[1])] = int(_temp[-1])

    return _word_freqs


def bigram_word_freqs() -> defaultdict:
    """
    Get bigram word frequency from Thai National Corpus (TNC)
    """
    _path = get_corpus_path(_BIGRAM)
    _word_freqs = defaultdict(int)
    with open(_path, "r", encoding="utf-8-sig") as fh:
        for i in fh.readlines():
            _temp = i.strip().split("	")
            _word_freqs[(_temp[0], _temp[1])] = int(_temp[-1])

    return _word_freqs


def tigram_word_freqs() -> defaultdict:
    """
    Get tigram word frequency from Thai National Corpus (TNC)
    """
    _path = get_corpus_path(_TIGRAM)
    _word_freqs = defaultdict(int)
    with open(_path, "r", encoding="utf-8-sig") as fh:
        for i in fh.readlines():
            _temp = i.strip().split("	")
            _word_freqs[(_temp[0], _temp[1], _temp[2])] = int(_temp[-1])

    return _word_freqs
