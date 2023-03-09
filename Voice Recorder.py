import sounddevice,colorama.ansi
from scipy.io.wavfile import write
from playsound import playsound


fs=44_100 #Sample Rate
second=float(input("Enter the time Duration in second: ")) #Enter your required time
print(colorama.ansi.Fore.LIGHTRED_EX,"Recording...\n")
record_voice=sounddevice.rec(int(second*fs),fs,channels=2)
sounddevice.wait()
write("C:/Users/asus/Desktop/Sample.wav",fs,record_voice)
print(colorama.ansi.Fore.GREEN,"Your Record is Ready...")
playsound("C:/Users/asus/Desktop/Sample.wav")
print(colorama.ansi.Fore.RESET)
