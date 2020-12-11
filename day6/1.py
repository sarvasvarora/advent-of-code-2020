from collections import defaultdict


def count(filename: str) -> int:
    with open(filename, "r") as f:
        count = 0
        questions = defaultdict(int)
        while True:
            line = f.readline()
            if line == '\n':
                for _ in questions.keys():
                    count += 1
                questions.clear()
                continue
            if line == "":
                for _ in questions.keys():
                    count += 1
                break
            line = line.strip('\n')
            for question in line:
                questions[question] += 1

        return count


if __name__ == '__main__':
    print(f'The sum of counts is: { count("input.txt") }')