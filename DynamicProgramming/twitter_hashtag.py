"""
Q: given a dictionary of valid words and a twitter hashtag parse it into exactly two words
E.g. #happybirthday -> happy birthday  words = (happy, birthday)
E.g. #happya -> happy a  words = (happy, a)

search string of length K in a set

Q: what if now we can have any number of words?
E.g. #planstovetothebill -> plans to veto the bill
                         -> plan stove to the bill
                         

memoize = {
    "thebill" : ["the", "bill"]
}
plans to veto -> recurse_string(...,"thebill")
plan stove to -> recurse_string(...,"thebill")

sliced_words = [plan, stove]
i = len-2
hashtag = bill

dump of wikipedia articles

aaaaaaaaaaaaaaaaaaaaaaaaaa

a
aa
aaa
aaaa
aaaaa


"""
def parse_multi_word_hashtag(word_dict, hashtag):
    memo = {}
    return helper(word_dict, hashtag, memo)
        
def helper(word_dict, hashtag, memo):

    if hashtag in memo:
        return memo[hashtag]

    output = []
    if hashtag in word_dict:
        output.append(hashtag)

    for i in range(1, len(hashtag)):
        word1 = hashtag[:i]
        if word1 in word_dict:
            for break_word in helper(word_dict, hashtag[i:], memo):
                added = word1 + ' ' + break_word
                output.append(word1 + ' ' + break_word)
    
    memo[hashtag] = output
    return output


def parse_double_word_hashtag(words, hashtag):
    
    ans = []
    for i in range(len(hashtag)-1): # i = len(hashtag) - 1, word2 = ?
        word1 = hashtag[:i+1]
        if word1 in words:
            word2 = hashtag[i+1:]
            if word2 in words:
                ans.append(word1 + " " + word2)
    return ans

def test1():
    hashtag = "planstovetothebill"
    words = set(["plan", "plans", "to", "veto", "the", "bill", "stove"])
    return parse_multi_word_hashtag(words, hashtag)

def test2():
    hashtag = "catsanddog"
    words = set(['cat', 'cats', 'sand', 'and', 'dog'])
    return parse_multi_word_hashtag(words, hashtag)

print(test1())
print(test2())