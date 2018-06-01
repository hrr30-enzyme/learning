# Express.js with Babel 

The catalyst learning service updates the recomendations for every user every 10 minutes

#### URL

https://hrr30-enzyme-frontend.herokuapp.com/

### Dependencies:
- [Flask](http://flask.pocoo.org/) as the web framework.
- [Suprise](http://surpriselib.com/) as the main Machine Learning library.
- [Numpy](http://www.numpy.org/)
- [Pandas](http://www.numpy.org/)
- [Requests](http://docs.python-requests.org/en/master/)

## Getting started

# Install dependencies
$ pip install -r requirements.txt


## FAQ

**Why Python instead of Node?**

Python's ecosystem of libraries make it well suited for machine learning and data science.

**How does the recomendation system work?**

It uses a collaborative-based machine learning algorithm called SVD and popularized by Simon Funk in his famous [Try this at home](http://sifter.org/~simon/journal/20061211.html) blog post.
At a high-level, a collaborative-based recomendation algorithm learns what a user may like based on what other users like.  In this specific case, it is predicting what posts a user wants to interact with based on what posts similar users have interacted with.

**Why Flask instead of Django?**

Django is really awesome but would be overkill here.  This service serves only one function and thus a microframework like Flask is more appropriate.
