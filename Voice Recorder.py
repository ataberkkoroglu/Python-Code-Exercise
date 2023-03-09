import sounddevice,colorama.ansi,sys,time
from scipy.io.wavfile import write
from playsound import playsound
import colorama,fontstyle
from datetime import datetime

print(colorama.ansi.Fore.LIGHTWHITE_EX+"Welcome To Program.. \n"+datetime.strftime(datetime.now(),"%H : %M : %S  %d.%m.%Y\n"))
fs=44_100 #Sample Rate
while(1):
 second=float(input("\033[1mEnter the time Duration in second: ")) #Enter your required time
 name=input("\033[1mWhat is Name Of Voice File : ")
 print(colorama.ansi.Fore.LIGHTRED_EX,fontstyle.apply("Recording...\n","BOLD/UNDERLINE"))
 record_voice=sounddevice.rec(int(second*fs),fs,channels=2)
 sounddevice.wait()
 write(f"C:/Users/asus/Desktop/{name}.wav",fs,record_voice)
 print(colorama.ansi.Fore.GREEN,fontstyle.apply("Your Record is Ready...","BOLD/UNDERLINE"))
 print(colorama.ansi.Fore.CYAN)
 
 while(1):
  ch_1=input("Would You Like To Listen Your Record Of Voice (Y/N) ? : ")
  if (ch_1=='Y' or ch_1=='y'):
     playsound(f"C:/Users/asus/Desktop/{name}.wav")
     break
  elif (ch_1=='N' or ch_1=='n'):
      break
  else:
      print(fontstyle.apply("\nWrong Character...\nPlease Write Again\n","RED/BOLD/INVERSE"))
      
 while(1):
    print(colorama.ansi.Fore.YELLOW)
    ch=input("Would You Like To Contunie (Y/N) ? : ")
    if(ch=='Y' or ch=='y'):
        time.sleep(2)
        print(colorama.ansi.Fore.RESET)
        break
    elif (ch=='N' or ch=='n'):
        print(colorama.ansi.Fore.LIGHTMAGENTA_EX,"\n\033[1mHave a Good Days...",colorama.ansi.Fore.RESET)
        sys.exit()
    else:
        print(fontstyle.apply("\nWrong Character...\nPlease Write Again","RED/BOLD/INVERSE"))


