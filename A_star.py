###
# pseudo code
# def evaluate path(grid_list, start_node, end_node)
#       set up open and closed sets of notes
#       start while loop with starting node
#       while open_set > 0:
#           first node of open set gets current node
#           node which is current node gets moved from open to closed set
#           if current note == end_node
#               return path via backtracking of parents of current_nodes
#           find/assign children/adjacent nodes of current node
#           check if children are "legal" --> in grid, not on obstacle
#           check if child of children on closed list or open list
#           create fgh values
#           add child to open_set
#                bring open set in correct queue --> node with biggest f gets lowest index
#       no solution if no path found here###


def reconstruct_path(end_node, start_node):
    path = []
    child_node = end_node
    while child_node is not start_node:
        path.insert(0, child_node)
        child_node = child_node.parent
    return path


def determine_children_of_current_node(current_node, grid_list, closed_nodes, open_nodes):
    children = []
    adjacent_positions_of_current_node = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for position in adjacent_positions_of_current_node:
        x_coordinate = position[1] + current_node.coordinates[0]
        y_coordinate = position[0] + current_node.coordinates[1]
        child = check_if_child_legal(x_coordinate, y_coordinate, grid_list, closed_nodes, open_nodes)
        if child is None:
            continue
        else:
            child.parent = current_node
            children.append(child)
    return children


def check_if_child_legal(x_coordinate, y_coordinate, grid_list, closed_nodes, open_nodes):
    if len(grid_list) - 1 < y_coordinate or y_coordinate < 0:
        return None
    elif len(grid_list[0]) - 1 < x_coordinate or x_coordinate < 0:
        return None
    elif grid_list[y_coordinate][x_coordinate].value == 1:
        return None
    else:
        child = grid_list[y_coordinate][x_coordinate]
        if child in closed_nodes or child in open_nodes:
            return None
        else:
            return child


def set_fgh_values(children, start_node, end_node, current_node):
    for child in children:
        child.g = current_node.g + 1
        child.h = ((start_node.coordinates[0] - end_node.coordinates[0]) ** 2) +\
                  ((start_node.coordinates[1] - end_node.coordinates[1]) ** 2)
        child.f = child.g + child.h
    return children


def add_children_to_open_nodes(children, open_nodes):
    for child in children:
        if len(open_nodes) == 0:
            open_nodes.append(child)
            continue
        for child_of_open_nodes in open_nodes:
            if child.f > child_of_open_nodes.f:
                open_nodes.insert(open_nodes.index(child_of_open_nodes), child)
                break
            elif child.f == child_of_open_nodes.f:
                open_nodes.insert(open_nodes.index(child_of_open_nodes) - 1, child)
                break
            elif child.f < open_nodes[-1].f:
                open_nodes.append(child)
                break
            else:
                continue
    return open_nodes


def evaluate_path(grid_list):

    start_node = grid_list[0][0]
    end_node = grid_list[-1][-1]

    open_nodes = []
    closed_nodes = []

    open_nodes.append(start_node)

    while len(open_nodes) > 0:
        current_node = open_nodes[0]
        closed_nodes.append(open_nodes.pop(0))
        if current_node == end_node:
            path = reconstruct_path(end_node, start_node)
            return path
        children = determine_children_of_current_node(current_node, grid_list, closed_nodes, open_nodes)
        children = set_fgh_values(children, start_node, end_node, current_node)
        open_nodes = add_children_to_open_nodes(children, open_nodes)
        continue
    return False
