__author__ = 'Vaio-190X'

import pysrt

def produce_dict(filename):
    srt = pysrt.open(filename)
    start = []
    end = []
    text = []
    for sub in srt:
        start.append(sub.start.ordinal)
        end.append(sub.end.ordinal)
        text.append(sub.text)
    srt_dict = dict()
    srt_dict['start'] = start
    srt_dict['end'] = end
    srt_dict['text'] = text
    srt_dict['filename'] = [filename] * len(start)
    return srt_dict

d = produce_dict('c:\\yahel\\The Simpsons.s25e11.srt')
import pandas
pandas.DataFrame.from_dict(d)