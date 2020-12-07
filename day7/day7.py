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


def get_visited(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            get_visited(graph, neighbor, visited)
    return visited


def num_paths(graph, end):
    paths = 0
    for node in graph.keys():
        if node == end:
            continue
        else:
            visited = get_visited(graph, node)
            if end in visited:
                paths += 1
    return paths


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
