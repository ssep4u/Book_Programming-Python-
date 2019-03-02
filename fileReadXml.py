import xml.etree.ElementTree as ET
import codecs

f = codecs.open('movie.xml', encoding='utf8')
str = f.read()
tree = ET.ElementTree(ET.fromstring(str))
root = tree.getroot()
print("****")
print(root.tag)
for child in root:
    print("tag : " + child.tag + ": " + child.text)

print("****")
f.close()