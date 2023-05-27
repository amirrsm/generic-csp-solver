from CSP.Constraint import Constraint


class MagicPotionsNotSameConstraint(Constraint):
    def is_satisfied(self) -> bool:
        list_of_values = [x.value for x in self.variables if x.value is not None]
        if len(list_of_values) == 1:
            return True
        else:
            if list_of_values[0][0] == list_of_values[1][0] or list_of_values[0][1] == list_of_values[1][1]:
                return False
            return True
