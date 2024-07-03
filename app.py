from flask import Flask, render_template
from DeepImageSearch import Load_Data, Search_Setup
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = os.path.join('static', 'images')
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('home.html', images=images)
    
@app.route('/image/<path:filename>')
def serve_image(filename):
    similar_images = get_similar_images(filename)
    return render_template('image.html', filename=filename, images=similar_images)

def get_similar_images(filename):
    
    pass
if __name__ == '__main__':
    app.run(debug=True)
