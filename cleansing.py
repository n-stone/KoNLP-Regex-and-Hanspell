import pandas as pd
import numpy as np
import re
from hanspell import spell_checker
import sys

sys.stdout = open('stdout.txt', 'w')

# -*- coding: utf-8 -*-
df=pd.read_csv("/root/dmjeong/dmjeong/NLP/emotiondata.csv")


def cleasing(text):
    pattern = '[^A-Za-z0-9가-힣 ! ?]' # 자음, 모음, 특수기호 제거
    text = re.sub(pattern = pattern, repl='', string=text)
    pattern = '<[^>]*>' # html 제거
    text = re.sub(pattern = pattern, repl='', string=text)
    pattern = '!{1,}' # ! n개 이상 시 1개로 치환
    text = re.sub(pattern = pattern, repl='!', string=text)
    pattern = '\\?{1,}' # ? n개 이상 시 1개로 치환
    text = re.sub(pattern = pattern, repl='?', string=text)  
    return text

result = 0
df=df['Sentence']

for index in df:
  result = cleasing(index)
  spelled_sent = spell_checker.check(result)
  hanspell_sent = spelled_sent.checked
  print(hanspell_sent)

sys.stdout.close()