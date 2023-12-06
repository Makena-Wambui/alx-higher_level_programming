#!/usr/bin/python3
def dictionaries():
    Personal_Info = {'Name': 'Alice', 'Home': 'Meru', 'Age': 25}
    print("The Value of the Name key is: {:s}".format(Personal_Info['Name']))
    # print("Absent key: {:s}".format(Personal_Info['Address']))
    Personal_Info['Address'] = '1046 Kiambu'
    print("VaLue of Address key is {:s}".format(Personal_Info['Address']))
    Personal_Info['Name'] = 'Makena'
    print("{}".format(Personal_Info))


if __name__ == '__main__':
    dictionaries()
