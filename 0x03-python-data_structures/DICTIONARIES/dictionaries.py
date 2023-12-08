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
    print("{}".format(Person.get('Town', -1)))
    print("{}".format(list(Person.items())))
    print("{}".format(list(Person.items())[0][1]))  # Perform indexing
    print("{}".format(list(Person.keys())))
    print("{}".format(list(Person.keys())[2]))
    Animals = dict([('Herbivore', 'Rhino'), ('Carnivore', 'Lion'), ('Omnivore', 'Cat')])
    s = {1: 'bbb', 2: 'bbb', 3: 'bbb'}
    print(Animals)
    print("{}".format(list(Animals.values())))
    print("{}".format(list(s.values())))
    print(s)
    s.pop(1)
    print("{}".format(list(s.keys())))
    print("{}".format(s.pop(5, -1)))
    Animals.popitem()
    Animals.popitem()
    Animals.pop('Herbivore')
    print(Animals)
    # Animals.popitem() an empty dictionary
    d1 = {'a': 10, 'b': 20, 'c': 30}
    d2 = {'a': 1000, 'c': True}
    d1.update(d2)  # Merging two dictionaries
    d2.update([('County', 'Meru'), ('c', None)])
    d1.update(a=4000, c='Jeopardy')
    print(d1)
    print(d2)
    GRADES = {'Jake': 'Grade 1', 'Abby': 'Grade 2', 'Bilha': 'Grade 3'}
    GRADES['Vikky'] = 'Grade 1'
    print("This is the GRADES dictionary: {}".format(GRADES))
    print(GRADES['Abby'])
    del GRADES['Vikky']
    print("This is the GRADES dictionary: {}".format(GRADES))
    print(list(GRADES))
    print(sorted(GRADES))
    print('Abby' in GRADES)
    print('Bilha' not in GRADES)
    # let us use dict comprehension to build a dictionary
    CUBES = {num: num**3 for num in range(10)}
    print(CUBES)
    # Let us build using keyword arguments
    FAMILY = dict(JAKE=7, ALICE=25, MOM=52)
    print(FAMILY)
    # Lets us demonstarate looping
    print(list(FAMILY.items()))
    for key, value in FAMILY.items():
        print(key, value)
    # Let us loop through sequence and extract index and its corresponding value using enumerate.
    LIST = ['cats', 'dogs', 'rats']
    for index, value in enumerate(LIST):
        print(index, value)
    # demonstrate zip()
    FOOD = ['chicken', 'pizza', 'pilau']
    ALLERGY = ['peanuts', 'milk', 'wheat']
    STUDENT = ['Tyson', 'James', 'Carrie']
    for f, a, s in zip(FOOD, ALLERGY, STUDENT):
        print("My name is {2}. My favorite food is {0}. I am allergic to {1}.".format(f, a, s))
    print(FAMILY)
    for i, j in reversed(list(FAMILY.items())):
        print(i, j)
    for number in reversed(range(2, 20, 2)):
        print(number)


if __name__ == '__main__':
    dictionaries()
