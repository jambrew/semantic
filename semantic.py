# A program to play around with semantic similarity using spacy
import spacy

# Load the medium dictionary
nlp = spacy.load('en_core_web_md')

# Code snippet 1 - compare simple words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''It's interesting to see the higher similarity between monkeys and bananas.
My example would be that comparing mouse with cheese would result in greater
similarity than comparing chicken with cheese'''

word4 = nlp("mouse")
word5 = nlp("cheese")
word6 = nlp("chicken")
print(word4.similarity(word5))
print(word5.similarity(word6))

''' OK so that was interesting, my theory was wrong! Chicken and cheese was a 
lot greater similarity. Maybe because they both start with ch. But it didn't
seem to recognise that mice like cheese! '''

# Code snippet 2 - use for loop to compare simple words
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Code snippet 3 - compare simple sentences using a list, and loop with for loop
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

''' It's interesting that it doesn't seem able to recognise the key word in the sentence,
being the CAT that is doing something strange, instead it gives car greater emphasis. 
Although interesting that the sentence with car in my car scored lower than there is my car'''  


# ==== Example file run with medium dictionary:

# To save you scrolling down, the smaller dictionary doesn't have word vectors and the similarity
# probability is a lot lower. It says you can add your own vectors, so if you wanted to specify
# similarities in a particular application, then using the small dictionary might be preferable
# as it's not going to confidently predict anything that you haven't fed it yourself
-------------Complaints similarity---------------
""" 1.0
0.835077095517691
0.9246800668484182
0.8959758607031337
0.8395325736974772
0.8622109066850939
0.835077095517691
1.0
0.8906698507861426
0.8145960252423514
0.9506983440908762
0.794650864741391
0.9246800668484182
0.8906698507861426
1.0
0.8905291077014569
0.88184629454754
0.8692563822438262
0.8959758607031337
0.8145960252423514
0.8905291077014569
1.0
0.8115091428079356
0.8775634120991097
0.8395325736974772
0.9506983440908762
0.88184629454754
0.8115091428079356
1.0
0.759590996735251
0.8622109066850939
0.794650864741391
0.8692563822438262
0.8775634120991097
0.759590996735251
1.0
-------------Recipes similarity---------------
1.0
0.9058970680531702
0.876188281410988
0.8921914246767313
0.9362319998716938
0.9077991339554589
0.9058970680531702
1.0
0.8960303314307113
0.8683352787585712
0.9251986105731227
0.9092774425049626
0.876188281410988
0.8960303314307113
1.0
0.8206932481018961
0.9234997668651656
0.9066167238062411
0.8921914246767313
0.8683352787585712
0.8206932481018961
1.0
0.8436152755971948
0.8890459855149918
0.9362319998716938
0.9251986105731227
0.9234997668651656
0.8436152755971948
1.0
0.8970581769256016
0.9077991339554589
0.9092774425049626
0.9066167238062411
0.8890459855149918
0.8970581769256016
1.0
-------------Recipes similarity---------------
0.7908974953781049
0.6548518295341987
0.739868093247277
0.7337805432695084
0.6703983067394562
0.7674085842432804
0.7580808759364783
0.5323926147261138
0.711456026675044
0.7008472217256502
0.5443126469769464
0.7254376905581942
0.7884092498717231
0.5253234387230952
0.7214799557383781
0.6939840662542774
0.5243623425430298
0.7301757749509531
0.6633546838990971
0.4596805288222233
0.5643795549917598
0.6354896663817883
0.4868229640175464
0.6469780047472005
0.6612351139999046
0.7954999302389468
0.7757727786024005
0.6793217450290933
0.7921867919801224
0.7706409888372543
0.5407034497147122
0.6932683264149205
0.7135981756961652
0.5491464776242874
0.7118486371023985 """


# ========= Example file with small dictionary
""" -------------Complaints similarity---------------
1.0
c: \Users\xxx\Dropbox\Software Engineer Bootcamp\T38\example.py: 38: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity
method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
print(token.similarity(token_))
0.5181293629218388
0.7174057736869824
0.7698360013516957
0.6591949085239377
0.6330322286003275
0.5181293629218388
1.0
0.6737944505227248
0.44519008375901153
0.6772693850371372
0.5799084515536763
0.7174057736869824
0.6737944505227248
1.0
0.6654231257750414
0.6732007512296015
0.6399289452728729
0.7698360013516957
0.44519008375901153
0.6654231257750414
1.0
0.5691884250412407
0.6025169115271116
0.6591949085239377
0.6772693850371372
0.6732007512296015
0.5691884250412407
1.0
0.4699567134204638
0.6330322286003275
0.5799084515536763
0.6399289452728729
0.6025169115271116
0.4699567134204638
1.0
-------------Recipes similarity---------------
1.0
c: \Users\xxx\Dropbox\Software Engineer Bootcamp\T38\example.py: 58: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity
method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
print(token.similarity(token_))
0.6941871022469235
0.5810681005482409
0.7831206509781176
0.7158291678387089
0.6553959698023811
0.6941871022469235
1.0
0.7292983532621446
0.6922874911586636
0.6848676478683343
0.6753270645716931
0.5810681005482409
0.7292983532621446
1.0
0.6040473502986585
0.6870433427406674
0.7279227309095853
0.7831206509781176
0.6922874911586636
0.6040473502986585
1.0
0.7286111960948528
0.6861022895524735
0.7158291678387089
0.6848676478683343
0.6870433427406674
0.7286111960948528
1.0
0.7674538812820649
0.6553959698023811
0.6753270645716931
0.7279227309095853
0.6861022895524735
0.7674538812820649
1.0
-------------Recipes similarity---------------
c: \Users\xxx\Dropbox\Software Engineer Bootcamp\T38\example.py: 69: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity
method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
print(token.similarity(token_))
0.5513360875982837
0.335117380420155
0.41689606792616624
0.6338377915487959
0.3672419463205099
0.6037977867676815
0.4209769027495883
0.14340380564138017
0.4036027983358455
0.55621528929681
0.18598145531717794
0.5272081854129193
0.5599701082584037
0.2591301534031977
0.49097644903874005
0.6101887714630961
0.2803351875651966
0.5525952346358938
0.460195388090958
0.2205403454300301
0.3653624523229293
0.5815826778441873
0.34659801805699975
0.5066580705467741
0.6887837011383555
0.4213207720402798
0.6347594347387364
0.7833611584235314
0.5892171540068428
0.592517429072337
0.6184740318733216
0.13972157484904535
0.4273962520329554
0.7195851534910702
0.3685528234800124
0.38373040751763593 """
