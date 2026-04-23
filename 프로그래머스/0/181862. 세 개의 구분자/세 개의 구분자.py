import re
def solution(myStr):
    
    split_lists = re.split('[abc]', myStr)
    answer = [s for s in split_lists if s]
    return answer if answer else ['EMPTY']