import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional

from Problem import Problem
from Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv=False, use_lcv=False, use_forward_check=False):
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_forward_check = use_forward_check

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        self.problem.calculate_neighbors()
        start = time.time()
        for var in self.problem.variables:
            if not self.forward_check(var):
                print("Problem Unsolvable")
                return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self):
        return self.recursive_backtracking([])

    def recursive_backtracking(self, assignment_list):
        if len(assignment_list) == len(self.problem.variables):
            return self.problem.variables
        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            var.value = value
            if self.is_consistent(var):
                assignment_list.append(var)
                result = self.recursive_backtracking(assignment_list)
                if result is not False:
                    return result
            assignment_list.remove(var)
            var.value = None
        return False

    def forward_check(self, var: Variable):
        for neighbor in var.neighbors:
            if not neighbor.has_value:
                for value in neighbor.domain:
                    neighbor.value = value
                    if not self.is_consistent(neighbor):
                        neighbor.domain.remove(value)
                        if len(neighbor.domain) == 0:
                            return False
        return True

    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        unassigned_variables = self.problem.get_unassigned_variables()
        if len(unassigned_variables) == 0:
            return None
        else:
            return min(unassigned_variables, key=lambda value: len(value.domain))

    def is_consistent(self, var: Variable):
        for c in self.problem.constraints:
            if var in c.variables and not c.is_satisfied():
                return False
        return True

    def lcv(self, var: Variable):
        min_conflict = float('+inf')
        min_index = 0
        index = 0
        for value in var.domain:
            counter = 0
            var.value = value
            for c in self.problem.constraints:
                if var in c.variables and not c.is_satisfied():
                    counter += 1
            if counter < min_conflict:
                min_conflict = counter
                min_index = index
            index += 1
        var.value = None
        return min_index
