#!/usr/bin/python3
def dictionaries():
    Personal_Info = {'Name': 'Alice', 'Home': 'Meru', 'Age': 25}
    Cities = dict([('Kenya', 'Nairobi'), ('Ethiopia', 'Addis Ababa'), ('UK', 'London')])
    print("The Value of the Name key is: {:s}".format(Personal_Info['Name']))
    # print("Absent key: {:s}".format(Personal_Info['Address']))
    Personal_Info['Address'] = '1046 Kiambu'
    print("VaLue of Address key is {:s}".format(Personal_Info['Address']))
    Personal_Info['Name'] = 'Makena'
    del Personal_Info['Age']
    print("{}".format(Personal_Info))
    print(Cities)
    # print("{}".format(Cities[2]))
    del Cities['UK']
    # print("The value of the UK Key is {:s}.".format(Cities['UK']))
    print(Cities)
    # lets create a dict using integers as keys
    Alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    Alpha = {4: 'D', 3: 'C', 2: 'B', 1: 'A'}
    List = ['a', 'b', 'c', 'd']
    print("{}".format(Alphabet))
    print("{}".format(Alpha))
    print("The value of 1 is : {:s} and 2 is {:s}".format(Alphabet[1], Alphabet[2]))
    print("The value of 1 is : {:s} and 2 is {:s}".format(Alpha[1], Alpha[2]))
    print("{:s}".format(List[-1]))
    # print("{:s}".format(Alpha[-1])) accessing a dictionary like a list
    print(List[0:3])
    print(List[:3])
    print(List[-3:])
    print(List[:-3])
    # print(Alpha[:3]) no slicing
    # Alpha.append('E') traeting a dict like a list
    print(Alpha)
    # creating a dictinary on the move
    Person = {}
    print("Empty dictionary {}. This is its type: {}".format(Person, type(Person)))
    Person['fname'] = 'Alice'
    Person['lname'] = 'Makena'
    Person['Age'] = '31'
    Person['Spouse'] = 'Gerald'
    Person['Kids'] = ['Jake', 'Ann']
    Person['Pets'] = {'Dog': 'Rex', 'Cat': 'Niko'}
    print(Person)
    print("{}".format(Person['Kids'][-1]))  # retrieve the last name in the Kids sublist
    print("{}".format(Person['Pets']['Dog']))
    # keys can also be of different types
    d = {'name': 'Kezy', 3.14: 'pi', True: 1, 1: 'aaa'}
    # you can use built in objects like types and functions as keys
    d[int] = 1
    d[float] = 2.5
    d[bool] = 10
    d[bool] = 16
    # let us use tuples as keys and lists
    f = {(1, 2): 'a', (4, 5): 'c', (8, 9): 'q', int: 'p', 'letter': 'p'}
    print(d)
    print("{}".format(d[3.14]))
    print("{:d}".format(d[bool]))
    print(f)
    print("These two keys int and letter are equal: {:s} and {:s}.".format(f[int], f['letter']))
    # in and not in operators
    print("{}".format((1, 2) in f))
    print("{}".format((4, 5) not in f))
    del d[bool]
    print("{:d}".format(len(d)))
    d.clear()  # will empty a dictionary
    print(d)
    print("{:s}".format(Person.get('lname')))
    print("{}".format(Person.get('Town')))


if __name__ == '__main__':
    dictionaries()
