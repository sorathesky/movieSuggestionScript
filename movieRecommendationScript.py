# Dependencies
from lightfm import LightFM as LFM 
from lightfm.datasets import fetch_movielens as fm
import numpy as np 

#fetching data and formatting it
data = fm(min_rating=4.0)

# Printing training and testing data
print(repr(data['train']))
print(repr(data['test']))

# Instantiating and trainign model using warp gradient descent
model = LFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)


def sample_recommendation(model, data, user_ids):

    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like 
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least liked 
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out results
        print("User %s" % user_id)
        print("     Known positives:")

        for X in known_positives[:3]:
            print("           %s" % X)


        print("     Recommend:")

        for X in top_items[:3]:
            print("           %s" % X)

sample_recommendation(model, data, [3, 25, 450])




