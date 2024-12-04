import os
import re


# Load input file
filename:str = 'input'
day:str = '3'
file_path:str = os.path.join('2024', day, filename)

with open(file_path, 'r') as in_file:
    content:list[str] = in_file.read()



# Part 1: Calculating the sum of all valid mul expressions
# Valid form: 'mul(%INT,%INT)'
def extract_integers(content:str,
                     start:str,
                     delim:str,
                     end:str
                     ) -> tuple[int, int]:
    '''
    Extracts the integers from a mul function and returns them in a tuple.
    '''
    # Lengths of strings
    start_len:int = len(start)
    delim_len:str = len(delim)
    end_len:str = len(end)

    # Indices of strings
    start_idx:int = content.find(start)
    delim_idx:int = content.find(delim)
    end_idx:int = content.find(end)

    # Extract the integers
    num1:int = int(content[start_idx+start_len:delim_idx])
    num2:int = int(content[delim_idx+delim_len:end_idx])

    return num1, num2


mul_pattern = r'mul\(\d+\,\d+\)'
mul_exps:list[str] = re.findall(mul_pattern, content)

mul_sum:int = 0
for exp in mul_exps:
    num1, num2 = extract_integers(exp, 'mul(', ',', ')')
    mul_sum += num1 * num2

print(mul_sum)



# Part 2: Only calculating the mul expressions
# that are marked as "do()", and skip those marked as "don't()"
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"
do_exps:list[str] = re.findall(do_pattern, content)
dont_exps:list[str] = re.findall(dont_pattern, content)

mul_indices:list[int] = [content.find(exp) for exp in mul_exps]


final_sum:int = 0
for exp in mul_exps:
    # Find the indices for the do() and dont() expressions
    # right before the mul() expression
    curr_exp_idx:int = content.find(exp)
    curr_do_idx:int = content.rfind(do_exps[0], 0, curr_exp_idx) 
    
    curr_dont_idx:int = content.rfind(dont_exps[0], 0, curr_exp_idx)

    # If the do() expression is closer than the dont() expression,
    # then add the multiplication result to the sum
    if curr_do_idx >= curr_dont_idx:
        num1, num2 = extract_integers(exp, 'mul(', ',', ')')
        final_sum += num1 * num2


print(final_sum)


