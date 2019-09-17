# -*- coding: utf-8 -*-

def average_temps(temps):
    sum_of_tems = 0

    for temp in temps:
        sum_of_tems += temp     #float(temp)

    return sum_of_tems/len(temps)

if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temps(temps)
    print('La temperatura promedio es {}'.format(average))
