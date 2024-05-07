import jieba.posseg as psq

text = '我昨天去南山植物园玩'
seg = psq.cut(text)
for ele in seg:
    print(ele)
