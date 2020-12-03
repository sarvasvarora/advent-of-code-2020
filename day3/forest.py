class Forest():

    forest = []
    len = int()

    def __init__(self, fname: str) -> None:
        with open(fname, "r") as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                self.forest.append(line.strip(" \n"))
                self.len = len(self.forest[0])


    def print_forest(self, start: int, end: int) -> None:
        for i in range(start, end):
            print(self.forest[i], '\n')


    def count_trees(self, right: int, down: int) -> int:
        count = 0
        pos = 0

        for i in range(0, len(self.forest), down):
            if self.forest[i][pos] == '#':
                count += 1
            pos = (pos + right) % self.len

        return count