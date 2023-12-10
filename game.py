import logic

# global running variable
RUN = True

# Driver code
if __name__ == '__main__':
    # calling start_game function
    # to initialize the matrix
    mat = logic.start_game()

    while RUN:
        # taking the user input for the next step
        x = input(":")

        # Define a dictionary to map user input to functions
        move_actions = {
            'W': logic.move_up,
            'S': logic.move_down,
            'A': logic.move_left,
            'D': logic.move_right
        }

        # Check if the input is a valid key
        if x.upper() in move_actions:
            # Call the corresponding move function
            mat, flag = move_actions[x.upper()](mat)

            # get the current state and print it
            status = logic.get_current_state(mat)
            print(status)

            # if the game is not over, continue and add a new two
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
            else:
                RUN = False  # Set RUN to False when the game is over

        # Show Commands
        elif x.upper() == 'P':
            logic.show_commands()

        # exit game
        elif x.upper() == 'X':
            print("Exiting Game")
            RUN = False

        else:
            print("Invalid Key Pressed")

        # print the matrix after each move.
        if x.upper() not in ('P', 'X') and status != 'GAME OVER':
            logic.draw_grid(mat)
