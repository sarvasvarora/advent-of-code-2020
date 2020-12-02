def binary_search(a, val, start, end):
    mid = (start + end)//2
    if start >= end:
        return val == a[mid]

    if val == a[mid]:
        return True
    elif val < a[mid]:
        return binary_search(a, val, start, mid - 1)
    elif val > a[mid]:
        return binary_search(a, val, mid + 1, end)

def main():
    entries = []

    with open("report.txt", "r") as f:
        entries = f.readlines()

    entries = [int(i) for i in entries]
    entries.sort()

    for i in entries:
        rem = 2020 - i
        if binary_search(entries, rem, 0, len(entries)):
            print(f"Numbers found: {i} and {rem}\nProduct is {i * rem}")
            break


if __name__ == "__main__":
    main()