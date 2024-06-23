from flask import Flask, render_template
import os

app = Flask(__name__)

#ithan home page inte function
@app.route('/')
def index():
    #image kedakkana folder evide anen variable ilek itt
    image_folder = os.path.join('static', 'images')
    
    # for loop vechit ella images um koode list aaki images enna variable il itt 
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    #ippa images enn paranja variable il ella images um ind 
    
    #ini nammada home.html run chyyanam ( render enna ithil parayane )
    return render_template('home.html', images=images)
    #home.html run chyyukayum athilek images argument ayit pass chyyum
    
    # ini templeates folderil ulla home.html vayikku
    
if __name__ == '__main__':
    
    app.run(debug=True)
