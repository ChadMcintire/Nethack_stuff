import matplotlib.pyplot as plt

class GraphBuilder:
    """Builder to store data points and build graphs

    Keyword Arguments:
        - graph_types       -- List of the type of graph to build. i.e: "heat_pos" builds a heat map of all positions the agent visited

    """
    def __init__(self, graph_types):
        self.graphs_data = {}

        for g in graph_types:
            self.graphs_data[g] = []

    def add_data(self, graph_type, data):
        """
        Keyword Arguments:
            - graph_type    --Type of graph, also the key in graphs_data
            - data          --Expects an array of tuples for graph_type of 'heat_pos' and 'heat_search'
        """
        self.graphs_data[graph_type] = data

    def render_graphs(self):
        for key in self.graphs_data:
            data = self.graphs_data[key]
            # unzip tuple and convert into two 1D lists
            pts = [[i for i in data], [j for j in data]]

            plt.imsave(fname="tmp.png", arr=pts, cmap='coolwarm')

