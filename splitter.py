import os
from pydub import AudioSegment
from pydub.utils import make_chunks

chunk_length_ms = 2000 # pydub calculates in millisec
load_path = "/data/musicnet/musicnet/data"
save_path = "/data/musicnet/musicnet/data_chunks"
files = os.listdir(load_path)

for i, file in enumerate(files):
    path_to_file = load_path + file
    audio_file = AudioSegment.from_file(path_to_file , "wav")
    chunks = make_chunks(audio_file, chunk_length_ms)

    #Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        print "exporting", chunk_name
        chunk.export(chunk_name, format="wav")
