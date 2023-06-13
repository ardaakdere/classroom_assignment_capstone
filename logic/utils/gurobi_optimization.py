# Course assginment to classroom
import gurobipy as gp
from gurobipy import GRB
import pandas as pd
from logic.models import Course, Classroom, Result
from django_pandas.io import read_frame

def run_optimization():

    courses = Course.objects.all()
    classrooms = Classroom.objects.all()

    df1 = read_frame(courses)
    df2 = read_frame(classrooms)

    df1['course_code'] = df1['course_code'] + " (" + df1['course_section'] + ")"
    
    I=range(len(df1))
    K=range(len(df2))

    NS =  df1.registered_student.tolist() #df1.popu.tolist()
    COT = df1.course_type.tolist() #df1.type.tolist()
    CAP = df2.classroom_quota.tolist() #df2.cap.tolist()
    CLT = df2.classroom_type.tolist() #df2.type.tolist()

    # Model
    m = gp.Model("course-classroom")

    # Decision variables
    x = m.addVars(I,K, vtype=GRB.BINARY)
    mxa = m.addVar()

    # Objective function
    m.setObjective(mxa, GRB.MINIMIZE)

    m.addConstrs((x.sum(i,'*') == 1 for i in I))

    m.addConstrs(NS[i] <= sum(x[i,k]*CAP[k] for k in K) for i in I)

    m.addConstrs(COT[i] <= sum(x[i,k]*CLT[k] for k in K) for i in I)

    m.addConstrs(x.sum('*',k) <= mxa for k in K)

    # Solve
    m.optimize()

    # Print solution
    print('\nSOLUTION RESULT:')
    if m.Status == GRB.OPTIMAL:
        print('Obj. func. value: %g\n' % m.objVal)
        df3 = df1[["course_code", "course_name"]].copy()
        for i in I:
            for k in K:
                if x[i,k].X == 1:
                    df3.loc[i,"classroom"] = df2.loc[k,"classroom_code"] 
                    break
        print(df3)
        print('\n')
    else:
        print('Model Status: %g' % m.status)

    Result.objects.all().delete()
    for index, row in df3.iterrows():
        course_code, course_section = row['course_code'].split()
        course_section = course_section.replace('(', '')
        course_section = course_section.replace(')', '')
        course = Result(
            course_code=course_code,
            course_section=course_section,
            course_name=row['course_name'],
            classroom=row['classroom']
        )
        course.save()
    
    print('Done.')
        
