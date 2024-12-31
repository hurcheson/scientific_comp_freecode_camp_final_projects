def arithmetic_arranger(problems, show_answers=False):

    # Implementing Error Checking
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')
    for problem in problems:
        if any('*' in s or '/' in s for s in problem):
            raise Exception("Error: Operator must be '+' or '-'.")
    for problem in problems:
        if not (problem.split(' ')[0].isdigit() and problem.split(' ')[-1].isdigit()):
            raise Exception('Error: Numbers must only contain digits.')
    for problem in problems:
        if not (len(problem.split(' ')[0]) <= 4 and len(problem.split(' ')[-1]) <= 4):
            raise Exception('Error: Numbers cannot be more than four digits.')

    
    # Obtaining row 1 and row 2 to be formatted later
    row1 = [(problem.split(' ')[0]) for problem in problems]
    row2 = [(problem.split(' ')[1:]) for problem in problems]

    # Obtaining the max with of each problem
    width = list((len(max(i, j[-1])) + 2) for i, j in zip(row1, row2))

    # Obtaining formatted first row and second row
    fr1 = '    '.join([i.rjust(j) for i,j in zip(row1, width)])
    fr2 = '    '.join([(i[0])+(i[-1].rjust(j-1)) for i,j in zip(row2, width)])

    # Adding dashes
    dashes = '    '.join([('-'*d) for d in width])

    # Storing answers
    answers = []
    if show_answers:
        for i, j in zip(row1, row2):
            if j[0] == '+':
                answers.append(int(i) + int(j[-1]))
            else:
                answers.append(int(i) - int(j[-1]))
    final_ans = '    '.join([str(i).rjust(j) for i,j in zip(answers, width)])

    # Display of final output
    print(fr1)
    print(fr2)
    print(dashes)
    print(final_ans)

    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=1)}')