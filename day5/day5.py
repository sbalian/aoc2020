#!/usr/bin/env python


def get_boarding_passes(path):
    with open(path) as f:
        boarding_passes = f.read().strip().split()
    return boarding_passes


def get_coord(boarding_pass_section, positive_char, n):
    array = [i for i in range(n)]
    for char in boarding_pass_section:
        if char == positive_char:
            array = array[: len(array) // 2]
        else:
            array = array[len(array) // 2 :]  # noqa
    return array[0]


def get_row_section(boarding_pass):
    return boarding_pass[:7]


def get_col_section(boarding_pass):
    return boarding_pass[7:]


def get_row(boarding_pass):
    section = get_row_section(boarding_pass)
    return get_coord(section, "F", 128)


def get_col(boarding_pass):
    section = get_col_section(boarding_pass)
    return get_coord(section, "L", 8)


def get_all_sections(n, char1, char2):
    return [
        bin(i)[2:].zfill(n).replace("0", char1, -1).replace("1", char2, -1)
        for i in range(2 ** n)
    ]


def generate_all_boarding_passes():
    all_row_sections = get_all_sections(7, "F", "B")
    all_col_sections = get_all_sections(3, "L", "R")

    boarding_passes = []
    for row_section in all_row_sections:
        for col_section in all_col_sections:
            boarding_passes.append(row_section + col_section)

    return boarding_passes


def find_my_seat(boarding_passes):
    all_boarding_passes = generate_all_boarding_passes()
    possible_boaring_passes = set(all_boarding_passes) - set(boarding_passes)

    coords = [
        (get_row(boarding_pass), get_col(boarding_pass))
        for boarding_pass in possible_boaring_passes
    ]
    rows = [coord[0] for coord in coords]
    unique_rows = set(rows)

    for row in unique_rows:
        if rows.count(row) == 1:
            break
    my_row = row

    for row, col in coords:
        if row == my_row:
            break
    my_col = col

    return seat_id_from_row_col(my_row, my_col)


def seat_id_from_row_col(row, col):
    return row * 8 + col


def seat_id(boarding_pass):
    return seat_id_from_row_col(get_row(boarding_pass), get_col(boarding_pass))


def max_seat_id(boarding_passes):
    return max([seat_id(boarding_pass) for boarding_pass in boarding_passes])


def main():
    boarding_passes = get_boarding_passes("input.txt")
    assert max_seat_id(boarding_passes) == 991
    assert find_my_seat(boarding_passes) == 534
    print("All tests passed.")


if __name__ == "__main__":
    main()
