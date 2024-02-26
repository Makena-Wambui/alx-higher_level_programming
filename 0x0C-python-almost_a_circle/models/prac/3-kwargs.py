#!/usr/bin/python3

def test_args_kwargs(arg1, arg2, arg3):
    print("Arg1: ", arg1)
    print("Arg2: ", arg2)
    print("Arg3: ", arg3)

# use args or kwargs to pass arguments to this function:
if __name__ == "__main__":
    args = ("five", 10.1, 3)
    test_args_kwargs(*args)
    print('\n\n')
    kwargs = {"arg3": 6, "arg1": 10, "arg2": "chicken"}
    test_args_kwargs(**kwargs)
