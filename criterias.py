from math import *
import copy

def getVectorMaximinOptimal(projects : list):
    vectors = dict.fromkeys(projects)
    for project in vectors:
         minf1 = min(map(lambda x: x[0],project.getStates()))
         minf2 = min(map(lambda x: x[1],project.getStates()))
         vectors[project] = sqrt(minf1**2 + minf2**2)
    maxmin = max(vectors.values())
    vectorMaxminEffective = [k for k, v in vectors.items() if v == maxmin]
    for project in vectorMaxminEffective:
        project.setOptimal("Векторный максимин")
    return vectorMaxminEffective

def getVectorMinimaxOptimal(projects : list):
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
    for project in filtered:
        project.setOptimal("Векторное минимаксное сожаление)")
    return filtered

