def arithmetic_arranger(problems: list, solve=False ) -> str:
    first_line = "" #empty strings of each line
    second_line = ""
    empty_line = ""
    ans_line = ""
    if len(problems)>5:
        return "Error: Too many problems."

  #      first_line += (" " * (5 - len(nums[0]))) + (nums[0]) + (" " * 4)
    #print(nums)

    for i in range(len(problems)):
        problems[i] = problems[i].split()

        if problems[i][1] != "+" and problems[i][1] != "-":
            return "Error: Operator must be '+' or '-'."
        
        elif len(problems[i][2]) > len(problems[i][0]):
            space_place = len(problems[i][2])
        else:
            space_place = len(problems[i][0])
        top_indent = space_place+2-len(problems[i][0])
        if space_place>4:
            return "Error: Numbers cannot be more than four digits."
        elif i == len(problems):
            first_line+=" "*top_indent+problems[i][0]
        else:
            first_line+=" "*top_indent+problems[i][0]+" "*4
        second_line += problems[i][1]+" "+(" "*(space_place-len(problems[i][2])))+problems[i][2] + " "*4
        empty_line += "-" * (space_place + 2) + " " * 4
        if (problems[i][0].isnumeric() == False) or (problems[i][2].isnumeric() == False):
            return "Error: Numbers must only contain digits."

        elif problems[i][1] == "+":
            answer = str(int(problems[i][0])+int(problems[i][2]))
        else:
            answer = str(int(problems[i][0])-int(problems[i][2]))
        ans_line += " "*(space_place+2-len(str(answer)))+answer+" "*4

    if solve == True:
        return first_line[:len(first_line)-4]+"\n"+second_line[:len(second_line)-4]+"\n"+empty_line[:len(empty_line)-4]+"\n"+ans_line[:len(ans_line)-4]

    return first_line[:len(first_line)-4]+"\n"+second_line[:len(second_line)-4]+"\n"+empty_line[:len(empty_line)-4]

    #
    #     second_line += nums[1]+" "+" "*(space_place-len(nums[2])) + (nums[2]) + (" " * 4)
    # print(first_line+"\n"+second_line)
    # for k in range(len(problems)):
    #     empty_line += "_"*5+" "*3
    #
    # arranged_problems = first_line+"\n"+second_line+"\n"+empty_line+"\n"
    #
    # return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
