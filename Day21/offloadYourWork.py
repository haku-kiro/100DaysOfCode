'''
You are the best freelancer in the city. Everybody knows you, but what they don't know, is that you are actually offloading your work to other freelancers and and you rarely need to do any work. You're living the life!

To make this process easier you need to write a method called workNeeded to figure out how much time you need to contribute to a project.

Giving the amount of time in minutes needed to complete the project and an array of pair values representing other freelancers' time in [Hours, Minutes] format ie. [[2, 33], [3, 44]] calculate how much time you will need to contribute to the project (if at all) and return a string depending on the case.

    If we need to contribute time to the project then return "I need to work x hour(s) and y minute(s)"
    If we don't have to contribute any time to the project then return "Easy Money!"

'''

# my solution:
def work_needed(projectMinutes, freeLancers):
    totalTime = 0
    for x in freeLancers:
        totalTime += x[0] * 60 
        totalTime += x[1] 
    remainingTime = projectMinutes - totalTime 
    if remainingTime <= 0:
        return "Easy Money!"
    else:
        if remainingTime % 60 == 0: 
            return f"I need to work {int(remainingTime/60)} hour(s) and 0 minute(s)"        
        else:  # mins
            return f"I need to work {int(remainingTime/60)} hour(s) and {remainingTime%60} minute(s)"


# really cool, solution:
def work_needed2(project_minutes, freelancers):
    available_minutes = sum(hours * 60 + minutes for hours, minutes in freelancers)
    workload_minutes = project_minutes - available_minutes
    if workload_minutes <= 0:
        return 'Easy Money!'
    else:
        hours, minutes = divmod(workload_minutes, 60)
        return 'I need to work {} hour(s) and {} minute(s)'.format(hours, minutes)