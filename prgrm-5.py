str = "i am learning python from youtube"
print(str.endswith("tube"))#true
print(str.endswith("arm"))#false
print(str.capitalize())#i am learning python from youtube
str = str.capitalize()
print(str)
print(str.replace("from","to"))#i am learning python to youtube
print(str.find("youtube"))#26
print(str.find("f"))#21
print(str.find("w"))#-1
print(str.count("p"))#1
print(str.startswith("python"))
print(str.count("a"))#2
print(str.removeprefix("you"))
