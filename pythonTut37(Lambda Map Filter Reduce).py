# Lambda Functions
def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value
    return mult_by

def mult_by_2(num):
    return num * 2

def do_math(func, num):
    return func(num)

times_two = mult_by_2

print("8 * 2 = ", do_math(mult_by_2, 8))

generated = get_func_mult_by_num(5)
print("5 * 10 = ", generated(10))
list_of_funcs = [times_two, generated]
print("5 * 9 = ", list_of_funcs[1](9))