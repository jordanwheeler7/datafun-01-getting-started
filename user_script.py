"""
Complete the script.
"""



print("Hello!")
print()
print("Enter your latest three run times")
print()
run_time1 = float(input("What was your latest run time?"))
run_time2 = float(input("What was the second to latest run time?"))
run_time3 = float(input("What was your third latest run time?"))
print()
run_timesum = int(run_time1 + run_time2 + run_time3)
run_timeaverage = int(run_timesum / 3)
# Use this information to perform calculations for the total and average run time

print("We will see our stats for our run times")
print()
print(f"With our first run={run_time1}, our second run={run_time2}, and our last run={run_time3}")
print()
print("Our average run time")
print(round(run_timeaverage))
print()
print("Total time spent running")
print(run_timesum)
print()
# This section will allow us to see the minimum and maximum run times
min = run_time1
if run_time2 < run_time1:
    min = run_time2
if run_time3 < run_time1:
    min= run_time3
print(" Your fastest run was ")
print(min)

max = run_time1
if run_time2 > run_time1:
    max = run_time2
if run_time3 > run_time1:
    max = run_time3
    
print( "Your slowest run was") 
print(max)

# This area allows us to see the ranage of times

print("Our runs ranged in times from")
print('Range:', int(min), '-', int(max))

# This section shows the adjustment for an increase in elevation of 1,000 feet

print("Below we will see our times adjusted for running at 1,000 ft higher elevation")

print(round(float(run_time1 * (1 + float(.4)))))
print(round(float(run_time2 * (1 + float(.4)))))
print(round(float(run_time3 * (1 + float(.4)))))

print()
print()
# The variables below are the fastest, slowest, and average time to run 1 mile based off a sampling. We will compare our minimum:
# maximum and average to see where we stand as a runner

x = 5
y = 8
z = 12

# This section is to compare user run times to those of :
# a case study of other runners in the mile

if min < x :
    print( min, "Man, you are fast!")
if run_timeaverage == y :
    print(run_timeaverage, "You are average")
if max > z :
    print(max, "Keep working! You are slower than the study")

