class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    
    def print_person(self):
        print('Name:',self.__name)
        print('Addr:',self.__address)
        print('Phone:',self.__phone)

class Customer(Person):
    def __init__(self, name, address, phone, cust_num, on_list):
        Person.__init__(self, name, address, phone)

        self.__cust_num = cust_num
        self.__on_list = on_list

    def print_person(self):
        #you could also call each get_*** individually instead of the print.person
        Person.print_person(self)
        print('Customer Number:',self.__cust_num)
        if self.__on_list:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')
