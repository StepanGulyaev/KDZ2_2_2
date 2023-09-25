class Project:
    def __init__(self, name: str, states: list):
        self.name = name
        self.states = states
        self.criterias = dict.fromkeys(["Векторный максимин", "Векторное минимаксное сожаление",
                                        "f1 по критериям Вальда,Сэвиджа,Гурвица и Лапласа",
                                        "f2 по критериям Вальда,Сэвиджа,Гурвица и Лапласа"],False)
        self.miniCriterias = dict.fromkeys(["Вальд","Сэвидж","Гурвиц","Лаплас"],False)

    def getStates(self):
        return self.states

    def setOptimal(self,criteriaName : str):
        self.criterias[criteriaName] = True

    def setOptimalMiniCriteria(self, miniCriteriaName : str):
        self.miniCriterias[miniCriteriaName] = True

    def getNumOptimalCriteria(self):
        numOfOptimalcriteria = 0
        for criteria in self.criterias:
            if self.criterias[criteria] == True:
                numOfOptimalcriteria+=1
        return numOfOptimalcriteria

    def getNumOptimalMiniCriteria(self):
        numOfOptimalMiniCriteria = 0
        for criteria in self.miniCriterias:
            if self.miniCriterias[criteria] == True:
                numOfOptimalMiniCriteria+=1
        return numOfOptimalMiniCriteria