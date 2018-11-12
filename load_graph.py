# Maxine Liu
# 10/31/2018
# COSC 1
# Lab 3 - Dartmouth pathfinder check point
# load graph function that takes in file_name as formal parameter
# reformat text file for use in building breadth first search map


from vertex import *

def load_graph(file_name):

    # first pass through the text file.
    in_file = open(file_name, "r")

    list_all_vertices = {}


    # semicolon splits each line and strips spaces off each item in python list.
    for line in in_file:
        split_line = line.split(";")

        for n in split_line:
            n.strip()

        # set up variables for name and x and y coordinates into an integer.
        name = split_line[0]
        x_and_y_split = split_line[2].split(",")
        x = int(x_and_y_split[0].strip())
        y = int(x_and_y_split[1].strip())

        # create vertex object with three formal parameters.
        this_vertex = Vertex(name, x, y)

        # adds vertex object to the dictionary
        list_all_vertices[name] = this_vertex

    in_file.close()

    # second pass through the text file.
    in_file = open(file_name, "r")


    for line in in_file:
        split_line = line.split(";")

        for n in split_line:
            n.strip()

        # set up variables for name and adjacent vertices list.
        name = split_line[0]
        adj_vert_list = []
        adj_vert_split = split_line[1].split(",")

        # finds the adjacent vertex from the list_all_vertices dictionary
        for i in adj_vert_split:
            k = i.strip()
            adj_vert_list.append(list_all_vertices[k])  # appends stripped adjacent vertex from the dictionary

        # for every line in the text file, once the previous two loops have been executed
        # add the identified adjacent vertices as an attribute of the vertex referenced by name.
        list_all_vertices[name].adjacent_vertices = adj_vert_list

    in_file.close()
    return list_all_vertices
