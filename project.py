class Project:
    def __init__(self, name: str, states: list):
        self.name = name
        self.states = states
        self.criterias = dict.fromkeys(["Векторный максимин", "Векторное минимаксное сожаление",
                                        "f1 по критериям Вальда,Сэвиджа,Гурвица,Байеса и Лапласа",
                                        "f2 по критериям Вальда,Сэвиджа,Гурвица,Байеса и Лапласа"],False)

    def getStates(self):
        return self.states

    def setOptimal(self,criteriaName : str):
        self.criterias[criteriaName] = True

    def getNumOptimalCriteria(self):
        numOfOptimalcriteria = 0
        for criteria in self.criterias:
            if self.criterias[criteria] == True:
                numOfOptimalcriteria+=1
        return numOfOptimalcriteria