# compute_graph.py
# could use some optimizations
import scipy.spatial
from typing import Dict, Set, List
from flashcard import Flashcard, Node, Graph


def compute_graph(flashcards: List[Flashcard], sim_max = 5) -> Graph:
    """Construct a graph of nodes from a list of Flashcards."""
    graph = Graph()
    for flashcard in flashcards:
        graph.add_node(Node(flashcard, set(), set()))
    done = set()
    available = set(graph.nodes)
    if len(available) == 1:
        node = available.pop()
        graph.add_edge((node, node))
        return graph.graph_to_json()
    while len(available) > 0:
        sim_scores = compute_sim_scores(graph, sim_max)
        sim_scores.sort(key=lambda x: x[2], reverse=True)
        for edge in sim_scores:
            if edge[0] in done or edge[1] in done:
                continue
            if len(edge[0].point_out) == 2 and len(edge[0].point_in) == 2:
                done.add(edge[0])
                available.remove(edge[0])
            elif len(edge[1].point_out) == 2 and len(edge[1].point_in) == 2:
                done.add(edge[1])
                available.remove(edge[1])
            elif len(edge[0].point_out) < 2 and len(edge[1].point_in) < 2:
                graph.add_edge(edge)
                edge[0].point_out.add(edge[1])
                edge[1].point_in.add(edge[0])
        if sim_max < len(graph.nodes) * 2:
            sim_max *= 2
        else:
            break

    return graph.graph_to_json()


def compute_sim_scores(graph, depth_limit):
    sim_scores = set()
    for node in graph.nodes:
        depth = 0
        for other_node in graph.nodes:
            if node.flashcard.front != other_node.flashcard.front:
                cos_sim = 1 - scipy.spatial.distance.cosine(
                    node.flashcard.get_embedding(), other_node.flashcard.get_embedding()
                )
                sim_scores.add((node, other_node, cos_sim))
            else:
                continue
            depth += 1
            if depth > depth_limit:
                break

    return list(sim_scores)
