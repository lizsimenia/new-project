def calc(x, operand):
    string = ""

    for i in range(operand):
        print("Введите операнд", i + 1, end=": ")
        a = int(input())

        string += str(a)
        string += " "

        if i == operand - 1:
            string += "="
        else:
            string += x
            string += " "

        if i == 0: res = a

        else:
            if x == "*": res *= a
            elif x == ":": res /= a
            elif x == "+": res += a
            else: res -= a

    print(string, res)

#Проверка ввода.
def check(x):
    while True:
        if (x != "*" and x != "+" and x != "-" and x != ":"):
            x = input("Введите корректную операцию (*, :, +, -): ")
        else:
            break

operation = input("Введите операцию: ")
check(operation)

operand = int(input("Сколько операндов? "))
calc(operation, operand)