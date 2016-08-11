# Housing Recommendation Engine

## Implemented by Winnie & Nik

> Problem:
Finding affordable housing in San Francisco.

###In this project we build a housing recommendation system with information provided from zillow.com.


This project demonstrates the usage of k-means clustering and k nearest neighbors on a dataset which included homes from the san francisco bay area. A recommendation system is an important component in many online services. The recommendation system can help the user find interesting content or goods to take a look at. When a user sees a product or in this case home this increases the chance that will proceed with a purchase.
  
Recommendation systems have gained traction fairly quickly in the past few years a famous usage example of this technology would be the netflix prize where machine learning was used to predict the ratings for movies and provide recommendations for users of what to watch next based on their interests. 
  
###By using K-means clustering and K-nearest neighbors this recommendation system will suggest compatible homes to the user based on the inputs they provide.

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

### Methods:

The K-means clustering algorithm is used to group homes into individual clusters based on various inputs selected from the data set criteria.
Random centroids were picked from the given range of the dataset. Distance was measured using Euclidean Distance to define the cluster and its neighboring inhabitants.

![Zest v. sqft (SF)](http://g.recordit.co/UDT2gRkMrq.gif)

![Zest v. sqft(SJ)](http://g.recordit.co/zERsuQoRyJ.gif)

Data was loaded using python with the aid of the pandas and numpy libraries.
 
### Results:

The estimated price  of homes in San Francisco and San Jose compared to price per square foot.

[![Zestimate vs. Sqft (San Francisco).png](https://s9.postimg.org/kzzsx5oxr/Zestimate_vs_Sqft_San_Francisco.png)](https://postimg.org/image/i5wnjpmrf/)



[![Zestimate vs. sqft (San Jose).png](https://s9.postimg.org/99vutz53j/Zestimate_vs_sqft_San_Jose.png)](https://postimg.org/image/gpv4frssr/)




## Goals:

