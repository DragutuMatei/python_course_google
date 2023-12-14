# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale. ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3). ○ your_function() va returna 0. ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
def my_function(*args, **kwargs):
    sum = 0
    for x in args:
        if type(x) == int or type(x) == float:
            sum += x
    return sum


print(my_function(1, 5, -3, "abc", [12, 56, "cad"]))
print(my_function())
print(my_function(2, 4, "abc", param_1=2))


# def recursive(lista):

    # total =
#     sum_total = 0
#     sum_par = 0
#     sum_impar = 0
#
#     sum_total = sum_total +
#
#
# print(recursive([0, 2, 4, 6, 8, 10]))


def fct():
    var = input("scrie ceva: ")
    if var.isnumeric():
        return int(var)
    else:
        return 0

print(fct())