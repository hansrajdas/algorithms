#!/usr/bin/python

# Date: 2021-03-31
#
# Description:
# Given an array of jobs where every job has a deadline and associated profit
# if the job is finished before the deadline. It is also given that every job
# takes the single unit of time, so the minimum possible deadline for any job
# is 1. How to maximize total profit if only one job can be scheduled at a time.
#
# Approach:
# 1) Sort all jobs in decreasing order of profit. 
# 2) Iterate on jobs in decreasing order of profit.For each job, do the following: 
#    a) Find a time slot i, such that slot is empty and i < deadline and i is
#       greatest. Put the job in this slot and mark this slot filled. 
#    b) If no such i exists, then ignore the job.
#
# Reference: https://www.geeksforgeeks.org/job-sequencing-problem/
#
# Complexity:
# O(N^2) time
#
# Note: This can be optimized using union find

def get_job_scheduling(arr, t):
    """
    arr -> List of jobs with (job_id, deadline, profit)
    n -> Number of jobs to schedule
    """
    arr = sorted(arr, key=lambda x: x[2], reverse=True)  # Sort jobs by profit

    jobs = [-1] * t
    slots = [False] * t
    for i in range(len(arr)):
        # Start from min of jobs deadline or number of jobs required and check
        # if we can fit this job within it's deadline
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if slots[j] is False:  # Found a free slot within job i's deadline
                slots[j] = True
                jobs[j] = arr[i][0]
                break

    return jobs  # Return job sequence 

def main():
    arr = [
        ['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]
    ]
    assert get_job_scheduling(arr, 3) == ['c', 'a', 'e']

main()
