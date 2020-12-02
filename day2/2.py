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
        index1 = int(item[0].split(' ')[0].split('-')[0]) - 1
        index2 = int(item[0].split(' ')[0].split('-')[1]) - 1
        alph = item[0].split(' ')[1]

        for i in item[1]:
            l1 = i[index1]
            l2 = i[index2]

            if (l1 == alph and l2 != alph) or (l1 != alph and l2 == alph):
                num += 1

    return num


if __name__ == "__main__":
    print(main())