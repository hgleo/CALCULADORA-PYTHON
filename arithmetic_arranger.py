def arithmetic_arranger(problems, show_result=False):
    # Verifica se há muitos problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializa as listas dos operandos e operadores
    operands_1 = []
    operands_2 = []
    operators = []
    results = []

    # Separa os operandos e operadores dos problemas e verifica se eles são válidos
    for problem in problems:
        operand_1, operator, operand_2 = problem.split()

        if not operand_1.isdigit() or not operand_2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        operands_1.append(operand_1)
        operands_2.append(operand_2)
        operators.append(operator)

        # Calcula o resultado (se for o caso) e o armazena
        if show_result:
            result = str(eval(problem))
            results.append(result)

    # Cria as linhas da saída
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for i in range(len(problems)):
        operand_1 = operands_1[i]
        operand_2 = operands_2[i]
        operator = operators[i]

        max_length = max(len(operand_1), len(operand_2)) + 2
        space_1 = " " * (max_length - len(operand_1))
        space_2 = " " * (max_length - len(operand_2))
        line_1 += operand_1 + space_1 + "    "
        line_2 += operator + " " + operand_2 + space_2 + "    "
        line_3 += "-" * max_length + "    "

        if show_result:
            result = results[i]
            space_3 = " " * (max_length - len(result))
            line_4 += result + space_3 + "    "

    # Remove o último espaço em cada linha
    line_1 = line_1.rstrip()
    line_2 = line_2.rstrip()
    line_3 = line_3.rstrip()
    line_4 = line_4.rstrip()

    # Combina as linhas em uma única string
    if show_result:
        arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    else:
        arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3

    return arranged_problems
