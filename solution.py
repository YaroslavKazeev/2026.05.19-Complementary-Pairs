def countComplementaryPairs(stringData):
    concatPermStrings = []
    counter = 0

    for i in range(len(stringData) - 1):
        for j in range(i + 1, len(stringData)):
            concatPermStrings.append(stringData[i] + stringData[j])

    for string in concatPermStrings:
        isOddityOnce = False
        isPalindrome = True
        for char in set(string):
            if not isOddityOnce and string.count(char) % 2 != 0:
                isOddityOnce = True
                continue
            if string.count(char) % 2 != 0:
                isPalindrome = False
                break

        if isPalindrome:
            counter += 1

    return counter


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
        "input": ["ab", "ba"],
        "expected": 1,
        "description": "Two strings that are exact reverses",
    },
]
