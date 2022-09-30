def int_input(message):
    while True:
        try:

            result = int(input(massage))
        except ValueError:
            print("Error")
        except Exception as error:
            print(f"Неизвесная ошибка:{type(error)} {error}!")
        else:
            return result


a = int_input(("Введите первое число"))
b = int_input(("Введите второе число"))
c = int_input(("Введите третье число"))



print(a+b+c)
print(a-b-c)
print(a*b*c)


try:
    print(a / b / c)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except Exception as error:
    print(f"Неизвесная ошибка:{type(error)} {error}!")

