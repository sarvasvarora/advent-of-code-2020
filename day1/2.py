def main():
    entries = set([])

    with open("report.txt", "r") as f:
        entries = f.readlines()

    entries = [int(i) for i in entries]
    entries.sort()

    # Very naïve solution :")
    for i in entries:
        entries.remove(i)
        for j in entries:
            entries.remove(j)
            for k in entries:
                if (i + j + k) == 2020:
                    return f"Numbers found: {i}, {j}, and {k}\nProduct is {i * j * k}"
            entries.append(j)
        entries.append(i)
        entries.sort()



if __name__ == "__main__":
    print(main())