def read_lines_until_empty():
    lines=[]
    while True:
        line=input()
        if line=="":
            break
        else:
            lines.append(line)
    return lines

print("Enter multiple lines of input. press enter on an empty line to finish")
input_lines=read_lines_until_empty()

print("\n The entered lines are: ")
for line in input_lines:
    print(line)