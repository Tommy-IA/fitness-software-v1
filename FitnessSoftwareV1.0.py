goal_input = {
    1 : "Hypertrophy",
    2 : "Fat Loss/ Definition",
    3 : "Strength"
}

experience_level = {
    1 : "Beginner (0-1 year)",
    2 : "Intermediate (1-3 years)",
    3 : "Advanced (3+ years)"
}

weekly_availability = {
     1 : "2 training days per week",
     2 : "3 training days per week" ,
     3 : "4 training days per week"
}

muscle_focus = {
    1 : "Chest",
    2 : "Back",
    3 : "Quads and Ham",
    4 : "Glutes",
    5 : "None"
}

report = []

blue = "\033[94m"
green = "\033[92m"
yellow = "\033[33m"
red = "\033[91m"
reset = "\033[0m"
cyan = "\033[36m"

compound_exercise = {
    "Chest" : ["Bench Press", "Incline Bench Press", "Dumbbell Bench Press", 
               "Chest Dips", "Machine Chest Press\n"],
    "Back" : ["Pull up", "Lat Pulldown", "Barbell Row", "Seated Cable Row", "Landmine\n"],
    "Quads and Ham" : ["Back Squat", "Front Squat", "Romanian Deadlift", "Leg Press\n",
               "Hack Squat"],
    "Glutes" : ["Back Squat", "Glute Trainer", "Hip thrust", "Booty Builder\n" ],
    "Deltoids" : ["Military Press","Dumbbell Shoulder Press", "Arnold Press", "Push Press\n"]
}


## future V2.0 Isolation exercises integration 
isolation_exercise = {
    "Biceps": ["Barbell Curl", "Dumbbell Curl", "Preacher Curl", "Spider Curl", 
               "Hammer Curl", "Incline Curl"],
    "Triceps": ["close grip bench press", "Skullcrusher", "Cable Pushdown", "Overhead Triceps Extendion", 
                "Dips"],
    "Delts": ["Lateral Raise","Cable Lateral Raise", "Rear Delt Fly"],
    "Chest": ["Cable Fly", "Pec Deck","Dumbbell Fly"],
    "Quads and Ham": ["Leg Extension", "Quads-focused Bulgarian Split Squat", "Seated Leg Curl", "Lying Hamstring curl"],
    "Glutes": ["Kickback", "Hip abduction", "Glute-focused Back Extendion", "Glute-focused Bulgarian Split squat"],
    "Calves": ["Standing Calf Raise", "Seated Calf Raise"],
    "ABS": ["Cable crunch", "Hanging Leg raise", "Decline Crunch"]
}


priority_map = {
    "Chest": "Bench Press", 
    "Back": "Pull/Row",
    "Deltoids": "Shoulder Press",
    "Quads and Ham" : "Squat/ Hinge",
    "Glutes" : "Thrust/Stretch",
    "Arms" : "Curl/ Triceps Extension",
    "None" : "Balanced"
}

split_map = {
    "2 training days per week" : ["Full Body / Full Body", "Full Body / Upper", "Full Body / Lower"],
    "3 training days per week" : ["Upper A / Lower / Upper B", "Lower A / Upper / Lower B", "Upper / Lower / Full Body"],
    "4 training days per week" : ["Upper A / Lower A / Upper B / Lower B", "Upper / Lower / Full Body / Deltoids",
    "Upper / Lower / Full Body / Arms"]
}

muscle_f = {
    "Upper" : ["Chest", "Back", "Deltoids"],
    "Quads and Ham" : ["Quads and Ham"],
    "Glutes" : ["Glutes"]
}

fatloss_decision = {
    "2 training days per week": {
        "Upper": "Full Body / Upper + include 20-30 min of post-workout LISS cardio after each session",
        "Quads and Ham": "Full Body / Lower + include 20-25 min of post-workout LISS cardio after Full Body and 10-15 min after Lower",
        "Glutes": "Full Body / Lower + include 20-25 min of post-workout LISS cardio after Full Body and 10-15 min after Lower",
        "None": "Full Body / Full Body + include 20-30 min of post-workout LISS cardio after each session"
    },

    "3 training days per week": {
        "Upper": "Upper A / Lower / Upper B + include 20-30 min of post-workout LISS cardio after Upper sessions and 10-15 min after Lower",
        "Quads and Ham": "Lower A / Upper / Lower B + include 10-15 min of post-workout LISS cardio after Lower sessions and 20-30 min after Upper",
        "Glutes": "Lower A / Upper / Lower B + include 10-15 min of post-workout LISS cardio after Lower sessions and 20-30 min after Upper",
        "None": "Upper / Lower / Full Body + include 20-25 min of post-workout LISS cardio after Upper and Full Body sessions, and 10-15 min after Lower"
    },

    "4 training days per week": {
        "Upper": "Upper A / Lower A / Upper B / Lower B + include 15-25 min of post-workout LISS cardio after Upper sessions and 10-15 min after Lower sessions",
        "Quads and Ham": "Upper A / Lower A / Upper B / Lower B + include 20-25 min of post-workout LISS cardio after Upper sessions and 10-15 min after Lower sessions",
        "Glutes": "Upper A / Lower A / Upper B / Lower B + include 20-25 min of post-workout LISS cardio after Upper sessions and 10-15 min after Lower sessions",
        "None": "Upper A / Lower A / Upper B / Lower B + include 15-25 min of post-workout LISS cardio after Upper sessions and 10-15 min after Lower sessions"
    }
}


split_decision = {
"2 training days per week": {
"Upper" : "Full Body / Upper",
"Quads and Ham" : "Full Body / Lower",
"Glutes": "Full Body / Lower",
"None": "Full Body / Full Body"
},
"3 training days per week": {
"Upper": "Upper A / Lower / Upper B",
"Quads and Ham": "Lower A / Upper / Lower B",
"Glutes": "Lower A / Upper / Lower B",
"None": "Upper / Lower / Full Body"
},
"4 training days per week": {
"Upper": "Upper A / Lower A / Upper B / Lower B",
"Quads and Ham": "Upper A / Lower A / Upper B / Lower B",
"Glutes": "Upper A / Lower A / Upper B / Lower B",
"None": "Upper A / Lower A / Upper B / Lower B"}}

goal_dict = {
    "Hypertrophy": {
        "Rep range compound": "6-12",
        "Rep range isolation": "10-15",
        "Rest compound": "2-3 min",
        "Rest isolation": "60-90 sec",
        "Cardio": "minimal or optional",
        "Priority": "maximize muscle growth through progressive overload, controlled execution, and full range of motion\n"
    },

    "Fat Loss/ Definition": {
        "Rep range compound": "8-12",
        "Rep range isolation": "10-15",
        "Rest compound": "90-120 sec",
        "Rest isolation": "45-75 sec",
        "Cardio": "include post-workout LISS cardio, follow 'split'.",
        "Priority": "preserve muscle mass, maintain training intensity, and increase total energy expenditure\n"
    },

    "Strength": {
        "Rep range compound": "3-6",
        "Rep range isolation": "6-10",
        "Rest compound": "3-5 min",
        "Rest isolation": "90-120 sec",
        "Cardio": "Minimal or optional",
        "Priority": "Maximize force production, technical precision, and load progression\n"
    }
}
experience_dict = {
    "Beginner (0-1 year)": {
        "Volume": "6-10 hard sets per muscle per week",
        "Exercise complexity": "Simple",
        "Progression": "Focus on technique consistency and gradual load progression, start low with weight",
        "notes": "Prefer stable exercises and manageable total workload\n"
    },

    "Intermediate (1-3 years)": {
        "Volume": "10-16 hard sets per muscle per week",
        "Exercise complexity": "Moderate",
        "Progression": "Use structured progressive overload and more precise volume allocation, follow techinique",
        "notes": "Can tolerate more volume and exercise variation\n"
    },

    "Advanced (3+ years)": {
        "Volume": "12-20 hard sets per muscle per week",
        "Exercise complexity": "High",
        "Progression": "Use precise fatigue management and advanced progression strategies",
        "notes": "Can handle higher volume and more targeted specialization\n"
    }
}

muscle_group = {}
for key, value in muscle_f.items():
    for muscle in value:
        muscle_group[muscle] = key





def input_user(title, options):
    while True:
        print(f"\n{yellow}{title}{reset}")
        for key, value in options.items():
            print(f"{key}. {green}{value}{reset}")
        try:
            user_input = int(input("Choose the option: "))
        except ValueError:
            print(f"{red}Please enter a valid number{reset}")
            continue
        if user_input in options:
            result = options[user_input]
            report.append((title, result))
            print(f"\n \033[47m\033[1m{cyan}-- Current Report --{reset} \n")
            for title, result in (report):
                print(f"- {yellow}{title}{reset} : {green}{result}{reset}")
            return result
        else:
            print(f"{red}Please insert a correct number from the options.{reset}")


def choose_split(muscle_group, muscle_focus, goal_input, weekly_availability, report):
    if muscle_focus == "None":
         muscle_cat = "None"
    else:
         muscle_cat = muscle_group[muscle_focus]
    if goal_input == "Fat Loss/ Definition":
        split = fatloss_decision[weekly_availability][muscle_cat]
    else:
        split = split_decision[weekly_availability][muscle_cat]
    report.append(f"\nRecommended split: {split}\n")
    return split, report

def muscle_focus_modifier(muscle_focus, compound_exercise, report):
    priority = priority_map.get(muscle_focus, "Balanced")
    report.append(f"Type of priority exercise: {priority}\n")
    if muscle_focus in compound_exercise:
            report.append(f"Priority exercise for {muscle_focus}:")
            report.append(compound_exercise[muscle_focus])
    return report        




def goal_modifier(goal_input, report):
    goal= goal_dict[goal_input]
    report.append(f"Recommended approach for {goal_input}:")
    report.append({goal_input: goal})
    return report

def experience_modifier(experience_level, report):
    level = experience_dict[experience_level]
    report.append(f"Recommended approach for {experience_level}:")
    report.append({experience_level: level})
    return report 

     
def main():
    global report
    try:
        goal = input_user("Goal:", goal_input)
        experience = input_user("Experience level:", experience_level)
        availability = input_user("Weekly availability:", weekly_availability)
        m_focus = input_user("Focus of a muscle:", muscle_focus)
        muscle_focus_modifier(m_focus, compound_exercise, report)
        split, report = choose_split(muscle_group, m_focus, goal, availability, report)
        goal_modifier(goal, report)
        experience_modifier(experience, report)
        if m_focus == "None":
             print(f"\n\033[47m\033[1mWith no specific muscle priority, the program is designed to maintain a balanced distribution of volume following the {split} split, \nand exercise selection across all muscle groups, ensuring overall development and symmetry matching your weekly availability of {availability} \nThe plan is further shaped around a {goal} objective, meaning that training variables such as volume, rep ranges, rest intervals, and cardio \nintegration should be adjusted to maximize results toward that specific outcome. \nFinally, your {experience} level indicates the amount of workload, exercise complexity, and progression strategy that is most appropriate to \nensure both performance and long-term consistency.{reset}\n")
        else:
             print(f"\n \033[47m\033[1mThis training plan is structured around a {split} split to match your weekly availability for {availability} and \nprovide an efficient balance between stimulus and recovery. \nWith {m_focus} as your current priority, the program should allocate exercise selection, training volume, and session emphasis in a way that gives extra \nattention to that area without neglecting overall development. \nThe plan is further shaped around a {goal} objective, meaning that training variables such as volume, rep ranges, rest intervals, and cardio \nintegration should be adjusted to maximize results toward that specific outcome. \nFinally, your {experience} level indicates the amount of workload, exercise complexity, and progression strategy that is most appropriate to \nensure both performance and long-term consistency.{reset}\n")
        for item in report:
            if isinstance (item, dict):
                    for key, value in item.items():
                        if isinstance(value,dict):
                            for chiavi, valori in value.items():
                                print(f"{chiavi}: {valori}")
                        else:
                            print(f"{key}:{value}")
            elif isinstance (item, str):
                    print(item)
            elif isinstance (item, list):
                 for i in item:
                      print(f"-{i}")
            elif not isinstance(item, tuple):
                    print(item)
    except KeyError as e:
        print(f"\n Cannot plan: error {e}")
    
if __name__ == "__main__":
     main()


