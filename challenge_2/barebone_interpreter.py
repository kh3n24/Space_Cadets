with open("../challenge_2/barebone_programme_example.txt", "r", encoding="utf-8") as text:
    barebone_input = text.read()
print(f"programme_overview:\n{barebone_input}")
barebone_arr = barebone_input.split(";\n")                    #split by lines and put into an array
barebone_arr[len(barebone_arr) - 1] = barebone_arr[len(barebone_arr) - 1].strip(";")        #delete ; in the last line
var = {}                                   #dictionary to store variables
line_count = 0
meaningless_loop_count = 0
meaningless_loop_index = 0

def barebone_interpreter():
    global var, line_count, meaningless_loop_count, meaningless_loop_index
    for x in range(0, len(barebone_arr)):
        print(f"\nline{line_count}")
        line = barebone_arr[x]
        print(line)
        if meaningless_loop_index != 0:         #skip while loop when the variable = 0 at the first loop
            meaningless_loop_index -= 1
            continue
        func = line.split()                    #split each word in the line
        if func[0] == "clear":
            var[func[1]] = 0
            print(var)
        elif func[0] == "incr":
            var[func[1]] += 1
            print(var)
        elif func[0] == "decr":
            var[func[1]] -= 1
            print(var)
        elif func[0] == "while":                #to skip while loop when the variable = 0 at the first loop
            if func[1] == 0:
                meaningless_loop_count = 0
                for n in range(x + 1, 100):
                    if barebone_arr[n].strip().startswith("end"):
                        meaningless_loop_count += 1
                    elif barebone_arr[n].strip().startswith("while"):
                        meaningless_loop_count -= 1
                    if meaningless_loop_count == 1:
                        meaningless_loop_index = n - x

        elif func[0] == "end":                          #when "end" appears, trace back to corresponding "while"
            while_loop_count = 1
            trace_back_count = 0
            for i in range(line_count, -1, -1):
                trace_back_count += 1
                if barebone_arr[i].strip().startswith("end"):
                    while_loop_count -= 1
                elif barebone_arr[i].strip().startswith("while"):
                    while_loop_count += 1
                if while_loop_count == 1:
                    line_count = i
                    while_line = barebone_arr[i].split()
                    if var[while_line[1]] == 0:
                        line_count = line_count + trace_back_count - 1
                    else:
                        barebone_interpreter_for_recursion(i, while_line[1])
                    break
        line_count += 1

def barebone_interpreter_for_recursion(start_line, return_index):    #use to control the recursion
    global var, line_count, meaningless_loop_count, meaningless_loop_index
    for x in range(start_line, len(barebone_arr)):
        print(f"\nline{line_count}")
        line = barebone_arr[x]
        print(line)
        if meaningless_loop_index != 0:
            meaningless_loop_index -= 1
            continue
        func = line.split()
        if func[0] == "clear":
            var[func[1]] = 0
            print(var)
        elif func[0] == "incr":
            var[func[1]] += 1
            print(var)
        elif func[0] == "decr":
            var[func[1]] -= 1
            print(var)
        elif func[0] == "while":
            if func[1] == 0:
                meaningless_loop_count = 0
                for n in range(x + 1, 100):
                    if barebone_arr[n].strip().startswith("end"):
                        meaningless_loop_count += 1
                    elif barebone_arr[n].strip().startswith("while"):
                        meaningless_loop_count -= 1
                    if meaningless_loop_count == 1:
                        meaningless_loop_index = n - x
        elif func[0] == "end":                          #when "end" appears, trace back to corresponding "while"
            while_loop_count = 1
            trace_back_count = 0
            for i in range(line_count, -1, -1):
                trace_back_count += 1
                if barebone_arr[i].strip().startswith("end"):
                    while_loop_count -= 1
                elif barebone_arr[i].strip().startswith("while"):
                    while_loop_count += 1
                if while_loop_count == 1:
                    line_count = i
                    while_line = barebone_arr[i].split()
                    if var[while_line[1]] == 0:
                        line_count = line_count + trace_back_count - 1
                        return
                    else:
                        barebone_interpreter_for_recursion(i, while_line[1])
                        if var[return_index] == 0:                          #to control the recursion
                            return
                        break
        line_count += 1

barebone_interpreter()