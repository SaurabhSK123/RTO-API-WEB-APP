from flask import render_template, request
from main import app
from prediction import *



@app.route('/')

@app.route('/home')
def homepage():
   return render_template("index.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['imagefile']
        f.save(f.filename)
        img = cv2.imread(f.filename)
        detect_num = detect_plate(img)
        info = get_vehicle_info(detect_num)
        return render_template("result.html",
                               model = info[0],
                               regyear = info[1],
                               engsize = info[2],
                               sea = info[3],
                               idfi = info[4],
                               engnum =  info[5],
                               fuelt =  info[6],
                               regdate =  info[7],
                               loc =  info[8]
         )