# nflgamepredictor

The Big Idea:

For this project, I am hoping to combine my interest in sports, analytics, and machine learning to build a model that can predict the results of NFL games with relative accuracy. The sports betting market is already a booming industry in America and is expected to reach $8 billion by 2025. This number only accounts for the revenue generated via registered sportsbooks, as sports fans often compete at the individual level in fantasy leagues and Pick em’ Pools. Thus, an individual's ability to accurately predict the results of sporting events is often tied to both their income and their dignity. While many habitual gamblers do take statistics and historical trends into account when placing their bets, it is impossible to completely remove bias from human-generated decisions. In building this model, I intend to remove this inherent bias and identify the features that most accurately reflect the results of NFL games.

The MVP for this project will consist of a simple UI that... 
1) Allows users to input whichever features are deemed most relevant after training our model on several subsets of features
2) Outputs our model’s response variable based on the user’s input and generates related statistics (confidence intervals, standard deviation, etc.)

I hope sports fanatics will use this site or interface before their games of interest and receive a prediction that outperforms human insight. I have listed some of the suggested features below, though this will change as I explore more data and train my model on different subsets.


and 


 
Since my baseline goal is to predict whether a given team will win or lose a chosen game, a logistic regression model likely makes the most sense. We have a binary dependent variable (W/L), and several numerical and/or categorical predictors. As a stretch goal, I would also like to predict the point differentials of these contests to benefit those interested in spread betting.  While I believe this would be a popular addition, it would also require that I build a separate model with a numerical response and may extend beyond this project’s time constraints.


Learning Goals

There are several skills and techniques I am hoping to learn and/or improve throughout this project, those of which include:
Working with large complex datasets -- I am considering basing my model on historical data from the past ten NFL seasons, which will likely return a data frame with at least a few thousand records. Although this number pales in comparison to many of the datasets that are used in the real world, it is still large enough to complicate certain processes and encourage oversights.
Working with fragmented data from various sources -- I will mention this again in the following section, but I am planning on accessing an actively maintained fork of the nflgame API to pull a majority of my data. While this API will allow me to retrieve and read a lot of pertinent information, I may still have to access other sources to pull data for certain features (E.g. nflgame has no data related to game spreads). I know retrieving this data and combining it with any preexisting records is doable, but it may also be time-intensive. 
Cleaning and data preprocessing -- As I alluded to in the last bullet point, I will likely have to do a lot of preprocessing before I am ready to build the predictive model. This will be more apparent if I choose to collect data from various sources. Although data preprocessing is not the most exciting part of data science, it is a vital skill that I would like to try and hone through this project.
Working with APIs -- Over the summer I participated in a three-day-long hackathon and my team integrated data from the Google Map’s API into our product, however, as a PM intern with little programming experience I did not write the lines of code to access this API. I think getting familiar with how API’s work from an engineering perspective will be useful for future projects that require third-party data.
Machine learning: The core of this project is machine learning and building a model that (hopefully) has some degree of validity. Machine learning is already reshaping the tech industry, and understanding how it works, even at a microlevel, should prove useful.
Python fundamentals -- I do not foresee this project requiring knowledge that is beyond the scope of this course. That being said, it will put my skills to the test and force me to sharpen my understanding of the language.
Building a GUI: Though this is not the portion of the project I am most excited about, I think it is important to understand how to build an intuitive GUI as this allows the general public to access and use your creation.

Implementation Plan:

The way I see it, this project will likely be broken down into three phases:

Data Collection and Preprocessing: Before I can create a model that accurately predicts the results of NFL games, I first need to obtain historical data as fuel for that model. As I mentioned, I can access a great deal of this data via an actively maintained fork of the nflgame API. To access historical game lines, I may use the beatifulsoup module to scrape data from oddsshark.com (or another source if I find something more appealing). I will likely use the pandas library to store information in data frames, as this will make it easier to work with the data moving forward. Before I reach the model building phase I will likely have to join multiple data frames together, which I can do using Python or SQL. I am more comfortable doing this in SQL, so I may look to install a package in Python that allows me to run SQL commands. This way, I will be able to synthesize the data into a single data frame before moving to the next step.
Model Building and Subset Selection: I am planning on using the sci-kit learn library to build my logistic regression model during this phase. At this stage, my sole focus will hopefully be removing irrelevant features from the model, so I should not need to worry about any additional packages at this time.
Integrating the completed model into a GUI: I am pretty unfamiliar with how this process works, however, Professor Li mentioned we will spend an entire session building a simple UI. I am sure this will give me a better idea of what packages I will need to install and what LOE I will need to dedicate to this task.

Project schedule:

I think collecting and reformatting the data will take the most amount of time so I am dedicating the first three weeks to that task. The next two will be spent building the model and selecting relevant features. I do not foresee this being a difficult process so I’ve only reserved three weeks for this stage. Finally, I will spend the last three weeks incorporating the model into a user-friendly UI. As I mentioned, my knowledge of this process is limited, so there is a high probability I will have to adjust this range.

Week 1 - Data collection/preprocessing
Week 2 - Data collection/preprocessing
Week 3 - Data collection/preprocessing
Week 4 - Model Building and Subset Selection
Week 5 - Model Building and Subset Selection
Week 6 - Integrating the completed model into a GUI
Week 7 - Integrating the completed model into a GUI
Week 8 - Integrating the completed model into a GUI / Finishing touches

Collaboration plan: 

Since I am working on this project alone, I will contact Professor Li if I reach an impasse. There are also plenty of online resources that may be helpful to me (such as Stack Overflow), so I will consider collaborating with others online via these platforms if I feel my progress has been stalled.

Risks:

It is entirely possible that the model I build will show no greater signs of predictive accuracy than other methods commonly used by gamblers. This will render my work useless. I need to ensure that I have a broad range of features that encapsulate various elements of NFL football games, otherwise, my model will not accurately reflect the determinants of these games. I am sort of limited by the data that is made publicly available, as there may be inaccessible features that would contribute greater to the model.

As I have mentioned countless times, I also have little knowledge pertaining to user interface design. Since this portion of the project will allow outsiders to interact with the model I built, it is arguably the most important step of the entire process. Learning how to do this effectively may take longer than I anticipated leaving me with little time to touch up or tweak other aspects of the project.

Working alone is also a risk, even though I am excited to involve myself in all of these processes. I will not have people to constantly bounce ideas off of, nor will I be able to specialize in one particular task.

Additional Course Content: 

Some topics we will cover in class that may be useful to my project include the sessions on data analytics using python, object-oriented programming, and user interface design. All of these are extremely relevant to my minimum viable product.
