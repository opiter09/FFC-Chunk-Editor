import os

if (os.path.exists("./vivoFiles/") == True):
    binn = open("0.bin", "rb")
    whole = binn.read()
    binn.close()
    binn = open("0.bin", "rb")
    section = binn.read(48)
    binn.close()

    binn = open("0.bin", "wb")
    binn.write(section)
    binn.close()

    binn = open("0.bin", "ab")
    text = open("vivoNames.txt", "rt").read()
    offset = int.from_bytes(whole[44:48], "little")
    for i in range(209):
        offset = offset + os.stat("vivoFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin").st_size
        binn.write(offset.to_bytes(4, "little"))
    binn.write(whole[884:1072])
    for i in range(210):
        binn.write(open("vivoFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "rb").read())
    binn.close()