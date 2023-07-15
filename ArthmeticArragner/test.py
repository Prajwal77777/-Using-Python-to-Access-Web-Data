def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error"
    arranged_line = ""
    first_line = ""
    second_line = ""
    dashes_line = ""
    answer_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Only Number is Allowed"
        if operator not in ["+", "-"]:
            return "Error: Operator Must be '+' or '-'"
        if operator == "+":
            answer = str(int(operand1) + int(operand2))
        else:
            answer = str(int(operand1) - int(operand2))

    max_length = max(len(operand1), len(operand2))

    first_line += operand1.rjust(max_length + 2) + "    "
    second_line += operator + " " + operand2.rjust(max_length) + "    "
    dashes_line += "-" * (max_length + 2) + "    "
    answer_line += answer.rjust(max_length + 2) + "    "

    arranged_line += first_line.rstrip() + "\n"
    arranged_line += second_line.rstrip() + "\n"
    arranged_line += dashes_line.rstrip()

    if display_answers:
        arranged_line += "\n" + answer_line.rstrip()
    return arranged_line
