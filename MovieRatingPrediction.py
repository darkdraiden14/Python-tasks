import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading ratings file
# Ignore the timestamp column
ratings = pd.read_csv('ratings.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'movie_id', 'rating'])

# Reading users file
users = pd.read_csv('users.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading movies file
movies = pd.read_csv('movies.csv', sep='\t', encoding='latin-1', usecols=['movie_id', 'title', 'genres'])
# Join all 3 files into one dataframe
dataset = pd.merge(pd.merge(movies, ratings),users)
# Display 20 movies with highest ratings
data=dataset[['title','rating','genres','age_desc','gender']].sort_values('rating', ascending=False)
data.head()
# Make a census of the genre keywords
genre_labels = set()
for s in movies['genres'].str.split('|').values:
    genre_labels = genre_labels.union(set(s))

# Function that counts the number of times each of the genre keywords appear
def count_word(dataset, ref_col, census):
    keyword_count = dict()
    for s in census:
        keyword_count[s] = 0
    for census_keywords in dataset[ref_col].str.split('|'):
        if type(census_keywords) == float and pd.isnull(census_keywords):
            continue
        for s in [s for s in census_keywords if s in census]:
            if pd.notnull(s):
                keyword_count[s] += 1
    #______________________________________________________________________
    # convert the dictionary in a list to sort the keywords by frequency
    keyword_occurences = []
    for k,v in keyword_count.items():
        keyword_occurences.append([k,v])
    keyword_occurences.sort(key = lambda x:x[1], reverse = True)
    return keyword_occurences, keyword_count

# Calling this function gives access to a list of genre keywords which are sorted by decreasing frequency
keyword_occurences, dum = count_word(movies, 'genres', genre_labels)
# Fill NaN values in user_id and movie_id column with 0
ratings['user_id'] = ratings['user_id'].fillna(0)
ratings['movie_id'] = ratings['movie_id'].fillna(0)

# Replace NaN values in rating column with average of all values
ratings['rating'] = ratings['rating'].fillna(ratings['rating'].mean())
# extracting feature
features=data.iloc[:,2:].values   # genres,age,gender
# extracting label
labels=data.iloc[:,1].values
from sklearn.preprocessing import LabelEncoder
cont=LabelEncoder()
# label encoding on features
features[:,0]=cont.fit_transform(features[:,0])
features[:,1]=cont.fit_transform(features[:,1])
features[:,2]=cont.fit_transform(features[:,2])
def MovieEncod(m_genre):
    movie_dict={'Action': 0, 'Action|Adventure': 1, 'Action|Adventure|Animation': 2,
                "Action|Adventure|Animation|Children's|Fantasy": 3, 'Action|Adventure|Animation|Horror|Sci-Fi': 4,
                "Action|Adventure|Children's": 5, "Action|Adventure|Children's|Comedy": 6,
                "Action|Adventure|Children's|Fantasy": 7, "Action|Adventure|Children's|Sci-Fi": 8,
                'Action|Adventure|Comedy': 9, 'Action|Adventure|Comedy|Crime': 10,
                'Action|Adventure|Comedy|Horror': 11, 'Action|Adventure|Comedy|Horror|Sci-Fi': 12,
                'Action|Adventure|Comedy|Romance': 13, 'Action|Adventure|Comedy|Sci-Fi': 14,
                'Action|Adventure|Comedy|War': 15, 'Action|Adventure|Crime': 16, 'Action|Adventure|Crime|Drama': 17,
                'Action|Adventure|Crime|Thriller': 18, 'Action|Adventure|Drama': 19,
                'Action|Adventure|Drama|Romance': 20, 'Action|Adventure|Drama|Sci-Fi|War': 21,
                'Action|Adventure|Drama|Thriller': 22, 'Action|Adventure|Fantasy': 23,
                'Action|Adventure|Fantasy|Sci-Fi': 24, 'Action|Adventure|Horror': 25,
                'Action|Adventure|Horror|Thriller': 26, 'Action|Adventure|Mystery': 27, 'Action|Adventure|Mystery|Sci-Fi': 28, 'Action|Adventure|Romance': 29, 'Action|Adventure|Romance|Sci-Fi|War': 30, 'Action|Adventure|Romance|Thriller': 31, 'Action|Adventure|Romance|War': 32, 'Action|Adventure|Sci-Fi': 33, 'Action|Adventure|Sci-Fi|Thriller': 34, 'Action|Adventure|Sci-Fi|Thriller|War': 35, 'Action|Adventure|Sci-Fi|War': 36, 'Action|Adventure|Thriller': 37, 'Action|Adventure|War': 38, 'Action|Adventure|Western': 39, "Action|Animation|Children's|Sci-Fi|Thriller|War": 40, "Action|Children's": 41, "Action|Children's|Fantasy": 42, 'Action|Comedy': 43, 'Action|Comedy|Crime': 44, 'Action|Comedy|Crime|Drama': 45, 'Action|Comedy|Crime|Horror|Thriller': 46, 'Action|Comedy|Drama': 47, 'Action|Comedy|Fantasy': 48, 'Action|Comedy|Musical': 49, 'Action|Comedy|Musical|Sci-Fi': 50, 'Action|Comedy|Romance|Thriller': 51, 'Action|Comedy|Sci-Fi|Thriller': 52, 'Action|Comedy|Sci-Fi|War': 53, 'Action|Comedy|War': 54, 'Action|Comedy|Western': 55, 'Action|Crime': 56, 'Action|Crime|Drama': 57, 'Action|Crime|Drama|Thriller': 58, 'Action|Crime|Mystery': 59, 'Action|Crime|Mystery|Thriller': 60, 'Action|Crime|Romance': 61, 'Action|Crime|Sci-Fi': 62, 'Action|Crime|Thriller': 63, 'Action|Drama': 64, 'Action|Drama|Fantasy|Romance': 65, 'Action|Drama|Mystery': 66, 'Action|Drama|Mystery|Romance|Thriller': 67, 'Action|Drama|Romance': 68, 'Action|Drama|Romance|Thriller': 69, 'Action|Drama|Sci-Fi|Thriller': 70, 'Action|Drama|Thriller': 71, 'Action|Drama|Thriller|War': 72, 'Action|Drama|War': 73, 'Action|Drama|Western': 74, 'Action|Horror': 75, 'Action|Horror|Sci-Fi': 76, 'Action|Horror|Sci-Fi|Thriller': 77, 'Action|Horror|Thriller': 78, 'Action|Mystery|Romance|Thriller': 79, 'Action|Mystery|Sci-Fi|Thriller': 80, 'Action|Mystery|Thriller': 81, 'Action|Romance': 82, 'Action|Romance|Sci-Fi': 83, 'Action|Romance|Thriller': 84, 'Action|Romance|War': 85, 'Action|Sci-Fi': 86, 'Action|Sci-Fi|Thriller': 87, 'Action|Sci-Fi|Thriller|War': 88, 'Action|Sci-Fi|Thriller|Western': 89, 'Action|Sci-Fi|War': 90, 'Action|Sci-Fi|Western': 91, 'Action|Thriller': 92, 'Action|Thriller|War': 93, 'Action|War': 94, 'Action|Western': 95, 'Adventure': 96, "Adventure|Animation|Children's": 97, "Adventure|Animation|Children's|Comedy|Fantasy": 98, "Adventure|Animation|Children's|Comedy|Musical": 99, "Adventure|Animation|Children's|Fantasy": 100, "Adventure|Animation|Children's|Musical": 101, "Adventure|Animation|Children's|Sci-Fi": 102, 'Adventure|Animation|Film-Noir': 103, 'Adventure|Animation|Sci-Fi': 104, 'Adventure|Animation|Sci-Fi|Thriller': 105, "Adventure|Children's": 106, "Adventure|Children's|Comedy": 107, "Adventure|Children's|Comedy|Fantasy": 108, "Adventure|Children's|Comedy|Fantasy|Romance": 109, "Adventure|Children's|Comedy|Fantasy|Sci-Fi": 110, "Adventure|Children's|Comedy|Musical": 111, "Adventure|Children's|Drama": 112, "Adventure|Children's|Drama|Musical": 113, "Adventure|Children's|Drama|Romance": 114, "Adventure|Children's|Fantasy": 115, "Adventure|Children's|Fantasy|Sci-Fi": 116, "Adventure|Children's|Musical": 117, "Adventure|Children's|Romance": 118, "Adventure|Children's|Sci-Fi": 119, 'Adventure|Comedy': 120, 'Adventure|Comedy|Drama': 121, 'Adventure|Comedy|Musical': 122, 'Adventure|Comedy|Romance': 123, 'Adventure|Comedy|Sci-Fi': 124, 'Adventure|Crime|Sci-Fi|Thriller': 125, 'Adventure|Drama': 126, 'Adventure|Drama|Romance': 127, 'Adventure|Drama|Romance|Sci-Fi': 128, 'Adventure|Drama|Thriller': 129, 'Adventure|Drama|Western': 130, 'Adventure|Fantasy': 131, 'Adventure|Fantasy|Romance': 132, 'Adventure|Fantasy|Sci-Fi': 133, 'Adventure|Musical': 134, 'Adventure|Musical|Romance': 135, 'Adventure|Romance': 136, 'Adventure|Romance|Sci-Fi': 137, 'Adventure|Sci-Fi': 138, 'Adventure|Sci-Fi|Thriller': 139, 'Adventure|Thriller': 140, 'Adventure|War': 141, 'Adventure|Western': 142, 'Animation': 143, "Animation|Children's": 144, "Animation|Children's|Comedy": 145, "Animation|Children's|Comedy|Musical": 146, "Animation|Children's|Comedy|Musical|Romance": 147, "Animation|Children's|Comedy|Romance": 148, "Animation|Children's|Drama|Fantasy": 149, "Animation|Children's|Fantasy|Musical": 150, "Animation|Children's|Fantasy|War": 151, "Animation|Children's|Musical": 152, "Animation|Children's|Musical|Romance": 153, 'Animation|Comedy': 154, 'Animation|Comedy|Thriller': 155, 'Animation|Musical': 156, 'Animation|Mystery': 157, 'Animation|Sci-Fi': 158, "Children's": 159, "Children's|Comedy": 160, "Children's|Comedy|Drama": 161, "Children's|Comedy|Fantasy": 162, "Children's|Comedy|Musical": 163, "Children's|Comedy|Mystery": 164, "Children's|Comedy|Sci-Fi": 165, "Children's|Comedy|Western": 166, "Children's|Drama": 167, "Children's|Drama|Fantasy": 168, "Children's|Drama|Fantasy|Sci-Fi": 169, "Children's|Fantasy": 170, "Children's|Fantasy|Musical": 171, "Children's|Fantasy|Sci-Fi": 172, "Children's|Horror": 173, "Children's|Musical": 174, "Children's|Sci-Fi": 175, 'Comedy': 176, 'Comedy|Crime': 177, 'Comedy|Crime|Drama': 178, 'Comedy|Crime|Drama|Mystery': 179, 'Comedy|Crime|Fantasy': 180, 'Comedy|Crime|Horror': 181, 'Comedy|Crime|Mystery|Thriller': 182, 'Comedy|Crime|Thriller': 183, 'Comedy|Documentary': 184, 'Comedy|Drama': 185, 'Comedy|Drama|Musical': 186, 'Comedy|Drama|Romance': 187, 'Comedy|Drama|Sci-Fi': 188, 'Comedy|Drama|Thriller': 189, 'Comedy|Drama|War': 190, 'Comedy|Drama|Western': 191, 'Comedy|Fantasy': 192, 'Comedy|Fantasy|Romance': 193, 'Comedy|Fantasy|Romance|Sci-Fi': 194, 'Comedy|Film-Noir|Thriller': 195, 'Comedy|Horror': 196, 'Comedy|Horror|Musical': 197, 'Comedy|Horror|Musical|Sci-Fi': 198, 'Comedy|Horror|Sci-Fi': 199, 'Comedy|Horror|Thriller': 200, 'Comedy|Musical': 201, 'Comedy|Musical|Romance': 202, 'Comedy|Mystery': 203, 'Comedy|Mystery|Romance': 204, 'Comedy|Mystery|Romance|Thriller': 205, 'Comedy|Mystery|Thriller': 206, 'Comedy|Romance': 207, 'Comedy|Romance|Sci-Fi': 208, 'Comedy|Romance|Thriller': 209, 'Comedy|Romance|War': 210, 'Comedy|Sci-Fi': 211, 'Comedy|Sci-Fi|Western': 212, 'Comedy|Thriller': 213, 'Comedy|War': 214, 'Comedy|Western': 215, 'Crime': 216, 'Crime|Drama': 217, 'Crime|Drama|Film-Noir': 218, 'Crime|Drama|Film-Noir|Thriller': 219, 'Crime|Drama|Mystery': 220, 'Crime|Drama|Mystery|Thriller': 221, 'Crime|Drama|Romance': 222, 'Crime|Drama|Romance|Thriller': 223, 'Crime|Drama|Sci-Fi': 224, 'Crime|Drama|Thriller': 225, 'Crime|Film-Noir': 226, 'Crime|Film-Noir|Mystery': 227, 'Crime|Film-Noir|Mystery|Thriller': 228, 'Crime|Film-Noir|Thriller': 229, 'Crime|Horror': 230, 'Crime|Horror|Mystery|Thriller': 231, 'Crime|Horror|Thriller': 232, 'Crime|Mystery': 233, 'Crime|Thriller': 234, 'Documentary': 235, 'Documentary|Drama': 236, 'Documentary|Musical': 237, 'Documentary|War': 238, 'Drama': 239, 'Drama|Fantasy': 240, 'Drama|Fantasy|Romance|Thriller': 241, 'Drama|Film-Noir': 242, 'Drama|Film-Noir|Thriller': 243, 'Drama|Horror': 244, 'Drama|Horror|Thriller': 245, 'Drama|Musical': 246, 'Drama|Musical|War': 247, 'Drama|Mystery': 248, 'Drama|Mystery|Romance': 249, 'Drama|Mystery|Sci-Fi|Thriller': 250, 'Drama|Mystery|Thriller': 251, 'Drama|Romance': 252, 'Drama|Romance|Sci-Fi': 253, 'Drama|Romance|Thriller': 254, 'Drama|Romance|War': 255, 'Drama|Romance|War|Western': 256, 'Drama|Romance|Western': 257, 'Drama|Sci-Fi': 258, 'Drama|Sci-Fi|Thriller': 259, 'Drama|Thriller': 260, 'Drama|Thriller|War': 261, 'Drama|War': 262, 'Drama|Western': 263, 'Fantasy': 264, 'Fantasy|Sci-Fi': 265, 'Film-Noir': 266, 'Film-Noir|Horror': 267, 'Film-Noir|Mystery': 268, 'Film-Noir|Mystery|Thriller': 269, 'Film-Noir|Romance|Thriller': 270, 'Film-Noir|Sci-Fi': 271, 'Film-Noir|Sci-Fi|Thriller': 272, 'Film-Noir|Thriller': 273, 'Horror': 274, 'Horror|Mystery': 275, 'Horror|Mystery|Thriller': 276, 'Horror|Romance': 277, 'Horror|Sci-Fi': 278, 'Horror|Sci-Fi|Thriller': 279, 'Horror|Thriller': 280, 'Musical': 281, 'Musical|Romance': 282, 'Musical|Romance|War': 283, 'Musical|War': 284, 'Mystery': 285, 'Mystery|Romance|Thriller': 286, 'Mystery|Sci-Fi': 287, 'Mystery|Sci-Fi|Thriller': 288, 'Mystery|Thriller': 289, 'Romance': 290, 'Romance|Thriller': 291, 'Romance|War': 292, 'Romance|Western': 293, 'Sci-Fi': 294,
                'Sci-Fi|Thriller': 295, 'Sci-Fi|Thriller|War': 296, 'Sci-Fi|War': 297, 'Thriller': 298, 'War': 299, 'Western': 300}
    genre_no=movie_dict.get(m_genre,"none")
    return genre_no

def gender(u_gender):
    if u_gender in ("M","MALE","male","m","Male"):
        return 1
    elif u_gender in ("F","f","FEMALE","female","Female"):
        return 0
    else:
        print("ERROR please choose right option")

def age(u_age):
    if u_age in range(18,25):
        return 0
    elif u_age in range(25,35):
        return 1
    elif u_age in range(35,45):
        return 2
    elif u_age in range(45,50):
        return 3
    elif u_age in range(50,56):
        return 4
    elif u_age in range(56,100):
        return 5
    else:
        return 6

# calling Classifier
from sklearn.ensemble import RandomForestClassifier
# call
clf=RandomForestClassifier(n_estimators=20)
# train
trained=clf.fit(features,labels)

Name=input("Enter the name  of USER:")
Age=int(input("Enter the age:"))
Movie=input("Enter the Movie  Name:")
Genre=input("Enter the Genre of Movie (for ex: Action|Adventure|Comedy) :")
Gender=input("Enter the gender (F for Female and M for Male) :")

# convert these as per label encoderGen
U_age=age(Age)
U_genre=MovieEncod(Genre)
U_gender=gender(Gender)

# forming it a label
test=[[U_genre,U_age,U_gender]]
# predicting the rating
predicted_rating=trained.predict(test)

print("As per the Prediction, " + Name+ " is likely to give '" + str(predicted_rating[0]) + "' Rating To " + Movie + "movie")
