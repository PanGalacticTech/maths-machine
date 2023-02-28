# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def decimal_binary(decimal_int):
    binary_list = []
    new_val = decimal_int
    while new_val > 0:
        remainder = new_val % 2
        new_val = int(new_val / 2)
        #binary_list.append(remainder)
        binary_list.insert(0, remainder)  ## Insert at the front of the list
        print(f"Initial Int: {decimal_int}, new_val: {new_val}, remainder:{remainder}, binary:{binary_list}")
        decimal_int = new_val
    print("Output:")
    for i in binary_list:
        print(i, end="")
    print("\n")




def main():
    decimal_binary(101)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
