## 说明文档

文件|说明
--|--
image|视频切分图片存储位置
config.conf|配置文件
config.py|配置文件调用
peopleRecognition.py|行人检测
taobao\_api.py|调用淘宝商品识别接口
video2graph.py|视频转图片
progarm.py|执行文件
requirements.txt|环境依赖
video_cut.py|剪切视频（按需调用）

1. pip3 install -r requirements.txt
2. 在config.conf配置自己的cookie
3. 配置视频路径，根目录
4. python program.py

行人标记：
![示例]("https://github.com/SuiMingYang/productvideo2feature/_readme/example.png")

商品接口返回：
![示例]("https://github.com/SuiMingYang/productvideo2feature/_readme/feature.png")
