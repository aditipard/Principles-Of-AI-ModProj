#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset from downloads folder and creating an array for the dataset
dataset = pd.read_csv(r"/Users/aditipardeshi/Downloads/datasetedited.csv")
dataset = np.array(dataset)


# %%
#converting strings to integers

followers = dataset[:,2]
eng_auth = dataset[:,4]
eng_avg = dataset[:,5]

def convert(array):
    new_list = []

    for index in range(len(array)):#iterate through the array 
        temp = array[index] #creating a new variable for the index
        if temp[-1] == "M": #identifying the M in the string to indicate number in millions 
            temp2 = float(temp[:-1])*1000000 #deleted the last character of the string, converted to float, multiplied by 1,000,000
        if temp[-1] == "K":#identifying the "K" in the string to indicate number in thousands 
            temp2 = float(temp[:-1])*1000 #deleted last character of the string, converted to float, multiplied by 1,000
        new_list.append(temp2) #appending the new array of adjusted followers with the temp2 variable 
    return new_list

followers_adj = convert(followers)
eng_auth_adj = convert(eng_auth)
eng_avg_adj = convert(eng_avg)

# %%
#sorting data into specific categories using class

class category:
    def __init__(self): #class constructor to assign features to labels
        self.entertainment = []
        self.health_sport_fitness = []
        self.fashion = [] 
        self.beauty_and_makeup = []
        self.photography = []
        self.politics = []
        self.lifestyle = []
        self.finance = []


fa = category() #followers adjusted class
eau = category() #engagement(authentic) adjusted class
eavg = category() #engagement average adjusted class

for i in range(len(dataset)): #sorting by category and follower count, engagement(authentic), and engagement average values
    if dataset[i,1] == "Entertainment":
        fa.entertainment.append(followers_adj[i])
        eau.entertainment.append(eng_auth_adj[i])
        eavg.entertainment.append(eng_avg_adj[i])
    if dataset[i,1] == "Health, Sport, Fitness":
        fa.health_sport_fitness.append(followers_adj[i])
        eau.health_sport_fitness.append(eng_auth_adj[i])
        eavg.health_sport_fitness.append(eng_avg_adj[i])
    if dataset[i,1] == "Fashion":
        fa.fashion.append(followers_adj[i])
        eau.fashion.append(eng_auth_adj[i])
        eavg.fashion.append(eng_avg_adj[i])
    if dataset[i,1] == "Beauty and Makeup":
        fa.beauty_and_makeup.append(followers_adj[i])
        eau.beauty_and_makeup.append(eng_auth_adj[i])
        eavg.beauty_and_makeup.append(eng_avg_adj[i])
    if dataset[i,1] == "Photography":
        fa.photography.append(followers_adj[i])
        eau.photography.append(eng_auth_adj[i])
        eavg.photography.append(eng_avg_adj[i])
    if dataset[i,1] == "Politics":
        fa.politics.append(followers_adj[i])
        eau.politics.append(eng_auth_adj[i])
        eavg.politics.append(eng_avg_adj[i])
    if dataset[i,1] == "Lifestyle":
        fa.lifestyle.append(followers_adj[i])
        eau.lifestyle.append(eng_auth_adj[i])
        eavg.lifestyle.append(eng_avg_adj[i])
    if dataset[i,1] == "Finance":
        fa.finance.append(followers_adj[i])
        eau.finance.append(eng_auth_adj[i])
        eavg.finance.append(eng_avg_adj[i])


# %%
#plotting a scatterplot

plt.figure()
plt.scatter(fa.entertainment,eau.entertainment, color = "Green", s = 15, label = "Engagement Count (Authentic)", marker = "x")
plt.scatter(fa.entertainment,eavg.entertainment, color = "Red", s = 15, label = "Engagement Count Average", marker = "^" )
plt.xlabel("Follower Count")
plt.ylabel("Engagement Count")
plt.legend()
plt.grid()
plt.title("Entertainment Category")
plt.show()
# %%

