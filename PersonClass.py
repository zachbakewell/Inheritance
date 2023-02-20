class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print(self.__name, self.__address, self.__phone)

class Customer(Person):
    def __init__(self, name, address, phone, cust_num, m_list):
        Person.__init__(self, name, address, phone)

        self.__cust_num = cust_num
        self.__m_list = m_list

    def print_person(self):
        print(Person.__init__, self.__cust_num, self.__m_list)
