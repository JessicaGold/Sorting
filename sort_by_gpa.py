import random

"""togr is an object meant for grading that has verbal grades
and is represented as a python dictionary.
grades is a dictionary that maps verbal grades to numeral ones"""
def grades_to_numbers(togr, grades):
    res = {}
    for sub in togr:
        res[sub] = grades[togr[sub]]
    return res

#getting gpa from dictionary of grades per subject and dictionary of weihts per subject
def get_gpa(grades, weights):
    res = 0
    i = 0
    for sub in grades:
        res += grades[sub] * weights[sub]
        i += weights[sub]
    return (res/i)

#main event...
"""input should be:
    - list or set of objects for grading
    - dictionary maping worded grades to numeral grades
    - wights of subjects for grading
every object for grading should be a pair (name, grades).
grades is a dictionary that maps subjects to the grades in those subjects
"""
def sort_by_gpa(obs, grs, wih):
    res = []
    for ob in obs:
        res.append((ob[0], grades_to_numbers(ob[1], grs)))
    for i in range(len(res)):
        res[i] = (res[i][0], get_gpa(res[i][1], wih))
    return sort_by_sec(res)


def sort_by_sec(lst): #using random quick sort algorithm
    if len(lst) <= 1:
        return lst
    p = random.randint(1,len(lst))
    pivot = lst[p - 1][1]
    smaller = [elem for elem in lst if elem[1] < pivot]
    equal = [elem for elem in lst if elem[1] == pivot]
    greater = [elem for elem in lst if elem[1] > pivot]
    return sort_by_sec(greater) + equal + sort_by_sec(smaller)
