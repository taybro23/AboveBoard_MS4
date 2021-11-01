# Taylor Brookes - Milestone Project 4
## Above Board

[Visit my live website here!](https://aboveboard-ms4.herokuapp.com/)

![Site preview](static/images/site-view.png)

# Table Of Contents

1. [Overview](#overview)
2. [UX](#ux)
    * [Five UX Planes](#five-ux-planes)
        * [Strategy](#strategy)
            * [Target Audience](#target-audience)
            * [Business Goals](#business-goals)
            * [User Stories](#user-stories)
        * [Scope](#scope)
        * [Structure](#structure)
        * [Skeleton](#skeleton)
            * [Wireframes](#wireframes)
        * [Surface](#surface)
            * [Colours](#colours)
            * [Typography](#typography)
            * [Imagery](#imagery)
3. [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks](#frameworks)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

# Overview

Above Board is an e-commerce site used for educational purposes, and I have focused on Skateboarding for the theme of my project. 

You’ll find the essential products you’d need to start or continue skating, from complete decks, trucks and wheels, to t-shirts, hats and skate shoes. The Help & Guidance section provides information on how to start skating, useful links and more!

[Back to Contents](#table-of-contents)

# UX
## Five UX Planes

### Strategy

#### Target Audience
The target audience of my site is people who are looking to purchase skateboards, skateboarding hardware or clothes. It is geared towards both current and new skaters, and includes products for both of these types of customer. 

#### Business Goals
-	To provide an easily navigable e-commerce site
-	Connect with users via social media and through blog posts
-	Making a profit by selling products

#### User Stories
#### Common User Stories
-	To be able to easily navigate through the site on any size screen
-	Search for products
-	Sort products by Price, Name etc.
-	View product details
-	Ability to choose quantity of items, and size if applicable
-	Able to purchase products without an account
-	View their shopping bag and amend their order
-	View Posts in Help & Guidance section
-	Contact the company with any queries or if an issue occurs

#### First Time Users
-	Understand the purpose of the site
-	See the reasons behind registering for an account
-	Being able to easily sign up for an account

#### Returning Users
-	Ability to securely log into their account
-	View their past orders and order confirmations
-	Purchase products and have their orders saved to their profile
-	Receive their order confirmations directly to their email inbox
-	Leave reviews of products

#### Site Owner/Admin
-	Provide a clean, simple e-commerce store so that users can easily find what they’re looking for
-	Have the ability to add, edit/update and delete products
-	Have the ability to add, edit and delete blog posts
-	Keep the site secure by only allowing authorised users access certain areas of the site
-	Securely store user information in case an error occurs


### Scope


### Structure


### Skeleton

#### Wireframes

<details>
<summary>Home</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Products</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Product Detail</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Checkout</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Checkout Success/Order History</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Sign Up</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Sign In</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Profile</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Product Management</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Help & Guidance</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>Help & Guidance Management</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

<details>
<summary>404/500 Pages</summary>

![Mobile Wireframe]()
![Desktop Wireframe]()

</details>

### Surface
#### Colours
#### Typography
#### Imagery

[Back to Contents](#table-of-contents)

# Features

## Current Features

## Future Features

[Back to Contents](#table-of-contents)

# Technologies Used

## Languages
-	HTML5
-	CSS3
-	JavaScript
-	Python3

## Frameworks
-	Django - Used as the main framework
-	Bootstrap 5 - Used for the responsive layout and various classes
-	Google Fonts - Used for the fonts on the site
-	Font Awesome - Used for Icons that are displayed throughout the site
-	SQlite3 - Used as the development database
-	PostgreSQL - Used as the deployed database
-	Stripe - Used for card payments
-	AWS S3 - Amazon Web Services, used for hosting images and static files
-	GitHub - Used for storing the project files
-	GitPod - Used as the IDE for my project
-	Heroku - Used for deploying the site
-	Balsamiq - Used to create Wireframes
-	Adobe Photoshop - Used for re-sizing of images

[Back to Contents](#table-of-contents)

# Testing

Find the full Testing Document [here!](TESTING.md)

[Back to Contents](#table-of-contents)

# Deployment

Below, is the process to deploy the site using Heroku, and to set up and store the images and static files in AWS;

## Heroku

•	Go to [Heroku](https://www.heroku.com)

•	Create an account if you don’t have one already, log in if you do

•	Create a new app, making sure to use only lower case letters and no spaces for the name

•	Choose the region closest to you and select “Create App”

<br>

•	When the app has been created, click on the “Resources” tab to add the Postgres database

•	Type in “Heroku Postgres” and select it from the dropdown list

•	This will automatically create a DATABASE_URL variable in Heroku Config Vars which can be found by clicking on the “Settings” tab, and clicking the “Reveal Config Vars” button

•	Now head over to the “Deployment” tab to set automatic deployments when pushing to GitHub

•	Set the deployment method to “GitHub” and search for your repository

•	Click “Connect”, then “Enable automatic deployments”

<br>

•	Back in your IDE, install both ‘dj_database_url’ and ‘psycopg2-binary’ in order to use Heroku Postgres

•	In your ‘settings.py’ file, comment out the existing sqlite DATABASES and add the following code;

DATABASES = {
	‘default’ = dj_database_url.parse(‘database_url_goes_here’)
}


•	Login to Heroku within your IDE by typing ‘heroku login –i’

•	Once logged in, you will need to run migrations to migrate your models to Postgres

•	In the terminal, enter ‘heroku run python3 manage.py migrate --plan’ to show what will be migrated

•	If you are happy with the migrations, enter ‘heroku run python3 manage.py migrate’

•	If you are using a JSON file with product information stores, you will need to load these to Heroku also

•	‘heroku run python3 manage.py loaddata categories’

•	‘heroku run python3 manage.py loaddata products’

•	Make sure to also create a super user so you can access the admin page by entering ‘python3 manage.py createsuperuser’

•	If you haven’t already, you will need to create a requirements.txt file and a procfile

•	Install ‘gunicorn’ and make a create your requirements.txt by entering ‘pip3 freeze > requirements.txt’ in your terminal

•	Create a procfile by entering the following into your terminal;

‘web: gunicorn name_of_your_app.wsgi:application’

•	Before committing and pushing these changes to GitHub, make sure you uncomment your ‘DATABASES’ in settings.py and amend your code to ensure your database url doesn’t get accidentally committed to GitHub!

•	Once this is done, add, commit and push your changes to GitHub


IMPORTANT!

Make sure that all of your configuration variables are up to date on Heroku such as any secret keys to ensure your app works as intended.

## AWS


[Back to Contents](#table-of-contents)

# Credits

## Code

I followed the course walkthrough project "Boutique Ado" by Code Institute which helped massively in setting up my project. 

#### Hover on menu items

https://bootstrap-menu.com/detail-basic-hover.html

#### Django Pagination

https://www.youtube.com/watch?v=N-PB-HMFmdo

https://www.youtube.com/watch?v=wY_BNsxCEi4

#### Product Reviews

For the product reviews, I had a lot of help from student Harry Dhillon who I thank immensely. 

## Images

### Favicon

https://cdn-icons-png.flaticon.com/128/1099/1099579.png

### Product Images

All product images were taken from external sources, and none of the images belong to me. Please see the [Product Image Credits](PRODUCTS.md) document for full product image credits and where I sourced them from. 

### Featured Images

#### Home Clothing Carousel Image

https://images.pexels.com/photos/3761523/pexels-photo-3761523.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940

#### Home Skate Shoes Carousel Image

https://images.pexels.com/photos/4663421/pexels-photo-4663421.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940

#### Skateboard Product Page

https://pixabay.com/photos/skater-skateboarder-skatepark-la-4618922/

#### Clothing Product Page

https://www.pexels.com/photo/woman-in-white-shirt-and-black-pants-holding-girl-in-pink-jacket-8415139/

#### Shoes Product Page

https://pixabay.com/photos/skateboard-sports-shoes-shoelaces-1150036/

#### 404/500 Pages

https://images.pexels.com/photos/6864673/pexels-photo-6864673.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940

## Acknowledgements

-	I would like to thank my mentor, Maranatha Ilesanmi, for his guidance and feedback
-	Fellow/past students within the slack community for helping me with my coding queries
-	Tutor support for the more complex queries and issues I faced in this project

## Disclaimer!

This website was developed for educational purposes only.

[Back to Contents](#table-of-contents)