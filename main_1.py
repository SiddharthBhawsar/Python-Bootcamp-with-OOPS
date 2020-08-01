def matchingWord(Sentence1, Sentence2):
    words1=Sentence1.split(" ")
    # print(words1)
    words2=Sentence2.split(" ")
    # print(words2)
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return score





if __name__ == '__main__':
    # print(matchingWord("Python is good Language", "Good Morning"))
    sentences = ["Machine Learning by simply Learn machine",
                 "Computer is Machine",
                 "Hello World"]
    query=input("Enter word or sentence you want to search! \n")
    sentScore=[matchingWord(query, var)  for var in sentences]
    # print(sentScore)
    sortSentScore=[sortScore for sortScore in sorted(zip(sentScore, sentences),reverse=True) if sortScore[0] != 0 ]
    # print(sortSentScore)
    print(f"{len(sentScore)} mathes found!")
    for score, item in sortSentScore:
        print(f"\"{item}\" having {score} matches found"  )