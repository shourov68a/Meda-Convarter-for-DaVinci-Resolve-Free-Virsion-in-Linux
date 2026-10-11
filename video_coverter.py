import subprocess
import random
import os
def file_name_check():
  file_number = random.randrange(1,10000)
  file_namegen ="output_file"+str(file_number)+".mov"

  with open("chash_file_name_check.txt","w") as file_Cash_namechack:
   variable_chack_name=subprocess.run("ls -la ",shell=True,stdout=file_Cash_namechack,text=True)
  
  with open("chash_file_name_check.txt","r",encoding="utf-8") as file_Cash_namechack1:
   text = file_Cash_namechack1.read()
   text_list = text.split()

   ##print(text_list)
   if file_namegen in text_list:
        file_number2 = random.randrange(1,10000)
        file_namegen2 ="output_file"+str(file_number)+".mov"
        file_namegen = file_namegen2
        return file_namegen
   else:
            file_namegen = file_namegen
            return file_namegen 


output_filename = file_name_check()
variable = input("pest the file path :")
p1 = subprocess.run(["ffmpeg", "-i", variable, "-c:v", "dnxhd", "-profile:v", "dnxhr_hq",
                      "-pix_fmt", "yuv422p", "-c:a", "pcm_s16le", output_filename],stdout=subprocess.PIPE)
print(p1.returncode)
os.remove("chash_file_name_check.txt")