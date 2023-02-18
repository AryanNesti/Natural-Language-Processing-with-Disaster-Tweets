correct = 0
total = 0
with open('labels.csv', 'r') as labels:
    with open('submission.csv','r') as ss:
        labels.readline()
        ss.readline()
        for i,j in zip(labels,ss):
            # print(i,j)
            if(i==j):
                correct +=1
            total +=1
print(correct)
print("ACC = " ,correct/total)