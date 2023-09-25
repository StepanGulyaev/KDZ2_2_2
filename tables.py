from prettytable import PrettyTable

def draw_projects_table(projects):
    projects_table = PrettyTable()
    projects_table.field_names = [" ","Z1","Z2","Z3","Z4"]
    for i in range(len(projects)):
        row = []
        row.append(projects[i].name)
        for j in range(len(projects[i].states)):
            row.append("(" + ','.join(str(x) for x in projects[i].states[j]) + ")")
        projects_table.add_row(row)
    print(projects_table)

def drawVotingTable(projects):
    voting_table = PrettyTable()
    voting_table.field_names = [" ","Векторный максимин","Векторное минимаксное сожаление","f1 по критериям В,С,Г и Л","f2 по критериям В,С,Г и Л"]
    for project in projects :
        row = []
        row.append(project.name)
        for criteria in project.criterias:
            if project.criterias[criteria] == True:
                row.append("+")
            else:
                row.append(" ")
        voting_table.add_row(row)
    print(voting_table)
