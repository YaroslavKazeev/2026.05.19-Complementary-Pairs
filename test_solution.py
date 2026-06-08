import pytest

from solution import EXAMPLE_TEST_CASES, countComplementaryPairs


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_countComplementaryPairs(case):
    result = countComplementaryPairs(case["input"])
    assert (
        result == case["expected"]
    ), f'{case["name"]} failed: expected {case["expected"]}, got {result}'


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
