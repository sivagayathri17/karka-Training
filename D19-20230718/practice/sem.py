educations=[{"study":"b.sc",
            "sem_mark":[{"sem":1,
                         "subject":["tamil","eng","maths","c"],
                         "grade":"A"
                         },
                         {"sem":2,
                         "subject":["tamil","eng","maths","cpp"],
                         "grade":"B"
                         }]
                         },
            {"study":"m.sc",
            "sem_mark":[{"sem":1,
                         "subject":["tamil","eng","maths","java"],
                         "grade":"A+"
                         },
                         {"sem":2,
                         "subject":["tamil","eng","maths","html"],
                         "grade":"B"
                         }]
                         }]
for education in educations:
    print(education)
    marks=education["sem_mark"]
    print(marks)
    for subject in marks:
        print(subject)
        

    


