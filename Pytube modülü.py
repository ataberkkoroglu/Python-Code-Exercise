import pytube
link=input("Enter Youtube URL Which is You Want To Load= ")
yt=pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded",link)