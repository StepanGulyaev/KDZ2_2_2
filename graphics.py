import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tables import *

matplotlib.use('TkAgg')

def draw_maxmin(projects : dict, pareto : dict):

    #make graph

    windows_size = (9,9)
    plt.figure(figsize=windows_size)
    maxmin = plt.gca()

    maxmin.set_title('Maxmin')
    maxmin.set_aspect(1)
    maxmin.set_xlim((-2,8))
    maxmin.set_ylim((-2,8))

    plt.xlabel(r'$v1$')
    plt.ylabel(r'$v2$')

    #make grid

    major_ticks = np.arange(-2, 8, 2)
    minor_ticks = np.arange(-2, 8, 1)

    maxmin.set_xticks(major_ticks)
    maxmin.set_xticks(minor_ticks, minor=True)
    maxmin.set_yticks(major_ticks)
    maxmin.set_yticks(minor_ticks, minor=True)
    maxmin.tick_params(axis='both', which='major', labelsize=10)
    maxmin.tick_params(axis='both', which='minor', labelsize=10)
    maxmin.grid(which='both')

    plt.grid(True)

    #make axis

    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')

    #make dots

    dot_size = 8
    for project in projects:
        if project in pareto: maxmin.plot(projects[project][0], projects[project][1], 'r.', markersize=dot_size)
        else: maxmin.plot(projects[project][0], projects[project][1], 'k.', markersize=dot_size)
        maxmin.annotate("V" + project.name[1], xy=(projects[project][0] + 0.15,projects[project][1] + 0.15),fontsize = 8)

def draw_minmax(projects : dict, pareto : dict):
    # make graph

    windows_size = (9, 9)
    plt.figure(figsize=windows_size)
    minmax = plt.gca()

    minmax.set_title('Minmax')
    minmax.set_aspect(1)
    minmax.set_xlim((-2, 16))
    minmax.set_ylim((-2, 16))

    plt.xlabel(r'$s1$')
    plt.ylabel(r'$s2$')

    # make grid

    major_ticks = np.arange(-2, 16, 2)
    minor_ticks = np.arange(-2, 16, 1)

    minmax.set_xticks(major_ticks)
    minmax.set_xticks(minor_ticks, minor=True)
    minmax.set_yticks(major_ticks)
    minmax.set_yticks(minor_ticks, minor=True)
    minmax.tick_params(axis='both', which='major', labelsize=10)
    minmax.tick_params(axis='both', which='minor', labelsize=10)
    minmax.grid(which='both')

    plt.grid(True)

    # make axis

    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')

    # make dots

    dot_size = 8
    for project in projects:
        if project in pareto:
            minmax.plot(projects[project][0], projects[project][1], 'r.', markersize=dot_size)
        else:
            minmax.plot(projects[project][0], projects[project][1], 'k.', markersize=dot_size)
        minmax.annotate("V" + project.name[1], xy=(projects[project][0] + 0.15, projects[project][1] + 0.15),fontsize=8)