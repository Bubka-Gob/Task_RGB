
class Structure:
    __colors = []
    __connections = []

    def __init__(self, rgb_list):
        self.__colors = rgb_list
        self.create_connections()

    def create_connections(self):
        self.__connections = [list(range(15 * y, 15 * y + 15)) for y in range(10)]
        for y in range(10):
            for x in range(15):
                if self.__colors[y][x] != 0:
                    if y < 9:
                        if self.__colors[y][x] == self.__colors[y+1][x]:
                            self.__connections[y+1][x] = self.__connections[y][x]
                    if x < 14:
                        if self.__colors[y][x] == self.__colors[y][x+1]:
                            self.__connections[y][x+1] = self.__connections[y][x]

    def __shift_down(self):
        for x in range(15):
            for y in range(10):
                if self.__colors[y][x] != 0:
                    temp_y = 0
                    while temp_y < 9:
                        if self.__colors[temp_y][x] != 0 and self.__colors[temp_y+1][x] == 0:
                            self.__colors[temp_y+1][x] = self.__colors[temp_y][x]
                            self.__colors[temp_y][x] = 0
                        temp_y += 1

    def __shift_left(self):
        for x in reversed(range(15)):
            if not self.__is_empty_column(x):
                temp_x = 14
                while temp_x > 0:
                    if not self.__is_empty_column(temp_x) and self.__is_empty_column(temp_x-1):
                        self.__move_column_left(temp_x)
                    temp_x -= 1

    def remove(self, y_picked, x_picked):
        if y_picked < 0 or y_picked > 9 or x_picked < 0 or x_picked > 14:
            print(f"Invalid move at {x_picked} {y_picked}")
            return -1, -1
        cluster_number = self.__connections[y_picked][x_picked]
        if not self.is_valid_cluster(cluster_number):
            print(f"Invalid move at {x_picked} {y_picked}")
            return -1, -1
        counter = 0
        color = self.__colors[y_picked][x_picked]
        for y in range(10):
            for x in range(15):
                if self.__connections[y][x] == cluster_number:
                    self.__colors[y][x] = 0
                    counter += 1
        self.__shift_down()
        self.__shift_left()
        self.create_connections()
        return counter, color

    def is_valid_cluster(self, cluster_number):
        counter = 0
        for y in self.__connections:
            for x in y:
                if x == cluster_number:
                    counter += 1
        if counter > 1:
            return True
        else:
            return False

    def __is_empty_column(self, column_number):
        for y in range(10):
            if self.__colors[y][column_number] != 0:
                return False
        return True

    def __move_column_left(self, column_number):
        for y in range(10):
            self.__colors[y][column_number-1] = self.__colors[y][column_number]
            self.__colors[y][column_number] = 0

    def get_biggest_cluster(self):
        flat_list = [el for sublist in self.__connections for el in sublist]
        cluster = max(flat_list, key=flat_list.count)
        if not self.is_valid_cluster(cluster):
            return None
        return cluster

    def is_empty_field(self):
        for y in self.__colors:
            for x in y:
                if y != 0:
                    return False
        return True

    def get_cluster_number(self, y, x):
        return self.__connections[y][x]

    def get_cluster_axis(self, cluster_number):
        flat_list = [el for sublist in self.__connections for el in sublist]
        index = flat_list.index(cluster_number)
        y = index // 15
        x = index % 15
        return y, x

    def show_colors(self):
        for y in self.__colors:
            print(y)

    def show_connections(self):
        for y in self.__connections:
            print(y)