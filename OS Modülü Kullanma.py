import os
print(os.getcwd())


with open("Txt_dosyaları2.txt","w",encoding="utf-8") as file:
    for i,e,u in os.walk ("c:/Users/atabe/OneDrive/",".txt"):
        for x in u:
            if (x.endswith("txt")):
                file.write(x)
                file.write("\n")
    file.close()

with open("Pdf_dosyaları.txt","w",encoding="utf-8") as file2:
    for i,e,u in os.walk ("c:/Users/atabe/OneDrive/"):
        for x in u:
            if (x.endswith("pdf")):
                file2.write(x)
                file2.write("\n")
    file2.close()   
with open("MP4_dosyaları.txt","w",encoding="utf-8") as file3:
    for i,e,u in os.walk ("c:/Users/atabe/OneDrive/"):
        for x in u:
            if (x.endswith("mp4")):
                file3.write(x)
                file3.write("\n")
    file3.close()


 
