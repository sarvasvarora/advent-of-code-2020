from boarding_pass import BoardingPass


if __name__ == "__main__":
    boarding_passes = BoardingPass("input.txt")
    boarding_pass, seat_ID = boarding_passes.get_highest_seat_ID()
    print(f"The boarding pass with highest seat ID is {boarding_pass} and the corresponding ID is {seat_ID}")