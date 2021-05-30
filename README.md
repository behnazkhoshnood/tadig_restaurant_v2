# **Milestone Project 4**
**Full Stack Frameworks with Django Milestone Project Milestone Project.**

**Tadig Restaurant**

[View the live project here.]()
This website is made for restaurants. We named our restaurant "Tadig restaurant" which is a made-up Persian restaurant.
It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential customers.

![Tadig Restaurant]()
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

The main purpose of this project is to build a full-stack site based around business logic used to control a centrally-owned dataset.
By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

### **User Stories**

#### **As a Site Users**

- **Registeration and User Account**
  - I want to be able to easily register for an account, so that I can have a personal account and be able to view my profile.
  - I want to be able to easily login and logout, so that I can have access my personal account information.
  - I want to be able to easily recover my password in case I forget it, so that I can recover access to my account.
  - I want to be able to receive an email confirmation after registering, so that I can verify that my account registeration was successful.
  - I want to be able to have a personalized user profile, so that I can view my personal order history and order confirmations and save my payment information.

#### **As a Shopper**

- **Viewing and Navigating**
  - I want to be able to view a list of products, so that I can select some to purchase.
  - I want to be able to view individual product details, so that I can identify the price, description, product rating and product image.
  - I want to be able to easily view the total of my purchases at any time, so that I can avoid spending too much.

- **Sorting and Searching**
  - I want to be able to sort the list of availabe products, so that I can easily identify the best rated, best priced and categorically sorted products.
  - I want to be able to sort a specific category of product, so that I can find the best priced or best rated product in a specific category, or sort the products in each category.
  - I want to be able to sort multiple categories of products simultaneously, so that I can find the best priced or best rated products.
  - I want to be able to search for a product by name, category or description, so that I can find a specific product I'd like to purchase.
  - I want to be able to easily see what I've searched for and the number of results, so that I can quickly decide wheather the product I want is availabe.

- **Purchasing and Checkout**
  - I want to be able to easily select the quantity of a product when purchasing it, so that I can ensure I don't accidentally select the wrong product or quantity.
  - I want to be able to view items in my bag to be purchased, so that I can identify the total cost of my purchase and all items I will receive.
  - I want to be able to adjust the quantity of individual items in my bag, so that I can easily make changes to my purchase before checkout.
  - I want to be able to easily enter my paiment information, so that I can check out quickly and with no hassles.
  - I want to be able to feel my personal and payment information is safe and secure, so that I can confindently provide the needed information to make a purchase.
  - I want to be able to view an order confirmation after checkout, so that I can verify that I haven't made any mistakes.
  - I want to be able to receive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records.

#### **As a Store Owner**

- **Admin and Store Managment**
  - I want to be able to add a product, so that I can add new items to my store.
  - I want to be able to edit or update a product, so that I can change product pricees, descriptins, image or other product criteria.
  - I want to be able to delete a product, so that I can remove items that are no longer available.

### **Design choices**

  The goal in design was to create a website that is overall user friendly, has a modern feel with emphasis on providing information about the restaurant dishes/drinks in a readable and eye-catching way. Therefore, following design choices were made:
- **Framework**
  * Front-end framework, [Bootstrap](https://Bootstrap.com/),  based on bootstrap Design was chosen for this project for its modern interface and ease of use.

  * [JQuery](https://jquery.com/) was used for initializing some bootstrap elements.

- **Typography**
  - I used [Google Fonts](https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600&family=Raleway:wght@100;200;300;400;500&display=swap") for the font style of my project:
    - The font I have used for this project is called **Raleway** and **Open+Sans** font with sans-serif as a backup font.

- **Icons**
  - I used [Favicon](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/) to make a unic brand for my website.
  - I used [FontAwesome]() as the main icon library across the project (e.g. for forms and buttons).

- **Colour Scheme**

  The idea of using different shades of the same colour is implemented accross the website. The primary colour used for main buttons and headings is deep purple as it seems to create a nice contrast with white backgrounds. The secondary colour used for icons, dividers and some other buttons is blue and pink.

  - **Main colour palette**

    - Main colors that have been used are black and white and some shades of gray due to their high contrast which complement the colorful images.
    - For toast messeges headers and some labels I used bootstrap scheme:
        - Succsess: #28a745; which is a shade of green color.
        - Danger: #dc3545 ; which is a shade of red color.
        - Primary: #007bff ; which is a shade of blue color.
        - secondary: #6c757d ; which is a shade of gray color.
        - warning: ##ffc107 ; which is a shade of yellow color.
        - info: #17a2b8 ; which is a shade of blue color.
        - light: #f8f9fa ; which is a shade of light gray color.
        - dark: #343a40 ; which is a shade of dark gray color.
---
## **Wireframes**
[Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create all wireframes for the project.

 #### <center>All Recipes<center>

Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]()
![Registered users]() **Registered users** | ![Registered users]()
![Not registered user]() **Not registered users** | ![Not registered user]()
---

 #### <center>Profile<center>

Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]() 
![Registered users]()**Registered users** | ![Registered users]()
---

 #### <center>Add Recipes<center>
 Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]() 
![Registered users]() **Registered users** | ![Registered users]()
---
 #### <center>Manage Categories<center>
 Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]()
---

 #### <center>Manage Marks<center>
Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]()
---

 #### <center>Add Category<center>
 Desktop view | Mobile view
- | -
![Admin]() **Admin**| ![Admin]()
---

 #### <center>Add Mark<center>
 Desktop view | Mobile view
- | -
![Admin]() **Admin** | ![Admin]()

 #### <center>Log In<center>
 Desktop view | Mobile view
- | -
![All users]() **All users** | ![All users]()
---

 #### <center>Register<center>
Desktop view | Mobile view
- | -
![All users]() **All users** | ![All users]()
---

## **Features**
- **Implemented features**
  - **Common features in all pages**
    - All of the pages contain a 3 part layout with the header, main part of the page and the footer.
        - **Header**
            - **main navbar**
                - Main navbar is deviding the products that are provided in to diffrent categories of: appetizers, main dishes, desserts and beverages.
                on medium and large screens, main navbar is fixed on top of the page and is lined up in a line. In smaller screens this navbar turns to a dropdown navbar.
                - Another item in this navbar is "Sort" which sorts all the products by their name, price or rating.
            - **Home button**
               - On medium and large screens restaurant logo works as the home button but in smaller screen home button is added to the dropdown navbar.
            - **Search, Account and Bag**

                In all views,the search area, account and bag are fixed on top of the page.

                **Search**

                - Customers can search for the name, category or any word from a product description to easily find them, 
                - By clicking on the search icon, the search result and the number of the search result will be shown under the search area.
                - If the filed is empty when search icon is clicked a toast message appear on top right corner of the page and notifies the user.

                **Account**

                - Account is a dropdown button which contains the *register* and *logout* for all the users.
                - **Log in button** is added to this list for registered users.
                - Admin or super user access an extra button from here which is called *Manage Products*, which is used to add new products to the list of products.

                **Bag**

                - This shows a grand total amount of the products added to the shopping bag and placed on the top right corner.

                **Delivery Banner**
                - This part will notify the user that by shopping more than 200 kr, which is the free delivery treshold, they would earn the free delivery.

        - **Footer**

            Footer is devided to 3 parts. *Social* , *Contacts* and *Copyright*, which is locted at the bottom of the pages.
            **Social** contains the facebook, twitter and instagram.
            **Contacts** contains the address, phone number, opening time and email address of the restaurant.
            these parts are positioned under each other in small views and in medium and larger views contacts and social are positioned side by side and copyright is positioned under them.
---
  - **Home Page**

    - The home page contains the eyecatching carousel slide with the colorful images that makes the perpose of the website clear from the begining.
    - breaf information about the restaurant in provided to the left side of the carousel in medium and larg screens and in smaller screens, this information is placed ontop of the carousel.
    - carousel is showing all the product images. By clicking on each image user is directed to product details page, which shoes that product, all the information related to it, and can add it to the back right away.
---
  - **Products Pages**

    - By clicking on the main navbar categories in the top header, users are directed to respective category page, which has the name, image, price and rating information of all producs in that category.
    - Under the price of each product is also a form that user can use to add any product in this category to their shoping bag.
    - When user adds a product to their shoping bag they will be notified by a toast message on top on the page, which shows that product information.
    - If the price of the items are lower than free delivery treshold, it will show in this toast message that how much more they should add to their bag to get the free delivery.
    - User is informed with the header on top of the page that by clicking on product images they get more information about that product.
    - when clicking on product image user is redirected to the product details page which has the description of that product.
    - Sorting only in each specific category is also possible by the sorting dropdown input provided on top of this page, which can sort the products based on their price, rating or name.
    - There is also a scroll back to top button is provided in this page, to easily go back to the top of the page.
    - On medium and larger views the product info and image are positioned side by side but on smaller views they are placed under each other.
    - Admin or super user provided with extra links under eah product price to either delete or edit that product.
---
  - **Product Details Page**

    - This page shows the product name, price, rating,image and description.
    - A form to add this product to the shopping bag is located under the product price.
    - By choosing the amount, and then clicking on Add to Bag, user will see a toast messege on top of the page that shows the product information in their bag.
    - If the grand total of the products value is lower than the delivery treshold, user will be notified the amount that they should spend more in order to get free delivery in the toast messege.
    - The toast message also provide the user with a button to be redirected to thier shopping bag.
    - on small screens the product information, shopping and quantity bottons are placed under each other, but in medium and larger views they are placed side by side.
    - Admin or super user provided with extra links under the product price to either delete or edit this product.
---
  - **Shopping Bag Page**

    - user can easily reach this page by clicking on the bag icon on top right corner of all pages or on the notification toast that they will see on top of the products and products details, after clicking on the add to bag button.
    - If user has any pruduct in their shopping bag, they can review them in this page.
    - User can easily update the amount or remove the products in their bag, in this page.
    - The amount on Total shopping, delivery fee and grand total is shown under this page with two buttons.
    - One button is to redirect the user to products page, to order something more, and the other redirects the user to checkout page.
    - If there isn't any product in the shoping list, user will be notified that the bag is empty and get the option to be redirected to products page.
    - In small views the Grand total and secure checkout botton is placed on top of the page and the chosen products and their details placed under the buttons.
    - In larger views the products information is placed on top of the billing information and the checkout botton.
---
  - **Checkout Page**

    - By clicking on the secure checkout button on the shopping bag page, user will be redirected to checkout page.
    - In this page user can see the summary of their order, and a form to fill the information required for the delivery.
    - by filling this form and clicking on the *Compelete Order* button, user can securely purchase from the site with the help of stripe elements.
    - On x-small screens order summary is placed on top of the order form and under the form there is the *Compelete Order* button and *Adjust Bag*.
    - Product images is not seenable in the x-small views to improve the page layout.
    - On small and larger screens the order summary and form placed side by side and the compelete order and adjust bag is at the bottom of the page.
---
  - **Checkout Success Page**

    - After compeleting the order form and click on the compelete order botton, in checkout page, user will see a nice overlay for a short time untill the proccess of shoping compelets.
    - User then will be redirected to checkout success page and see a toast message on top of the page, notifing the user that the order is prossessed, the order number.
    - User also recives a confirmation email to their email address.
    - In this page all the order information is shown to the user, including the order number and date, purchased products and the price for each product, delivery information and the total amount of the purchase.
---
  - **Profile Page**

    - Profile user is only accessable for registered users.
    - If a non registered user try to go to profile page by writing it in the browser he/she will be redirected to the sign in page.
    - Registered user have an access to their profile in account dropdown button, in the header.
    - In profile page, there is a information form that can be filled.
    - The first time that the user compelete an order these information will be filled automaticlly.
    - User can update these information in profile page, with filling the form and click on update information botton.
    - After filling this form, these information will set to the checkout form when user want to order any products.
    - In this page, user can see all the previous orders list, in a table, and can review each on of them.
    - Clicking on each order in the table redirects the user to checkout success page.
    - On entering the checkout Success page from the profile, user gets a toast messege that this is a past confirmation for that order number.
    - under the form there is a button that redirects the user back to their profile page.
---
  - **Manage Product Page and Admin features**

    - Admin or super user has access to an extra button in account dropdown menu.
    - by clicking it, the add product form opens, and a new product can be added to the products.
    - Super user also can edit or delete each product with clicking on the edit or delete links provided under the price of each product in the products and product details page.

  - **Register**

    - On registeration user is asked to enter their email address, email confirmation , fullname, username and a password and password confirmation.
    - If a user tries to register an email which is used by someone else already, they will not be allowed to use that username. The user will be notified of this - "A user is already registered with this e-mail address.".
    - If a user tries to register an username which is used by someone else already, they will not be allowed to use that username. The user will be notified of this - "A user with that username already exists.".
    - If a user password and confirm password dosen't match user gets a toast message - "Passwords do not match, please re-enter"
    - User is not allowed to use a common, all numeric, under 8 charecter or too similar to the user name for seurity reseons.
    - If user already has an account the can click on the sign in link on the line on top of this page to sign in.
    - there is a home button under the page that redirects the user to home page if they don't want to make an account.
    - When a user has successfully registered their new account, they will be redirected to home page.
---
  - **Login page**

    - There is a link on top of this page that redirects the user to sign up page if they don't have an account yet.
    - User needs to fill in the username and password to login.
    - There is a checkbox with *Remember Me* label. clicking this checkbox will same the username and password for next login.
    - If a registered user puts their infomation in incorrectly when loging in, they will be notified by a messages - "The username and/or password you specified are not correct.".
    - If a user attempts to login several time unsuccfully, they will be notified by a message - "Too many failed login attempts. Try again later."
    - there is a home button under the page that redirects the user to home page if they don't want to login.
    - When a user has successfully logged in, they will be redirected to home page with a toast messege.

  - **Log Out**
    - user is provided by the option to log out when clicking on the button provided on the navbar.
    - By clicking on "Log Out" button user get a message to check if they really want to log out.
    - On log out user redirects to log in page and getting a flash message: "You have been logged out!"
---
- **Features Left to Implement**
   - Adding a like/dislike button for each Recipe and sort the recipes from the most to least favorites.
   - Adding the liked recipes in a new section in profile page.
   - Make the design of the site more appealing and more food friendly.
   - Adding a footer with social media sites for the app.
   - Seperating the recipes in different sections for each category.
   - More secure pathway for the admin.
---
## **Technologies**
- **Front-End**

  - [HTML5](https://en.wikipedia.org/wiki/HTML)
    - To give the page its structure and presenting static data.
    - All HTML files are located within the 'templates' directory.
  - [CSS](https://en.wikipedia.org/wiki/CSS)
    - CSS has been used to style and customise the content of this project.
  - [Materialize](https://materializecss.com/)
    - This is a framework that I have used to simplify CSS classes, features that have been used and modified include the navbar, responsive design classes, and colors for backgrounds and text.
  - [JQuery](https://en.wikipedia.org/wiki/JQuery)
    - JQuery has been used to give the site its functionality as well as making DOM manipulation simpler.

- **Back-end**
  - [MongoDB](https://en.wikipedia.org/wiki/MongoDB) 
    - As the data entered by users can always be different from one to the next, the project uses MongoDB to store its data as MongoDB is a Document Based Database.
  - [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
    - Flask is a framework that allows developers to easily present data in an orderly fashion. All data entered by a user, such as the Recipe Name, is presented to users with a few lines of code embedded into the HTML.
      - Modules from Flask that have been included are:
      - Flask
      - flash
      - render_template
      - redirect
      - request
      - session
      - url_for
      - PyMongo
  - [bson.objectid](https://www.npmjs.com/package/bson-objectid)
      - ObjectId
  - [werkzeug.security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
      - generate_password_hash
      - check_password_hash
  - [datetime](https://docs.python.org/3/library/datetime.html)
      - datetime
  - [Python](https://www.python.org/)
    - Python is working very closely with Flask to manipulate data and HTML across multiple pages within the app.
- **Deployment**
  * [Heroku](https://dashboard.heroku.com/)
  * [Git](https://git-scm.com/)
  * [Github](https://github.com/)
  * [Gitpod](https://gitpod.io/)
- **validators**
  - The validators that have been used on the project are as followed:
    - [HTML Validator](https://validator.w3.org/nu/) - No issues apart from jinja templating
    - [CSS Validator](https://jigsaw.w3.org/css-validator/) - No issues
    - [JavaScript Validator](https://jshint.com/) - No issues 
    - [Python Validator](http://pep8online.com/) - No issues
---
## **Testing**
- **Supported browsers and screens**

  - The Website was tested on Google Chrome, Microsoft Edge, and Firefox and Opera browser.

  - The website was shown responsive on a variety of emulated devices such as iphone4, 5, SE, 6, 6 plus, 7, 7plus, 8, 8plus and X, Nokia Lumia 520 and N9, Moto G4, Galaxy S5, Blackberry Z30 and playbook, Galaxy note, Microsoft Lumia 950 and 550, LG Optimus L70, Nexus 4, 5, 6, 7 and 10, 6P, Pixel 2 and 2XL, iPad mini, iPad, Kindle Fire, iPad pro and laptop with MDPI, touch, and HiDPI.

  - A large amount of testing was done to ensure that all pages were linking correctly.

  - Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

- **Register.html**
  - **Test 1 - Register - Test Passed ✓**

    - **Step 1** - Click the register button on the navbar for desktop view devices or side navbar for tablet or mobile view devices.
    - **Step 2** - Put in a first name(2 character minimum).

    - **Step 3** - Put in a last name (also 2 character minimum).
    - **Step 4** - Put in a username which is unique (5 character minimum).
    - **Step 5** - Put in a password (also 5 character minimum).
    - **Step 6** - Click 'Register' button.
    - **Step 7** - Be redirected to 'get_recipes.html' with a flash message, welcoming the user.

  - **Test 2 - Register with a username which already exists - Test Passed ✓**

    - **Step 1** - While on 'register.html', enter username 'admin' or any username existing in our data base.

    - **Step 2** - Enter password (5 character minimum).
    - **Step 3** - Click the 'Register' button.
    - **Step 4** - Be presented by flash message containing "Username already exists!".
  - **Test 3 - Register with less than 2 Alphabet for first and last name and less than 5 characters for username - Test Passed ✓**
    - **step 1** - While on 'register.html', enter first or last name with numbers or less than 2 alphabet is shown invalid.

    - **Step 2** - While on 'register.html', enter username or password with less than 5 charecters is shown invalid.
    - **Step 3** - As the 'Required' and minlength=2 for first and last name, and minlength=5 for username and password has been added, the form will not be submitted.
    - **Step 4** - Changing first and last name to more than 1 alphabet, and username and password to more than 4 charecters will submit the form.
    - **step 5** - All the tooltips are shown an the page by hovering over the input icon.

  Desktop view | Mobile view
  - | -
  ![register All users desktop](static/images/desktopview-all-users.png) | ![register All users mobile](static/images/mobile-view-all-users.png)
  ---
- **Login.html**

  - **Test 1 - Log In - Test Passed ✓**

    - **Step 1** - Enter your Username.

    - **Step 2** - Enter your Password.
    - **Step 3** - Click the 'log in' buttton.
    - **Step 4** - Be redirected to 'get_recipes.html' with flash message containing "Welcome, [ user ]".

  - **Test 2 - Log in attempt with incorrect info - Test Passed ✓**

    - **Step 1** - Enter credentials that are incorrect.

    - **Step 2** - Click the 'log in' button.
    - **Step 3** - Be redirected to the log in page with a flash message containing "Incorrect Username and/or Password".

  Desktop view | Mobile view
  - | -
  ![log in All users desktop](static/images/login-desktop-all-users.png) | ![log in All users mobile](static/images/login-mobile-all-users.png)

- **Adding a New Recipe**

  - **Test 1 - Adding a New Recipe - Test Passed ✓**

    - **Step 1** - Log In.

    - **Step 2** - Be redirected to get_recipes.
    - **Step 3** - Click the button labeled 'Add Recipe'.
    - **Step 4** - Be redirected to the form for user to fill in.
    - **Step 5** - Form is tried to be submitted with empty fields for required fields and faild; user is notified of missing items.
    - **Step 6** - There is 1 multichoice dropdown field on the form, which is called marks. This field is not required and the form still successfully post if this field is empty.
    - **Step 7** - There is a cancel button provided on the bottom of the form. If the user don't want to add the recipe. he/she can click on this button and get redirected to their profile page.
    - **Step 8** - Once the form is filled out to the satisfaction of the constraints and the 'Add Recipe!' button is clicked user will be redirected to 'profile.html' where the user can see their newly added recipe located alphabeticly in the collapsible dropdown list. User also be notified that the new recipe added by flash notifications.
    - **Step 9** - Check the contents of the newly added recipe right away by clicking on that recipe in the dropdown list.

  Desktop view | Mobile view
  - | -
  ![add recipe admin desktop view](static/images/add-desktop-admin.png) Admin views: | ![add recipe admin mobile view](static/images/add-mobile-admin.png)
    **note:** same for all users, except that in the admin page there is manage Catogory and manage mak buttons visable in the navbar.

  - **Test 2 - Avoids empty strings in out textarea fields - Test Passed ✓**

    - **Step 1** - Fill in all the required feilds in "Add Recipe" form.
    - **Step 2** - Add an empty line to the ingredients or cooking steps textarea.
    - **Step 3** - click on "Add Recipe" button.
    - **Step 4** - Empty lines will be removed when showing the recipe in the "All Recipes" or "Profile" page.

- **Editing/Deleting a Recipe**
  - **Test 1 - Editing a Recipe - Test Passed ✓**

    - **Step 1** - Navigate to profile or All recdipe page.
    - **Step 2** - Click the button labeled "EDIT" for the desired recipe.
    - **Step 3** - Navitgate to the part of the recipe that the user wishes to edit.
    - **Step 4** - After editing the desired part, click on the blue button, "EDIT RECIPE" at the bottom of the page to edit the recipe.
    - **Step 5** - Be redirected to profile.html and a flash message, notifing the user that the recipe is updated.
    - **Step 6** - Should the user wish to cancel the action, they can click on the cancel button located on bottom left.
    - **Step 7** - If user clicks the cancel button he/she will be redirected to profile page and all changes will be disregarded.

  Desktop view | Mobile view
  - | -
  ![edit form admin desktop view](static/images/edit-desktop-admin.png) | ![edit form admin mobile view](static/images/edit-mobile-admin.png)
---
  - **Test 2 - Avoid duplication in multi choice dropdown input field - Test Passed ✓**
    - **step 1** - In edit form in marks field user can just add one of each choices to the list.

  - **Test 3 - Deleting a Recipe for registered users - Test Passed ✓**
    - **Step 1** - Navigate to All Recipes, or profile page.
    - **Step 2** - Click the button labeled "DELETE". In mobile phone view this button can be found on top of the recipe collapsible body but in desktop view it is placed in the head of the collapsible.
    - **Step 3** - User gets a message if they are sure to delete this recipe.
    - **step 4** - If confirm the recipe deletes and user redirects to their profile page but if press cancel, recipe stays unchanged and the user will be redirected to their profile page. Admin user will stay in any page that they deleted the recipe from.

  Desktop view | Mobile view
  - | -
  ![profile admin desktop view](static/images/profile-desktop-view.png) | ![profile admin mobile view](static/images/profile-mobile-view.png)
---
  - **Test 2 - Deleting a Recipe for Admin - Test Passed ✓**
    - **Step 1** - Navigate to All Recipes, or profile page.
    - **Step 2** - Click the button labeled "DELETE", in the head of collapsible, for each rcipe.
    - **Step 3** - User gets a message if they are sure to delete this recipe.
    - **step 4** - If confirm the recipe deletes and user redirects to their profile page but if press cancel, recipe stays unchanged and the user will be redirected to their profile page. Admin user will stay in any page that they deleted the recipe from.

  Desktop view | Mobile view
  - | -
  ![All recipes Admin desktop view](static/images/desktop-view-admin.png) | ![all recipes Admin mobile view](static/images/mobile-view-admin.png)

- ### **Manage categories and marks pages( only admin accessibility )**

  - **Test 1 - Add, edit or delete categories or marks - Test Passed ✓**

    - **step 1** - Click on the Manage Categries to manage the categories or Manage Marks to manage the marks.
    - **step 2** - Admin can sees all the categories in manage categories and all the marks in manage marks in a seperate card with an option of delete or edit and an Add button on top of the page to add a new category or mark.
    - **step 3** - By clicking on the add button, a one input field form, called add category or add mark opens regardingly.
    - **step 4** - Admin can write the desired name for the new category/mark and press the Add category or Add mark at the bottom of the form.
    - **step 5** - Admin is provided also with a cancel button in both pages if he/she decided to not add any new category or mark.
  - **step 6** - Pressing this button bring up a note if he/she is sure not to add any category or mark.
    - **step 7** - if press ok, admin redirects to the get_categories if in add category form, or get_marks if in add marks form.
    - **step 8** - if press cancel, no category or mark will be added and user will be redirected to "Add Catogory" or "Add mark" regarding to which one that he/she was adding.

  Desktop view | Mobile view
  - | -
  ![manage categories desktop](static/images/manage-categories-desktop.png) | ![manage categories mobile](static/images/manage-categories-mobile.png)
  ![manage marks desktop](static/images/manage-marks-desktop.png) | ![manage marks mobile](static/images/manage-marks-mobile.png)
  ![add categories desktop](static/images/add-category-desktop.png) | ![add categories mobile](static/images/add-category-mobile.png)
  ![add marks desktop](static/images/add-mark-desktop.png) | ![add marks mobile](static/images/add-mark-mobile.png)
  ---
- ### **Log Out**

  - **Test 1 - Log out - Test Passed ✓**
    - **step 1** - Click on the "log Out" button in the navbar to log out.
    - **step 2** - Pressing this button bring up a note: "Are you sure you want to log out?".
    - **step 3** - if press ok user will log out.
    - **step 4** - if press cancel, the user would not log out.
---
## **Fixed Issues**

- **Issue 1** - When a user were adding a recipe with empty lines in multi-line textarea inputs, empty lines were shown in these areas.
  - I fixed this issue by adding the above script.js file to trim the empty lines.

```$('li, .edit-delete-div').filter(function () {
        return $(this).text().trim() === '';}).remove();
```
- **Issue 2** - When editing a recipe user could add the marks that they have chosen for this recipe from before, again, in the dropdown list.
  - I fixed this issue by adding the above edit.js file code to avoid duplication.
```$(document).ready(function () {
var marks = document.getElementById("mark");

[].slice.call(marks.options)
  .map(function(a){
    if(this[a.value]){ 
      marks.removeChild(a); 
    } else { 
      this[a.value]=1; 
    } 
  },{});
});
```
- **Issue 3** - Users could open unauthorized pages if providing it's url route path in the browser.

  - I fixed this problem with adding error handlers in my python and using relative error conditions in the functions that needed like manage, add, edit and delete categories and mark pages, users profile page, add, edit and delete buttons. These codes are provided with docstrings in my [app.py](app.py) in more details.
```
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 500
```
- **Issue 4** - The title areas for category and marks where changing height depending on their html note.
    - I fixed this issue with adding the code below to my script.js file
```
    var manageTitleHight = 0;

$(".manage-title").each(function(){
   if ($(this).height() > manageTitleHight) { manageTitleHight = $(this).height(); }
});

$(".manage-title").height(manageTitleHight);
   // to avoid copying the link of the delete and edit btns
$(".delete-btn, .edit-btn").contextmenu(function () { return false; });
});
```
- **Issue 5** - By putting some recipe informations with both edit and delete buttons in the recipes collapsible header, mas not a good choice for smaller views.
  - I fixed that issue by using some materialize classes to replace dome of these info in the body of the collapsible in smaller views.
```
This class is in the collapsible header and hide this buttton in small views.
 <a href="{{ url_for('delete_recipe', recipe_id=recipe._id) }}"
 class="btn-small delete-btn hide-on-small-only">Delete</a>

This class is in the collapsible body and hide this buttton in medium and large views.
 <a href="{{ url_for('delete_recipe', recipe_id=recipe._id) }}"
class="btn-small delete-btn hide-on-med-and-up -align">Delete Recipe</a>
```
---
## **Deployment**
This project is stored in a GitHub repository and hosted on Heroku.
### **How to deploy to Github**
1. Click [here](https://github.com/behnazkhoshnood/good-cook-ms3") to get to the projects repository.

2. Click on 'Settings' to the far right in navigation menu below your repository name.

3. Scroll down to 'GitHub Pages' and select 'master branch' as the source.

4. Click save.

5. The link to the site hosted on GitHub Pages should appear at the top of the section.

### **How to clone this repository in order to run the code locally on your machine**
1. Click [here](https://github.com/behnazkhoshnood/good-cook-ms3") to get to the projects repository.

2. Click "Clone or Download".

3. Click the "copy" icon.

4. Open Git Bash in your local IDE.

5. Change your current working directory to where you want the cloned directory to be made.

6. Type `$ git clone` and then paste the URL you copied earlier.

   `git clone https://github.com/USERNAME/REPOSITORY`
7. When you press enter your local clone will be ready.
### **How to clone this repository in order to run the code locally on your machine**

1. Created a new application using the Heroku dashboard.

2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).

3. Install Heroku via the console using 'npm install -g Heroku'.

4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.

5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.

6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.

7. Connect GitHub to Heroku via the console using 'heroku git:remote a creative-hub'

8. Commit all files in your project via the console using 'git add .' and 'git commit -m "Message"'.

9. Deploy your project to Heroku via the consol using 'git push heroku master'.

### **Running the application locally using Gitpod**

1. Clone the repository as outlined above and upload it to GitPod.

2. Install the necessary libraries specified in the requirements.txt.

3. Set your environment variables by creating and adding them into a env.py file.

4. Create a .gitignore file in the root directory and add the env.py file to avoid it being pushed to GitHub.

5. Import the env.py file into the app.py file.

6. Run the application.

## **Credits**
- **Content and Media**

  The content and images used in this site were obtained from links below:
  Images | Content
  - | - 
  [Adas polo image](https://www.saveur.com/resizer/Wnizk_4UQkqFMI5XmMydgOXf4J8=/1200x628/smart/arc-anglerfish-arc2-prod-bonnier.s3.amazonaws.com/public/L2N233EB3VWQE43J7IJHYBS3Z4.jpg) |[Adas polo content](https://almondandthehazelnut.com/recipes/adas-polo/)
  [Chicken enchilada dip image](https://www.familyfreshmeals.com/wp-content/uploads/2014/06/Cheesy-Chicken-Enchilada-Dip-BEAUTY_1-768x512.jpg) | [Chicken enchilada dip content](https://www.familyfreshmeals.com/2014/06/cheesy-chicken-enchilada-dip.html)
  [Chicken tikka masala image](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-chicken-tikka-masala-jpg-1526059261.jpg) | [Chicken tikka masala content](https://www.topochicousa.net/recipe-blog/2020/9/2/chicken-tikka-masala)
  [Khoreshte ghorme sabzi image](https://thecaspianchef.com/wp-content/uploads/2019/12/ghormehsabzi3.jpg) | content added by me
  [Mojito image](https://kitchenswagger.com/wp-content/uploads/2020/07/mojito-recipe3.jpg) | [Mojito content](https://www.allrecipes.com/recipe/147363/the-real-mojito/)
  [Pepper & walnut hummus image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/houmous_0-a0c19df.jpg?quality=90&webp=true&resize=375,341) | [Pepper & walnut hummus content](https://www.bbcgoodfood.com/recipes/pepper-walnut-houmous-veggie-dippers) | 

- **Resources**

  Below is a list of the resources used to create this project:

  - [Handeling Applications Errors -- Flask Documentation](https://flask.palletsprojects.com/en/master/errorhandling/#error-handlers)
  - [(Totorial) Docstring in Python](https://www.datacamp.com/community/tutorials/docstrings-python)
  - [quick start -- Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [Adding a favicon -- Flask documentations](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
  - [Stack Overflow](https://stackoverflow.com/)
### **Acknowledgements**

 - Big thanks to my mentor, Rohit Sharma who provided me with tips, support and some helpful resources.

 - Also the whole code instetute support team for fast support and help all the time.

**This project is purely educational, please contact me if there are any issues with Copyright.**
behnaz.khoshnood@gmail.com


https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_fixed_footer

used codes:
to align my ratings under each image in product page I used this code from stackoverfroW[https://stackoverflow.com/questions/22592064/how-to-align-text-below-an-image-in-css/22592136]
known bugs:
the image in my product page is showing on the border line of my fixed navbar.

to pot the footer at the bottom of the page
https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/

my main nav menu items text were seperating to 2 line. I used this code to fix it:
https://stackoverflow.com/questions/17704539/css-getting-text-in-one-line-rather-than-two
.navbar-nav li{
    white-space: nowrap
    }

used this for fixing my scrollbar style
https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp

Project Tools
Django — Web Framework
Back end Python 3.8 — Back end Programming language
PostgreSQL — databases
Front end — HTML 5, CSS 3, Bootstrap, JavaScript
QR code Generation JavaScript JQuery
Deployment Activity Heroku server
Amazon Web Services — S3 Bucket Storage Allocation

to make my carousel dynamic
https://stackoverflow.com/questions/30483186/bootstrap-carousel-and-django

to make the rating and review models
https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a

radio star input:
https://gist.github.com/blairanderson/7f9d1c08345c6573e09edaa1f7316fa1

known bugs:
when clicking on rating star buttons the page jumps up to the top.

future features:
confirmation toast message for deleting a product.