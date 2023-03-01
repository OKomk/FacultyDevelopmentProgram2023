
# Q3
#importing libraries
import random
import matplotlib.pyplot as plt

#function for calculating probability by generating random numbers
def prob(n):
    c = 0 #count
    #simulate for 1000 times
    for i in range(1000):
        l = [random.randrange(1, 366) for i in range(n)] #generate random numbers from 1 to 365
        for x in l:
            if l.count(x) > 1: # condition that atleast two have same birthday
                c+=1 #increase the count
                break
    return c/1000

p1 = prob(23)
print(f'Probability that atleast 2 people out of 23 people have same birthday:{p1}')
p2 = prob(40)
print(f'Probability that atleast 2 people out of 40 people have same birthday:{p2}')
p3 = prob(80)
print(f'Probability that atleast 2 people out of 80 people have same birthday:{p3}')
p4 = prob(300)
print(f'Probability that atleast 2 people out of 300 people have same birthday:{p4}')

p = [] # list for storing probabilities (y-axis for plot)
np = [i for i in range(1, 301)] # all numbers in range 1 to 300 (x-axis for plot)
# append probabilities by calling the prob function
for i in range(1, 301):
    p.append(prob(i))

#plot using matplotlib
plt.plot(np, p)
plt.grid()
plt.xlabel('n')
plt.ylabel('p')
plt.title('p vs n')
plt.show()

#Finding n for p>=0.8
for j in range(len(p)):
    if p[j]>=0.8:
        print(f'Probability is 0.8 for n = {j+1}')
        break



# # Q4
# #importing libraries
# import random
# import matplotlib.pyplot as plt
# from numpy.random import choice

# d = [i for i in range(1, 244)] #array for storing numbers 1 to 244 (days)
# l1 = [2/365 for i in range(1, 123)] # probability array for 1-122 days (2/(122*2+121))

# # appending probabilities for 123-243 days (1/(122*2+121))
# for i in range(123, 244):
#     l1.append(1/365)

# np, p = [], [] # declaring lists for n and p
# for i in range(1, 244):
#     c=0 #count
#     np.append(i) 
#     # simulate for 1000 times
#     for j in range(1000):
#         # generate random numbers from 1-243 with probabilities given by list l1
#         d1 = choice(d, size = i, p = l1) # numpy.random.choice()
#         # obtain list from numpy array d1
#         l = []
#         for k in range(i):
#             l.append(d1[k])
#         for li in l:
#             if l.count(li) > 1: # condition that atleast two have same birthday
#                 c+=1
#                 break
#     p.append(c/1000)
# # Print probabilities for n = 23, 40, 80
# print(f'P(23) = {p[22]}')
# print(f'P(40) = {p[39]}')
# print(f'P(80) = {p[79]}')

# #plot using matplotlib
# plt.plot(np, p)
# plt.grid()
# plt.xlabel('n')
# plt.ylabel('p')
# plt.title('p vs n')
# plt.show()

