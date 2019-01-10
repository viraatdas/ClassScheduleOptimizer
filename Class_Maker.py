#program assumes the number of required classes for a requirement will be less than 10,
#which is a fair assumption

#variables refer to the various track requirements
#first number in front of the inner list refer to how many of those classes need to be satisfied
ml = [373, 381, [1, 471,473],[1, 416, 512], [2, 348, 352, 448,456,471, 483, 473, 490,497]] #machine learning
se = [307, [1, 352,354], 408, 407, [2, 348,352,354,381,422,426,448,456,473,473,490]] #software engineering
pl = [352, 354, 456, [3, 307, 353, 381, 390, 422, 483]] #programming languages

all_class = []
all_class.append(ml)
all_class.append(se)
all_class.append(pl)

class_list = [] #optimized class list based on requirments
length = len(all_class) #number of tracks you are optimizing for
dict = {}
for e in all_class:
    for i in range(len(e)):
        if isinstance(e[i], list):
            pass
        else:
            #this must mean it is a required
            if e[i] not in class_list:
                class_list.append(e[i])
