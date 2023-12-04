import os

name=input('Enter Your Name')
state=input('Enter Your State Of Origin')
age=input('Enter Your Age')
address=input('Enter Your Address')
num=input('Enter Your Phone Number')

#First Way
os.system('python calculator2.py')

output=f"""
█████      ██    ██ ███████ ███████ ██████      ███████  ██████  ██████  ███    ███ 
██   ██     ██    ██ ██      ██      ██   ██     ██      ██    ██ ██   ██ ████  ████ 
███████     ██    ██ ███████ █████   ██████      █████   ██    ██ ██████  ██ ████ ██ 
██   ██     ██    ██      ██ ██      ██   ██     ██      ██    ██ ██   ██ ██  ██  ██ 
██   ██      ██████  ███████ ███████ ██   ██     ██       ██████  ██   ██ ██      ██ 
                                                                                     
Your Name Is: {name}
You  Are From {state}
And You Are {age} years old
And You Live At {address}
This Is Your Number {num}
"""
print(output)


