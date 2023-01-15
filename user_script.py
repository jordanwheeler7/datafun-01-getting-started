"""
Complete the script.
"""
from decimal import Decimal


print("Hello!")
print()
print("Enter your latest three run times")
print()
run_time1 = int(input("What was your latest run time?"))
run_time2 = int(input("What was the second to latest run time?"))
run_time3 = int(input("What was your third latest run time?"))
print()
run_timesum = int(run_time1 + run_time2 + run_time3)
run_timeaverage = int(run_timesum / 3)


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

print("Our runs ranged in times from")
print('Range:', (min), '-', (max))

print("Below we will see our times adjusted for running at 1,000 ft higher elevation")

print(round(int(run_time1 * (1 + Decimal(.4)))))
print(round(int(run_time2 * (1 + Decimal(.4)))))
print(round(int(run_time3 * (1 + Decimal(.4)))))