# Imagine Gallery

![gallery](/static/img/md.jpg)

## Built By [Dan Kariuki](https://github.com/Buttonupd/)

## Description
This is an application that allows users to view images. Image details are stored in categories and tagged by Location. The admin is responsible for uploading, editing or deleting images.

## User Stories

Users would like to:
* View all images submitted.
* Click on images to display more details.
* Search for images by category.
* Copy links to images to share with their friends

## Admin Abilities

Admin should:
* Sign in to the gallery
* Create new images for showcasing
* Delete images
* Update image post details.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images by Location|


## SetUp / Installation Requirements
### Prerequisites
* python3.7
* pip3
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/Buttonupd/Imagine
        $ cd gallery

## Running the Application
* Creating the virtual environment

        $ Virtualenv env(* 'env is the name of the enviroment')
        $ source env/bin/activate
        

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ ./manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ ./manage.py test pictures

## Technologies Used
* Python3.7
* Django Framework
* Postgresql Database



