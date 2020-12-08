from boarding_pass import BoardingPass


if __name__ == "__main__":
    boarding_passes = BoardingPass("input.txt")
    print(f"The missing ID is: {boarding_passes.find_missing_ID()}")