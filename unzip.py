import zipfile
import sys
file_name = sys.argv[1]
passwords = open("words.txt","r").read().split('\n')
#passwords = ["pswd", "test"]
for password in passwords:
  with zipfile.ZipFile(file_name) as file:
    try:
      file.extractall(pwd = bytes(password, 'utf-8'))
    except:
      continue
    else:
      print("Password found: %s" % (password))
