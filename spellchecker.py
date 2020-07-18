dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
correct = True              
sentence = input().split()
for i in sentence:
    if i not in dictionary:
        print(i)
        correct = False
if correct is True:
    print("OK")
