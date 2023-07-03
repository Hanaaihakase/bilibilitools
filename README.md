# bilitools

- bilibilitools、一個自用的、也歡迎公用的bilibili視頻下載的python腳本工具、力圖簡潔而優雅。
- 想要脫離[bilibili-api](https://github.com/Nemo2011/bilibili-api)這個pip包的DIY產物。
- 使用前請確保安裝ffmpeg、Windows系統建議使用chocolatey安裝、即`choco install ffmpeg`。
- 直接 `git clone https://github.com/Hanaaihakase/bilibilitools.git`、進入本文件夾、在終端輸入 `python main.py` 、根據提示使用即可。
- 初次使用、需要輸入sessdata、請登錄bilibili後按下`F12`在cookie中查看。一旦輸入、即保存在同文件夾下的`sessdata.json`中、無需再次輸入。
- 原理是使用bilibili公用的api接口。參考[哔哩哔哩-API收集整理](https://socialsisteryi.github.io/bilibili-API-collect/)。
- Windows系統下的非法標題會經過剔除非法字符處理、請注意。
- 默認下載非會員下的最高音質和最高畫質。
- 目前支持單個bvid輸入、以後會支持批量輸入。
- 2023/6/30、目前版本爲1.1。
- 2023/7/3、目前版本爲1.2、重構了代碼、已支持txt文件批量導入bvid。