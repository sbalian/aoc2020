#!/usr/bin/env python


def is_digits(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_valid_year(value, min, max):
    if not is_digits(value):
        return False
    elif min <= int(value) <= max:
        return True
    else:
        return False


def is_valid_byr(value):
    return is_valid_year(value, 1920, 2002)


def is_valid_iyr(value):
    return is_valid_year(value, 2010, 2020)


def is_valid_eyr(value):
    return is_valid_year(value, 2020, 2030)


def is_valid_hgt(value):
    if value.endswith("cm") or value.endswith("in"):
        v = value[:-2]
        if not is_digits(v):
            return False
        else:
            v = int(v)
            if value.endswith("cm") and (150 <= v <= 193):
                return True
            elif value.endswith("in") and (59 <= v <= 76):
                return True
            else:
                return False
    else:
        return False


def is_valid_hcl(value):
    if not value.startswith("#"):
        return False
    else:
        if len(value[1:]) != 6:
            return False
        else:
            num_valid = 0
            for char in value[1:]:
                if (97 <= ord(char) <= 102) or (48 <= ord(char) <= 57):
                    num_valid += 1
            if num_valid == 6:
                return True
            else:
                return False


def is_valid_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_pid(value):
    if len(value) != 9:
        return False
    else:
        num_valid = 0
        for char in value:
            if 48 <= ord(char) <= 57:
                num_valid += 1
        if num_valid == 9:
            return True
        else:
            return False


def is_valid_key(key, value):
    if key == "byr":
        return is_valid_byr(value)
    elif key == "iyr":
        return is_valid_iyr(value)
    elif key == "eyr":
        return is_valid_eyr(value)
    elif key == "hgt":
        return is_valid_hgt(value)
    elif key == "hcl":
        return is_valid_hcl(value)
    elif key == "ecl":
        return is_valid_ecl(value)
    else:
        return is_valid_pid(value)


def read_passports(path):
    with open(path) as f:
        passports = f.read().split("\n\n")
    return passports


def valid_passports1(passports):
    num_valid = 0
    for passport in passports:
        if passport.count(":") == 8:
            num_valid += 1
        elif (passport.count(":") == 7) and (passport.find("cid:") == -1):
            num_valid += 1
    return num_valid


def extract_fields(passport):
    passport = passport.replace("\n", " ")
    combined_fields = passport.split()
    fields = {}
    for key_value in combined_fields:
        key, value = key_value.split(":")
        if key != "cid":
            fields[key] = value
    return fields


def is_valid(fields):
    if len(fields.keys()) == 7:
        num_keys_valid = 0
        for key, value in fields.items():
            if is_valid_key(key, value):
                num_keys_valid += 1
        if num_keys_valid == 7:
            return True
        else:
            return False
    else:
        return False


def valid_passports2(passports):
    return sum([is_valid(extract_fields(passport)) for passport in passports])


def main():
    passports = read_passports("input.txt")
    assert valid_passports1(passports) == 219
    assert valid_passports2(passports) == 127
    print("All tests passed.")


if __name__ == "__main__":
    main()
