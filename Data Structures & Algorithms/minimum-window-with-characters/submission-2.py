class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        start = 0
        length = len(s) + 1
        substring = ""

        # target count of letter occurences
        target_letters = Counter(t)
        # dictionary with letters as keys, but all values set to 0
        substring_letters = Counter({letter: 0 for letter in t})

        have, need = 0, len(set(t))

        # add letters from the right until we reach the end
        for index, char in enumerate(s):
            if char in substring_letters:
                substring_letters[char] += 1
                # only update have if the letter reqs haven't been met yet
                #print(f"We have {substring_letters[char]} instaces of {char} compared to {target_letters[char]}")
                if substring_letters[char] == target_letters[char]:
                    have += 1
                    #print(f"Updating have count to {have} letters out of {need} letters")
                #else:
                    #print(f"Not updating {char} in have count")
                
                # pop off letters from left until we no longer have a valid substring
                while have == need:
                    temp_substring = s[start:index+1]
                    print(f"Evaluating the valid substring {temp_substring} against {substring}")
                    print(f"Current range is [{start}, {index}]")
                    # save the substring if its shorter than the original string
                    current_length = index - start + 1
                   # print(f"Comparing {current_length} against {length}")
                    if current_length <= length:
                        length = current_length
                        substring = temp_substring
                        #print(f"Successfully updated substring to {substring}")
                        
                    char = s[start]
                    # move pointer to remove substring's starting letter
                    start += 1
                    print(f"Removing {char} and updating starting index to {start}")

                    # if it is an important letter, update it in the dicts
                    if char in substring_letters:
                        substring_letters[char] -= 1
                        if substring_letters[char] == target_letters[char] - 1:
                            have -= 1

        return substring


        