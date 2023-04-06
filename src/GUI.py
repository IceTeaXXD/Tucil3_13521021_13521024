import sys
import networkx as nx
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget, QDesktopWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Graph import*
from UCS import*

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Bewe <3 Nadil")
        self.setGeometry(0, 0, 1280, 720) # set initial position and size of the window

        # Center the window on the screen
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())


        # Create a Matplotlib figure and a NetworkX graph
        self.figure = Figure()
        self.graph = self.figure.add_subplot(111)
        self.graph.set_axis_off()

        # Create a canvas for the Matplotlib figure
        self.canvas = FigureCanvas(self.figure)

        # Create a vertical layout and add the Matplotlib canvas to it
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Add nodes and edges to the NetworkX graph
        G = nx.DiGraph()
        graph = Graph()
        graph.createGraph("test/map2.txt")
        # insert edges to G
        graph.printGraph()
        for node in graph.nodes:
            for neighbor in graph.nodes[node]:
                G.add_edge(node, neighbor[0], weight=neighbor[1])
        start = 1
        goal = 8
        ucspath = list_to_adjacent_pairs(resultToArray(ucs(graph, start, goal)))
        print(ucspath)
        # Draw the NetworkX graph on the Matplotlib figure
        pos = nx.circular_layout(G)
        # color blue for 1->3;  2->3
        edge_colors = ['red' if (u,v) in ucspath else 'black' for u,v in G.edges()]
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx(G, pos, with_labels=True, font_weight='bold', node_color='red', alpha=0.7, node_size=2000, ax=self.graph, edge_color=edge_colors, width=[1 if c=='black' else 4 for c in edge_colors])

        
        # Show the window
        self.show()


if __name__ == "__main__":
    # Start the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    sys.exit(app.exec_())
