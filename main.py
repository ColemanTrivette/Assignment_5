# This is the file that should contain your solution.
def main():

    # Opens the input file
    input_file = None

    while input_file is None:
        input_file_name = input("Please enter the name of the input data file: ")

        try:
            input_file = open(input_file_name, "r")
        except FileNotFoundError:
            print("File not found. Please try again.")


    # Gets the output file name
    output_file_name = input("Please enter the name of the output data file: ")


    # Asks if the grades should be curved
    curve_choice = input("Would you like to curve the grades? (Y/N) ")

    while curve_choice != "Y" and curve_choice != "N":
        print("Please enter Y or N.")
        curve_choice = input("Would you like to curve the grades? (Y/N) ")


    # Gets the curve score if needed
    curve_score = 100

    if curve_choice == "Y":
        curve_score = None

        while curve_score is None:
            try:
                curve_score = float(
                    input("Please enter the score that should map to a '100%' grade: ")
                )

                if curve_score <= 0:
                    print("The curve score must be greater than 0.")
                    curve_score = None

            except ValueError:
                print("Please enter a valid number.")


    # Creates lists to hold the results
    student_names = []
    letter_grades = []

    error_found = False


    # Reads the first student type
    student_type = input_file.readline()

    # Processes students until the end of the file
    while student_type != "" and error_found == False:

        student_type = student_type.rstrip("\n")

        student_name = input_file.readline()
        grade_text = input_file.readline()


        # Checks for an incomplete student record
        if student_name == "" or grade_text == "":
            print("Incomplete student record detected.")
            error_found = True

        else:
            student_name = student_name.rstrip("\n")
            grade_text = grade_text.rstrip("\n")


            # Checks the student category
            if student_type != "GRAD" and student_type != "UNDERGRAD":
                print("Unknown student category detected (" + student_type + ").")
                error_found = True

            else:

                # Checks that the grade is a number
                try:
                    number_grade = float(grade_text)

                    if number_grade < 0 or number_grade > 100:
                        print("Invalid grade detected (" + grade_text + ").")
                        error_found = True

                except ValueError:
                    print("Invalid grade detected (" + grade_text + ").")
                    error_found = True


                # Curves the grade if needed
                if error_found == False:

                    if curve_choice == "Y":
                        number_grade = number_grade * (100 / curve_score)


                    # Finds the letter grade for a grad student
                    if student_type == "GRAD":

                        if number_grade >= 95:
                            letter_grade = "H"
                        elif number_grade >= 80:
                            letter_grade = "P"
                        elif number_grade >= 70:
                            letter_grade = "L"
                        else:
                            letter_grade = "F"


                    # Finds the letter grade for an undergrad student
                    else:

                        if number_grade >= 90:
                            letter_grade = "A"
                        elif number_grade >= 80:
                            letter_grade = "B"
                        elif number_grade >= 70:
                            letter_grade = "C"
                        elif number_grade >= 60:
                            letter_grade = "D"
                        else:
                            letter_grade = "F"


                    # Saves the student's results
                    student_names.append(student_name)
                    letter_grades.append(letter_grade)


        # Reads the next student type
        if error_found == False:
            student_type = input_file.readline()


    input_file.close()


    # Stops if an error was found
    if error_found == True:
        print("Error occurred while determining letter grade. Aborting.")

    else:

        # Opens the output file and writes the results
        output_file = open(output_file_name, "w")

        for i in range(len(student_names)):
            output_file.write(student_names[i] + "\n")
            output_file.write(letter_grades[i] + "\n")

        output_file.close()

        print("All data was successfully processed and saved to the requested output file.")


main()