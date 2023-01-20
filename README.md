![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

<center><h1>PREDICTION OF AN AMERICAN FOOTBALL PLAY</h1></center>


<br>
Welcome to my Ironhack Data Analyst Bootcamp Final Project (cohort july'22 part time), I hope you enjoy reading it as much as I did doing it.
<br>
<br>

* <h2>What can you see here?</h2><br>

In this repo you will find a Jupyter Notebook with the implementation of three Machine Learning models (Random Forest Classifier, Gadient Boosting Classifier and XGBoost Classifier) , a presentation on [Canva](https://www.canva.com/design/DAFYG6At7Ko/TpFLLTKn64EbB8CAxYaEDg/view?utm_content=DAFYG6At7Ko&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu) and a [Tableau Dashboard](https://public.tableau.com/views/finalproject_16739118765190/IHFinalProjectDashboard?:language=es-ES&publish=yes&:display_count=n&:origin=viz_share_link).
<br>
<br>

* <h2>Introduction to the topic</h2><br>

American football is a team game of 11 players per team that is played in a 100 yards long field with a 10-yard "endzone" at either end, in which teams score touchdowns.

Similar to most team sports, the objective is to work the ball down the field towards your opponent's goal-line in order to score.

In order to do so, the team's quarterback will usually either throw the ball downfield to a receiver, or hand the ball off to his running back, who will attempt to carry the ball forwards.

Teams get four attempts – known as "downs" – to move the ball a total of at least 10 yards up the field. The first of these tries is "first down", the next "second down" and so on. Once they make it 10 yards (or further), the downs reset and it's back to first down.

If a team has not made it ten yards after four downs, possession is turned over to the opposition.

As a result, teams facing fourth down will usually choose to either kick a field goal, if they are close enough to the posts, or else "punt" the ball downfield, ensuring their opponents take possession closer to their own goal-line.
<br>
<br>

* <h2>Goals & objectives of this study</h2><br>

This study is made from a defensive coordinator's point of view and has the main objective of predicting whether the next play the opposing offense will make will be a pass or a run play.

This knowledge is crucial for a defensive coordinator and it can give a tremendous advantage to a defensive coordinator, because if he can anticipate the opponent's play, he will be able to put a better defense on the field.
<br>
<br>

* <h2>Description of the database</h2><br>

This database was made by me, after watching 4 recorded games of Alcobendas Cavaliers, one of the american football teams that are currently playing in the first division of the Spanish National League and one of the teams I faced last December. (we won btw 😏)

I filled up a spreadsheet in excel with the features I normally use to scout my opponents and some others that I considered interesting and useful to run a machine learning model to try to predict the next play they are going to play.

Following I am going to describe each feature for better comprehension.<br>
<br>

| **FEATURES** | **TYPE** |  **DESCRIPTION** |
| :--- | :---: | :--- |
| Quarter | Numerical (discrete) | A football game has 4 quarters, 2 of them in each half of the game. |
| Drive number | Numerical (discrete) | A drive is a set of offensive plays from the time they iniciate their attack until the opponent team gets the possession of the ball. |
| Scoreboard | Categorical | It shows if the studied team is winning, losing or tying in the moment they are attacking. Teams normally play different plays depending on the result of the scoreboard. |
| Down | Numerical (discrete) | As explained before, every down is an attempt that the offensive team has. They have 4 downs to move the ball 10 yards up to the field. Teams play different type of plays depending on which down they are in order to get 4 new downs. |
| Distance | Categorical | The distance to get a new first down, or to score. "Short" for distances of 4 or less yards, "medium" for distances between 5 and 10 yards, "long" for distances further than 10 yards. It's obvious to think that teams will play different type of plays depending on that distance i.e. long passes on long distances. |
| Field | Categorical | Teams play different types of plays depending on whether they are in their own field or in the opponent's field close to score. |
| Hash | Categorical | Hash marks are two rows of lines near the middle of the field that are parallel to the side lines. They work as a limit where the ball is going to be spotted depending where the previous play finished. Some team have patterns of plays played depending if they start the play on the left or right side. |
| Formation | Categorical | The initial formation of the offensive players is going to give information about the play (i.e. a formation with plenty of wide receivers is going to be more likely to be a pass play) |
| Motion | Categorical | If there is a previous movement of one of the players before the snap of the ball or not. |
| Box | Numerical (discrete) | Number of players placed within the space between the players at the end of the offensive line. |
| Personnel | Numerical (discrete) | Classification of how many runningbacks and tight ends are aligned on the offensive formation (i.e. "10 personnel" means 1 RB 0 TE, "21 personnel" means 2 RB and 1 TE). We can think that as much RB's are in the offense, more likely to run the ball instead of passing it.|
| QB position | Categorical | Initial position of the quarterback. It can be under the center or shotgun. |
| RB position | Categorical | Where the runningback or runningbacks are placed. We can see patterns of plays on where they are placed |
| WR field side | Numerical (discrete) | Number of wide receivers are placed on the wide side of the field |
| WR boundary side | Numerical (discrete) | Number of wide receivers are placed on the narrow side of the field |
| Play | Categorical | This is the name of the exact play itself. This feature is going to be deleted in order to avoid errors in our prediction. |
| Play type specific | Categorical | Classification of the type of play more detailed than just "run" or "pass". There are different kind of runs and different kind of passes. This feature is going to be deleted in order to avoid errors in our prediction. |
| Play type | Categorical | In our case, the target variable. Type of the play. Run or pass the ball, that's the question. |
| Result | Categorical | The result that the play produced (i.e. if the pass was complete or not). This feature is going to be deleted in order to avoid errors in our prediction. |
| Gain | Categorical | The result of the play in distance. This feature is going to be deleted in order to avoid errors in our prediction. |
| Score | Categorical | If the play produced a Touchdown, another kind of score or not. This feature is going to be deleted in order to avoid errors in our prediction. |
| Defense front | Numerical (discrete) | Number of defensive line and linebackers are expected on the defense. Offensive Coordinators play diferent plays depending on the front they expect. |
| Defense rush | Numerical (discrete) | Number of defenders expected to go directly to tackle the QB. Offensive Coordinators play diferent plays depending if the defense is aggresive or more conservative. |
| Defense cover type | Categorical | Type of cover that defensive backs are expected to play. There are some teams that they like to play more zone coverage or man to man coverage. Offensive Coordinators play diferent plays depending on that. |

<br>
<br>
<a class="anchor" id="0.1"></a>

* <h2>Table of contents</h2><br>

* 1. [Importing libraries and dependencies](#1)
* 2. [Import the dataset](#2)
* 3. [Data cleaning](#3)
* 4. [Exploratory Data Analysis](#4)
* 5. [Visualizations of the target variable](#5)
    - 5.1 [Visualization of the target variable with some of the explanative variables](#5.1)
* 6. [Preprocessing](#6)
    - 6.1 [Encoding the features](#6.1)
    - 6.2 [Define the target and explanative variables](#6.2)
    - 6.3 [Train Test Split](#6.3)
* 7. [Modeling a Random Forest Classifier using GridSearchCV](#7)
    - 7.1 [Evaluation of the Random Forest Classifier](#7.1)
* 8. [Modeling a Gradient Boosting Classifier using GridSearchCV](#8)
    - 8.1 [Evaluation of the Gradient Boosting Classifier](#8.1)
* 9. [Modeling a XGboost Classifier using GridSearchCV](#9)
    - 9.1 [Evaluation of the XGboost Classifier](#9.1)
* 10. [Conclusions](#10)
* 11. [Saving the model to deploy it](#11)
<br>
<br>
