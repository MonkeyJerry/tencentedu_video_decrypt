import sqlite3 as db


def get_url_key(sqlite_file):
    con = db.connect(sqlite_file)
    cu = con.cursor()
    result = cu.execute('SELECT * FROM caches')

    data = result.fetchall()
    m3u8_url = data[0][0]
    # video_base_url = data[2][0]
    video_base_url = data[2][0].split("?")[0]
    aes_key = data[1][1]
    return m3u8_url, video_base_url, aes_key


if __name__ == '__main__':
    print(get_url_key('sqlite/e7b89b8f5214b85c6e9fdf83d638d41a.m3u8.sqlite'))
