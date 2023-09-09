def read_scores(filename):
    try:
        if type(filename) != str:
            raise Exception("Invalid input!")
        elif filename == '':
            raise Exception("Invalid filename!")
        try:
            input_file = open(filename, "r")
        except FileNotFoundError:
            print("ERROR: The file '{}' does not exist.".format(filename))
            return
        scores = input_file.read().split()
        if not scores:
            raise Exception("No positive scores in the input file.")
        numbers = [float(score) for score in scores if float(score) >= 0 ]
        if not numbers:
            raise Exception("No positive scores in the input file.")
        input_file.close()
        number_of_marks = len(numbers)
        total_marks = sum(numbers)
        print("There are {} score(s).".format(number_of_marks))
        print("The total is {:.2f}.".format(total_marks))
        print("The average is {:.2f}.".format(total_marks/number_of_marks))
    except ValueError:
        print("ERROR: The input file contains invalid values.")
    except Exception as result:
        print("ERROR: {}".format(result))


#read_scores('eight_marks.txt')
#read_scores('input_unknown.txt')
#read_scores('empty.txt')
#read_scores('all_negatives.txt')
#read_scores('')
#read_scores(123)