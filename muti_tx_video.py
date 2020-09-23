import os
import threading

from Crypto.Cipher import AES
import requests

from m3u8_handler import *
from sqlite_handler import *

THIS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_FILE_PATH = os.path.join(THIS_FILE_PATH, 'output')
SQLITE_FILE_PATH = os.path.join(THIS_FILE_PATH, 'sqlite')


def decrypt_video(sqlite_file):
    print("thread start......")
    file_saved_name = sqlite_file.split('.')[0] + ".mp4"
    m3u8_url, video_base_url, aes_key = get_url_key(os.path.join(SQLITE_FILE_PATH, sqlite_file))
    # print(m3u8_url, video_base_url, aes_key, sep='\n')
    seg_uri = get_seg_uri(m3u8_url)
    video_url = video_base_url + '?' + seg_uri
    # print(video_url)
    res = requests.get(video_url, stream=True)
    video_stream = b''
    for chunk in res.iter_content(chunk_size=1024 * 20):
        if chunk:
            video_stream += chunk
    decrypted_video = AES.new(aes_key, AES.MODE_CBC).decrypt(video_stream)
    with open(os.path.join(OUTPUT_FILE_PATH, file_saved_name), 'ab') as f:
        f.write(decrypted_video)
    print("thread end .....")


for file in os.listdir(SQLITE_FILE_PATH):
    if file.endswith('sqlite'):
        decrypt_video_thread = threading.Thread(target=decrypt_video, args=(file,))
        decrypt_video_thread.start()
