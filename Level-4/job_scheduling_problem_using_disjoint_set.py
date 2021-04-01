#!/usr/bin/python

# Date: 2021-04-01
#
# Description:
# Given an array of jobs where every job has a deadline and associated profit
# if the job is finished before the deadline. It is also given that every job
# takes the single unit of time, so the minimum possible deadline for any job
# is 1. How to maximize total profit if only one job can be scheduled at a time.
#
# Approach:
# https://www.geeksforgeeks.org/job-sequencing-using-disjoint-set-union/
#
# Complexity:
# O(N)

class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, u, v):  # Union fn
        self.parent[v] = u

def get_max_deadline(arr):
    mx = float('-inf')
    for i in range(len(arr)):
        if mx < arr[i]['deadline']:
            mx = arr[i]['deadline']
    return mx

def get_job_scheduling(arr, t):
    """
    arr -> List of jobs with (job_id, deadline, profit)
    n -> Number of jobs to schedule
    """
    jobs = []
    arr = sorted(arr, key=lambda x: x['profit'], reverse=True)  # Sort jobs by profit in decreasing order
    max_deadline = get_max_deadline(arr)
    ds = Disjoint(max_deadline + 1)
    for i in range(t):
        available_slot = ds.find(arr[i]['deadline'])
        if available_slot > 0:
            ds.merge(available_slot - 1, available_slot)
            jobs.append(arr[i]['id'])
    return jobs  # Return job sequence

def main():
    arr = [
        {'id': 'a', 'deadline': 2, 'profit': 100},
        {'id': 'b', 'deadline': 1, 'profit': 19},
        {'id': 'c', 'deadline': 2, 'profit': 27},
        {'id': 'd', 'deadline': 1, 'profit': 25},
        {'id': 'e', 'deadline': 3, 'profit': 15}
    ]
    assert get_job_scheduling(arr, len(arr)) == ['a', 'c', 'e']

main()
