import time

start = time.time()

with open("Mansion\\MANSION_TABBED.txt") as f:
    tabbed = f.read()

splitted = tabbed.split("\n")
out = []
for x in splitted:
    while x.startswith(" "):
        x = x.removeprefix(" ")
    out.append(x)

out = "\n".join(x for x in out)

with open("Mansion\\MANSION.txt", "w") as f:
    f.write(out)

end = time.time()
diff = end - start

print(diff)
print(len(out))
print(str(len(out)/1024/1024/diff) + "MB/s")