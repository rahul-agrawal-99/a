
jobs  = []
total_time = 0
max_profit = 0

total_jobs = int(input("Enter the number of jobs: "))
for i in range(total_jobs):
    print("Enter the arrival time and burst time of job", i+1, ":")
    p = int(input("Profit : "))
    d = int(input("Deadline: "))
    jobs.append([f"j{i+1}",d,p])
    if total_time < d:
        total_time = d
      


jobs = sorted(jobs, key=lambda x: x[2] , reverse=True)

result = [False] * total_time
print("\n\nSelected  jobs  are :")

for i in range(len(jobs)):
    for j in range(min(total_time - 1, jobs[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                print(jobs[i][0] , end=" -> ")
                max_profit = max_profit + jobs[i][2]
                break
            
            
print(" END")
    
print("\nMax profit:", max_profit)

