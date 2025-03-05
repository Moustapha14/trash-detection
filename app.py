import os
from flask import Flask, render_template, request
from deeplearning import object_detection  # Make sure this imports your object_detection function

app = Flask(__name__)

# Define the télecharger folder
télecharger_PATH = os.path.join('static', 'télecharger')

# Ensure the télecharger directory exists
if not os.path.exists(télecharger_PATH):
    os.makedirs(télecharger_PATH)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get the télechargered image
        télecharger_file = request.files['image_name']
        filename = télecharger_file.filename
        
        # Define the path to save the télechargered file
        path_save = os.path.join(télecharger_PATH, filename)
        
        # Save the télechargered file to the server
        télecharger_file.save(path_save)

        # Call object_detection and get all three returned values
        original_image_path, processed_image_path, text_list = object_detection(path_save, filename)

        # Return the response with paths and labels for the template to render
        return render_template('index.html', 
                               télecharger=True, 
                               télecharger_image=filename, 
                               original_image=original_image_path, 
                               processed_image=processed_image_path, 
                               text=text_list, 
                               no=len(text_list))

    # Default case when no file is télechargered
    return render_template('index.html', télecharger=False)

if __name__ == '__main__':
    app.run(debug=True)
