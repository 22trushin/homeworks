import random
from math import sqrt
from heapq import heappop, heappush


"""def draw_board(board):
    print('__________')
    print('|' + str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|' + str(board[3]) + '|')
    print('----------')
    print('|' + str(board[4]) + '|' + str(board[5]) + '|' + str(board[6]) + '|' + str(board[7]) + '|')
    print('----------')
    print('|' + str(board[8]) + '|' + str(board[9]) + '|' + str(board[10]) + '|' + str(board[11]) + '|')
    print('----------')
    print('|' + str(board[12]) + '|' + str(board[13]) + '|' + str(board[14]) + '|' + str(board[15]) + '|')
    print('----------')"""


def draw_board9(board):
    print('_______')
    print('|' + str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|')
    print('-------')
    print('|' + str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]) + '|')
    print('-------')
    print('|' + str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]) + '|')
    print('-------')


def creating_random_list():
    list1 = list(range(0, 9))
    random.shuffle(list1)
    # list1 = [7, 2, 4, 3, 1, 6, 0, 8, 5]  # - решение есть
    # list1 = [7, 2, 4, 3, 1, 6, 0, 5, 8]  # - решения нет
    return list1


def manh_dst_matrix(a, b, n):
    """Find manhattan distance between `a` and `b` in matrix of size `n`
    """
    return abs(a % n - b % n) + abs(a // n - b // n)


class Chain15:

    def __str__(self):
        i = 0
        sstr = ""
        while i < self.size ** 2:
            sstr += str(self.board_state[i]) + " "
            if i % self.size == 3:
                sstr += "\n"
            i += 1
        return sstr

    def __init__(self, board_state, history=[]):
        self.board_state = list(board_state)
        self.size = int(sqrt(len(board_state)))
        self.history = history
        self.quad_size = int(self.size * self.size)

    def __getitem__(self, key):
        return self.board_state[key]

    def __len__(self):
        return len(self.board_state)

    def manh_dst(self):
        dst = 0
        for i in range(0, self.quad_size):
            dst += manh_dst_matrix((self.board_state[i] - 1) % self.quad_size, i, self.size)
        return int(dst)

    def last_node(self):
        return str(self.board_state)

    def last_move(self):
        if self.board_state[-1] == self.quad_size - 1 or self.board_state[-1] == self.quad_size - self.size:
            return 0
        return 2

    def corner_tiles(self):
        conflict_count = 0
        # upper left corner
        if self.board_state[0] != 1:
            if self.board_state[1] == 2 or self.board_state[self.size] == self.size + 1:
                conflict_count += 1
        # upper right corner
        if self.board_state[self.size - 1] != self.size:
            if self.board_state[self.size - 2] == self.size - 1 or self.board_state[self.size * 2 - 1] == self.size * 2:
                conflict_count += 1
        # lower left corner
        if self.board_state[self.quad_size - self.size] != self.quad_size - self.size + 1:
            if self.board_state[self.quad_size - self.size * 2] == self.quad_size - self.size * 2 + 1 or self.board_state[self.quad_size - self.size + 1] == self.quad_size - self.size + 2:
                conflict_count += 1

        return 2 * conflict_count

    def simple_heur(self):
        dst = 0
        for i in range(0, int(self.quad_size)):
            if (self.board_state[i] - 1) != i:
                dst += 1
        return dst

    def h(self):
        return self.manh_dst() + self.last_move()

    def g(self):
        return len(self.history)

    def f(self):
        return self.h() + self.g()

    def __lt__(self, other):
        return self.f() < other.f()

    def get_neighbours(self):
        neighs = []
        zero_coord = self.board_state.index(0)

        # look at neighbours
        if zero_coord + 1 < self.size ** 2 and manh_dst_matrix(zero_coord, zero_coord + 1, self.size) == 1:
            new_state = self.board_state.copy()
            new_state[zero_coord], new_state[zero_coord + 1] = new_state[zero_coord + 1], new_state[zero_coord]
            neighs.append(Chain15(new_state, self.history + [self]))

        if zero_coord - 1 >= 0 and manh_dst_matrix(zero_coord, zero_coord - 1, self.size) == 1:
            new_state = self.board_state.copy()
            new_state[zero_coord], new_state[zero_coord - 1] = new_state[zero_coord - 1], new_state[zero_coord]
            neighs.append(Chain15(new_state, self.history + [self]))

        if zero_coord + self.size < self.size ** 2 and manh_dst_matrix(zero_coord, zero_coord + self.size,
                                                                       self.size) == 1:
            new_state = self.board_state.copy()
            new_state[zero_coord], new_state[zero_coord + self.size] = new_state[zero_coord + self.size], new_state[
                zero_coord]
            neighs.append(Chain15(new_state, self.history + [self]))

        if zero_coord - self.size >= 0 and manh_dst_matrix(zero_coord, zero_coord - self.size, self.size) == 1:
            new_state = self.board_state.copy()
            new_state[zero_coord], new_state[zero_coord - self.size] = new_state[zero_coord - self.size], new_state[
                zero_coord]
            neighs.append(Chain15(new_state, self.history + [self]))

        return neighs


def a_star(start_chain, goal_node):
    node_hash = {}
    chains_queue = []
    heappush(chains_queue, start_chain)
    while chains_queue:
        cur_chain = heappop(chains_queue)
        cur_node = cur_chain.last_node()
        if cur_node == goal_node:
            return cur_chain
        node_hash[cur_node] = cur_chain.g()
        for chain in cur_chain.get_neighbours():
            if chain.last_node() in node_hash:
                if chain.g() >= node_hash[chain.last_node()]:
                    continue
                node_hash[chain.last_node()] = chain.g()
            heappush(chains_queue, chain)

    raise Exception("No solution?!")


def check_solution(list, index_zero):
    count = 0
    for i in range(len(list)):
        for k in range(len(list[i:])):
            if (list[i] > list[i + k]) and (list[i + k]):
                count = count + 1
    free_space_local = index_zero
    e = free_space_local // sqrt(len(list))
    count = count + e
    if count % 2 != 0:
        solution = 'Not exist'
    else:
        solution = 'Exist'
    return solution


new_list = creating_random_list()
free_space = new_list.index(0)
print('Ноль сейчас на позиции: ', free_space)

start = Chain15(new_list)
end = Chain15((1, 2, 3, 4, 5, 6, 7, 8, 0))
draw_board9(start)
print('Решение: ', check_solution(start, free_space))

if check_solution(start, free_space) == 'Exist':
    result = a_star(start, end.last_node())
    print('Количество ходов: ', str(len(result.history)))
    for node in result.history:

        draw_board9(node)
        print('\n', 'Next', '\n')

    draw_board9(result)
else:
    print('Данное расположение фишек решения не имеет :(((')
