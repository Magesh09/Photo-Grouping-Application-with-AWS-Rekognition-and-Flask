# Photo Grouping with AWS Rekognition

## Overview

This project demonstrates how to use AWS Rekognition for facial recognition and photo grouping. Users can upload photos, and the application detects and groups these photos based on recognized faces. The grouped photos can be downloaded as a zip file. This application is built using Flask and is deployed to AWS Elastic Beanstalk.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Key Learnings](#key-learnings)
7. [References](#references)

## Features

- Upload multiple photos.
- Automatically detect and group photos based on recognized faces.
- Download grouped photos in a zip file.
- Elegant and user-friendly interface.

## Technologies Used

- **Flask Framework with Python**: Web framework for Python.
- **AWS Rekognition**: AWS service for facial recognition.
- **AWS Elastic Beanstalk**: Platform for deploying and managing applications.
- **Bootstrap**: For styling and responsive design.
- **HTML/CSS**: For frontend development.

## Setup Instructions

### Prerequisites

- Python 3.x
- AWS account with Rekognition service
- Flask
- AWS Elastic Beanstalk CLI

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/photo-grouping-rekognition.git
    cd photo-grouping-rekognition
    ```

2. **Install Dependencies**

    Ensure you have `pip` installed, then install the required Python packages:

    ```bash
    pip install flask boto3 werkzeug
    ```

3. **Configure AWS Credentials**

    Ensure your AWS credentials are configured. You can do this by setting environment variables or using the AWS CLI:

    ```bash
    aws configure
    ```

4. **Deploy to AWS Elastic Beanstalk**

    Make sure the Elastic Beanstalk CLI is installed and configured. Then, deploy the application:

    ```bash
    eb init -p python-3.8 photo-grouping-rekognition
    eb create photo-grouping-rekognition-env
    eb deploy
    ```

    The application will be available at the URL provided by Elastic Beanstalk.

## Usage

1. **Upload Photos**

    - Navigate to the index page.
    - Use the upload form to select and upload your photos.

2. **View Grouping Results**

    - After uploading, the application will process the photos and group them based on detected faces.
    - You will be redirected to the details page where you can see the total number of detected persons and download the categorized images.

3. **Download Grouped Images**

    - On the details page, click the "Download Categorized Images" button to get a zip file of the grouped photos.

## File Structure

```
project_root/
    app.py                   # Main Flask application
    static/
        style.css            # CSS stylesheet for styling
        (other static files)
    templates/
        index.html           # HTML template for the index page
        photo_details.html   # HTML template for the photo details page
```

## Key Learnings

- Integration of AWS Rekognition with a Flask application for facial recognition.
- Handling file uploads and processing images in Flask.
- Generating and downloading zip files of grouped images.
- Deploying a Flask application to AWS Elastic Beanstalk.
- Designing user-friendly interfaces with HTML and CSS.

## References

- [AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/latest/dg/what-is-rekognition.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Broadcast

Watch the broadcast of this project to see it in action: [Broadcast Link](https://drive.google.com/file/d/1YncD5w7ZWdJwovbiJOQO_Yt9NNFEERsl/view?usp=sharing)

