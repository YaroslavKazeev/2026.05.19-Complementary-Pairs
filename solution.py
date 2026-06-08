def countComplementaryPairs(stringData):
    # write your code here
    pass


EXAMPLE_TEST_CASES = [
    {
        "name": "example_main",
        "input": ["abc", "abcd", "bc", "adc"],
        "expected": 3,
        "description": "Main example from README",
    },
    {
        "name": "sample_case_0",
        "input": ["ball", "all", "call", "bal"],
        "expected": 3,
        "description": "Sample Case 0 from README",
    },
    {
        "name": "sample_case_1",
        "input": ["eye", "aa", "c"],
        "expected": 2,
        "description": "Sample Case 1 from README",
    },
    {
        "name": "edge_case_no_pairs",
        "input": ["ab", "cd", "ef"],
        "expected": 0,
        "description": "No complementary pairs can be formed",
    },
    {
        "name": "edge_case_all_same_chars",
        "input": ["a", "a", "a"],
        "expected": 3,
        "description": "All identical single characters",
    },
    {
        "name": "edge_case_single_string",
        "input": ["abc"],
        "expected": 0,
        "description": "Only one string, no pairs possible",
    },
    {
        "name": "edge_case_two_strings_palindrome",
        "input": ["ab", "ab"],
        "expected": 1,
        "description": "Two strings that are exact reverses",
    },
]
