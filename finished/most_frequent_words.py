'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words,
in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples

top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
'''

import re
def top_3_words(text):
    text = text.lower()
    stripped_text = re.sub(r"[^a-zA-Z0-9 ']| '{2,} | ' ",' ',text)
    # regex does not handle apostrophe's like i would expect, so i swap them to underscores after i filter out
    # any underscores that would be here
    stripped_text = re.sub(r"'","_",stripped_text)
    match_list = set(stripped_text.split())
    match_dict = {match : len(re.findall(rf'\b{match}\b', stripped_text)) for match in match_list}
    top_three = [{'null':0}, {'null':0}, {'null':0}]
    for match, value in match_dict.items():
        comparison = [value > list(top_value.values())[0] for top_value in top_three]
        if any(comparison):
            top_three.insert(-1 * sum(comparison), {match:value})
            top_three.pop()
    # swap the underscrores back to apostrophe's afer we're done
    final_top_three = [re.sub('_',"'",list(key.keys())[0]) for key in top_three]
    final_top_three = [val for val in final_top_three if not val == 'null']

    return final_top_three

def assert_equals(first, second):
    print(first == second,first,second)
    return
def main():
    
    assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
    assert_equals(top_3_words("  , e   .. "), ["e"])
    assert_equals(top_3_words("  ...  "), [])
    assert_equals(top_3_words("  '  "), [])
    assert_equals(top_3_words("  '''  "), [])
    assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
    assert_equals(top_3_words("""
    Your output: ['rbdlbdxc', 'wznwrtt', 'hgmkomab']. One possible output: ['rbdlbdxc', "jqee'", 'wznwrtt']['rbdlbdxc', "jqee'"]'rbdlbdxc', "jqee'"]['rbdlbdxc', "jqee'", 'wznwrtt']['rbdlbdxc', "jqee'"]'rbdlbdxc', "jqee'"]
    """),['rbdlbdxc', "jqee'", 'wznwrtt'])
    

if __name__ == "__main__":
    main()