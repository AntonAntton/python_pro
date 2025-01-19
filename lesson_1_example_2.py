def outer_function():
    my_var = 5

    def inner_function():
        nonlocal my_var
        my_var = 12
        # return global_var

    print(my_var)
    inner_function()
    print(my_var)
    # return inner_function


my_var = 10
print(my_var)
outer_function()

# print(func())
print(my_var)

