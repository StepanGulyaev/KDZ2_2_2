from project import Project
from tables import *
from criterias import *

x1 = Project("X1",[[5,10],[2,7],[8,6],[5,9]])
x2 = Project("X2",[[4,4],[5,7],[9,6],[4,4]])
x3 = Project("X3",[[4,8],[1,9],[7,3],[7,5]])
x4 = Project("X4",[[4,1],[6,4],[9,2],[7,2]])
x5 = Project("X5",[[1,3],[3,5],[4,2],[3,3]])
x6 = Project("X6",[[5,4],[2,6],[3,3],[2,4]])
x7 = Project("X7",[[11,5],[2,7],[4,5],[2,3]])
x8 = Project("X8",[[4,3],[3,7],[10,4],[3,8]])

projects = []
projects.extend([x1,x2,x3,x4,x5,x6,x7,x8])

if __name__ == '__main__':
    draw_projects_table(projects)

    print("Решения эффективные по принципу векторного максимина: ",end='')
    maxminOptimal = getVectorMaxminOptimal(projects)
    setOptimal("Векторный максимин",maxminOptimal)
    print(*map(lambda x: x.name, maxminOptimal), sep=",")

    print("Решения эффективные по принципу минимаксного сожаления: ",end='')
    minmaxOptimal = getVectorMinmaxOptimal(projects)
    setOptimal("Векторное минимаксное сожаление",minmaxOptimal)
    print(*map(lambda x: x.name, minmaxOptimal), sep=",")

    optimalByF1 = getOptimalByF("f1",projects)
    print("Лучшие решения по Вальду,Сэвиджу,Гурвицу,Байесу и Лапласу по f1: ", end='')
    setOptimal("f1 по критериям Вальда,Сэвиджа,Гурвица,Байеса и Лапласа",optimalByF1)
    print(*map(lambda x: x.name, optimalByF1), sep=",")

    optimalByF2 = getOptimalByF("f2",projects)
    print("Лучшие решения по Вальду,Сэвиджу,Гурвицу,Байесу и Лапласу по f2: ", end='')
    setOptimal("f2 по критериям Вальда,Сэвиджа,Гурвица,Байеса и Лапласа",optimalByF2)
    print(*map(lambda x: x.name, optimalByF2), sep=",")

    drawVotingTable(projects)

    print("Лучшие решения: ", end='')
    print(*map(lambda x: x.name, getBest(projects)), sep=",")


