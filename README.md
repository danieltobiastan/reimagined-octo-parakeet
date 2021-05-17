# UWA CITS3403 FINAL PROJECT
**remagined-octo-parakeet**

## key.stroke
![image](https://github.com/danieltobiastan/reimagined-octo-parakeet/blob/frontpagestyle/images/frontpage.jpg)

a minimalistic typing game designed to test and train speed and accuracy under time pressure.

## Required Software and Setup
**IMPORTANT:** in order to run flask and create a locally hosted domain on which to use the webpage, you
must have some python packages installed, this can be done by creating and entering a virtual environment 
within the working directory. Open the terminal and follow the steps:

to create virtual environment: _python3 -m venv venv_

to activate virtual environment (Windows): _venv\Scripts\activate_

to activate virtual environment (Mac/Linux): _source venv\Scripts\activate_

from the virtual environment, the following python packages must be installed using: _pip install 'packagename'_

- _flask_
- _flask-wtf_
- _flask-sqlalchemy_
- _flask-login_
- _flask-migrate_
- _email-validator_

from here you are able to: _run flask_

which will create a localhost domain where you can view and interact with the webpage by going to your browser and typing: _http://localhost:5000/_

## Tutorial
When on the home webpage, in order to start a new game, the user must press the begin button at the bottom of the page. 

![image](https://github.com/danieltobiastan/reimagined-octo-parakeet/blob/frontpagestyle/images/playtutorial.jpg)

They must then begin typing over the text that appears at the center of the screen, until the timer reaches zero. Their score will then be sent to the database and the user will be able to view it in the scores page.

The user is able to click on the icons at the top of the page to navigate between their scores, logging out, and leaderboards.

![image](https://github.com/danieltobiastan/reimagined-octo-parakeet/blob/frontpagestyle/images/navtutorial.jpg)

## Development
This webpage combines client-side and server-side programming techniques to enhance the user experience.
a template was built using flask, a python based web app framework. Flask connects the html, javascript and css with a database, and login and register forms. This allows the user to view their scores as well as a leaderboard of the top global scores.

## Testing
Constant revision of code by group members allowed us to keep an efficient, well written and succinct product throughout. Branches were constructed where the work was divided between group members, with it being merged together regularly at our group meetings via zoom.

Some basic unittests were written to test password hashing and whether or not information was being accepted into the database. 

to run the test cases: _python test.py <filename>_ 

## Contributors
- Daniel Tan (22684196)
- Callum Brown (22985036)
- Shaobo Zhang (22133027)
- Ye Liu (22560064)
