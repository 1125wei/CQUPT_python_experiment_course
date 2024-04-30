import requests
import re
import os
import json
from pprint import pprint  # 格式化输出模块，方便观察层级
import subprocess
ffmpeg_path = r'E:\ffmpeg-2023-11-09-git-acf63d5350-essentials_build\bin'
folder_path = 'video'
if not os.path.exists(folder_path):  # 检查是否存在“video”文件夹，如果没有就创建
    os.makedirs(folder_path)
url = input("输入url:")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "referer": "https://www.bilibili.com/",
"Cookie":"i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid4=6284CE9E-58AC-A961-8034-39AC76856AFC06953-022081209-LKyJvix6SQi%2B82s5omlXFg%3D%3D; is-2022-channel=1; buvid3=E31524B0-A6BC-1270-2891-1CB30A114E7276229infoc; b_nut=1691842876; _uuid=23B83D410-EE6D-D8D3-9F10A-2C110785ED3101081221infoc; header_theme_version=CLOSE; hit-new-style-dyn=1; enable_web_push=DISABLE; LIVE_BUVID=AUTO5816984852393005; CURRENT_FNVAL=4048; DedeUserID=25922591; DedeUserID__ckMd5=a7ec17d1f99bb197; CURRENT_QUALITY=80; rpdid=|(J|)lJ|~|YY0J'u~|Jku~)~~; hit-dyn-v2=1; PVID=1; fingerprint=1aba8348eca985ed23e539e88d5dc6af; buvid_fp=1aba8348eca985ed23e539e88d5dc6af; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; home_feed_column=5; browser_resolution=1652-916; SESSDATA=8f700636%2C1729596891%2C09327%2A42CjDCEX1GOJiS2Xvmmktax20cRp-Q05UH-nbGEybIdewNFte4wMcH4mpOT9Btsx8IhpgSVkl0N2pqWWRCWU1melp5NmNuTDM5NnNMYVdfdFJzcGJVcGxDYjhqc2lqbDd1ZVJ4VlZwSkhMTlMzZlFpbVJkUU5LRGRXaXEwOXM2QVdLMDlOV1paS1N3IIEC; bili_jct=f154d9997b4fff16b1470625acfa966f; bp_video_offset_25922591=924304806404685840; bsource=search_baidu; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; sid=8t2ugqnf; b_lsid=3BCD101B5_18F1ECFF8E1"
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
video_name = re.findall('"title":"(.*?)",', response.text)[0].replace(' ', '')  # 视频标题，需要消去视频标题中可能存在的空格，避免命令行报错
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]  # 视频信息
json_data = json.loads(html_data)  # 转换为json字典类型数据，方便提取视频画面和音频 注意json.load 和json.loads的区别，前者需要文件作为参数，后者需要字符串作为参数
print(video_name)
print(json_data)  # 变成键值对取值
pprint(json_data)
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_url = json_data['data']['dash']['video'][0]['baseUrl']
print(audio_url)
print(video_url)
video_content = requests.get(url=video_url, headers=headers).content
audio_content = requests.get(url=audio_url, headers=headers).content
# 保存图像和音频
with open('video\\' + video_name + '.mp4', mode='wb') as video:
    video.write(video_content)
with open('video\\' + video_name + '.mp3', mode='wb') as audio:
    audio.write(audio_content)
# 合并音频和视频
cmd = fr'ffmpeg -i "E:\Python_Code\RedRockWork\video\{video_name}.mp4" -i "E:\Python_Code\RedRockWork\video\{video_name}.mp3" -c:v copy -c:a aac -strict experimental "E:\Python_Code\RedRockWork\video\{video_name}合成完成版.mp4"'
subprocess.run(cmd, shell=True)
# import ffmpeg
#
# # 视频文件和音频文件的路径
# video_file = fr"E:\Python_Code\红岩作业\video\{video_name}.mp4"
# audio_file = fr"E:\Python_Code\红岩作业\video\{video_name}.mp3"
#
# # 合并后的输出文件路径
# output_file = fr"E:\Python_Code\红岩作业\video\{video_name}转换完成.mp4"
#
# # 使用 ffmpeg 函数合并视频和音频
# ffmpeg.input(video_file).output(output_file, vf='pad=ceil(iw/2)*2:ceil(ih/2)*2').run(overwrite_output=True)
# ffmpeg.input(audio_file).output(output_file, acodec='aac', strict='experimental').run(overwrite_output=True)

