from urllib import request

target= request.urlopen('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
output = target.read()
print(output)

with open('a.png','wb') as file:
    file.write(output)