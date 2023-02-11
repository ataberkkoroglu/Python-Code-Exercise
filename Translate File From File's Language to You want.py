import deep_translator,docx,os,time,sys
from docx2pdf import convert

ceviri=deep_translator.GoogleTranslator()
os.chdir("C:/Users/asus/Desktop")
lang=ceviri.get_supported_languages(as_dict=True)

while 1:
 for i in lang:
    print("Language: {}".format(i))
    
 Target=input("Which Language Would You Like To Translate Your World File(Your File should contain the most 5000 character) ? : ")
 Target=Target.lower()
 google=deep_translator.GoogleTranslator(source="auto",target=lang[Target])

 path=input(f"Write Path of World File Which be wanted Translate to {Target.capitalize()}: ")
 doc=docx.Document(path)
 trans=list()

 for para in doc.paragraphs:
    print("Preparing...")
    trans.append(google.translate(para.text)+'\n')
    
 world=docx.Document()
 world.add_heading(f"{trans[0]}",5)
 Trans="".join(trans)
 world.add_paragraph(Trans)
 filename=input("What is Your File's Name: ")
 world.save(f"{filename}.docx")
 convert(f"{filename}.docx",f"{filename}.pdf")
 
 with open(f"{filename}.txt",mode='w',encoding="utf-8") as file:
    file.write(Trans)
 while 1:
     ch=input("Would You Like To Contunie(Y/N) ? : ")
     if ch=='Y' or ch=='y':
         time.sleep(2)
         break
     elif ch=='N' or ch=='n':
         print("\nHave a Good Days...")
         sys.exit()
     else:
         print("Wrong Character...\nPlease Write Again...")