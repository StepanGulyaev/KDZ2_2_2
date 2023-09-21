from prettytable import PrettyTable

def draw_projects_table(projects):
    projects_table = PrettyTable()
    projects_table.field_names = [" ","Z1","Z2","Z3","Z4"]
    for i in range(len(projects)):
        row = []
        row.append(projects[i].name)
        for j in range(len(projects[i].states)):
            row.append(projects[i].states[j])
        projects_table.add_row(row)
    print(projects_table)
