import os

# Load lists
base_dir:str = os.path.join('2024', '1')
filename:str = 'input'
filepath:str = os.path.join(base_dir, filename)


with open(filepath, 'r') as in_file:
    lines:list[str] = in_file.readlines()


fst_lst:list[int] = []
snd_lst:list[int] = []

for line in lines:
    tmp:list[str] = line.split('   ')
    fst_lst.append(int(tmp[0]))
    snd_lst.append(int(tmp[1]))


fst_lst.sort()
snd_lst.sort()



# Part 1: Distance between each number summed
result_1:int = 0
for i in range(len(fst_lst)):
    x:int = fst_lst[i]
    y:int = snd_lst[i]
    result_1 += x - y if x > y else y - x

print(result_1)



# Part 2: Num in list 1 multiplied by occurence in list 2
result_2:int = 0
for num in fst_lst:
    result_2 += num * snd_lst.count(num)

print(result_2)

