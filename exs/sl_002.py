# coding: utf-8

s1 = "Dear Sir,|I wish|to complain|in the|strongest possible|terms" 
s2 = "About The Song Which Had Just Broadcast About The Lumberjack Who Wears Women'S Clothes."
s3 = "[błąd w druku] Many of my best friends are lumberjacks and only a few of them are transvestites. "
s4 = "yours faithfully, brigadier sir charles arthur strong (ms.). "
s5 = "xxxP.S. I have never kissed the editor of the Radio Times.xxx"

print s1.replace('|', ' ')
print s2.lower()
print s3[:15]
print s3[15:]
print s4.title()
print s5.strip('xxx')
