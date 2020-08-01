def matchingWords(sentence1, sentence2):

#sentence1="Python is good language"
#sentence2="Good Scripting"
    words1=sentence1.strip().split(" ")
    words2=sentence2.strip().split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            if word2.lower() == word1.lower():
                score+=1

    return score
if __name__ == '__main__':
    # print(matchingWors("Python is good Language", "Good Scripting"))
    sentences=["Python is good Language", "Good Scripting", "Subscribe to python language"]
    query=input("Enter the word which you want to search:\n")
    sentScore=[matchingWords(query, sentence) for sentence in sentences]
    # print(sentScore)
    sortSentScore=[sentScore for sentScore in sorted(zip(sentScore, sentences), reverse=True) if sentScore[0] != 0]
    # print(sortSentScore)
    print(f"{len(sortSentScore)} matches found")
    for score, item in sortSentScore:
        print(f"{item} matched {score} times")
