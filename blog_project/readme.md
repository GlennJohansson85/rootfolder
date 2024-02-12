# Django Blog Project

## Overview

This Django-based "blogging" platform provides users a.k.a my family members with the ability to create accounts, log in, and share their thoughts through posts. It includes features for post creation, category-based post filtering, and user interaction.

## Features

1. **User Registration:**
   - Users can register for an account using the user registration form.
   - The registration form includes fields for username and password.

2. **User Login:**
   - Registered users can log in using their credentials.
   - Authentication is handled using Django's built-in `AuthenticationForm`.

3. **User Logout:**
   - Users can log out of their accounts, clearing the session.

4. **Homepage:**
   - The homepage displays all posts in descending order of creation.
   - Each post includes details such as title, content, author, and creation date.
   - Users can delete their own posts from the homepage.

5. **Post Categories:**
   - Users can view posts filtered by categories.
   - Categories are displayed on the homepage, and selecting one shows posts specific to that category.

6. **Creating New Posts:**
   - Authenticated users can create new posts using the post creation form.
   - The form includes fields for title, content, and an image upload.

7. **Deleting Posts:**
   - Users can delete their own posts from the homepage.
   - A delete confirmation form is used to prevent accidental deletion.

8. **Commenting on Posts:**
   - Authenticated users can leave comments on individual posts.
   - Comment submission is handled through the comment form.
   - Comment errors and form validation issues are logged for debugging.

9. **Logging and Debugging:**
   - The project utilizes Python's logging module to log errors and debugging information.
   - Loggers are used in the `comment` view to track errors during comment submission.

10. **Authentication and Authorization:**
    - Certain views are protected with the `@login_required` decorator, ensuring only authenticated users can access them.
    - Authorization checks are implemented, such as verifying that the logged-in user owns a post before allowing deletion.

### Style ###
I used a vacationisch kind of style due to we, as in my family, usually take photos when going on trips and such. I used a yellowish contrast style due to it reminds me of summer and pink headers due to its a nice contrast. 
Probably because it so fun:)
I wanted to keep the app simple and modern.

### Images ###

## Navbar ##

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/73759dc7-65ac-42b7-9218-4fd7ba5726ed)
* Used four links = "Home", "Login", "Logout" and "Post". To register its enough to click on the post link to become a member.

