# Taylor Brookes - Milestone Project 4
## Above Board

[Visit my live website here!](https://aboveboard-ms4.herokuapp.com/)

![Site preview](media/readme/site-view.png)

# Table Of Contents

1. [Overview](#overview)
2. [UX - Five UX Planes](#ux---five-ux-planes)
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
    * [Heroku](#heroku)
    * [AWS](#aws)
7. [Credits](#credits)

# Overview

Above Board is an e-commerce site used for educational purposes, and I have focused on Skateboarding for the theme of my project. 

You’ll find the essential products you’d need to start or continue skating, from complete decks, trucks and wheels, to t-shirts, hats and skate shoes. The Help & Guidance section provides information on how to start skating, useful links and more!

[Back to Contents](#table-of-contents)

# UX - Five UX Planes

## Strategy

### Target Audience
The target audience of my site is people who are looking to purchase skateboards, skateboarding hardware or clothes. It is geared towards both current and new skaters, and includes products for both of these types of customer. 

### Business Goals
-	To provide an easily navigable e-commerce site
-	Connect with users via social media and through blog posts
-	Making a profit by selling products

### User Stories
### Common User Stories
-	To be able to easily navigate through the site on any size screen
-	Search for products
-	Sort products by Price, Name etc.
-	View product details
-	Ability to choose quantity of items, and size if applicable
-	Able to purchase products without an account
-	View their shopping bag and amend their order
-	View Posts in Help & Guidance section
-	Contact the company with any queries or if an issue occurs

### First Time Users
-	Understand the purpose of the site
-	See the reasons behind registering for an account
-	Being able to easily sign up for an account

### Returning Users
-	Ability to securely log into their account
-	View their past orders and order confirmations
-	Purchase products and have their orders saved to their profile
-	Receive their order confirmations directly to their email inbox
-	Leave reviews of products

### Site Owner/Admin
-	Provide a clean, simple e-commerce store so that users can easily find what they’re looking for
-	Have the ability to add, edit/update and delete products
-	Have the ability to add, edit and delete blog posts
-	Keep the site secure by only allowing authorised users access certain areas of the site
-	Securely store user information in case an error occurs

---

## Scope

The following features were implemented to reflect the user stories. For a full list of features please see the [Features](#features) section.
-	Clear and fully responsive site design and navigation
-	Detailed Product pages 
-	Working and secure payment system
-	Secure authorisation 
-	Profile page
-	Full admin access
-	404/500 pages set up for if errors occur

---

## Structure

The structure of my site is shown below. I outline the apps I have, and what HTML files and Models sit within those apps to make my site work;

### Home App 

**HTML files**

index.html
- This is the main page of my site. There is a carousel with two images and links to products on the site; Clothing and Skate Shoes. Below that is a Brand display section which highlights some of the popular brands that are stocked on the site. Towards the bottom of the page is an “About Above Board” section that overviews what the site is about, and a great incentive for registering for an account. 

### Products App

**HTML files**

add_product.html
- Template that contains a form to add a product. Only the admin has access to this page.

edit_product.html
- Similar template and form as the one to add a product, but allows the admin to edit an existing product.

product_detail.html
- Displays the Product detail page to the user. Shows the Product name, image, description, price, SKU and size (if applicable) and quantity options. The user is also given the option to add this product to their shopping bag in their size and quantity of choice. At the bottom of this page is a review section. This is where logged in users can leave a review of the product. 

products.html
- Displays a list of Products that are available to purchase to the user. The Products displayed on this page will differ depending on which Category, Brand or specified search query the user is searching by. If none have been selected, it will display all Products available on the site.

**Models**

Category
- Stores the Product categories.

Product
- Stores individual Product information.

Brand
- Stores the Product brands.

ProductReview
- Stores Product Reviews left by users.

### Bag App

**HTML files**

bag.html
- Users can view their shopping bag contents here, make changes to quantities of products and continue securely to the checkout page.

### Checkout App

**HTML files**

checkout.html
- Displays the final checkout page to the user. They can view their order via a summery, and complete a form with their personal details on so they can have the product/s delivered to them. This is where they will be asked to input their payment information, and once the “Complete Order Securely” button has been clicked, payment will be taken and the order processed. A warning note is placed below this button to warn users of this. 

checkout_success.html
- This is a confirmation page, and one that will be shown to the user upon successful completion of an order. Here will be the order confirmation summary, with all of the details of the order and the personal details the user put in on the page prior. 

**Models**

Order
- Holds information of each order, and is created when a user completes the checkout. 

OrderLineItem
- Contains information of each product added to the bag. 

### Profiles App 

**HTML files**

profile.html
- Displays the users profile to the user. Contains their saved personal details and order history. Only accessible by someone who is registered to the site. 

**Models**

UserProfile
- This model securely stores information on each user. Information is pulled from this Model to pre-fill the personal information form on the checkout page if the user is logged in, and has information saved. 

### Help App

**HTML files**

add_post.html
- Template that contains a form to add a post. Only the admin has access to this page.

edit_post.html
- Similar template and form as the one to add a post, but allows the admin to edit an existing post.

help.html
- This page displays all of the posts that have been created on the site. Pagination is used in this section to limit the number of posts per page, which is set to four. 

post_detail.html
- Page to display the full post details. 

**Models**

HelpGuidance
- This Model stores information on each Post made. 

---

## Skeleton

### Wireframes

<details>
<summary>Home</summary>

![Desktop Wireframe](media/wireframes/home-desktop.png)
![Mobile Wireframe](media/wireframes/home-mobile.png)

</details>

<details>
<summary>Products</summary>

![Desktop Wireframe](media/wireframes/products-desktop.png)
![Mobile Wireframe](media/wireframes/products-mobile.png)

</details>

<details>
<summary>Product Detail</summary>

![Desktop Wireframe](media/wireframes/product-detail-desktop.png)
![Mobile Wireframe](media/wireframes/product-detail-mobile.png)

</details>

<details>
<summary>Shopping Bag</summary>

![Desktop Wireframe](media/wireframes/shopping-bag-desktop.png)
![Mobile Wireframe](media/wireframes/shopping-bag-mobile.png)

</details>

<details>
<summary>Checkout</summary>

![Mobile Wireframe](media/wireframes/checkout-desktop.png)
![Desktop Wireframe](media/wireframes/checkout-mobile.png)

</details>

<details>
<summary>Checkout Success/Order History</summary>

![Desktop Wireframe](media/wireframes/checkout-success-desktop.png)
![Mobile Wireframe](media/wireframes/checkout-success-mobile.png)

</details>

<details>
<summary>Sign Up</summary>

![Desktop Wireframe](media/wireframes/signup-desktop.png)
![Mobile Wireframe](media/wireframes/signup-mobile.png)

</details>

<details>
<summary>Sign In</summary>

![Mobile Wireframe](media/wireframes/signin-desktop.png)
![Desktop Wireframe](media/wireframes/signin-mobile.png)

</details>

<details>
<summary>Profile</summary>

![Desktop Wireframe](media/wireframes/profile-desktop.png)
![Mobile Wireframe](media/wireframes/profile-mobile.png)

</details>

<details>
<summary>Product Management</summary>

![Desktop Wireframe](media/wireframes/product-add-desktop.png)
![Desktop Wireframe](media/wireframes/product-edit-desktop.png)
![Mobile Wireframe](media/wireframes/product-add-mobile.png)
![Mobile Wireframe](media/wireframes/product-edit-mobile.png)

</details>

<details>
<summary>Help & Guidance</summary>

![Desktop Wireframe](media/wireframes/help-and-guidance-desktop.png)
![Mobile Wireframe](media/wireframes/help-and-guidance-mobile.png)

</details>

<details>
<summary>Help & Guidance Management</summary>

![Desktop Wireframe](media/wireframes/help-and-guidance-add-desktop.png)
![Desktop Wireframe](media/wireframes/help-and-guidance-edit-desktop.png)
![Mobile Wireframe](media/wireframes/help-and-guidance-add-mobile.png)
![Mobile Wireframe](media/wireframes/help-and-guidance-edit-mobile.png)

</details>

<details>
<summary>404/500 Pages</summary>

![Desktop Wireframe](media/wireframes/404-500-desktop.png)
![Mobile Wireframe](media/wireframes/404-500-mobile.png)

</details>

---

## Surface

### Colours

The following colours were the main colours I used for my site;

![Colours Used](media/readme/colours.jpg)

White
- This was the background colour used for all of my pages. I didn't want any other colours as it would have detracted from the bright colours I had chosen for the other sections of each page. White was also used for the main logo on desktop view, and as a hover colour for certain buttons across the site.

Black
- I used black as the colour of the text. As I had a white background I chose black to stand out the most. The other colours I chose were being used for emphasis so I didn't want to overuse them. 

Red Orange Colour Wheel
- This colour was used as the primary colour throughout my site. It was used for the top navbar, primary buttons and for emphasis throughout the site. This colour was also used as an overlay on the carousel image for Skate Shoes, which I edited in Adobe Photoshop.

Mikado Yellow
- Mikado Yellow was used as the secondary colour on my site. It went extremely well with the shade of Orange I had chosen, and was bright which was what I wanted. I coloured the bottom navbar with Mikado Yellow, as well as the secondary buttons, and hover colour for certain buttons. 

### Other Colours

Antique White
- This was used as the background for the review section on the Product Details pages. I wanted the review section to stand out from the rest of the page so chose this colour as it was subtle enough to not detract from the colours already chosen, but also complimented them.

### Typography



### Imagery



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

---

•	When the app has been created, click on the “Resources” tab to add the Postgres database

•	Type in “Heroku Postgres” and select it from the dropdown list

•	This will automatically create a DATABASE_URL variable in Heroku Config Vars which can be found by clicking on the “Settings” tab, and clicking the “Reveal Config Vars” button

•	Now head over to the “Deployment” tab to set automatic deployments when pushing to GitHub

•	Set the deployment method to “GitHub” and search for your repository

•	Click “Connect”, then “Enable automatic deployments”

---

•	Back in your IDE, install both `dj_database_url` and `psycopg2-binary` in order to use Heroku Postgres

•	In your `settings.py` file, comment out the existing sqlite DATABASES and add the following code;
```
DATABASES = {
	‘default’ = dj_database_url.parse(‘database_url')
}
```

---

•	Login to Heroku within your IDE by typing `heroku login –i`

•	Once logged in, you will need to run migrations to migrate your models to Postgres;

•	In the terminal, enter `heroku run python3 manage.py migrate --plan` to show what will be migrated

•	If you are happy with the migrations, enter `heroku run python3 manage.py migrate`

•	If you are using a JSON file with product information stored, you will need to load these to Heroku also by entering the following into your terminal;

`heroku run python3 manage.py loaddata categories`

`heroku run python3 manage.py loaddata products`

•	Make sure to also create a super user so you can access the admin page by entering `python3 manage.py createsuperuser`

•	If you haven’t already, you will need to create a `requirements.txt` file and a `procfile`

•	Install `gunicorn` and make a create your `requirements.txt` by entering `pip3 freeze > requirements.txt` in your terminal

•	Create a `procfile` by entering the following into your terminal;

`web: gunicorn name_of_your_app.wsgi:application`

•	Before committing and pushing these changes to GitHub, make sure you uncomment your `DATABASES` code in `settings.py` and amend your code to ensure your database url doesn’t get accidentally committed to GitHub!

•	Once this is done, `add`, `commit` and `push` your changes to GitHub

---

IMPORTANT!

Make sure that all of your configuration variables are up to date on Heroku such as any secret keys to ensure your app works as intended! Your Config Variables should look similar to this (These variables also include ones for AWS which the following section will go over);

| Key                   | Value                    |
| --------------------- |--------------------------|
| AWS_ACCESS_KEY_ID     | `aws_access_key`         |
| AWS_SECRET_ACCESS_KEY | `aws_secret_access_key`  |
| DATABASE_URL          | `auto-generated`         |
| EMAIL_HOST_PASS       | `email_key`              |
| EMAIL_HOST_USER       | `your_email`             |
| SECRET_KEY            | `secret_key`             |
| STRIPE_PUBLIC_KEY     | `your_stripe_public_key` |
| STRIPE_SECRET_KEY     | `your_stripe_secret_key` |
| STRIPE_WH_SECRET      | `stripe_webhook_key`     |
| USE_AWS               | `True`                   |

---

## AWS

### Setting Up

1. Go to AWS and set up an account if you don’t already have one. You will be asked to enter credit/debit card details, but whilst you are using the free tier you should not need to make any payments. Please keep an eye on your usage though to avoid any charges!

2. Log in to AWS, and navigate to S3. You can search for “S3” in the search bar at the top of the screen. 

3. Create a new bucket by clicking on the orange “Create Bucket” button. 

4. Make sure that your bucket name matches the name of your app on Heroku, and that you select the region closest to you. 

5. Scroll down to “Block Public Access settings for this bucket” and uncheck the checked box. Confirm that you are happy to do this, then scroll to the bottom of the page and click the orange “Create Bucket” button. You will be taken to your bucket dashboard, and from here, you will need to make some amendments to your bucket. 

---

### Bucket Properties

1. Click on the “Properties” tab and scroll down to the bottom of the page, where you will find a “Static website hosting” section. Click on the edit button.

2. The top section will allow you to choose between “Disable” or “Enable”, and you will want to select “Enable” to enable static website hosting. 

3. The section below is “Hosting Type”. Select “Host a static website” and scroll down to the “Index Document” inputs. 

4. It will first ask you to specify the home or default page, which is `index.html`

5. It will then give you the option of entering an error link for if an error occurs. In the input, type `error.html`

6. Leave the Redirection rules blank, and click the orange “Save Changes”. 

---

### Setting Permissions

1. Next, click on the “Permissions” tab, scroll to the bottom of the page and click edit in the “Cross-origin resource sharing (CORS)” section. 

2. Add in the following code, making sure to use correct indentation;

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

3. Click on the orange “Save Changes” button and navigate to the “Bucket Policy” section which will be near the top of the page, and click edit. 

---

### Generating A Bucket Policy

1. Click on the “Policy Generator” button. This will open a new window. 

2. Within that new window will be a series of steps. For step one, you will need to select “S3 Bucket Policy from the dropdown list.

3. In step two, you will need the following options set;

    - Effect – Allow
    - Principle - *
    - Actions – GetObject, GetObjectAcl, PutObject, PutObjectAcl and DeleteObject
    - Amazon Resource Name (ARN) – This will be found on the previous page, under “Bucket ARN”. Copy this and paste it into this box

4. After these have been entered, click “Add Statement” then “Generate Policy”.

5. Copy the policy into the bucket policy editor, adding `/*` onto the end, the click “Save Changes”.

---

### Access Control List (ACL)

1. Staying in the permissions tab, click edit under the “Access Control List (ACL)” section. 

2. You will be shown a series of options and tick boxes. Navigate to “Everyone (public access)” and tick the box on the left, “List” under the “Objects” heading. You will need to agree that you understand the effects before you can save, so tick that, then click on “Save Changes”.

---

### IAM - Creating A Group and Policy

1. Next, search for IAM in the search bar at the top, and click on it to set up a group policy.

2. Under “Access Management” on the left hand side, click on “User Groups” and create a new group.

3. Give the group a name and click “Create Group”. 

4. This will take you back to the IAM dashboard. Go back to the “Access Management” section on the left hand side, and click on “Policies”. 

5. Click “Create Policy” and head over to the JSON tab, and select “Import Managed Policy”. 

6. Search for and click on “AmazonS3FullAccess” then “Import”.

7. Copy your ARN and place it in the code so that it looks like the below;

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR-ARN",
                "arn:aws:s3:::YOUR-ARN/*"
            ]
        }
    ]
}
```

8. Click on “Next: Tags”, “Next: Review”, put in a name and click on “Create Policy”. 

---

### Group Policy

1. Next, you will need to attach the Policy to the Group created.

2. Go to “User Groups” on the left hand side menu, under “Access Management”.

3. Click on the your newly created group and go over to the “Permissions” tab.

4. Click on the “Add Permissions” button, and select “Attach Policy”.

5. Search for and click on the checkbox next to the policy you have just created, then click “Add Permissions”.

---

### IAM - Create User

1. Back at the IAM dashboard, click on “Users” on the left hand side menu, then “Add User”.

2. Choose a name and tick the checkbox to give the user access, then click “Next: Permissions”.

3. Select the group to put the user in and keep clicking the next buttons until the very end and click “Create user”.

4. Click on “Download .csv” file and make sure you save this somewhere you remember, as you will not have access to this page again! This file will contain information such as your access codes (shown above in the Heroku Deployment section).

---

### **Important!**

Make sure to also update your settings.py file to reflect the changes to the database! It should look something like this;

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

---

### Saving Images To S3 Bucket

If you need to save images to your S3 bucket, you will need to do the following;

1. Go back to the S3 dashboard, and click on your bucket. 

2. Click “Create Folder”, call it ‘media’ and confirm with the second “Create Folder” button.

3. When you are in this folder, click “Upload”, then “Add Files” or “Add Folder”, then “Upload”.

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