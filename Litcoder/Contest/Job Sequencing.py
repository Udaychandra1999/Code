def job_sequencing(job_count, job_names, deadlines, profits):
    jobs = list(zip(job_names, deadlines, profits))
    jobs.sort(key=lambda x: x[2], reverse=True)

    result = [None] * job_count
    slot = [False] * job_count

    for i in range(job_count):
        for j in range(min(job_count, jobs[i][1]) - 1, -1, -1):
            if not slot[j]:
                result[j] = jobs[i][0]
                slot[j] = True
                break

    selected_jobs = [job for job in result if job is not None]
    return selected_jobs

job_count = int(input())
job_names = list(input().split())
deadlines = list(map(int, input().split()))
profits = list(map(int, input().split()))

output = job_sequencing(job_count, job_names, deadlines, profits)
print(" ".join(output))
                                                                                                                            