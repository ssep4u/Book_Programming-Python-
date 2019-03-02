f = open("file.txt", "w")

f.write("hello")
f.write("\n")
f.write("world")

f.close()

f = open("file.txt", "a")

f.write("\n")
f.write("append")
f.close()
f = open("file.txt", "a")

f.write("\n")
f.write("a한글은?")
f.close()

f = open("hangul.txt", "w", encoding="utf8")
f.write("한글")
f.write("\n")
f.write("English")
f.close()