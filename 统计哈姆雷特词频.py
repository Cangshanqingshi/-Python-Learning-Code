def gettext():
    txt = open("./附件/哈姆雷特.txt", "r").read()
    txt = txt.lower()  # 将所有大写变成小写防止大小写干扰
    for ch in '!"#$%&()*+-/.:;<=>?@[\\]^_{|}~`':  #避免标点符号干扰
        txt = txt.replace(ch, " ")
    return txt


hamlettxt = gettext()
words = hamlettxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))