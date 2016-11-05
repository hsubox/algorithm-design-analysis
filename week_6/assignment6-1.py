def load_file(file_to_open):
    file = open(file_to_open)
    lines = file.read().split('\n')
    hash_table = set();
    for line in lines[:-1]: # file ends with line break
        number = int(line)
        hash_table.add(number)
    file.close()
    return hash_table

file = "algo1-programming_prob-2sum.txt"
hash_table = load_file(file)

# compute the number of target values t
# in the interval [-10000,10000] (inclusive)
# such that there are distinct numbers x,y
# in the input file that satisfy x+y=t.
def two_sum(hash_table, target_value):
    for value in hash_table:
        if target_value - value in hash_table and (target_value - value) != value:
            return True
    return False

def two_sum_range(hash_table, target_value_range):
    has_sums = 0
    for target_value in range(target_value_range[0], target_value_range[1] + 1):
        if two_sum(hash_table, target_value):
            has_sums += 1
    return has_sums

target_value_range = [-10000,10000]
has_sums = two_sum_range(hash_table, target_value_range)
print has_sums

# 427
