# Content based filtering using K-Means and K-Nearest Neighbors algorithms to provide housing suggestions.

## Implemented by Winnie & Nik

> Problem: Finding the perfect home.

## In this project we constructed a housing recommendation system with information provided from zillow.

This project demonstrates the usage of k-means clustering and k nearest neighbors on a data set which included homes from through-out the united states. A recommendation system is an important component in many online services. The recommendation system can help the user find interesting content or goods to take a look at. When a user sees a product or in this case home this increases the chance that will proceed with a purchase.
  
Recommendation systems have gained traction fairly quickly in the past few years a famous usage example of this technology would be the netflix prize where machine learning was used to predict the ratings for movies and provide recommendations for users of what to watch next based on their interests. 
  
## By using K-means clustering and K-nearest neighbors this recommendation system will suggest compatible homes to the user based on the inputs they provide.

| Dataset Criteria |
|------------------|
| Property ID      |
| House number     |
| City             |
| State            |
| Zip Code         |
| # Of Bedrooms    |
| # Of Bathrooms   |
| Sqft             |
| Property Value   |

## Methods:

Data was loaded using python with the aid of the pandas and numpy libraries.

The K-means clustering algorithm is used to group homes into individual clusters based on various inputs selected from the data set criteria.
Random centroids were picked from the given range of the dataset. Distance was measured using Euclidean Distance to define the cluster and its neighboring inhabitants.

![Screen Shot 2016-08-10 at 10.16.22 AM.png](https://s9.postimg.org/nqv517wvj/Screen_Shot_2016_08_10_at_10_16_22_AM.png)

![Screen Shot 2016-08-10 at 9.48.45 AM.png](https://s10.postimg.org/g558e7lmh/Screen_Shot_2016_08_10_at_9_48_45_AM.png)

## Results:

### The estimated price  of homes in San Francisco and San Jose compared to price per square foot:

![Zest v. sqft (SF)](http://g.recordit.co/UDT2gRkMrq.gif)

![Zest v. sqft(SJ)](http://g.recordit.co/zERsuQoRyJ.gif)

![Zest v. sqft(N)](http://g.recordit.co/6k825Wel8Q.gif)


### How many Bedrooms you would expect to get at a certain price:

![Zest v. bedrooms(SF)](http://g.recordit.co/KTZoBi7jTF.gif)

![Zest v. bedrooms(SJ)](http://g.recordit.co/R6z7e7JqZY.gif)

![Zest v. bedrooms(N)](http://g.recordit.co/eZ8aVoPB5N.gif)


Organizing these homes into clusters helped us gain the information needed to execute the K nearest neighbor algorithm.

### K-Nearest Neighbors:

This algorithm is what really ties things together. Using the clusters that we have allocated for each home we can now select a specific "ideal" home and locate homes that match the same criteria.

![KNN](https://predictoanalycto.files.wordpress.com/2014/06/selection_004.png)

### Recommendation system output:

Here we select a home nationally and provide recommended homes based on the price desired.

![Screen Shot 2016-08-12 at 9.20.09 AM.png](https://s9.postimg.org/6y1rnozkf/Screen_Shot_2016_08_12_at_9_20_09_AM.png)

In this example we give preference equally to square feet of the home along with the price. 

![Screen Shot 2016-08-12 at 9.19.30 AM.png](https://s10.postimg.org/gl462ghhl/Screen_Shot_2016_08_12_at_9_19_30_AM.png)



### Conclusion and future work:

In this project we implemented a recommendation engine, that based on certain target inputs would suggest housing. The two algorithms KNN and K-means provided us two different aspects of machine learning specifically, supervised and unsupervised learning. In the future we would like to implement some performance enhancements to reduce the time complexity of the algorithms since the data-set is very large. Another extension to build upon for this project would be to have a working application where a user would be able to drag different preferences for criteria allowing the clusters to shift around and reflect the individual choices.


