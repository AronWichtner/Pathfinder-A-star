import pygame
import sys
import time
from Node import *
from Grid import *
from A_star import *


grid = Grid()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((grid.cell_size * grid.grid_width, grid.cell_size * grid.grid_height))


def create_grid_list():
    grid_list = []
    for i in range(grid.grid_height):
        row_list = []
        for j in range(grid.grid_width):
            node = Node(j, i, None)
            row_list.append(node)
        grid_list.append(row_list)
    return grid_list


def create_rectangles_from_grid_list(grid_list):
    list_of_rect = []
    for row_list in enumerate(grid_list):
        for row_element in enumerate(row_list[1]):
            rect = pygame.Rect(row_element[0] * grid.cell_size,
                               row_list[0] * grid.cell_size,
                               grid.cell_size, grid.cell_size)
            rect_tuple = (rect, row_element[1].value)
            list_of_rect.append(rect_tuple)
    return list_of_rect


def draw_grid(list_of_rect):
    for rect_tuple in list_of_rect:
        if rect_tuple[1] == 1:
            pygame.draw.rect(screen, (131, 139, 139), rect_tuple[0])
        else:
            pygame.draw.rect(screen, (0, 255, 255), rect_tuple[0])


def find_shortest_path(grid_list):
    path = evaluate_path(grid_list)
    return path


def draw_shortest_path(path):
    if path is False:
        print("no path found")
        pygame.display.update()
    else:
        for node in path:
            rect = pygame.Rect((node.coordinates[0]) * grid.cell_size,
                               (node.coordinates[1]) * grid.cell_size,
                               grid.cell_size, grid.cell_size)
            pygame.draw.rect(screen, (255, 64, 64), rect)
            pygame.display.update()
            time.sleep(0.1)


def main():
    grid_list = create_grid_list()
    rectangles = create_rectangles_from_grid_list(grid_list)
    while True:
        screen.fill((250, 250, 250))
        pygame.display.set_caption("PathFinder")
        draw_grid(rectangles)
        path = find_shortest_path(grid_list)
        draw_shortest_path(path)
        time.sleep(3)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
