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
    print(Cities)


if __name__ == '__main__':
    dictionaries()
