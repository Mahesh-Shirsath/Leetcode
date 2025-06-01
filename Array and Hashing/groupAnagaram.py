from collections import defaultdict

def groupAnagrams(list):
    anagrams = defaultdict(list)

    for word in list:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

test_cases = [
    {
        "list": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    }
]

for test_case in test_cases:
    result = groupAnagrams(test_case["list"])
    print(result)
    assert result == test_case["expected"]

print("All test cases passed")