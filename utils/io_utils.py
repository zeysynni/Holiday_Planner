def save_graph_png(graph, path="graph.png"):
    png_data = graph.get_graph().draw_mermaid_png()
    with open(path, "wb") as f:
        f.write(png_data)
