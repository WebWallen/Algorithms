def is_anagram(word1, word2): 
    # Step 1: base case = if words aren't same length, can't possibly be anagram, so return "False"
    if len(word1) != len(word2): 
        return False
    # Step 2: convert the first word into a list of strings for ease of comparing and assign to variable (letter_list)
    letter_list = list(word1)
    # Step 3: initialized for loop so we can compare the letters in word #2 to word #1
    for letter in list(word2):
        # Step 4: if the letter appears in both words, remove and continue comparing
        if letter in letter_list:
            # Step 5: if both words are indeed anagrams, they will end up empty
            letter_list.remove(letter)
        # Step 6: otherwise, if we run into a not-shared letter, return "False"
        else:
            return False  
    # Step 7: we made it to the end and all letters are gone, thus return True  
    return True

print(is_anagram('iceman', 'cinema'))
print(is_anagram('iceman', 'mice'))

def anagrams(word):
    # Step 1: establish a list of words or there's nothing to compare
    word_list =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Step 2: intialized an empty array where we can place anagrams
    anagrams = []
    # Step 3: start a loop so we can compare two different words
    for w in word_list:
        # Step 4: if both words are anagrams and not the same...
        if is_anagram(word, w) and word != w:
            # Step 5: append second word (on list) to anagrams
            anagrams.append(w)
    # Step 6: return words that qualify as anagrams of input
    return anagrams

print(anagrams('tan'))
print(anagrams('nat'))