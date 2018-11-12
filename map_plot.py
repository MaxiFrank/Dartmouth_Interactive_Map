# Maxine Liu
# 10/31/2018
# COSC 1
# Lab 3 - drawing code

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

# setting global variables and the default color to blue
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
r = 0
g = 0
b = 1

# call the capabilities of load_graph to get the dictionary.
list_all_vertices = load_graph("dartmouth_graph.txt")
img = load_image("dartmouth_map.png")

# initiate variables
start_vertex = None
goal_vertex = None
special_vertex = None

# main drawing function
def main():
    global start_vertex, goal_vertex, r, g, b, special_vertex


    draw_image(img, 0, 0)

    # draw all the vertices and edges in blue
    for key in list_all_vertices:
        list_all_vertices[key].draw_vertex(r, g, b)
        list_all_vertices[key].draw_all_edges(r, g, b)

    # identify the vertex that the mouse is on
    for key in list_all_vertices:
        if list_all_vertices[key].check_in_vertex_square(mouse_x(), mouse_y()):
            special_vertex = list_all_vertices[key]
            break

    # is the mouse is pressed, the vertex identified above is my starting vertex
    if is_mouse_pressed():
        start_vertex = special_vertex

    # if there's a start vertex and the mouse hovers over a vertex, then it's the goal vertex
    if start_vertex != None:
        set_font_size(15)
        draw_text(start_vertex.name, start_vertex.x + 5, start_vertex.y + 20)
        start_vertex.draw_vertex(1, 0, 0)
        goal_vertex = special_vertex
        draw_text(goal_vertex.name, goal_vertex.x + 5, goal_vertex.y + 20)

    # when there's a start vertex and a goal vertex, call the bfs function to return the shortest path
    if start_vertex != None and goal_vertex != None:
        bfs_path = bfs(start_vertex, goal_vertex)
        item_before = goal_vertex

        # for very vertex in the shortest path, draw the vertex and edge linking the vertex and its backpointer vertex.
        for item in bfs_path:
            item.draw_vertex(1, 0, 0)
            item.draw_edge(item_before, 1, 0, 0)
            item_before = item

start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)




