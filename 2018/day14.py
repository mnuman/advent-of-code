class RecipeList:
    def __init__(self, initial_recipes):
        self.recipes = initial_recipes
        self.elf1 = 0
        self.elf2 = 1

    def cycle(self):
        score = self.recipes[self.elf1] + self.recipes[self.elf2]
        if score < 10:
            self.recipes.append(score)
        else:
            self.recipes.append(1)
            self.recipes.append(score - 10)
        self.elf1 = (self.elf1 + 1 +
                     self.recipes[self.elf1]) % len(self.recipes)
        self.elf2 = (self.elf2 + 1 +
                     self.recipes[self.elf2]) % len(self.recipes)


def day14(number_of_recipes):
    recipes = RecipeList([3, 7])
    while len(recipes.recipes) < number_of_recipes + 10:
        recipes.cycle()
    return ''.join([str(c)
                    for c in recipes.recipes[number_of_recipes:number_of_recipes+10]])


def day14_2(sublist):
    recipes = RecipeList([3, 7])
    foundIt = False
    total = 0
    while not foundIt:
        recipes.cycle()
        total += 1
        foundIt = (recipes.recipes[-1] == sublist[-1] and
                   recipes.recipes[-2] == sublist[-2] and
                   recipes.recipes[-3] == sublist[-3] and
                   recipes.recipes[-4] == sublist[-4] and
                   recipes.recipes[-5] == sublist[-5] and
                   recipes.recipes[-6] == sublist[-6]
                   )
        if foundIt:
            print(recipes.recipes[-10:])
            return len(recipes.recipes) - 6
        else:
            foundIt = (recipes.recipes[-2] == sublist[-1] and
                       recipes.recipes[-3] == sublist[-2] and
                       recipes.recipes[-4] == sublist[-3] and
                       recipes.recipes[-5] == sublist[-4] and
                       recipes.recipes[-6] == sublist[-5] and
                       recipes.recipes[-7] == sublist[-6]
                       )
            if foundIt:
                print(recipes.recipes[-10:])
                return len(recipes.recipes) - 7
        if total % 5000 == 0:
            print(total)


# print(day14(890691))
# 8176111038
print(day14_2(sublist=[8, 9, 0, 6, 9, 1]))
# 20225578
