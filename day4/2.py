from passport import Passport

if __name__ == "__main__":
    data = Passport("input.txt")
    print(f"The number of valid passwords are: {data.find_num_valid_passports(strict=True)}")