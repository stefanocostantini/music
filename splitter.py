import os
from pydub import AudioSegment
from pydub.utils import make_chunks

chunk_length_ms = 2000 # pydub calculates in millisecs
load_path = "/data/music/musicnet/test/"
save_path = "/data/music/musicnet/test_chunks/"
files = os.listdir(load_path)

for i, file in enumerate(files):
    file_label = file.split(".")[0]
    path_to_file = load_path + file
    audio_file = AudioSegment.from_file(path_to_file , "wav")
    chunks = make_chunks(audio_file, chunk_length_ms)

    #Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        chunk_name = save_path + "{0}-chunk{1}.wav".format(file_label, i)
        print "exporting", chunk_name
        chunk.export(chunk_name, format="wav")
