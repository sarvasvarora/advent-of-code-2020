from typing import Tuple


class BoardingPass():
    def __init__(self, filename: str) -> None:
        with open(filename, "r") as f:
            self.boarding_passes = f.readlines()
            self.num = len(self.boarding_passes)


    @staticmethod
    def calculate_row(code: str, index: int = 0, start: int = 0, end: int = 127) -> int:
        if index == 6: # base case
            return start if code[index] == 'F' else end

        mid = (start + end) // 2

        if code[index] == 'B': # search the upper half of the rows
            index += 1
            return BoardingPass.calculate_row(code, index, mid + 1, end)
        
        elif code[index] == 'F': # search the lower half of the rows
            index += 1
            return BoardingPass.calculate_row(code, index, start, mid)


    @staticmethod
    def calculate_column(code: str, index: int = 7, start: int = 0, end: int = 7) -> int:
        if index == 9: # base case
            return start if code[index] == 'L' else end

        mid = (start + end) // 2

        if code[index] == 'R': # search the upper half of the columns
            index += 1
            return BoardingPass.calculate_column(code, index, mid + 1, end)
        
        elif code[index] == 'L': # search the lower half of the columns
            index += 1
            return BoardingPass.calculate_column(code, index, start, mid)


    @staticmethod
    def get_seat_ID(boarding_pass: str) -> int:
        row = BoardingPass.calculate_row(boarding_pass)
        column = BoardingPass.calculate_column(boarding_pass)
        seat_ID = (row * 8) + column
        return seat_ID


    def get_highest_seat_ID(self) -> Tuple[str, int]:
        boarding_pass_with_highest_seat_ID = ""
        highest_seat_ID = 0

        for boarding_pass in self.boarding_passes:
            seat_ID = BoardingPass.get_seat_ID(boarding_pass)
            if seat_ID > highest_seat_ID:
                boarding_pass_with_highest_seat_ID = boarding_pass
                highest_seat_ID = seat_ID 

        return (boarding_pass_with_highest_seat_ID, highest_seat_ID)


    def find_missing_ID(self) -> int:
        seat_IDs = list()

        for boarding_pass in self.boarding_passes:
            seat_IDs.append(BoardingPass.get_seat_ID(boarding_pass))
        seat_IDs.sort()

        for i in range(len(seat_IDs) - 1):
            if abs(seat_IDs[i] - seat_IDs[i+1]) > 1: 
                # if the IDs ain't consecutive, that means there's an ID missing. Since only one ID is missing, 
                # we return it.
                return seat_IDs[i] + 1