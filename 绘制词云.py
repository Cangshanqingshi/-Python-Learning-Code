import jieba
import wordcloud

''
# 设置停用词
stopwords = set()
content = [line.strip() for line in open('./附件/停用词库.txt', 'r', encoding="utf-8").readlines()]
stopwords.update(content)

print("输入用来生成词云的txt文档的绝对路径")
print("例子：C:/Users/李宏洋/Desktop/python 练习/测试文档/附件/水浒传.txt")
print("请务必用正斜杠“/”而非windows自带的反斜杠“\\”!")
a = input("请输入：")
txt = open(a, "rt", encoding="utf-8").read()
words = jieba.lcut(txt)
c = " ".join(words)
w = wordcloud.WordCloud(max_words=200, background_color="white", font_path="msyh.ttc", stopwords=stopwords)
w.generate(c)
w.to_file("词云.jpg")

