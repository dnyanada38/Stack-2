'''

## Problem 636: Exclusive time of functions

## Author: Neha Doiphode
## Date:   09-28-2022

## Description:
    On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
    Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack,
    and when a function call ends, its ID is popped off the stack.
    The function whose ID is at the top of the stack is the current function being executed.
    Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

    You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}".
    For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3,
    and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2.
    Note that a function can be called multiple times, possibly recursively.

    A function's exclusive time is the sum of execution times for all function calls in the program.
    For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit,
    the exclusive time is 2 + 1 = 3.

    Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.


## Examples:
    Example 1:
        Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        Output: [3,4]
        Explanation:
            Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
            Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
            Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
            So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

    Example 2:
        Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
        Output: [8]
        Explanation:
            Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
            Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
            Function 0 (initial call) resumes execution then immediately calls itself again.
            Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
            Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
            So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.

    Example 3:
        Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
        Output: [7,1]
        Explanation:
            Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
            Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
            Function 0 (initial call) resumes execution then immediately calls function 1.
            Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
            Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
            So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.

 ## Constraints:
    1 <= n <= 100
    1 <= logs.length <= 500
    0 <= function_id < n
    0 <= timestamp <= 109
    No two start events will happen at the same timestamp.
    No two end events will happen at the same timestamp.
    Each function has an "end" log for each "start" log.


## Time complexity: O(N), where N is number of log entries.

## Space complexity: O(N/2) = O(N), stack will have N/2 entries at the max, since half of the entries belong to "start" log type and "end" log type.

'''


from typing import List, Optional, Union

def get_input():
    print("Enter the number of functions: ", end = "")
    n = int(input())
    print()

    print("Enter the list of function logs in the format[function_id:{start | end}:function_timestamp, .........]: ")
    print("Example Input: 0:start:0,1:start:2,1:end:5,0:end:6")
    print("Input Logs: ", end = "")
    try:
        logs = input()
    except KeybordInterrupt:
        pass

    logs = [log for log in logs.split(",")]
    return n, logs

class Solution:
    def parse(self, entry: str) -> List[Union[int, str, int]]:
        entry = entry.split(":")
        entry[0] = int(entry[0])
        entry[2] = int(entry[2])
        return entry

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = []
        if len(logs) == 0 or n == 0:
            return answer

        call_stack = []
        answer = [0] * n
        current_timestamp = 0
        previous_timestamp = 0

        for entry in range(len(logs)):
            function_id, log_type, current_timestamp = self.parse(logs[entry])
            if log_type == "start":
                if len(call_stack) > 0:
                    duration = current_timestamp - previous_timestamp
                    answer[call_stack[-1]] += duration
                call_stack.append(function_id)
                previous_timestamp = current_timestamp
            else:
                duration = current_timestamp - previous_timestamp + 1
                answer[call_stack.pop()] += duration
                previous_timestamp = current_timestamp + 1
        return answer

# Driver code
solution = Solution()
n, logs = get_input()
print()
print(f"Input: Total number of functions: {n}")
print(f"Input: List of log enties: {logs}")
print(f"Output: Exclusive time per function: {solution.exclusiveTime(n, logs)}", end = "")
print()