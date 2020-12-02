from collections import defaultdict, Counter


def main():
    num = 0
    policy_pass_dict = defaultdict(list)

    with open("input.txt", "r") as f:
        tmp = f.readlines()
        tmp = [i.split("\n")[0] for i in tmp]

        policies = [i.split(": ")[0] for i in tmp]
        check = [i.split(": ")[1] for i in tmp]

        for entry in zip(policies, check):
            policy_pass_dict[entry[0]].append(entry[1])


    for item in policy_pass_dict.items():
        min = int(item[0].split(' ')[0].split('-')[0])
        max = int(item[0].split(' ')[0].split('-')[1])
        alph = item[0].split(' ')[1]

        for i in item[1]:
            count = Counter(i)[alph]
            if count >= min and count <= max:
                num += 1

    return num


if __name__ == "__main__":
    print(main())