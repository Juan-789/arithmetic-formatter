def arithmetic_arranger(problems: list, *solve: bool) -> str:
    first_line = ""
    second_line = ""
    empty_line = ""
    for j in range(len(problems)):
        nums = problems[j].split()
        print(len(nums[0]))
        first_line += (" " * (5 - len(nums[0]))) + (nums[0]) + (" " * 3)


    for i in range(len(problems)):
        nums = problems[i].split()
        second_line += (nums[1]+"  " * (4 - len(nums[2]))) + (nums[2]) + (" " * 3)
    print(first_line+"\n"+second_line)
    for k in range(len(problems)):
        empty_line += "_"*5+" "*3
    #
    # arranged_problems = first_line+"\n"+second_line+"\n"+empty_line+"\n"
    #
    # return arranged_problems
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))