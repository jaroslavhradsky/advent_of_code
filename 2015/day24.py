from time import sleep

spinkej = input("sleep: ")
for line in open("mbox.txt"):
    print(line.strip())
    sleep(float(spinkej))