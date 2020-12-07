#!/usr/bin/env python


from collections import defaultdict


def get_graph(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    graph = defaultdict(list)
    for line in lines:
        node, edges = (
            line.rstrip(".")
            .replace("bags", "")
            .replace("bag", "")
            .replace("contain", "")
        ).split("  ")
        if edges == " no other ":
            graph[node] = []
        else:
            edges = edges.strip().split(" , ")
            for edge in edges:
                graph[node].append((edge[2:], int(edge[:2])))
    return graph


def path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            path_exists(graph, neighbor, end, visited)
    return end in visited


def num_paths(graph, end):
    return sum(
        [
            node != end and path_exists(graph, node, end)
            for node in graph.keys()
        ]
    )


def num_bags_(graph, start):
    n = 1
    for neighbor, w in graph[start]:
        n += w * num_bags_(graph, neighbor)
    return n


def num_bags(graph, start):
    return num_bags_(graph, start) - 1


def main():
    graph = get_graph("input.txt")
    assert num_paths(graph, "shiny gold") == 126
    assert num_bags(graph, "shiny gold") == 220149
    print("All tests passed.")


if __name__ == "__main__":
    main()
