from math import *
import copy
from exclude import *

gurvitz_coef = 0.6

def setOptimal(criteriaName : str, projects : list):
    for project in projects:
        project.setOptimal(criteriaName)

def setOptimalMiniCriteria(miniCriteriaName : str, projects : list):
    for project in projects:
        project.setOptimalMiniCriteria(miniCriteriaName)

def getVectorMaxminOptimal(projects : list):
    vectors = dict.fromkeys(projects)
    for project in vectors:
         minf1 = min(map(lambda x: x[0],project.getStates()))
         minf2 = min(map(lambda x: x[1],project.getStates()))
         vectors[project] = [minf1,minf2]
    pareto = getPareto(vectors)
    return pareto
    

def getVectorMinmaxOptimal(projects : list):
    risk_matrix = copy.deepcopy(projects)
    for i in range(0,4):
        f1MaxCurState = max(map(lambda x: x.states[i][0],projects))
        f2MaxCurState = max(map(lambda x: x.states[i][1], projects))
        for project_copy in risk_matrix:
            project_copy.states[i][0] = f1MaxCurState - project_copy.states[i][0]
            project_copy.states[i][1] = f2MaxCurState - project_copy.states[i][1]
    maxes = dict.fromkeys(risk_matrix)
    for project in maxes:
        maxes[project] = max(map(lambda x: sqrt(x[0]**2 + x[1]**2),project.getStates()))
    minmax = min(maxes.values())
    minmaxEffective =  [k for k, v in maxes.items() if v == minmax]
    names = list(map(lambda x: x.name,minmaxEffective))
    origProjects = list(map(lambda x: x if (x.name in names) else None,projects))
    filtered = list(filter(lambda x: x is not None,origProjects))
    return filtered

def getOptimalByF(fName : str,projects : list):
    projects_copy = copy.deepcopy(projects)
    if fName == "f1":
        for project in projects_copy:
            project.states = list(map(lambda x: x[0],project.getStates()))
    elif fName == "f2":
        for project in projects_copy:
            project.states = list(map(lambda x: x[1],project.getStates()))

    print("     Вальд-эффективные решения по " + fName + ": " , end='')
    waldOptimal = getWaldOptimal(projects_copy)
    setOptimalMiniCriteria("Вальд",waldOptimal)
    print(*map(lambda x: x.name, waldOptimal), sep=",")

    print("     Сэвидж-эффективные решения по " + fName + ": " , end='')
    savidgeOptimal = getSavidgeOptimal(projects_copy)
    setOptimalMiniCriteria("Сэвидж",savidgeOptimal)
    print(*map(lambda x: x.name, savidgeOptimal), sep=",")

    print("     Гурвиц-эффективные решения по " + fName + ": " , end='')
    gurvitzOptimal = getGurvitzOptimal(projects_copy)
    setOptimalMiniCriteria("Гурвиц",gurvitzOptimal)
    print(*map(lambda x: x.name, gurvitzOptimal), sep=",")

    print("     Лаплас-эффективные решения по " + fName + ": " , end='')
    laplasOptimal = getLaplasOptimal(projects_copy)
    setOptimalMiniCriteria("Лаплас",laplasOptimal)
    print(*map(lambda x: x.name, laplasOptimal), sep=",")

    bestByMiniCriteria = getBestByMiniCriteria(projects_copy)
    names = list(map(lambda x: x.name, bestByMiniCriteria))
    orig_projects = list(map(lambda x: x if (x.name in names) else None,projects))
    filtered = list(filter(lambda x: x is not None, orig_projects))

    return filtered

def getWaldOptimal(projects):
    mins = dict.fromkeys(projects)
    for project in mins:
        mins[project] = min(project.states)
    maxmin = max(mins.values())
    wald_effective = [k for k, v in mins.items() if v == maxmin]
    return wald_effective


def getSavidgeOptimal(projects):
    risk_matrix = copy.deepcopy(projects)
    for i in range(0,4):
        max_cur_state = max(map(lambda x: x.states[i],projects))
        for project_copy in risk_matrix:
            project_copy.states[i] = max_cur_state - project_copy.states[i]
    maxes = dict.fromkeys(risk_matrix)
    for project in maxes:
        maxes[project] = max(project.states)
    minmax = min(maxes.values())
    savidge_effective = [k for k, v in maxes.items() if v == minmax]
    names = list(map(lambda x: x.name,savidge_effective))
    orig_projects = list(map(lambda x: x if (x.name in names) else None,projects))
    filtered = list(filter(lambda x: x is not None,orig_projects))
    return filtered

def getGurvitzOptimal(projects):
    gurvitz_dict = dict.fromkeys(projects)
    for project in gurvitz_dict:
        gurvitz_dict[project] = min(project.states) * gurvitz_coef + max(project.states) * (1 - gurvitz_coef)
    gurvitz_effective = [k for k, v in gurvitz_dict.items() if v == max(gurvitz_dict.values())]
    return gurvitz_effective

def getLaplasOptimal(projects):
    laplas_dict = dict.fromkeys(projects)
    for project in laplas_dict:
        laplas_dict[project] = sum(project.states)/len(project.states)
    laplas_effective = [k for k, v in laplas_dict.items() if v == max(laplas_dict.values())]
    return laplas_effective

def getBestByMiniCriteria(projects):
    best_dict = dict.fromkeys(projects)
    for project in best_dict:
        best_dict[project] = project.getNumOptimalMiniCriteria()
    best = [k for k, v in best_dict.items() if v == max(best_dict.values())]
    return best

def getBest(projects):
    best_dict = dict.fromkeys(projects)
    for project in best_dict:
        best_dict[project] = project.getNumOptimalCriteria()
    best = [k for k, v in best_dict.items() if v == max(best_dict.values())]
    return best
