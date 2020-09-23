# tencentedu_video_decrypt
## 腾讯课堂缓存*.m3u8.sqlite视频解密

sqlite: 缓存文件存放目录，手机视频缓存后，可通过`adb pull /sdcard/Android/data/com.tencent.edu/files/tencentedu/video/txdownload/`把手机缓存文件pull到该目录下

output：解密后视频存放目录

muti_tx_video.py：多线程处理

tecent_video.py：非多线程



## 第三方库依赖

```
pip install requests
pip install m3u8
pip install pycrypto
```



## 不完善

1. 解密后不能还原对应视频的文件名
2.  通过下载完整视频再解密受网络影响
3. 考虑直接走sqlite文件得到完整视频，16byte流相加合并是可以得到完整视频的，但声音并不能同步，放弃了
4. 可以通过类似方法（参考文章 [破解腾讯课堂缓存视频](https://www.jianshu.com/p/b3bb3104672d?utm_campaign=haruki))获取到的多个解密后的片段视频，但观看不方便，放弃
5.  sqlite文件如果是很早之前缓存的，方法失效，可能是sign之类的信息失效，如果想解密视频文件，需要是近期缓存的sqlite文件
6. 很多视频网站的视频加解密方式是类似这样的，有需要的可自行尝试

## 其他

参看我的博客[腾讯课堂缓存视频破解](https://1eq066.coding-pages.com/post/tencent_edu/)