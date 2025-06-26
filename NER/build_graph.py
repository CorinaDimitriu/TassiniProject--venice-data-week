import networkx as nx


def build_graph(entity_file):
    G = nx.Graph()
    with open(entity_file, 'r', encoding='utf-18') as ef:
        for line in ef.readlines():
            line = line.strip().lstrip('%').strip()
            split_line = line.split('%')
            place = split_line[0]
            entities = split_line[1].split('#')

            # add place and entities as nodes
            if place not in G:
                G.add_node(place)
            for entity in entities:
                if entity not in G:
                    G.add_node(entity)
                if not G.has_edge(place, entity) and not G.has_edge(entity, place):
                    G.add_edge(place, entity)

            #  we have edges between: place and entities, one for each connection
    return G


build_graph("NER\\temporary_NER_results.txt")
