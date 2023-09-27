from collections import defaultdict
import copy

def getPareto(projects : dict, mode : str):
    pareto = copy.copy(projects)
    for project in projects:
        for project1 in projects:
            if mode == "findMax":
                if (projects[project][0] >= projects[project1][0] and projects[project][1] >= projects[project1][1]) and\
                   (not(projects[project][0] == projects[project1][0] and projects[project][1] == projects[project1][1])):
                    if project1 in pareto: pareto.pop(project1)
            elif mode == "findMin":
                if (projects[project][0] <= projects[project1][0] and projects[project][1] <= projects[project1][1]) and\
                   (not(projects[project][0] == projects[project1][0] and projects[project][1] == projects[project1][1])):
                    if project1 in pareto: pareto.pop(project1)
            else:
                return []
    return pareto

