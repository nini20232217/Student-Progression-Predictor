# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# student id - 20232217
# date - 11/30/2023

from graphics import *

# ---------- initializing variables --------------
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
valid_credit_range = [0, 20, 40, 60, 80, 100, 120]
program_input_range = [1, 2]
OutcomeList = []

# ------------- selection of the program --------------
while True:
    print("")
    print("part 1")
    program_input = int(input("""Select the program output for:
         1. staff Program
         2. student program

         Enter input number: """))
    if program_input not in program_input_range:
        print("Invalid input. Please enter 1 or 2.")

    else:
        while True:
            while True:
                try:
                    pass_credit = int(input('Enter pass credits: '))  # user inputs pass credits
                    if pass_credit not in valid_credit_range:  # validating whether the pass credits are in range or not
                        print('Pass credits are out of range.')
                        continue

                    defer_credit = int(input('Enter defer credits: '))  # user inputs defer credits
                    if defer_credit not in valid_credit_range:  # validating whether the defer credits are in range or not
                        print('Defer credits are out of range.')
                        continue

                    fail_credit = int(input('Enter fail credits: '))  # user inputs fail credits
                    if fail_credit not in valid_credit_range:  # validating whether the fail credits are in range or not
                        print('Fail credits are out of range.')
                        continue

                    total = pass_credit + defer_credit + fail_credit
                    break

                except ValueError:
                    print("Integer required.")

            # ------------ STAFF PROGRAM ---------------
            if program_input == 1:
                if total == 120:
                    if pass_credit == 120:
                        result = 'Progress'
                        print('Progress')
                        progress_count += 1
                    elif fail_credit >= 80:
                        result = 'Exclude'
                        print('Exclude')
                        exclude_count += 1
                    elif pass_credit == 100:
                        result = 'Trailer'
                        print('Progress(module trailer)')
                        trailer_count += 1
                    else:
                        print('Module retriever')
                        result = 'Retriever'
                        retriever_count += 1
                else:
                    print('Total incorrect.')
                    continue
                OutcomeList.append([result, pass_credit, defer_credit, fail_credit])  # creating a list with the above outcomes

                # creating a histogram
                def create_histogram(outcome_list):
                    win = GraphWin('Histogram Results', 800, 600)
                    win.setBackground('light gray')  # background color of the histogram window

                    total_students = len(outcome_list)

                    progress_count = 0
                    trailer_count = 0
                    retriever_count = 0
                    exclude_count = 0

                    for outcome in outcome_list:  # counting the occurrences of different outcomes to create the histogram
                        result, _, _, _ = outcome
                        if result == 'Progress':
                            progress_count += 1
                        elif result == 'Trailer':
                            trailer_count += 1
                        elif result == 'Retriever':
                            retriever_count += 1
                        elif result == 'Exclude':
                            exclude_count += 1

                    x = 100  # the horizontal position of the first bar
                    width = 80  # deciding the width of each bar
                    spacing = 30  # the horizontal space between the bars
                    height = 400  # the height of each bar

                    colors = ['pink1', 'rosy brown', 'misty rose3', 'plum3']
                    progression_labels = ['Progress', 'Trailer', 'Retriever', 'Excluded']

                    for items, count in enumerate([progress_count, trailer_count, retriever_count, exclude_count]):
                        point1 = Point(x, height)
                        point2 = Point(x + width, height - count * 15)
                        bar = Rectangle(point1, point2)
                        bar.setFill(colors[items])
                        bar.setOutline('black')
                        bar.setWidth(2)
                        bar.draw(win)

                        bar_label = Text(Point(x + width / 2, height + 20), progression_labels[items])
                        bar_label.setStyle('normal')
                        bar_label.setSize(10)
                        bar_label.draw(win)

                        count_text = Text(Point(x + width / 2, height - count * 5 - 20), f"{count} students")
                        count_text.setSize(10)
                        count_text.draw(win)

                        x += width + spacing  # maintaining the width and space between each bars

                    total_text = Text(Point(400, 550),
                                      f" {total_students} students in total\n mouse click to continue")
                    total_text.setStyle('bold')
                    total_text.setSize(12)
                    total_text.draw(win)

                    win.getMouse()  # click to close the window
                    win.close()


                # asking the staff user to input whether to terminate the program
                user_input = input("Do you want to enter another set of data? (y to continue, q to quit): ")
                if user_input.lower() == 'y':
                    continue
                elif user_input.lower() == 'q':
                    create_histogram(OutcomeList)  # display histogram
                    # Part 2 - display the list
                    print("")
                    print("Part 2")
                    print("Reading the list:")
                    for outcomes in OutcomeList:
                        print(f'[{outcomes[0]} - {outcomes[1]}, {outcomes[2]}, {outcomes[3]}]')

                    while True:  # creating the text file
                        try:
                            f = open("W2053489.txt", "x")
                        except FileExistsError:
                            pass
                        with open("W2053489.txt", "w") as n:  # writing to the file
                            for i in range(0, len(OutcomeList)):
                                print(*OutcomeList[i], file=n)
                        print("")

                        print("Part 3")
                        print('Reading the text file:')
                        # reading from the file
                        with open("W2053489.txt", "r") as fo:
                            print(fo.read())
                        print("")
                        fo.close()
                        break
                    break
                raise SystemExit
        # ---- Student Program ------
            elif program_input == 2:
                if total == 120:
                    if pass_credit == 120:
                        print('Progress')
                        break
                    elif fail_credit >= 80:
                        print('Exclude')
                        break
                    elif pass_credit == 100:
                        print('Progress(module trailer)')
                        break
                    else:
                        print('Module retriever')
                        break
                else:
                    print('Total incorrect.')
                raise SystemExit
            else:
                print('Wrong input. Try Again')
                raise SystemExit  # Exiting the program

# References
# 1 - Python Lists - W3schools (2019). Python Lists. [online] W3schools.com. Available at: https://www.w3schools.com/python/python_lists.asp.
# 2 - Python file handling - www.w3schools.com. (n.d.). Python File Open. [online] Available at: https://www.w3schools.com/python/python_file_handling.asp.
# 3 - User defined functions in python - GeeksforGeeks. (2019). Python User defined functions. [online] Available at: https://www.geeksforgeeks.org/python-user-defined-functions/.
# 4 - Stack Overflow. (n.d.). ubuntu - How do I print the content of a .txt file in Python? [online] Available at: https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python.
# 5 - Stack Overflow. (n.d.). syntax - What does ‘while True’ mean in Python? [online] Available at: https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python.
# 6 - Python exit commands - freeCodeCamp.org. (2023). Python Exit – How to Use an Exit Function in Python to Stop a Program. [online] Available at: https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:~:text=The%20exit()%20function%20in.
# GeeksforGeeks. (2019). Python exit commands: quit(), exit(), sys.exit() and os._exit(). [online] Available at: https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/.
# 7 - Underscore in python - https://www.geeksforgeeks.org/underscore-_-python/
