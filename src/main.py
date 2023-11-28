import os
import pydot


file = input("Ingresa el nombre de tu archivo: ")

dotFile = f"/home/zatedev/Documents/python/autoMindMap/src/dotFiles/{file}.dot" # where the .dot file is in.
downloadFile = os.path.expanduser("/mnt/c/Users/Zateward/Documents/School/mapaMental2.svg") # where the .dot files will be downloaded

graph = pydot.graph_from_dot_file(dotFile)

# Si hay varios subgráficos en el archivo .dot, elige el primero
if graph:
    graph = graph[0]
    # Renderiza el gráfico como SVG
    svg_content = graph.create_svg(prog='dot')
    
    # Guarda el archivo SVG en la carpeta "Downloads"
    with open(downloadFile, 'wb') as f:
        f.write(svg_content)
    print(f"Archivo SVG guardado en {downloadFile}")
else:
    print("No se pudo cargar el archivo .dot")