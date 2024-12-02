import os

# Load input file
filename:str = 'input'
file_path:str = os.path.join('2024', '2', filename)

with open(file_path, 'r') as in_file:
    lines:list[str] = in_file.readlines()


reports:list[list[int]] = []

for line in lines:
    nums:list[str] = line.split(' ')
    nums_final:list[int] = []
    
    for i in range(len(nums)):
        nums_final.append(int(nums[i]))
    
    reports.append(nums_final)



# Part 1: Safe reports
## This solution sucks big time, bui it is what it is lmao
def is_increasing(lst:list[int],
                  min_diff:int,
                  max_diff:int) -> bool:
    old_elm:int = lst[0]
    
    for i in range(1, len(lst)):
        if i != 1:
            old_elm = lst[i-1]

        max_elm:int = max(old_elm, lst[i])
        min_elm:int = min(old_elm, lst[i])
        diff:int = max_elm - min_elm

        if any([old_elm >= lst[i],
                diff < min_diff,
                diff > max_diff]):
            return False

    return True


def is_decreasing(lst:list[int],
                  min_diff:int,
                  max_diff:int) -> bool:
    old_elm:int = lst[0]
    
    for i in range(1, len(lst)):
        if i != 1:
            old_elm = lst[i-1]
        max_elm:int = max(old_elm, lst[i])
        min_elm:int = min(old_elm, lst[i])
        diff:int = max_elm - min_elm
        
        if any([old_elm <= lst[i],
                diff < min_diff,
                diff > max_diff]):
            return False

    return True


safe_count:int = 0
for report in reports:
    if is_increasing(report, 1, 3) or is_decreasing(report, 1, 3):
        safe_count +=1

print(safe_count)



# Part 2: Safe reports with problem dampener
safe_count:int = 0
for i in range(len(reports)):
    safe_instances:list[bool] = []
    for j in range(len(reports[i])):
        tmp_lst:list[int] = reports[i].copy()
        tmp_lst.pop(j)
        safe_instances.append(is_increasing(tmp_lst, 1, 3) or is_decreasing(tmp_lst, 1, 3))

    if safe_instances.count(True) > 0:
        safe_count += 1


print(safe_count)

