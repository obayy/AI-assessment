studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ] 


def gemiddelde_per_student(studentencijfers):
    gemiddeldes_lijst = []
    for cijfers in studentencijfers:
        antw = 0
        for cijfer in cijfers:
            antw += cijfer
        gemiddeldes_lijst.append(round(antw / len(cijfers), 1))
    return gemiddeldes_lijst



def gemiddelde_van_alle_studenten(studentencijfers):
    appel = gemiddelde_per_student(studentencijfers)
    antw = sum(appel) / len(studentencijfers)
    return antw



print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))

