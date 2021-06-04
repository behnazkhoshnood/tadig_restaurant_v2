# **Milestone Project 4**
**Full-Stack Frameworks with Django Milestone Project.**

**Tadig Restaurant**

[View the live project here.]()
This website is made for restaurants. We named our restaurant "Tadig restaurant" which is a made-up Persian restaurant.
It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential customers.

## **Contents** ##
* UX
    * [Project Summary](#project-summary)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
* [Wireframes](#wireframes)
* [Features](#features)

* [Technologies](#technologies)
* [Testing](#testing)
* [Fixed Issues](#fixed-issues)
* [Deployment](#deployment)
* [Credit](#credits)

## **UX (User Experience)** ##

### **Project Summary** ###

The main purpose of this project is to build a full-stack site based on business logic used to control a centrally-owned dataset.
By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
The site owner can make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

### **User Stories**

#### **As a Site Users**

- **Registration and User Account**
  - I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
  - I want to be able to easily log in and logout, so that I can access my personal account information.
  - I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
  - I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
  - I want to be able to have a personalized user profile so that I can view my order history and order confirmations and save my payment information.
  - I want to be able to see each product review so that I can easily choose the meal(product), based on the comments and reviews.
  - I want to be able to add a review so that I can share my thoughts with other customers and the owners of the restaurant.
  - I want to see a list of my favourite dishes or drinks so that I can order them again or find them in my wishlist page.

#### **As a Shopper**

- **Viewing and Navigating**
  - I want to be able to view a list of products so that I can select some to purchase.
  - I want to be able to view individual product details so that I can identify the price, description, product rating, and product image.
  - I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much.

- **Sorting and Searching**
  - I want to be able to sort the list of available products, so that I can easily identify the best rated, best priced, and categorically sorted products.
  - I want to be able to sort a specific category of product so that I can find the best-priced product in a specific category, or sort the products in each category.
  - I want to be able to sort multiple categories of products simultaneously so that I can find the best-priced products.
  - I want to be able to search for a product by name, category, or description so that I can find a specific product I'd like to purchase.
  - I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.

- **Purchasing and Checkout**
  - I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity.
  - I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
  - I want to be able to adjust the number of individual items in my bag so that I can easily make changes to my purchase before checkout.
  - I want to be able to easily enter my payment information so that I can check out quickly and with no hassles.
  - I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
  - I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
  - I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.

#### **As a Store Owner**

- **Admin and Store Management**
  - I want to be able to add a product so that I can add new items to my store.
  - I want to be able to edit or update a product so that I can change product prices, descriptions, images, or other product criteria.
  - I want to be able to delete a product so that I can remove items that are no longer available.

### **Design choices**

  The goal in design was to create a website that is overall user friendly, has a modern feel with emphasis on providing information about the restaurant dishes/drinks in a readable and eye-catching way. Therefore, the following design choices were made:
- **Framework**
  * Front-end framework, [Bootstrap](https://Bootstrap.com/),  based on bootstrap Design was chosen for this project for its modern interface and ease of use.

  * [JQuery](https://jquery.com/) was used for initializing some bootstrap elements.

- **Typography**
  - I used [Google Fonts](https://fonts.googleapis.com/css?family=Lato&display=swap") for the font style of my project:
    - The font I have used for this project is called **Lato** and sans-serif as a backup font.

- **Icons**
  - I used [Favicon](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/) to make a unique brand for my website.
  - I used [FontAwesome]() as the main icon library across the project (e.g. for forms and buttons).

- **Colour Scheme**

  The idea of using different shades of the same color is implemented across the website. The primary color used for the main buttons and headings is deep purple as it seems to create a nice contrast with white backgrounds. The secondary color used for icons, dividers, and some other buttons is blue and pink.

  - **Main color palette**

    - Main colors that have been used are black and white and some shades of gray due to their high contrast which complement the colorful images.
    - For toast messages headers and some labels I used the bootstrap scheme:
        - Success: #28a745; which is a shade of green color.
        - Danger: #dc3545; which is a shade of red color.
        - Primary: #007bff; which is a shade of blue color.
        - secondary: #6c757d; which is a shade of gray color.
        - warning: ##ffc107; which is a shade of yellow color.
        - info: #17a2b8; which is a shade of blue color.
        - light: #f8f9fa ; which is a shade of light gray color.
        - dark: #343a40; which is a shade of dark gray color.
---
## **Wireframes**
[Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create all wireframes for the project.

---
 #### <center>Home Page<center>
---
Desktop view | Mobile view
- | -
![Home page-desktop](media/home-page-desktop.png) | ![Home-page-mobile](media/home-page-mobile.png)
---
 #### <center>Product details page<center>
---
Desktop view | Mobile view
- | -
![Product details page-desktop](media/product-details-page-desktop.png) | ![Admin](media/product-details-page.png)
---
 #### <center>Products page<center>
---
 Desktop view | Mobile view
- | -
![products-page-not-admin-desktop](media/product-page-not-admin-desktop.png) | ![products-page-not-admin-mobile](media/products-page-mobile.png) 
---
 #### <center>Shopping bag page<center>
---
 Desktop view | Mobile view
- | -
![shopping-bag-page-desktop.png](media/shopping-bag-page-desktop.png) | ![shopping-bag-page](media/shopping-bag-page.png)
---
 #### <center>Checkout page<center>
---
Desktop view | Mobile view
- | -
![checkout-page-desktop](media/checkout-page-desktop.png) | ![checkout-page-mobile](media/checkout-page-mobile.png)
---
 #### <center>Checkout success page<center>
---
 Desktop view | Mobile view
- | -
![checkout-success-page-desktop](media/checkout-success-page-desktop.png) | ![checkout-page-mobile](media/checkout-page-mobile.png)
---
 #### <center>Profile page<center>
---
 Desktop view | Mobile view
- | -
![profile-page-desktop](media/profile-page-desktop.png) | ![profile-page-mobile](media/profile-page-mobile.png)
---
 #### <center>wishlist page ( Only Admin)<center>
---
Desktop view | Mobile view
- | -
![wishlist-page-desktop](media/wishlist-page-desktop.png) | ![wishlist-page-mobile](media/wishlist-page-mobile.png)
---
 #### <center>Log In<center>
---
 Desktop view | Mobile view
- | -
![sign-in-page-desktop](media/sign-in-page-desktop.png) | ![sign-in-page-mobile](media/sign-in-page-mobile.png)
---
 #### <center>Register<center>
---
Desktop view | Mobile view
- | -
![register-page-desktop](media/register-page-desktop.png) | ![register-page-mobile](media/register-page-mobile.png)
---
 #### <center>Log OUt <center>
---
 Desktop view | Mobile view
- | -
![log-out-page-desktop](media/log-out-page-desktop.png) | ![log-out-mobile](media/log-out-mobile.png)
---
 #### <center>Add product page ( Only Admin)<center>
---
Desktop view | Mobile view
- | -
![add-poduct-page-only-admin](media/add-poduct-page-only-admin-desktop.png) | ![add-product-page-admin-mobile](media/add-product-page-admin-mobile.png)
---
 #### <center>edit review page ( Only Admin)<center>
---
Desktop view | Mobile view
- | -
![edit-page-desktop](media/edit-review-page-desktop.png) | ![edit-review-mobile](media/edit-review-mobile.png)
---

## **Features**
- **Implemented features**
  - **Common features in all pages**
    - All of the pages contain a 3 part layout with the header, main part of the page, and the footer.
        - **Header**
            - **main navbar**
                - Main navbar is dividing the products that are provided into different categories of appetizers, main dishes, desserts, and beverages and a sorting dropdown button.
                on medium and large screens, the main navbar is fixed on top of the page and is lined up in a line. On smaller screens, this navbar turns to a dropdown navbar.
                - Another item in this navbar is "Sort" which sorts all the products by their name, price, or category.
            - **Home button**
               - On medium and large screens restaurant logo works as the home button but on smaller screens, the home button is added to the dropdown navbar.
            - **Search, Account and Bag**

                In all views, the search area, account, and bag are fixed on top of the page.

                **Search**

                - Customers can search for the name, category, or any word from a product description to easily find them, 
                - By clicking on the search icon, the search result and the number of the search result will be shown under the search area.
                - If the file is empty when the search icon is clicked a toast message appears on the top right corner of the page and notifies the user.

                **Account**

                - Account is a dropdown button that contains the *register* , *logout*, *Login* for all the users.
                - *Wishlist* and *Profile* are added to this list for registered users.
                - Admin or superuser access an extra button from here which is called *Manage Products*, which is used to add new products to the list of products.

                **Bag**

                - This shows the total amount of the products added to the shopping bag and placed on the top right corner.

                **Delivery Banner**
                - This part will notify the user that by shopping more than 200 KR, which is the free delivery threshold, they would earn the free delivery.

        - **Footer**

            Footer is divided into 3 parts. *Social*, *Contacts* and *Copyright*, which are located at the bottom of the pages.
            **Social** contains Facebook, Twitter, and Instagram.
            **Contacts** contains the address, phone number, opening time, and email address of the restaurant.
            these parts are positioned under each other in small views and in medium and larger views contacts and social are positioned side by side and copyright is positioned under them.
---
  - **Home Page**

    - The home page contains the eye-catching carousel slide with colorful images that make the purpose of the website clear from the beginning.
    - Brief information about the restaurant is provided to the left side of the carousel on medium and large screens and smaller screens, this information is placed on top of the carousel.
    - Carousel is showing all the product images. By clicking on each image user is directed to the product details page, which shows that product, all the information related to it, and can add it to the back right away.
    - Under the about note and carousel, all the reviews that have been added for any product are displayed with their name, average rating, and the number of rates.
---
  - **Products Pages**

    - By clicking on the main navbar categories in the top header, users are directed to the respective category page, which has the name, image, price, number of reviews, and average rating information of all products in that category.
    - user also have the option to add the product to their wishlist by clicking on the heart icon positioned in the top right conrer of the images.
    - Under the price of each product is also a form that users can use to add any product in this category to their shopping bag.
    - When a user adds a product to their shopping bag they will be notified by a toast message on top of the page, which shows that product information.
    - If the price of the items is lower than the free delivery threshold, it will show in this toast message that how much more they should add to their bag to get the free delivery.
    - User is informed with the header on top of the page that by clicking on product images they get more information about that product.
    - when clicking on the product image user is redirected to the product details page which has the description of that product.
    - Sorting only in each specific category is also possible by the sorting dropdown input provided on top of this page, which can sort the products based on their price, rating, or name.
    - There is also a scroll back to the top button is provided on this page, to easily go back to the top of the page.
    - On medium and larger views the product info and image are positioned side by side but on smaller views, they are placed under each other.
    - Admin or superuser provided with extra links under each product price to either delete or edit that product.
---
  - **Product Details Page**

    - This page shows the product name, price, average rating, image, and description.
    - user also have the option to add the product to their wishlist by clicking on the heart icon positioned in the top right conrer of the image.
    - A form to add this product to the shopping bag is located under the product price.
    - By choosing the amount, and then clicking on Add to Bag, the user will see a toast message on top of the page that shows the product information in their bag.
    - If the total product value is lower than the delivery threshold, the user will be notified of the amount that they should spend more to get free delivery in the toast message.
    - The toast message also provides the user with a button to be redirected to their shopping bag.
    - under the product details and image there is a review form for the product with a comment and rating inputs and submit button.
    - All the reviews for this product are shown including the name of the user, rating, and their respective comments.
    - User can also edit or delete their reviews from this section.
    - on small screens, the product information, shopping, and quantity buttons review form and reviews are placed under each other, but in medium and larger views they are placed side by side.
    - Admin or superuser provided with extra links under the product price to either delete or edit this product.
---
  - **Edit review form**

    - If user added any reviwes to a product they can see it in the reviews section of that product and are able to edit or delete that review.
---
  - **Shopping Bag Page**

    - user can easily reach this page by clicking on the bag icon on the top right corner of all pages or on the notification toast that they will see on top of the products and products details, after clicking on the add to bag button.
    - If a user has any product in their shopping bag, they can review them on this page.
    - Users can easily update the amount or remove the products in their bag, on this page.
    - The amount on Total shopping, delivery fee, and the total is shown under this page with two buttons.
    - One button is to redirect the user to the products page, to order something more, and the other redirects the user to the checkout page.
    - If there isn't any product in the shopping list, the user will be notified that the bag is empty and get the option to be redirected to the products page.
    - In small views, the total price and secure checkout button are placed on top of the page, and the chosen products and their details are placed under the buttons.
    - In larger views, the product information is placed on top of the billing information and the checkout button.
---
  - **Checkout Page**

    - By clicking on the secure checkout button on the shopping bag page, the user will be redirected to the checkout page.
    - On this page users can see the summary of their order, and a form to fill in the information required for the delivery.
    - by filling this form and clicking on the *Complete Order* button, the user can securely purchase from the site with the help of stripe elements.
    - On x-small screens order summary is placed on top of the order form and under the form there is the *Complete Order* button and *Adjust Bag*.
    - Product images are not seeable in the x-small views to improve the page layout.
    - On small and larger screens the order summary and form are placed side by side and the complete order and adjust bag buttons are at the bottom of the page.
---
  - **Checkout Success Page**

    - After completing the order form and click on the complete order button, on the checkout page, the user will see a nice overlay for a short time until the process of shopping completes.
    - User then will be redirected to the checkout success page and see a toast message on top of the page, notifying the user that the order is processed, the order number.
    - User also receives a confirmation email to their email address.
    - On this page, all the order information is shown to the user, including the order number and date, purchased products and the price for each product, delivery information, and the total amount of the purchase.
---
  - **Profile Page**

    - Profile user is only accessible for registered users.
    - If a non-registered user tries to go to the profile page by writing it in the browser he/she will be redirected to the sign-in page.
    - Registered users have an access to their profile in the account dropdown button, in the header.
    - On the profile page, there is an information form that can be filled.
    - The first time that the user completes an order this information will be filled in automatically.
    - User can update this information on the profile page, by filling the form and click on the update information button.
    - After filling this form, this information will set to the checkout form when the user wants to order any products.
    - On this page, the user can see all the previous orders list, in a table, and can review each one of them.
    - Clicking on each order in the table redirects the user to the checkout success page.
    - On entering the checkout Success page from the profile, the user gets a toast message that this is a past confirmation for that order number.
    - under the form, there is a button that redirects the user back to their profile page.
---
  - **Wishlist Page**

    - Wish list page contains all the products that user added to their favourites. These products are positioned side by side in large views and in mobile views they are posisioned under each other.
    - name, price, average rating, number of reviews and number of products in the users wishlist also mentioned in this page.
    - by clicking on the product images user is redirectes to product details page.
---
  -**Shopping bag page**

    - Displays selected products to be purchased and their details 
    - Users can add and reduce product quantity from the shopping bag and the cost will adjust accordingly 
    - Users can remove selected products from the shipping bag and cost will adjust accordingly
    - Proceed to the checkout page

  - **Checkout App**

    - If a user is authenticated and has a profile the delivery/shipping form will be pre-populated with their default info else if the user is not authenticated the form will be empty 
    - A summary of the products & cost the user is about to purchase will be available on display next to the delivery/shipping form
    - Stripe secure card validation: the card entered by the user will be validated in real-time by stripe and if valid:
    - the purchase will go through and the user will be automatically redirected to the success page showing order confirmation details
    - Upon successful purchase: confirmation email is sent to the user, containing their order summary

  - **Manage Product Page and Admin features**

    - Admin or superuser has access to an extra button in the account dropdown menu.
    - by clicking it, the add product form opens, and a new product can be added to the products.
    - Superusers also can edit or delete each product by clicking on the edit or delete links provided under the price of each product on the products and product details page.

  - **Register**

    - On registration user is asked to enter their email address, email confirmation, full name, username, and a password and password confirmation.
    - If a user tries to register an email that is used by someone else already, they will not be allowed to use that username. The user will be notified of this - "A user is already registered with this e-mail address.".
    - If a user tries to register a username that is used by someone else already, they will not be allowed to use that username. The user will be notified of this - "A user with that username already exists.".
    - If a user password and confirm password doesn't match user gets a toast message - "Passwords do not match, please re-enter"
    - User is not allowed to use a common, all numeric, under 8 characters or too similar to the user name for security reasons.
    - If a user already has an account they can click on the sign-in link on the line on top of this page to sign in.
    - there is a home button under the page that redirects the user to the home page if they don't want to make an account.
    - When a user has successfully registered their new account, they will be redirected to the home page.
---
  - **Login page**

    - There is a link on top of this page that redirects the user to the sign-up page if they don't have an account yet.
    - User needs to fill in the username and password to log in.
    - There is a checkbox with the *Remember Me* label. clicking this checkbox will same the username and password for the next login.
    - If a registered user puts their information in incorrectly when logging in, they will be notified by a message - "The username and/or password you specified are not correct.".
    - If a user attempts to log in several times unsuccessfully, they will be notified by a message - "Too many failed login attempts. Try again later."
    - there is a home button under the page that redirects the user to the home page if they don't want to log in.
    - When a user has successfully logged in, they will be redirected to the home page with a success notification toast message.

  - **Log Out**
    - user is provided with the option to log out when clicking on the button provided on the account dropdown button in the top navbar.
    - By clicking on the "Log Out" button users get a message to check if they want to log out.
    - On log out, the user redirects to the login page and gets a flash message: "You have been logged out!"
---
- **Features Left to Implement**
   - adding more responsive design for my image fields.
   - Adding sort products based on the average rating.
   - Adding the like/dislike function in a new section on the profile page.
   - Adding social media sites for the app.
   - Adding a food delivery time system for the app.
   - Additional payment methods like Paypal or apple pay
   - Fix the rating template form.
   - better confirmation note for delete product.
---
## **Technologies**
- **Front-End**

    - HTML5 was used to put the page structure in place [HTML5](https://validator.w3.org/).
    - CSS was used to style and align images and other structures on the page [CSS](https://www.w3.org/Style/CSS/Overview.en.html).
    - Javascript was used for interactivity [JavaScript](https://www.ecma-international.org/).
    - Bootstrap was used for page layout [Bootstrap](https://getbootstrap.com/).
    - Google fonts were used for the site fonts [Google fonts](https://fonts.google.com/).
    - Fontawesome was used for its icons [Font Awesome](https://fontawesome.com/).

- **Back-end**

    - Python3 was used for the application scripting [Python](https://www.python.org/).
    - Django framework was used to build the Project [Django](https://www.djangoproject.com/).
    - Amazon web service was used to host static and media files [AWS](https://aws.amazon.com/).
    - Postgres database was used for the deployed app on Heroku [Postgres](https://www.postgresql.org/).
    - Gunicorn server was used for the deployed app on Heroku [Gunicorn](https://gunicorn.org/).
    - Stripe payment service was used for product payments [Stripe](https://stripe.com/).

- **validators**
  - The validators that have been used on the project are as followed:
    - [HTML Validator](https://validator.w3.org/nu/) - 2 warnning due to Meta and head element not found
        ![Warnings](media/html-validator.png)
    - [CSS Validator](https://jigsaw.w3.org/css-validator/) - No issues
    - [JavaScript Validator](https://jshint.com/) - No issues 
    - [Python Validator](http://pep8online.com/) - No issues

- **User stories tests**
- ****Testing user experience:****

  - **Product Owner**
    - can easily add a product via product form
    - can easily edit/update product info
    - can easily delete products
  - **Sign-up / Login**
    - user: can successfully sign up for an account by filling the required form fields and will receive a confirmation email
    - user: users also have an easy option of social login, by providing their google account
    - user: users can successfully recover their passwords by clicking on the forgot password: which will send an email to the provided email address with the necessary link for password recovery.
  - **Logged in / authenticated users**
    - user: Logged in users can save their default delivery/billing info on their profile page
    - user: logged in users can successfully add items to their wishlist for later purchase
    - user: logged in users can review products that they have bought
  - **authenticated and unauthenticated users**
    - user: can successfully browser the site by gender, category, or price and make a selection to buy
    - user: can successfully view each product details to identify price, read other users reviews on the product, select a product size or quantity
    - user: can quickly use the search icon to search for products they are interested in
    - user: can easily access products on sale and keep track of their total shopping bag cost throughout the site i. shopping bag:
    - user: can easily access their shopping bag items, which conveniently contains all their selected products, which can be added or removed from the shopping bag and the cost recalculates accordingly.
    - Easy and secure stripe checkout process with no hassle.
    - user: upon successful checkout: the user gets redirected to the success page with order details and a confirmation email is also sent to the user with their order details.
---
## **Testing**
- **Supported browsers and screens**

  - The Website was tested on Google Chrome, Microsoft Edge, and Firefox, and Opera browsers.

  - The website was shown responsive on a variety of emulated devices such as iphone4, 5, SE, 6, 6 plus, 7, 7plus, 8, 8plus and X, Nokia Lumia 520 and N9, Moto G4, Galaxy S5, Blackberry Z30, and playbook, Galaxy note, Microsoft Lumia 950 and 550, LG Optimus L70, Nexus 4, 5, 6, 7 and 10, 6P, Pixel 2 and 2XL, iPad mini, iPad, Kindle Fire, iPad pro and laptop with MDPI, touch, and HiDPI.

  - A large amount of testing was done to ensure that all pages were linking correctly.

  - Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
---
## **Fixed Issues**

- **Issue 1** 
  - By clicking on the stars in that rating inputs, a form was jumping on top of the page.
    I fixed this problem by changing the code below:

        .rating:not(:checked) > input { 
            position:absolute; 
            top:-9999px;
            clip:rect(0,0,0,0); 
        }

    to

        .rating:not(:checked) > input { 
        display: none; 
        }

- **Issue 2**
  - when rendering the divisibility by in products pages the last div with <hr> was showing even if there wasn't any other product in the list.
    I fixed this issue by adding this code in css:

        .divisibleby:last-child{
            display: none;

- **Issue 3** 
  - Some of the Images when blurry.
  - I fixed this issue by using this code to my img css:

        image-rendering: -webkit-optimize-contrast;

- **Issue 4**
  - I had some migration issues that have been fixed by deleting all migrations in all apps except the __int__ and migrate them again.

- **Issue 5** 
  - Bag was showing the delivery fee even when nothing in shoping bag.
  - I fixed this issue adding this code:

        if (
            self.order_total < settings.FREE_DELIVERY_THRESHOLD and
            self.order_total != 0):
            self.delivery_cost = settings.STANDARD_DELIVERY_FEE
        else:
            self.delivery_cost = 0

- **Issue 6**
  - migration for the wishlist time_added field was made after the model was migrated the first time. When adding the new time_added field I was getting an error that the previous wishlists need a default value.
  - I fixed this issue by choosing option 1 and adding a timezone. now().[Stack Overflow](https://stackoverflow.com/questions/56310322/django-datetimefield-with-auto-now-add-asks-for-default)
  

- ** Known Issues **
  - the social icons for Twitter and Instagram are not shown on my index page!
  - the review rating form stopped working and just adds one star to my products after deleting the migrations.
  - stripe payment-intent-success gives an error 500
  - in some views the toast notifications are blurry

---
## Deployment

### Steps to deploy Tadig to Heroku using Postgres

#### In Heroku:
1. Setup an account and log in to Heroku
2. On the apps page select `NEW`.
3. Give the app a name and select the closest region – then click `Create App`.
4. Click on the Resources tab to provision a new Postgres database for it.
5. Search in the Addons search bar for `Heroku Postgres`.
6. Select your Development plan (in my case - Hobby Dev Plan).

#### In GitPod or IDE:
7. To use Postgres open project in GitPod and install:
```
*   pip3 install dj_database_url
*   pip3 install psycopg2-binary
*   Update requirements: pip3 freeze > requirements.txt
```

#### In Django - setup new database:
In `Settings.py`:   

8. Make sure import os is there.
9. Add: `import dj_database_url`.
10. Goto Database settings and comment out existing database settings and add the below example to point the database at the new Postgres database.
```
example:
    DATABASES = {
        'default': dj_database_url.parse( # ***paste in the database URL from Heroku***)
    }
```
11. Run Migrations. `Migrations have now been made to the Postgres Database.`
12. After a Successful Migration goto memberships. models.

---
***Important:***

13. Comment out the `post_save_create_memberships` signal - ***this is because creating a user will trigger this signal to create a free membership. 
But as there will be no packages setup within our new database - we must stop this signal before we create our superuser.***   
---
14. Now we can create a superuser -: `python3 manage.py create a superuser.
15. Runserver and login as superuser to the admin page.
16. Goto Packages in the memberships section.
17. Click add the package to add each of the following 2 packages
*   package type: free.
*   Package price: 0.
*   stripe plan id: (price_id) get this from your stripe - Products - Free Plan - Pricing - API id.   

***and***  
*   package type: premium.
*   Package price: 5.
*   stripe plan id: (price_id) get this from your stripe - Products - Premium Plan - Pricing - API id.
18. Save and log out of admin.
19. Stop the server.
20. Uncomment the signal from step 13.
21. Restart the server and check admin - the superuser will now be linked to a free package type and have a stripe customer id.
22. Goto Settings -  Database settings - remove the Postgres database URL.
23.  Create an if/else code block to check if the os. environ variable is defined. 
if it is defined that will mean we are on Heroku so we will use the Postgres database.
Else we will be in our local environment and so use the default database.
```
    Example: 
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```

24. In the Terminal install gunicorn as our webserver: `pip3 install gunicorn`
25. Freeze requirements. `Pip3 freeze > requirements.txt`
26. Create a Procfile at the same level as the project. 
27. Enter the following code into the Procfile to tell Heroku to create a web dyno that will run gunicorn and serve Tadig Restaurant:
```
    web: gunicorn tadig-restaurant.wsgi:application
```
28. Temporarily disable collect static – to do this:
*   login via the terminal: Heroku login –i.
*   Enter Heroku email and password.
*   Enter the following in the terminal:
```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app tadig-restaurant
```
In `Settings.py`:

29. Add the hostname of the Heroku app – to ALLOWED_HOSTS (also include localhost):
```
    ALLOWED_HOSTS = ['tadig-restaurant.herokuapp.com', 'localhost'].
```
30. Ensure all .env variables such as the Django and stripe secret keys remain private. Also, make sure they are set up inside Heroku's config vars.

In `The Terminal`:

31. Deploy to Heroku:
*   Add and push to GitHub
*   git add.
*   git commit –m “**your-message**”
*   git push
*   Now initialize Heroku git remote (because we created our app on the website rather than with the CLI): 
*       Heroku git:remote -a tadig-restaurant
*   Then push to Heroku : git push heroku master

In `The Heroku`:

32. Setup automatic deployment in Heroku:
*   Goto the deploy tab
*   Set deployment method to GitHub
*   Search for tadig-restaurant
*   Click connect
*   Scroll down and click Enable Automatic Deploys

tadig-restaurant is now deployed to Heroku

## Local Deployment

**Before starting, some prerequisites:**

*   Before starting you should have an IDE set up - [Visual Studio Code](https://code.visualstudio.com/). - for example.
* It's advisable to have a virtual environment setup. Pythons own can be used : 

```
    python3 -m .venv venv
    .venv\Scripts\activate
```

*   Have **at least** the following installed:   
    *   Python3 - to run the application.
    *   Pip - to install any requirements.
    *   GIT - required for version control.


The above example displays an env for a local purpose only.

5.  Install all requirements for the application by using this command:
```
    sudo -H pip3 -r requirements.txt
```
6.  In the IDE terminal, use the following command to start tadig-restaurant:
```
    python manage.py runserver
```

tadig-restaurant should now be running locally on localhost port 8000. (http://127.0.0.1:8000)

7.  After running Django initially, it will create the local database **db.SQLite3**.
8.  Make all migrations:
```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```

9.  Create a superuser:
```
python3 manage.py createsuperuser
***Enter username, email and password***
```

You should now have a local copy of tadig-restaurant.

---  

## **Credits**
- **Content and Media**

  The content and images used in this site were obtained from the links below:

| Starter page | Main page | Dessert page | Drink page |
|:---------------|:---------------|:---------------|:---------------|
| [Kashke bademjan](https://persianfoodtours.com/wp-content/uploads/2019/10/Kashk-e-Bademjan.jpg) | [Baghali polo](https://www.behesht.co.ukimages/behesht/foods/maincourse/baghali-polo.jpg) | [Baklava](https://encrypted-tbn0.gstatic.comimages?q=tbn%3AANd9GcSyftLKhAJzlAmscp5fLjIjBYzrP-Vy1_7xsl9SHiQAFTu8vCeM&usqp=CAU) | [Doogh](https://www.thedeliciouscrescent.com/wp-content/uploads/2020/03/Doogh_5.jpg) |
| [Mirza ghasemi](https://claudiacanu.com/wp-content/uploads/2018/07/Mirza-Ghasemi-eggplant-sauce.jpg) | [Zereshk polo ba morgh](https://yummynotes.net/wp-content/uploads/2020/04/Zereshk-Polo.jpg) <br> Info : [Persian Mama](https://persianmama.com/zereshk-polo-ba-morgh/) | [Faloodeh shirazi](https://i.pinimg.com/originals/1b/d9/12/1bd9124c6ffb8cdfbc0e5e2c536dd2b1.jpg) | [Araghe bidmeshek](https://en.snapptrip.com/blog/wp-content/uploads/2017/05/Sharbat-e-Khakshi-1024x805.jpg) <br> Info : [Diba](https://dibaonline.de/NIK-Aragh-Bidmeshk-Willow-blossoms-430ml) |
| [Do piaze alo](https://3.bp.blogspot.com/-psIKWaAbLDc/Wt4mpNShYGI/AAAAAAAAKzM/Z4Rb5Bj-7Mka3VhIoJb6NAtpSwbJ0pQEgCLcBGAs/s1600/DoPiazeh_TurmericSaffron.JPG) | [Khoreshte gheyme bademjan](https://igotitfrommymaman.com/wp-content/uploads/2020/01/Khoreshe-Gheymeh-11-scaled.jpg) <br> Info : [Persian food tours](http://www.persianfoodtours.com/khoresht-gheymeh-bademjan-yellow-split-peas-stew/) | [Bastani sonnati](https://encrypted-tbn0.gstatic.comimages?q=tbn%3AANd9GcSgL85WQFb-72OdGFDShM4gpfIt5z1tGWhmIha_Tv8XBehXtcKE&usqp=CAU) | [Gol gav zaboon](https://images-na.ssl-images-amazon.comimages/I/61-KwamytGL._A.jpg) <br> Info : [The persian pot](http://www.thepersianpot.com/recipe/gol-gav-zaban-borage-tea/) |
| [Salad olvie](https://i.pinimg.com/originals/39/37/be/3937be2fea7c0c2fb2c9987b7a63bc4b.jpg) <br> Info : [Persian mama](https://persianmama.com/salad-olivieh-persian-chicken-salad/) | [Khoreshte ghorme Sabzi](https://www.196flavors.com/wp-content/uploads/2017/03/ghormeh-sabzi-3.jpg) | [Noon khamei](https://i1.wp.com/www.littleswissbaker.com/wp-content/uploads/2016/04/DSC_1897v2.jpg?w=680&ssl=1) | [Mojito](https://alldayidreamaboutfood.com/wp-content/uploads/2013/05/Honest-Mojitos-3.jpg) |
| [Noon panir sabzi](https://cdn.shortpixel.ai/spai/q_lossless+ret_img/https://3nkq72bhhp51kv1h2do55o5r-wpengine.netdna-ssl.com/wp-content/uploads/2.3_NAT_American-Herbal-Cookbook_NEW-Wordpress.jpg) <br> Info : [Clean plates](https://www.cleanplates.com/eat/recipes-eat/panir-sabzi/) | [Khoreshte fesenjoon ba morgh](https://3.bp.blogspot.com/-RaW9e0WBdAA/T_7DZs4o5sI/AAAAAAAACxs/xTdy-dEqpVQ/s1600/Fesenjoon-TS.jpg) | [Ranginak](https://4.bp.blogspot.com/-LBlaXdUqrYo/Tba1gvjYyHI/AAAAAAAACvs/l1bm02mG7-s/s1600/227458_206016996087508_100000376264948_606452_2793162_n.jpg) | [Berry juice](https://5.imimg.com/data5/LY/KU/OD/GLADMIN-7061725/berryjuice-500x500.jpg) |
| **More Drinks** |                                                                                                                                                                                                                                                                                  |
| [Watermelon juice](https://images.eatthismuch.com/site_media/img/854541_Shamarie84_45b61cdb-ddfc-43dd-bf1f-6c366caf07a5.png) | [Orange juice](https://www.earthfoodandfire.com/wp-content/uploads/2018/04/Homemade-Orange-Juice.jpg) | [Masala chai](https://wendypolisi.com/wp-content/uploads/2018/09/dirty-chai-latte-2.jpg) | [Bloody mary](https://www.bbcgoodfood.com/sites/default/files/user-collections/my-colelction-image/2015/12/bloody-mary.jpg) |
| [White russian](https://i.pinimg.com/originals/af/d2/4c/afd24c5047e6aaa1cfbe4dd8e8d7468f.jpg) |  [Espresso](https://kaffeexperterna.com/wp-content/uploads/2015/08/espresso-crema-kaffe.jpg) |

- **Resources**

  Below is a list of the resources used to create this project:

  - [Adding a favicon -- Flask documentations](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
  - [Stack Overflow](https://stackoverflow.com/)
  - [Slack Peer code review](https://slack.com/intl/en-se/)
  - [w3schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_fixed_footer)
  - [To make responsive Footer](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/)
  - [To fix my scrollbar style](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp)
  - [Dynamic carousel slider](https://stackoverflow.com/questions/30483186/bootstrap-carousel-and-django)
  - [Radio star input](https://gist.github.com/blairanderson/7f9d1c08345c6573e09edaa1f7316fa1)

### **Acknowledgements**

 - Big thanks to my mentor, Rohit Sharma who provided me with tips, support, and some helpful resources.

 - Also the code institute support teams for fast support and help all the time.

**This project is purely educational, please contact me if there are any issues with Copyright.**