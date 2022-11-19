from pytube import YouTube


while(1):
    link = input("Youtube link: ")
    try:
        yt = YouTube(link)
        break
    except:
        print("Bilinmeyen hata oluştu tekrar deneyiniz.")

title = yt.title

StreamList = yt.streams


itags = []
i = 1
for item in StreamList:
    if(item.type=="audio"):
        itags.append(item.itag)
        print(f"{i:2} | {item.mime_type:12} , {item.abr:9}, {(item.filesize/(1024**2)):.2f}MB")
    elif(item.is_progressive):
        itags.append(item.itag)
        print(f"{i:2} | {item.mime_type:12} , {item.resolution:8}, ,{(str(item.fps)):5}, {(item.filesize/(1024**2)):.2f}MB")
    else:
        continue
    i+=1

while(1):
    try:
        result = int(input(">>>:"))
    except:
        print("Hatalı giriş yaptınız.")
        continue
    if(0<result<i):
        break
    else:
        print("Geçersiz seçim.")

ys = yt.streams.get_by_itag(itags[result-1])

selected = StreamList[result-1]

time = selected._monostate.duration

print(selected.title)
print(f"{time//60}:{time%60}")

with open("Bin\\.ini","r") as f:
    no= f.read()

if(selected.type =="audio"):

    ys.download("Bin\\downloads",filename_prefix=f"{no}-{selected.abr}-")
else:
    ys.download("Bin\\downloads",filename_prefix=f"{no}-{selected.resolution}-{selected.fps}fps-")

with open("Bin\\.ini","w") as f:
    no = int(no)+1
    f.write(str(no))
    








