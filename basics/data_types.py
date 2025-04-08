class PrintNumbericInfo:
    # creating Non static method
    def print_data(self):
        # numeric data types
        x = 10  # int
        y = 10.5  # float
        complex_data_type = 2.3j  # complex
        print(str(x) + "This is int")
        print(str(y) + "This is float")
        print(str(complex_data_type) + "This is Complex Data type")


class PrintStringInfo:
    # creating static method
    @staticmethod
    def print_data():
        name = "Madhu Palli"
        age = "24"
        print(name + "Accessing Name")
        print(name[0] + "Accessing 0 Index in name")
        print(f"{name[-1]} Prints I (Because we are accessing with negative index)")
        print("-----------------------------------")

        print_numeric_info = PrintNumbericInfo()
        print_numeric_info.print_data()


class Collections:
    @staticmethod
    def print_collections():
        list_data_type = [1, 2, 3, 4, 5, 5]  # list
        print(list_data_type)

        tuple_data_type = (1, 2, 3, 4, 5, 5)  # tuple
        print(tuple_data_type)
        # tuple_data_type[3]=5 # Immutable we cant change so we will get error

        set_data_type = {1, 2, 3, 4, 5, 5}  # set it wont accept duplicates
        print(set_data_type)

        frozen_set_data_type = [1, 2, 4, 56]
        print(frozen_set_data_type)  # wont modify anymore

        # frozen_set_data_type[3]=5 # immutable so we will get error

        dict_data_type = {
            "name": "Madhu Palli",
            "age": 24,
        }  # dictionary same as like objects in javascript


Collections.print_collections()
PrintStringInfo.print_data()
