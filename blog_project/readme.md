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

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/3398e57b-81b9-4369-ac5c-917b1c7647cd)
* When doing this project I had facebook in mind the entire time. How could I make it better? What features should I implement and what should I leave out? This way of thinking made the project so much harder. However, by pressing this plus icon you add your post and upload your image. Easy peasy.

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/8172a554-0d53-4e60-86f8-7b482c4ed37b)
* When register your post you see the fill in the following fields.

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/547cfc8d-5124-4f3f-ab5a-ebf8e8feecfd)
* On the wall it looks like this. Only users whom post can delete their posts(and admins) by clicking the delete button below their post(which is only visible to the one that posted).

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/cf4013b9-3f5d-4ec6-abeb-caee0a2bb248)
* Users can then comment on the post and see what other users have commented before.

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/803b270d-9a88-4a35-bb0e-209ba79820be)
* To be able to post you must become a member. If you by any chance forget if your logged in or not it will show at the bottom of the screen.

![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/01b99742-6786-423e-bd80-ff7080786d23)
* When pressing the logout link you see this page.

### Testing
## Python test
In "tests.py" within the "blog_app" folder all tests performed can be showned excepts responsive tests and formalia:
* def test_user_registration_view
* def test_user_login_view
* def test_home_view
* def test_post_category_view
* def test_post_create_view
* def test_delete_post_view
* def test_comment_view
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/a1c9475c-80bf-487d-b8be-935b581b868c)

## Responsiveness - test - Iphone
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/f3d88262-d2aa-4dc0-9c9f-f04995496a67)

## FLAKE8
Used Visual Studios built-in pep8 control - No errors
(Note: First time using VS so i really hope I did it correct) 

## Agile - light
![image](https://github.com/GlennJohansson85/rootfolder/assets/139962883/05a8633a-3a75-405a-bd70-98bff0895b57)


