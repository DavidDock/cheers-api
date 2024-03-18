# Cheer To Beers API

Cheers To Beers is a social media platform where users can show thier love of different beers and share a drink with one another even if they aren't in the same room. It offers the chance to find friends, interact and review their drinks.


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

#### Posts

/posts/

* POST - Create post
* GET - Get a list of posts

/posts/int:pk/

* GET - Get a single post
* PUT - Update a single post
* DELETE - Delete a post

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

* For each cheers/star/comment give post owner a notification.
* Show post owner a list of users who gave cheer/star.

## Technologies Used

## Python Packages

## Testing

### Validators

### User Story Testing

#### (#1)  

##### Acceptance Criteria

##### Results  

### Manual Testing

### Bugs

## Deployment

### Heroku Deployment

### Fork Repository

### Clone Repository

## Credits
