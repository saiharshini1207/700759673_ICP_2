with open("input.txt", "r") as i_file:
    lns = i_file.readlines()


wd_list = []
for line in lns:
    wos = line.strip().split()
    wd_list.extend(wos)


with open("output.txt", "w") as o_file:
    o_file.write("".join(lns))
    o_file.write("\nWord_count:\n")

for wod in set(wd_list):
    count = wd_list.count(wod)
    with open("output.txt", "a") as o_file:
        o_file.write(f"{wod}: {count}\n")
    print(f"{wod}: {count}")


