"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0, 9],
            "answer": 9
        },
        {
            "input": [9, 0],
            "answer": 90
        },
        {
            "input": [90000, 11111],
            "answer": 9101010101
        },
    ],
    "Extra": [
        {
            "input": [0, 0],
            "answer": 0,
        },
                {
            "input": [10, 10],
            "answer": 1100,
        },
    ]
}
