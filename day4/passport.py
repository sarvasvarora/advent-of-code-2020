import re

class Passport():
    passports = list()
    strict_rules = {
        "byr": re.compile(r"19[2-9]\d|200[0-2]"), #four digits; at least 1920 and at most 2002
        "iyr": re.compile(r"201\d|2020"), #four digits; at least 2010 and at most 2020
        "eyr": re.compile(r"202\d|2030"), #four digits; at least 2020 and at most 2030.
        "hgt": re.compile(r"1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in"), #a number followed by either cm (>= 150 and <= 193) or in (>= 59 and <= 76)
        "hcl": re.compile(r"#[0-9a-f]{6}"), # a # followed by exactly six characters 0-9 or a-f
        "ecl": re.compile(r"amb|blu|brn|gry|grn|hzl|oth"), #exactly one of: amb blu brn gry grn hzl oth
        "pid": re.compile(r"\d{9}"), #a nine-digit number, including leading zeroes
        "cid": "" #ignored, missing or not
    }


    def __init__(self, fname: str) -> None:
        with open(fname, "r") as f:
            passport = dict()
            while True:
                # Read line
                line = f.readline()
                if line == '':
                    self.passports.append(passport.copy()) # Append current passport to self.passports
                    break # EOF reached
                elif line == '\n':
                    self.passports.append(passport.copy()) # Append current passport to self.passports
                    passport.clear() # Clear the current passport after appending it
                    continue
                else:
                    line = line.strip(" \n").split(" ") # Clean up line and make a list out of entries
                    # Save entries of current passport into the local variable
                    for l in line:
                        passport[l.split(':')[0]] = l.split(':')[1]


    def print_passport(self, start: int = 0, end: int = len(passports)) -> None:
        for i in range(start, end):
            print(f"PASSPORT {i + 1}\n{self.passports[i]}\n")


    @classmethod
    def validate_passport(cls, passport: dict) -> bool:
        
        def invalid_field(key: str, val: str) -> bool:
            if cls.strict_rules[key].fullmatch(val) == None:
                return True # if invalid
            return False # if valid
        
        check = [invalid_field(k, v) for k, v in passport.items() if k != "cid"]
        return False if any(check) else True # return False if any field (except "cid") is invalid, else True


    def find_num_valid_passports(self, strict: bool = False) -> int:
        valid_passwords = 0

        for i in self.passports:
            if len(i) == 8:
                valid_passwords += 1
                if strict and not Passport.validate_passport(i):
                    valid_passwords -= 1

            elif (len(i) == 7) and ("cid" not in i.keys()):
                valid_passwords += 1
                if strict and not Passport.validate_passport(i):
                    valid_passwords -= 1

        return valid_passwords
