#!/usr/bin/env python3

import subprocess
import sys
import tempfile
import os
from vosk import Model, KaldiRecognizer, SetLogLevel
def transcribe(name, lines, file):
    SAMPLE_RATE = 16000

    SetLogLevel(-1)

    model = Model(lang="en-us")
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(True)
    with tempfile.NamedTemporaryFile(dir="./", delete=False) as temp:
        temp.write(file.file.read())
        temp.flush()
        with open(name+".srt", 'w') as f:
            with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                                        temp.name,
                                        "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                                        stdout=subprocess.PIPE ).stdout as stream:
                temporary=rec.SrtResult(stream, words_per_line=lines)
                f.write(temporary)
    os.remove(temp.name) 
    return "./"+name+".srt"
# audio=sys.argv[1]
# file_name=sys.argv[2]
# transcribe(file_name+".srt", audio)