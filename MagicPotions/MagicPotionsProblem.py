from CSP.Problem import Problem
from CSP.Variable import Variable
from MagicPotions.MagicPotionsConstraint import MagicPotionsNotSameConstraint


class MagicPotionsProblem(Problem):
    def __init__(self):
        super().__init__([], [], "Magic Potions Problem")

        aldo = Variable[str]([['transformation', 'blue'],
                              ['transformation', 'black'],
                              ['transformation', 'purple']], 'ALDO')
        beatrice = Variable[str]([['poison', 'blue'],
                                  ['transformation', 'blue'],
                                  ['invisible', 'blue'],
                                  ['healer', 'blue']], 'BEATRICE')
        ignatius = Variable[str]([['poison', 'green'],
                                  ['poison', 'blue'],
                                  ['poison', 'red']], 'IGNATIUS')
        lorenzo = Variable[str]([['acidic', 'green'],
                                 ['healer', 'green'],
                                 ['transformation', 'green'],
                                 ['invisible', 'green']], 'LORENZO')
        orsola = Variable[str]([['invisible', 'green'],
                                ['invisible', 'red'],
                                ['invisible', 'purple']], 'ORSOLA')

        c1 = MagicPotionsNotSameConstraint([aldo, beatrice])
        c2 = MagicPotionsNotSameConstraint([aldo, ignatius])
        c3 = MagicPotionsNotSameConstraint([aldo, lorenzo])
        c4 = MagicPotionsNotSameConstraint([aldo, orsola])
        c5 = MagicPotionsNotSameConstraint([beatrice, ignatius])
        c6 = MagicPotionsNotSameConstraint([beatrice, lorenzo])
        c7 = MagicPotionsNotSameConstraint([beatrice, orsola])
        c8 = MagicPotionsNotSameConstraint([ignatius, lorenzo])
        c9 = MagicPotionsNotSameConstraint([ignatius, orsola])
        c10 = MagicPotionsNotSameConstraint([lorenzo, orsola])

        self.constraints = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
        self.variables = [aldo, beatrice, ignatius, lorenzo, orsola]