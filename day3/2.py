from forest import Forest

if __name__ == "__main__":
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    forest = Forest("input.txt")
    for slope in slopes:
        product *= forest.count_trees(slope[0], slope[1])
    print(f"The required product is: {product}")