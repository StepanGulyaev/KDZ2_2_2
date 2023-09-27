from collections import defaultdict
import copy

def getPareto(projects : dict):
    for project in projects:
        for project1 in projects:
            if (projects[project][0] >= projects[project1][0] and projects[project][1] >= projects[project1][1]) and\
               (not(projects[project][0] == projects[project1][0] and projects[project][1] == projects[project1][1])):
                project1.exclude()

    for project in projects:
        projects[project] = project.excluded

    pareto = [k for k, v in projects.items() if v == False]
    return pareto

def disableExclude(projects):
    for project in projects:
        project.include()

