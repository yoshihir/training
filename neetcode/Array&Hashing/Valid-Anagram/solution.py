def isAnagram(s: str, t: str) -> bool:
    # 文字列の長さが異なる場合はアナグラムではない
    if len(s) != len(t):
        return False
    
    # 各文字の出現回数を格納する辞書を作成
    char_count = {}
    
    # 1つ目の文字列の各文字をカウント
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # 2つ目の文字列の各文字をカウントから減算
    for char in t:
        # 文字が存在しない、または既にカウントが0の場合はアナグラムではない
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

# テストケース
def test_isAnagram():
    # テストケース1
    assert isAnagram("racecar", "carrace") == True, "Test case 1 failed"
    
    # テストケース2
    assert isAnagram("jar", "jam") == False, "Test case 2 failed"
    
    # 追加のテストケース
    assert isAnagram("anagram", "nagaram") == True, "Test case 3 failed"
    assert isAnagram("rat", "car") == False, "Test case 4 failed"
    assert isAnagram("", "") == True, "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_isAnagram()