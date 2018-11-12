# Maxine Liu
# 10/31/2018
# COSC 1
# Lab 3 - Dartmouth pathfinder check point
# creates Vertex class and includes 4 methods

from cs1lib import *

EDGE_WTDTH = 15
VERTEX_RADIUS = 5


class Vertex:

    # __init__ methods takes 3 formal parameters and an informal parameter.
    def __init__(self, name, x, y, adj_verts =[]):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent_vertices = adj_verts

    # append methods appends adjacent vertices to vertex.
    def append(self, vertex):
        self.adjacent_vertices.append(vertex)

    # get_adjacency_list methods returns list of adjacent vertices.
    def get_adjacency_list(self):
        return self.adjacent_vertices

    # __str__ methods formats each line in the vertices.txt file.
    def __str__(self):
        string = self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent Vertices: "
        for s in self.adjacent_vertices:
            string += s.name
            if s != self.adjacent_vertices[- 1]:
                string += ", "

        return string

    # draw a
    # self is local, but r, g, b is the values being passed in, self is reference to object I am currently working on.
    def draw_vertex(self, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # draw the edge between two vertices
    def draw_edge(self, other, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width = EDGE_WTDTH
        draw_line(self.x, self.y, other.x, other.y)

    # draw all the edges between the vertex and all the vertices in its adjacency list
    def draw_all_edges(self, r, g, b):
        set_stroke_width = EDGE_WTDTH
        set_stroke_color (r, g, b)
        for each in self.adjacent_vertices:
            draw_line(self.x, self.y, each.x, each.y)

    # takes as parameters x- and y- coordinates and returns a boolean indicating whether
    # this location is within the smallest surrounding square for this vertex

    def check_in_vertex_square(self, x, y):
        return self.x - VERTEX_RADIUS <= x and self.x + VERTEX_RADIUS >= x \
               and self.y - VERTEX_RADIUS <= y and self.y + VERTEX_RADIUS >= y





