from flask import Flask, request, render_template, send_file, redirect
import boto3
import io
import zipfile
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition')

# Helper function to create a collection
def create_collection(collection_id):
    response = rekognition.create_collection(CollectionId=collection_id)
    return response

# Helper function to index faces into a collection
def index_face(image_bytes, collection_id, external_image_id):
    response = rekognition.index_faces(
        CollectionId=collection_id,
        Image={'Bytes': image_bytes},
        ExternalImageId=external_image_id,
        DetectionAttributes=['ALL']
    )
    return response

# Helper function to search for faces in a collection
def search_faces(image_bytes, collection_id):
    response = rekognition.search_faces_by_image(
        CollectionId=collection_id,
        Image={'Bytes': image_bytes},
        MaxFaces=1,
        FaceMatchThreshold=90
    )
    return response

# Helper function to create a zip file
def create_zip_file(categories, images_folder):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for person, images in categories.items():
            person_folder = person.replace(" ", "_")
            for image in images:
                image_path = os.path.join(images_folder, image)
                zip_file.write(image_path, arcname=os.path.join(person_folder, image))
    zip_buffer.seek(0)
    return zip_buffer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    if 'photos' not in request.files:
        return redirect(request.url)
    
    files = request.files.getlist('photos')
    categories = {}
    images_folder = 'uploaded_images'
    collection_id = 'indian_celebrities_collection'  # Change to your actual collection ID
    
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
    
    for file in files:
        if file and file.filename:
            filename = secure_filename(file.filename)
            file_path = os.path.join(images_folder, filename)
            file.save(file_path)
            with open(file_path, 'rb') as img_file:
                file_bytes = img_file.read()
                # Search for faces and index if not found
                search_response = search_faces(file_bytes, collection_id)
                if search_response['FaceMatches']:
                    person_id = search_response['FaceMatches'][0]['Face']['ExternalImageId']
                    if person_id not in categories:
                        categories[person_id] = []
                    categories[person_id].append(filename)
                else:
                    index_response = index_face(file_bytes, collection_id, filename)
                    person_id = index_response['FaceRecords'][0]['Face']['ExternalImageId']
                    categories[person_id] = [filename]
    
    # Generate zip file
    zip_buffer = create_zip_file(categories, images_folder)
    zip_filename = 'categorized_images.zip'
    
    # Save zip file to server
    with open(zip_filename, 'wb') as f:
        f.write(zip_buffer.getvalue())
    
    return render_template('photo_details.html', categories=categories, zip_filename=zip_filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
