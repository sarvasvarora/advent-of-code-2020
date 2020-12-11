from collections import defaultdict


def count (filename: str) -> int:
    with open(filename, "r") as f:
        count = 0
        questions = defaultdict(int)
        n = 0

        while True:
            line = f.readline()
            if line == '\n':
                for question in questions.keys():
                    if questions[question] == n:
                        count += 1
                n = 0
                questions.clear()
                continue
            if line == '':
                for question in questions.keys():
                    if questions[question] == n:
                        count += 1
                break
            
            n += 1
            line = line.strip('\n')
            for question in line:
                questions[question] += 1

        return count


if __name__ == "__main__":
    print(f'The sum of counts is: {count("input.txt")}')