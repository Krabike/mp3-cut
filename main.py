import os
from tqdm import tqdm
from pydub import AudioSegment

set_time = 91000
input_dir = './files-here'
output_dir = './cuted-files'

files = [f for f in os.listdir(input_dir) if f.endswith('.mp3')]

with tqdm(total=len(files), desc='Cutting', unit='file') as pbar:
    for filename in files:
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        pbar.set_postfix({'file': filename})
        
        song = AudioSegment.from_mp3(input_path)
        first_minute = song[:set_time]
        first_minute.export(output_path, format='mp3')
        
        pbar.update(1)