import random

# N = 10
# EXPERTS = [(b:=random.randint(1, 50), random.randint(b, 50)) for i in range(N)]

SCHEDULE = [(15, 100, 5), (13, 50, 7), (10, 30, 4), (20, 80, 10), (30, 110, 14)]


class ScheduleTask:
    def __init__(self, schedules_list):
        self.schedule = schedules_list  # кінцевий срок сдачі, штраф, час виконання
        self.U = [0 for _ in schedules_list]
        self.tf_res = 0
        self.solution_method = None
        self.n = len(schedules_list)
        self.order = [-1 for _ in range(self.n)]

    def greedy_algorithm_1(self):
        self.__greedy_algorithm(lambda x: x[1] / x[2])
        self.solution_method = 'жадібний алгоритм #1'

    def greedy_algorithm_2(self):
        self.__greedy_algorithm(lambda x: x[1] / x[0])
        self.solution_method = 'жадібний алгоритм #2'

    def greedy_algorithm_3(self):
        self.__greedy_algorithm(lambda x: x[1] / (x[0] * x[2]))
        self.solution_method = 'жадібний алгоритм #3'

    def __greedy_algorithm(self, function):
        self.U = [0 for _ in self.schedule]
        self.order = [-1 for _ in range(self.n)]

        p = [() for _ in range(self.n)]
        for i in range(self.n):
            p[i] = (i, function(self.schedule[i]))

        p.sort(key=lambda x: x[1], reverse=True)
        self.order = [i[0] for i in p]

        self.count_fines_vector()
        self.tf_res = sum([i * j[1] for i, j in zip(self.U, self.schedule)])

    def count_fines_vector(self):
        #TODO ВОПРОС ПРО ВРЕМЯ
        time = 0
        for current in self.order:
            time += self.schedule[current][2]
            if time > self.schedule[current][0]:
                self.U[current] = 1

    def bee_algorithm(self, quantity_of_random=3):
        solutions = [{} for _ in range(quantity_of_random + 3)]
        self.greedy_algorithm_1()
        solutions[0].update({
            'method': 'жадібний алгоритм #1',
            'target function': self.tf_res,
            'fine vector': self.U,
            'order': self.order
        })

        self.greedy_algorithm_2()
        solutions[1].update({
            'method': 'жадібний алгоритм #2',
            'target function': self.tf_res,
            'fine vector': self.U,
            'order': self.order
        })

        self.greedy_algorithm_3()
        solutions[2].update({
            'method': 'жадібний алгоритм #3',
            'target function': self.tf_res,
            'fine vector': self.U,
            'order': self.order
        })
        for solution in solutions[3:]:
            self.order = random.sample(range(self.n), self.n)
            self.count_fines_vector()
            self.tf_res = sum([i * j[1] for i, j in zip(self.U, self.schedule)])
            solution.update({
                'method': 'random',
                'fine vector': self.U,
                'target function': self.tf_res,
                'order': self.order
            })

        best_index1 = -1
        best_target1 = -1
        best_index2 = -1
        best_target2 = -1

        for i, solution in enumerate(solutions):
            if solution['target function'] > best_target1:
                best_target1 = solution['target function']
                best_index1 = i
            elif solution['target function'] > best_target2:
                best_target2 = solution['target function']
                best_index2 = i


if __name__ == '__main__':
    task = ScheduleTask(SCHEDULE)
    task.greedy_algorithm_1()
    print(task.U, task.solution_method, task.tf_res)

    task.greedy_algorithm_2()
    print(task.U, task.solution_method, task.tf_res)

    task.greedy_algorithm_3()
    print(task.U, task.solution_method, task.tf_res)
