import functools


def compare_jobs(job1, job2):
    if job1[1] < job2[1]:
        return -1
    elif job1[1] > job2[1]:
        return 1
    return 0


def sjf(jobs):
    scheduling_order = sorted([[i, jobs[i], 0] for i in range(len(jobs))], key=functools.cmp_to_key(compare_jobs))
    avg_completion_time = 0
    for i in range(len(scheduling_order)):
        avg_completion_time += scheduling_order[i][1] * (len(scheduling_order) - i)
        for j in range(i, len(scheduling_order)):
            scheduling_order[j][2] += scheduling_order[i][1]

    avg_completion_time /= len(scheduling_order)
    return scheduling_order, avg_completion_time


if __name__ == '__main__':
    print(sjf([15, 8, 3, 10]))
