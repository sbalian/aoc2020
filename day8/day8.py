#!/usr/bin/env python


import copy


def get_instructions(path):
    with open(path) as f:
        instructions = f.read().strip().split("\n")
    return instructions


def parse_instruction(instruction):
    instruction_name, instruction_value = instruction.split()
    instruction_value = int(instruction_value)
    return instruction_name, instruction_value


def get_acc(instructions):
    visited = []
    position = 0
    acc = 0
    terminates = False
    n = len(instructions)
    while position not in visited:
        instruction, instruction_value = parse_instruction(
            instructions[position]
        )
        if instruction == "acc":
            acc += instruction_value
            visited.append(position)
            position += 1
        elif instruction == "nop":
            visited.append(position)
            position += 1
        else:  # jump
            visited.append(position)
            position += instruction_value
        if position == n:
            terminates = True
            break
    return acc, terminates


def get_terminating_acc(instructions):
    jmp_nop_positions = []
    for i, instruction in enumerate(instructions):
        instruction, _ = parse_instruction(instruction)
        if instruction in ["jmp", "nop"]:
            jmp_nop_positions.append(i)

    candidates = [instructions]
    for i in jmp_nop_positions:
        candidate = copy.copy(instructions)
        instruction = instructions[i]
        if instruction.startswith("jmp"):
            instruction = instruction.replace("jmp", "nop")
        else:
            instruction = instruction.replace("nop", "jmp")
        candidate[i] = instruction
        candidates.append(candidate)

    for candidate in candidates:
        acc, terminates = get_acc(candidate)
        if terminates:
            return acc
    return -1


def main():
    instructions = get_instructions("input.txt")
    acc, _ = get_acc(instructions)
    assert acc == 1563
    assert get_terminating_acc(instructions) == 767
    print("All tests passed.")


if __name__ == "__main__":
    main()
