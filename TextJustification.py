def adjust_remaining_spaces(total_elements, extra_space,word):
    if total_elements == 1:
        extra_space -= len(word)
    else:
        extra_space -= len(word) + 1
    return extra_space

def find_num_of_words_that_fit_and_extra_space(total_elements, extra_space, current_words):
    for word in words:
        if total_elements == 0 and len(word) <= extra_space or total_elements != 0 and len(word) + 1 <= extra_space:
            current_words.append(word)
            total_elements += 1
            extra_space = adjust_remaining_spaces(total_elements,extra_space,word)
        else:
            break

    for i in range(total_elements):
        words.pop(0)

    return total_elements,current_words,extra_space

def find_spacing_between_words(total_elements, extra_space):
    respective_extra_space = [0] * (total_elements - 1)
    while extra_space != 0:
        for i in range(total_elements - 1):
            if extra_space == 0:
                break
            else:
                respective_extra_space[i] += 1
                extra_space -= 1
    return respective_extra_space

def fully_justified(total_elements, extra_space, current_words):
    respective_extra_space = find_spacing_between_words(total_elements,extra_space)
    sub_answer = ""
    while len(current_words) != 0:
        # Not the last word
        if len(current_words) != 1:
            sub_answer += current_words[0] + " " + " " * respective_extra_space[0]
            current_words.pop(0)
            respective_extra_space.pop(0)
        # the last word
        else:
            sub_answer += current_words[0]
            current_words.pop(0)

    return sub_answer

def left_justified(total_elements, extra_space, current_words):
    sub_answer = ""
    for i in range(total_elements):
        if i == total_elements - 1:
            sub_answer += current_words[i] + " " * extra_space
        else:
            sub_answer += current_words[i] + " "
    return sub_answer


class Solution:

    def fullJustify(self, words, max_width):
        answer = []
        while words:  # This while loop is for each line
            current_words = []
            extra_space = max_width
            total_elements = 0

            total_elements,current_words,extra_space = find_num_of_words_that_fit_and_extra_space(total_elements,extra_space,current_words)

            if words and len(current_words) != 1 :
                sub_answer = fully_justified(total_elements, extra_space, current_words)
            else:
                sub_answer = left_justified(total_elements, extra_space, current_words)

            answer.append(sub_answer)

        return answer


hello = Solution()

# words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
words = ["What","must","be","acknowledgment","shall","be"]
# words = ["a"]

maxWidth = 16
print(hello.fullJustify(words,maxWidth))
