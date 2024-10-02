README

MY SUBMISSION IS IN BRANCH 'MASTER'

PWS Link: http://guruprasanth-meyyarasu-ecommerceapp.pbp.cs.ui.ac.id

Assignment 1:

Answer 1:
I created a new directory and installed Django on it. I didn’t only follow the tutorial but moreover I googled and researched on how to implement new things.

Answer 2: 
![alt text](<Screenshot 2024-09-11 at 10.23.18-1.png>)

urls.py: maps the url to the views.py
views.py: this is what handles the actual request, it is the UI basically. If it wants it can also retrieve data from models.py
models.py: this gives views.py everything it wants, for example all products from the database
HTML template: after the views.py is finished it will give the data to the HTML template, which shows it in an user-friendly style

Answer 3:
Git can be used in many different ways in software development. Firstly, if you have an app which has a bug, you can recover previous saved versions and update it till the bug is fixed. Secondly, if you have multiple people working on a project, it is often easier to use GitHub as software to individually create new features and merge them with the main branch.

Answer 4:
It’s a pretty easy to use framework which only needs little refinement. It is basically ready to use, while also not being too simple. It is a powerful tool, which is easy to learn.

Answer 5:
It is considered an ORM because it allows developers to interact with a database using python and not SQL. That makes it easier for developers, because raw SQL can be hard times use.


Assignment 2:

Answer 1:
It is important for efficient operation, user expceptations and rapid evolution of the digital landscape. Data delivery also provides real-time interaction, so companies like instagram can interacte with their users easily and instantanious.

Answer 2:
JSON gives way more information with clear signs which information is what. XML does not give that kind of info. Additionally json can be used for many different things, while xml can only be used limited. Also wider range of data types and it's just easier to read.

Answer 3:
The functional use of is_valid() is to validate submitted data. It checks if the submitted data meets the criteria and gives bakc errors if not. It provides the user with the necessary feedback while also assuring that only valid data is in the database.

Answer 4:
CSRF tokens ensure that form submissions are made by legitimate users. Without CSRF a hacker could use user data without their consent and sell it to thirs parties. That could be done in several ways including malicious links or auto-submissions, where a site will automatically extract user information by just visiting it.

Answer 5:
I followed the tutorial at first, but afterwards it got really messy with the names. because I changed the name from MoodEntry to ProductEntry. So I used the internet to help me with things like json_by_id and etc.

![xml](<Screenshot 2024-09-17 at 15.48.53.png>)
![json](<Screenshot 2024-09-17 at 15.49.14.png>)
![json_by_id](<Screenshot 2024-09-17 at 15.49.27.png>)
![xml_by_id](<Screenshot 2024-09-17 at 15.49.35.png>)

Assigment 3:

Answer 1:
Difference s simplicity and flexibility. You can use redirect() for easier and more flexible redirects, but HttpResponseRedirect() for a specific URL.

Answer 2:
The MoodEntry or even the Product is linked to the user via a foreignkey. If the user is deleted the key will also be deleted.

Answer 3:
Authentication is to see if the user is really the user with password for example. Authorization is to determine if the user is allowed to perform a specific task. If a user logs in, then first there will be an authentication, via the database, afterwards a session will be created and lastly the user will be authorized. Authorization (django.contrib.auth), Authentication (@login_required).

Answer 4:
Django remembers logged in users using sessions, which are stored in cookies. Django sets a session cookie when the user logs in. The cookie has a session id, which will give django the opportunity to log in the user without login information.

Answer 5:
I googled a lot, and also used the tutorial.

Assignment 4:

Answer 1:
The priority order of CSS selectors is determined by specificity (Inline Styles > ID Selectors > Class > Element > Universal Selector)

Answer 2:
Responsive design is crucial to todays world of multiple devices. It ensures that the website is visible and usable on every device no matter its size or proportions. Without it many websites would only be functionable on a specific device.

Answer 3:
The difference between these is how they create space around an element. Margin is the space outside an element and controls how far elements are to each other (margin: 20px). Border is betwen Margin and Padding, it is the line surrounding the element (border: 2px solid black). Padding is the space inside the element, between its content and border. (padding: 15px)

Answer 4:
Flexbox is an one-dimensional layour model which allows user to align and distribute space within a container. That way you can for example center elements or reorder them. With the Flexbox you can only do it either horizontally OR vertically, only one axis. The Grid Layout on the other hand has two axis which can be used, for example for creating full web page layouts or dashboards.

Answer 5:
I went on the tailwind and bootstrap websites and looked at the possible options I could use, but ended up sticking with the basics, because they looked the best.