# Cheer To Beers API

Cheers To Beers is a social media platform where users can show thier love of different beers and share a drink with one another even if they aren't in the same room. It offers the chance to find friends, interact and review their own drinks.


## Contents
* [Development Goals](#Development-Goals)
* [Agile Planning](#Agile-Planning)
    * [User Stories](#User-Stories)
* [Database Structure](#Database-Structure)
    * [Database Diagram](#Database-Diagram)
    * [API End Points](#API-Endpoints)
* [Future Implementations](#Future-Implementations)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
    * [Validators](#Validators)
    * [User Story Testing](#User-Story-Testing)
    * [Manual Testing](#Manual-Testing)
    * [Bugs](#Bugs)
* [Deployment](#Deployment)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Fork Repository](#Fork-Repository)
    * [Clone Repository](#Clone-Repository)
* [Credits](#Credits)

## Development Goals

The goal of this API is provide a backend service to allow the Cheers To Beers front end application to perform, Create, Read, Update and Delete operations via the user interface.

## Agile Planning

Agile methodology was used throughout the deveploment for this project and I found it extremly helpful to keep track of my project.

The project was broken down into Epics and User Stories and the MoSCoW method was used to determine relevent features needed for the scope of this project.

Issues were created in GitHub for each Epic and User Story with Tasks to complete and MoSCoW labels on each one. A Kanban board was also created to keep track of these Issues. A Milestone for the MVP was also created and linked to relevant Issues.

The project's issues can be found [Here](https://github.com/DavidDock/cheers-api/issues)

The project's Kanban board can be found [Here](https://github.com/users/DavidDock/projects/3)

### User Stories

![User-Stories](/documentation/cheers-api-user-stories.png)

## Database Structure

### Database Diagram

![Model-Diagram](/documentation/cheers-database-diagram.png)

### API Endpoints

#### Profiles

/profiles/

* GET - Get a list of profiles

/profiles/int:pk/

* GET - Get a single profile
* PUT - Update a single profile
* DELETE - Delete a profile

Profiles can be filtered by who the user is following or being followed.  
They can be ordered by amount of posts, following, followed by or most recently followed or followed by.

#### Posts

/posts/

* POST - Create post
* GET - Get a list of posts

/posts/int:pk/

* GET - Get a single post
* PUT - Update a single post
* DELETE - Delete a post

Posts can be searched by their title, type or author.  
They can be filtered by who the user is following, what posts they have stared or their own posts.  
The posts can be ordered by amount of comments, stars, cheers or most recently stared.

#### Stars

/stars/

* POST - Create a star
* GET - Get a list of stars

/stars/int:pk/

* GET - Get a single star
* DELETE - Delete a star

#### Cheers

/cheers/

* POST - Create a cheer
* GET - Get a list of cheers

/cheers/int:pk/

* GET - Get a single cheer
* DELETE - Delete a cheer

#### Comments

/comments/

* POST - Create a comment
* GET - Get a list of comments

/comments/int:pk/

* GET - Get a single comment
* PUT - Update a single comment
* DELETE - Delete a comment

Comments can be filtered by what post they are on.

#### Followers

/followers/

* POST - Create a follow
* GET - Get a list of followers

/followers/int:pk/

* GET - Get a single follow
* DELETE - Delete a follow

#### About

/about/

* GET - Get a list of abouts

#### Contact

/contact/

* POST - Create a contact message
* GET - Get a list of contact messages

## Future Implementations

4 Could Have issues are remaining for this project, they covered the following functionality for future implementation:
* About edit - Allows admin to edit the about message from the front-end.
* Contact List - Allows admin to view and delete all contact messages from the front-end.
* Create Review - Allows users to create and delete a review for other users posts/drinks. This will create an average user rating which can be seen in the post detail. 

Further future implentations:
* For each cheers/star/comment give post owner a notification.
* Show post owner a list of users who gave cheer/star.

## Technologies Used

### Languages
* Python

### Frameworks
* Django - Framework to build the app.
* Django REST framework - Toolkit for building the API

### Libaries and Programes Used
* Pillow - To process the image.
* Cloudinary - Used to store and serve images.
* Django filter - Used to filter API results.
* Git - Used for version control.
* GitHub - Used to store the repository and GitHub projects for the Kanban board.
* GitPod - IDE used to develop the site.
* ElephantSQL - Used for the database.
* lucid - To create model diagrams.
* Google Sheets - To create uer story and testing spreadsheet.
* Tiny PNG - Used to re-size image file.
* Heroku - Used for hosting the site.

## Testing

Testing was done throughout development using the local sqlite database.  
Further testing was completed as part of the front-end development by testing the deployed API and database.

### Validators
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to test the python code.  

The validation was completed on all python files written for this site.  
Settings.py contains important data which is longer than 79 lines and can not be ajusted.  
After removing some whitespace and adding blank lines all files passed validation.  


### User Story Testing

#### Profile-drf  
As a developer I can create a profile and view as admin.

##### Acceptance Criteria
* A profile is created each time a user is created, using signals.
* Can view profiles in admin.

##### Results
When a user is created so is their profile which you can view in the admin panel.

#### Profile list-drf   
As a developer I can display a list profiles so they can be used on api view.

##### Acceptance Criteria
* Can view list of profiles in API.

##### Results
A list of profiles can be seen correctly on the /profiles url API view.

#### Profile detail-drf
As a developer get (retrieve) each profile and display in api with ability to update (put)  

##### Acceptance Criteria
* Can view each profile in api view.
* Can edit profile in api view, with owner permissions

##### Results
A single profile can be correctly viewed in the API url /profiles/int:pk/ and can only be edited by the owner.

#### Create Post-drf 
As a developer I can create post and view in admin

##### Acceptance Criteria
* Can view posts in admin

##### Results
A post can be seen correctly with all fields in the admin panel.

#### Post List-drf
As a developer I can display a list of posts and create a post so it they can be viewed in api

##### Acceptance Criteria
 * Can view list of posts in api
 * Am able to create a post

##### Results
A list of posts can be seen correctly in /posts API view and a post can successfully be created by a logged in user in the view.

#### Post Detail-drf
As a developer display each post in api with ability to edit and delete

##### Acceptance Criteria
 * Can view each post in api
 * Can edit own post in api
 * Can delete own post in api

##### Results
A single post can be correctly viewed in /posts/int:pk/ API view and only the owner of the post can successfully update or destory the post in the view.

#### Create Comment-drf 
As a developer I can create comment and view in admin

##### Acceptance Criteria
* Can view comments in admin

##### Results
A comment can be seen correctly with all fields in the admin panel.

#### Comment List-drf
As a developer I can display a list of comments and create a comment so they can be viewed in api

##### Acceptance Criteria
 * Can view list of comments in api
 * Am able to create a comment

##### Results
A list of comments can be seen correctly in /comments API view and a comment can successfully be created by a logged in user in the view.

#### Comment Detail-drf
As a developer display each comment in api with ability to edit and delete  

##### Acceptance Criteria
* Can view each comment in api
* Can edit own comment in api
* Can delete own comment in api

##### Results
A single comment can be correctly viewed in /comments/int:pk/ API view and only the owner of the comment can successfully update or destory the comment in the view.

#### Create Star-drf
As a developer I can create star and view in admin 

##### Acceptance Criteria
*  Can view stars in admin

##### Results
A star can be seen correctly with all fields in the admin panel.

#### Star List-drf
As a developer I can display a list of stars and create a star so they can be viewed in api.  

##### Acceptance Criteria
* Can view list of stars in api
* Am able to create a star

##### Results
A list of stars can be seen correctly in /stars API view and a star can successfully be created by a logged in user in the view to see what post they have stared.

#### Star Detail-drf
As a developer display each star in api with ability to delete. 

##### Acceptance Criteria
* Can view each star in api
* Can delete own star in api

##### Results
A single star can be correctly viewed in /stars/int:pk/ API view and only the owner of the star can successfully destory the star in the view.

#### Create Cheer-drf
As a developer I can create cheer and view in admin 

##### Acceptance Criteria
*  Can view cheers in admin

##### Results
A cheer can be seen correctly with all fields in the admin panel.

#### Cheer List-drf
As a developer I can display a list of cheers and create a cheer so they can be viewed in api.  

##### Acceptance Criteria
* Can view list of cheers in api
* Am able to create a cheer

##### Results
A list of cheers can be seen correctly in /cheers API view and a cheer can successfully be created by a logged in user in the view to see what post they have cheered.

#### Cheer Detail-drf
As a developer display each cheer in api with ability to delete. 

##### Acceptance Criteria
* Can view each cheer in api
* Can delete own cheer in api

##### Results
A single cheer can be correctly viewed in /cheers/int:pk/ API view and only the owner of the cheer can successfully destory the cheer in the view.

#### Create Follower-drf
As a developer I can create a follower and view in admin.  

##### Acceptance Criteria
* Can view followers in admin.

##### Results
A follow can be seen correctly with all fields in the admin panel.

#### Follower List-drf
As a developer I can display a list of followers and create a follower so they can be viewed in api. 

##### Acceptance Criteria
 * Can view list of followers in api.
 * Am able to create a follower.

##### Results
A list of follows can be seen correctly in /followers API view and a logged in user can successfully create a follower in the view so they can follow another user.

#### Follower Detail-drf
As a developer display each follower in api with ability to delete  

##### Acceptance Criteria
 * Can view each follower in api.
 * Can delete own follower in api.

##### Results
A single follower can be correctly viewed in /followers/int:pk/ API view and only the follower owner can successfully destory it in the view.

#### Set following in profile-drf
As a developer display if user is following another user in api to determine who they follow 

##### Acceptance Criteria
* See following id or null in each profile api for each user.

##### Results
You can successfully see the following id or null of each user profile if user is logged in.

#### Set Star in posts-drf
As a developer display if user stared post in api to determine starred posts  

##### Acceptance Criteria
* Can see if user has starred post or not in api view.

##### Results
You can successfully see if the logged in user has stared each post or not in postlist and detail views.

#### Set Cheer in posts-drf
As a developer display if user cheered post in api to determine cheered posts  

##### Acceptance Criteria
* Can see if user has cheered post or not in api view.

##### Results
You can successfully see if the logged in user has cheered each post or not in postlist and detail views.

#### Add fields and order filters to profile-drf
As a developer display extra fields and order filters to determine how active the user is and provide api with more fields/filters to use

##### Acceptance Criteria
* Can see additional fields (post, following and followed counts) in profile list and profile detail api.
* Can see order filters in api.

##### Results
You can succesfully see the additional fields in each profile.

#### Add fields and order filters to posts-drf
As a developer display extra fields and order filters to the posts and provide api with more fields/filters to use.

##### Acceptance Criteria
 * Can see additional fields (comments, star and cheer counts) in post list and post detail api.
 * Can see order filters in api

##### Results
You can successfully see the additional fields in each post and can successfully use the order filters in the postlist API view.

#### Search posts-drf
As a developer display search filter to posts and provide api search function

##### Acceptance Criteria
 * Can search posts by title, author name or type

##### Results
You can successfully search the posts in postlist view by title, author or type.

#### Filter posts-drf
As a developer display search filter to posts and provide api search function

##### Acceptance Criteria
 *  Can filter by own posts, starred posts and followed users posts.

##### Results
You can successfully filter the posts in postlist view by logged in users posts, starred posts and followed users posts.

#### Filter profiles-drf
As a developer display field filter of profiles who follow and is followed by user so filter can be available in api

##### Acceptance Criteria
 *  Can filter profiles by who follows or is following user.

##### Results
You can successfully filter the profiles in profilelist view by follows or is following logged in user.

#### Filter Comments-drf
As a developer display all comments for a post in api if filter is used

##### Acceptance Criteria
 *  Can filter all comments for each post.

##### Results
You can successfully filter the comments for each post in the commentslist view.

#### Create About-drf
As a developer I can create about and view in admin.

##### Acceptance Criteria
* Can view about in admin.

##### Results
An about can be seen correctly with all fields in the admin panel.

#### About List-drf
As a developer display all about messages in api view  

##### Acceptance Criteria
* Can view about info in api list.

##### Results
A list of abouts can be seen correctly in /about API view.

#### Create Contact-drf
As a developer I can create a contact and view in admin.

##### Acceptance Criteria
* Can view contact in admin.

##### Results
A contact can be seen correctly with all fields in the admin panel.

#### User create contact-drf
As a developer allow user to create contact through api  

##### Acceptance Criteria
* Can see contacts made in admin.

##### Results
A contact can successfully be created by a user in the contactcreate view, /contact url, and be seen in the admin panel.

### Manual Testing
![Manual-Testing](/documentation/manual-testing-cheers-api.png)

### Bugs

## Deployment

### Heroku Deployment

### Fork Repository

### Clone Repository

## Credits

### Learning
The code used for this project was taught to me by code insitute. The Code Insitutes project run throughs 'Django Rest Framework' and 'Moments' helped me greatly with the development of my project.
