# Taylor Brookes - Milestone Project 4
## Above Board Testing Document

# Table Of Contents

1. [Code Validation](#code-validation)
2. [Functionality](#functionality)
    * [Security Testing](#security-testing)
    * [Responsiveness](#responsiveness)
    * [General Functionality Testing](#general-functionality-testing)
3. [User Stories Testing](#user-stories-testing)
4. [Unresolved Issues](#unresolved-issues)

# Code Validation

## HTML5
All tests passed

## CSS3
All tests passed

## JavaScript
All tests passed

## Python
All tests passed

*Please Note* - Warnings and errors were given on most pages due to template logic being used in this project. Certain Python files also failed PEP8 checks due to base code set by Django.

# Functionality

## Security Testing
All pages were tested with a non-admin account to make sure that no access was given to those users that should not be given. This was tested by me copying the links, accessing them on an incognito browser in Google Chrome that I was not logged into, then logging into it with a non-admin user, and trying the links again. The error pops up correctly and advises the user that only admins and site owners can view that page.

## Responsiveness
The responsiveness of the site was tested using Google Chrome on a windows laptop, Safari on an Apple MacBook Pro, Google Chrome on a Samsung Galaxy S20 and S21, and Safari on an iPhone 13. I found no issues with any elements of the site when testing this.

## General Functionality Testing

### Navbar
-	Navbar is positioned at the top of the screen, and is fixed so that it is visible even when the user has scrolled down the page 
-	All links have been tested and navigate to the correct area of the site
-	When the navigation links are hovered over, they change colour as intended, and the dropdowns appear
-	Dropdown hover colours are all correct and links work 
-	Navbar correctly collapses on smaller screens including mobile view. This has been tested both on Google Chrome devtools and mobile phones
-	Overall collapsed layout is consistent with rest of the site
-	Search bar toggle works correctly
-	Site Logo displays on mobile view (bottom navbar) and is correctly hidden when on larger screens

### Navbar Search Bar
-	Focus and hover colours work correctly
-	When searching for a product on the site, it brings up all relevant products. This has been tested by using keywords for products, product categories, brands and keywords that are not relevant to products on the site
-	All correct alerts and errors are shown based on search query

### Footer
-	Footer is fixed to the bottom of all content
-	Menu links work correctly
-	Social Links open a new tab and take the user to the correct site

### Home 
-	Carousel Images and text/button overlays are nicely responsive on desktop and mobile views
-	Buttons on carousel images work correctly and navigate the user to the correct pages, and position correctly depending on screen size
-	Featured Brand section works correctly, and all products that are under that brand are displayed when the option is clicked. This has been tested by adding and editing products with those set brands and making sure the products displayed were all correct

### Products
-	Main product page images only display on certain larger screen sizes, and this has been tested by viewing the site on small screens and mobile views
-	Correct titles are displayed when the categories are selected
-	Correct sub-category buttons are displayed under each main category, and when the sub-category has been selected, the correct button shows
-	All button effects including hover have been fully tested and work correctly
-	Sort By option dropdown works correctly and I have tested all options to make sure the order of products changed depending on the criteria
-	Product displays are all correct, and should a product not have an image, the correct default image is displayed
-	Category tag links, and edit/delete links for admins all work as intended
-	When the image is clicked, the user is taken to that products individual detail page. All products work

### Product Detail
-	Breadcrumb links work as they should, and I have tested this on a range of categories to make sure it is consistent
-	Product images are all correct, and should a product not have an image, the correct default image is displayed
-	Product information is correctly shown to the user, such as price, description etc.
-	Edit/Delete buttons for admin use work and direct admin to the correct pages
-	Size dropdown box (id applicable) works correctly and if user adds that product to the bag will see the size they have selected. I have checked every product to make sure that no products show as having sizes when they shouldn’t, and vice versa
-	Quantity selector works correctly, by changing the amount of the product using the up/down arrows within the box, at the sides of the box and by using the up/down arrow keys on the users keyboard. Focus colours work as intended
-	Keep Shopping button hover works, and takes the user back to the products page
-	Add To Bag button adds the product to the users shopping bag in the correct size (if applicable) and quantity that the user has selected. This is displayed to the user by way of an on screen alert, showing a mini view of the users shopping bag. This was tested using a range of products with different sizes and quantities selected
-	Reviews section shows reviews that users have left, and allows both the user who submitted the review and the admin to edit the review
-	If user is logged in, a review form is displayed with the submit button below to submit the review form once they are done. 
-	If form is not filled in correctly, a warning will show on the section of the form that is not correct. This was tested by leaving sections of the form blank and trying to submit. All input focus colours are correct
-	If the user is not logged in, text is displayed asking the user to register or log in to leave a review. This has been tested by viewing the site in Google Chromes Incognito mode

### Shopping Bag
-	Product details are correctly displayed, including size and quantity chosen
-	Quantity selector works correctly and when the update button is clicked, the quantity updates
-	Subtotal updates based on quantity
-	Clicking the remove button removes the item successfully from the shopping bag, and updates the total cost of the shopping bag contents
-	Delivery costs are correctly amended based on shopping bag contents
-	Pricing was tested by adding and removing multiple products in the shopping bag and triggering delivery charges
-	Keep Shopping button sends the user back to the products page when clicked, and hover colours work well
-	Secure Checkout button takes the user to the Checkout page, and correctly shows products that are in the shopping bag. This includes updated quantities. Hover colours work as intended

### Checkout
-	Order Summary is correctly displayed, and shows the products that were in the shopping bag
-	Checkout form is correctly displayed to the user
-	If the user is logged in, checkbox is displayed for the user to save this address to their profile. If they click this checkbox and the order is completed, the delivery details are added to the profile page
-	If user is not logged in, options to register or log in are displayed instead. These links work
-	I have tested this by creating new accounts, checking this box and checking the profile page after completing the order
-	Stripe default card number used for payments. No payment issues found
-	If incorrect card details are entered, an error is displayed to the user
-	If part of the form is left empty the order will not process and takes the user to the empty section of the form
-	Back to bag button works as intended. Hover colour works and if clicked, takes the user back to the shopping bag
-	Complete Order Securely button works and processes the order and payment for the user. Button colours are correct and hover effects work

### Checkout Success/Order History
-	Order information is displayed correctly
-	If user has reached this page from the checkout, a button to view other products will be displayed. This navigates the user to the products page
-	If user has reached this page from their profile, a back to profile button will instead be displayed. Again this works fully

### Sign Up
-	Sign Up page allows a user to register an account using their email address
-	It will then send the user an email to confirm their email address and complete the registration process
-	Once the user has confirmed their email, they can log in and use the site as a registered user
-	I have tested this by creating a number of accounts with different email addresses, all worked as predicted

### Sign In
-	Allows the user to sign in using the email address or username they signed up with and the password they chose
-	A checkbox can be ticked that will save the users information for future visits
-	If a user has forgotten their password, the option is there for them to click it, and run through the forgotten password journey that allows them to reset it. This has been tested with multiple accounts and works
-	If no user exists with those details, an error will display above the log in form to inform the user of that

### Profile
-	Order history display is correct and shows a preview of past orders
-	If the order number is clicked, it takes the user to the Order History page
-	Default Delivery Information form works as intended, and auto-fills if it has been selected in the checkout process
-	Updating the address works correctly, and is reflected both on the profile page and the checkout

### Product Add/Edit
-	Crispy form correctly displays all inputs
-	If editing a product, form is correctly pre-filled with existing information
-	Removing an image works as intended
-	Adding an image works as intended
-	Cancel button hover colour is correct, and takes admin back to the products page
-	Add product button successfully adds a product to the site, and auto directs the admin to the product details page of the product they have just added
-	Edit product button successfully amends the product information and/or image, directs the admin to the product details page and displays the edited information 

### Help & Guidance
-	Add Post button is correct style, and if clicked, directs the admin to the add post page
-	Post displays are all correct, and should a post not have an image, the correct default image is displayed
-	View Post button directs the user to the correct post details page
-	If the image is clicked, it also directs the user to the post details
-	Pagination is used in this part of the site, and works as intended. I have tested this by creating many posts and checking that the pagination works

### Help & Guidance Post Detail
-	Post displays are all correct, and should a post not have an image, the correct default image is displayed
-	Edit/Delete buttons for admin work correctly and take the admin to the edit page/delete the post from the site
-	Back button takes the user back to the main Help & Guidance page

### Help & Guidance Add/Edit Post
-	When adding a post, form is correctly displayed empty and allows the user to input the relevant information
-	If editing a post, form is correctly pre-filled with existing information
-	Adding and removing images works as intended
-	Cancel button hover colour is correct, and takes admin back to the posts page
-	Add post button successfully adds a post to the site, and auto directs the admin to the post details page of the post they have just added
-	Edit post button successfully amends the post information and/or image, directs the admin to the post details page and displays the edited information 

### 404/500 Pages
-	I have tested these pages by initiating the error codes
-	The page displays as it should, with the correct text depending on the error
-	Back To Home button directs the user back to the home page
-	Image displays correctly

# User Stories Testing

## Common User Stories

*To be able to easily navigate through the site on any size screen*
-	Full responsiveness has been tested thoroughly and all screen sizes are fully working

*Search for products*
-	Search bar can be used for searching by product name, category or keyword
-	This has been tested by using all of the above to search for set products. All products came up as expected

*Sort products by Price, Name etc.*
-	Sort By dropdown works and correctly displays products in the order the user has selected

*View product details*
-	Each product has a set product detail page. This shows all product information including description of product, and product reviews left by users

*Ability to choose quantity of items, and size if applicable*
-	Size dropdown displayed on all relevant products, and works correctly when product is added to the shopping bag
-	Product quantity works correctly and when product is added to the shopping bag, quantity is reflected

*Able to purchase products without an account*
-	Users are allowed to go through the entire site purchase process without the need for an account, although it is suggested at different stages to create an account

*View their shopping bag and amend their order*
-	Shopping Bag icon is always displayed on the navbar, even on a collapsed view so that users have easy access to the shopping bag at all stages of the site

*View Posts in Help & Guidance section*
-	Posts are displayed in the Help & Guidance section, and are displayed from newest post to oldest. Pagination is put to use here in case there are many posts to save users from having to scroll through many posts without knowing when they end

*Contact the company with any queries or if an issue occurs*
-	Contact number, email and address are provided in the footer of the site which is displayed on every page

## First Time Users

*Understand the purpose of the site*
-	Users are shown an About Above Board section on the home page 
-	There is a brief version of this in the footer

*See the reasons behind registering for an account*
-	This is also explained in the About Above Board section on the home page

*Being able to easily sign up for an account*
-	Sign in flows easily and it takes very little time to set up a secure account

## Returning Users

*Ability to securely log into their account*
-	Account log in is set up by Django and is extremely secure
-	Log in process is very quick, and allows a user to save their log in details for next time

*View their past orders and order confirmations*
-	When a user is logged in, if they navigate to the profile page they will be given their Order History
-	It will be a brief overview of the users past orders, but if they click on the order number it will take them to the order confirmation page
-	This is a historic order confirmation page, but displays all the necessary information that a user would need

*Purchase products and have their orders saved to their profile*
-	All users, regardless of logged in status, will be able to purchase products through the site
-	If a user is logged in when the process an order, it will be displayed on their profile order history

*Receive their order confirmations directly to their email inbox*
-	When a user completes an order, they will receive an email to confirm said order
-	This goes directly to the email address provided
-	I have tested this by using different email addresses from different providers, and all worked

*Leave reviews of products*
-	Logged in users are able to leave product reviews
-	On the product details page, reviews are displayed below the main product information display
-	User reviews are displayed at the top, and the review form is below them

## Site Owner/Admin

*Provide a clean, simple e-commerce store so that users can easily find what they’re looking for*
-	I have tested this by asking friends and family to view the site with no direction, and the feedback I have received has been positive
-	Users were easily able to search for what they wanted, find from product lists what they wanted, and successfully purchase products

*Have the ability to add, edit/update and delete products/posts*
-	Add, Edit/Update and Delete functions all work correctly with no errors
-	After editing, correct information is displayed on the site
-	Deleting a product deletes it from the site entirely, including reviews that have been left, and removing it from the admin view

*Keep the site secure by only allowing authorised users access certain areas of the site*
-	Full site authorisation has been implemented by using Djangos `@login_required`
-	This has been tested extensively to make sure no unauthorised access is given at any stage of the site

*Securely store user information in case an error occurs*
-	User information is stored securely using Django. Only information provided is kept, but does not include passwords for security reasons

# Unresolved Issues

I have been incredibly lucky during production and have not encountered many issues/bugs when creating this project. I do however have a few outstanding issues that I am yet to resolve. 

## Product reviews linked to product ratings.

I have implemented product reviews on my site, however I was unable to figure out a way to link these up to display as an average rating for the product the reviews are for. I attempted this by following tutorials but was unable to make this work.

## Product Fixtures.

As I wanted to display each shoe brand separately I created them as separate categories. This made some future developments rather difficult to navigate on my site as I essentially need to rebuild my fixtures, but did not want to edit them at a late stage in my project.
-	Pagination :- This was not something I could implement on Products pages due to the set up of my fixtures. I followed a few tutorials (which successfully worked for my Help & Guidance section) but they were not successful on my product pages

### Keep Shopping buttons.

I would like these buttons to take the user back by one page, but could not find a fix for this.