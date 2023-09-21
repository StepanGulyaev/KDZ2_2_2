from math import *

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

