import urllib.request

url = "http://post.naver.com/viewer/postView.nhn?volumeNo=9577951&memberNo=36405506&mainMenu=SCIENCE"

f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

begin = data.find("<span>일식은 연구자들에게",1)
end = data.find("확인하고자 하고 있다")
end += len("확인하고자 하고 있다")

print("total=", len(data))
print("begin=", begin)
print("length=", end-begin, '\n')

speech = data[begin:end]
re_speech = speech.replace('</span>',' ').replace('<span lang="EN-US">',' ').replace('<br>',' ').replace('<span>',' ').replace('&nbsp',' ').replace('(',' ').replace(')',' ').replace('.',' ').replace(';',' ').replace("\'",' ').replace('\"',' ').replace(',',' ')

speech = re_speech.split()

analyze = {}

for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist_1 = sorted(analyze.items())
flist_2 = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)


for key in flist_2:
    print (key)
