def set_list_element(a_list, index, value):
    try:
        a_list[index] = value
    except TypeError:
        print( "ERROR: Invalid input." )
    except IndexError:
        print( "ERROR: Invalid index: {}.".format(index))


list1 = [1, 2, 3]
set_list_element(list1, 1, 10);
print(list1)

list1 = [1, 2, 3]
set_list_element (list1, 4, 10);
print(list1)

list1 = [1, 2, 3]
set_list_element(list1, 'two', 10);
print(list1)