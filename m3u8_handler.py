import m3u8
import re

def get_seg_uri(m3u8_file):
    m3u8_obj = m3u8.load(m3u8_file)
    seg_start_uri = m3u8_obj.segments[0].uri
    seg_end_uri = m3u8_obj.segments[-1].uri
    end_time = re.search('end=([0-9]*)', seg_end_uri).group(1)
    pattern = r'end=[0-9]*'
    seg_uri = re.sub(pattern, r'end={}'.format(end_time), seg_start_uri)
    return seg_uri.split('?')[-1]
