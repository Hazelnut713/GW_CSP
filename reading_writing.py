# GW, Reading and Writing to Files

with open('practice.txt', "r+") as file:
    content = file.read()
    print(content)
    word = content.find("LaRose")
    lengeth = len("LaRose")
    print(content[word:word+lengeth])
    print(content.upper())
    content += " Treyson!"
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("Another line")
