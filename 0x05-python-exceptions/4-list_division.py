#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for a in range(list_length):
        try:
            result = ((my_list_1[a]) / (my_list_2[a]))
        except TypeError:
            result = 0
            print(f"wrong type")
        except ZeroDivisionError:
            result = 0
            print(f"division by 0")
        except IndexError:
            result = 0
            print(f"out of range")
        finally:
            pass
        new_list.append(result)
    return new_list
