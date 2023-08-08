from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
from module import output
from module import imageQuality
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
import cv2
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
file_arr = []
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
solutions=[[' Remove symptomatic plants from the field or greenhouse to prevent the spread of bacteria to healthy plants','To keep leaves dry and to prevent the spread of the pathogens, avoid overhead watering established plants and instead use a drip-tape or soaker-hose. '
'to prevent spread, DO NOT handle plants when they are wet (from dew)','Where bacterial spot has been a recurring problem, consider using preventative applications of copper-based products registered for use on tomato, especially during warm, wet periods.'],
           ['Prune or stake plants to improve air circulation and reduce fungal problems','Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.','Remove and destroy all garden debris after harvest and practice crop rotation the following year.','Drip irrigation and soaker hoses can be used to help keep the foliage dry.'],
           [],['Pull and remove infected plants, bag up the foliage and unripe tomatoes into black trash bags, and disposed it along with the household trash.','Do not compost diseased plants or fruit.'
'remove damaged lower leaves regularly since that’s where most fungi attacks begin.','Avoid watering in late afternoon or evening so that water can evaporate from the leaves and, if possible, water the ground and not the foliage'],['the first step is to let the plants air out and dry.Expose them to dry air conditions, because the humidity that the fungus needs to survive and thrive is dried up in the open air.',' One thing you can do to help keep the leaves as dry as possible is to water in the early morning hours, that way the plant has plenty of time to dry before the sun comes out',
'Another treatment option is fungicidal sprays. When using fungicide sprays, be sure to thoroughly cover all parts of the plant that is above ground, focusing specifically on the underside of leaves.','Calcium chloride sprays are among the most highly recommended types for leaf mold. There are a few organic fungicides on the market as well.'],
['Remove infected leaves immediately, and be sure to wash your hands and pruners thoroughly before working with uninfected plants.','Fungicides containing either copper or potassium bicarbonate will help prevent the spreading of the disease.'
'While chemical options are not ideal, they may be the only option for controlling advanced infections. One of the least toxic and most effective is chlorothalonil','A layer of mulch will help prevent spores on the ground from splashing up onto the lower leaves.'],
['Use a high-pressure water spray to dislodge twospotted spider mites. This can also wash away their protective webbing.','Using long-lasting pesticides like bifenthrin and permethrin kill natural enemies and should be avoided to encourage natural enemies.'
'Soaps and horticultural oils are reasonably effective against mites and have little impact on people, animals and nontarget insects','If twospotted spider mites continue to be a problem after control efforts have been attempted, and the plants are valued, consider hiring a landscape professional to treat them'],
[' Remove symptomatic plants from the field or greenhouse to prevent the spread of bacteria to healthy plants','To keep leaves dry and to prevent the spread of the pathogens, avoid overhead watering established plants and instead use a drip-tape or soaker-hose. '
'to prevent spread, DO NOT handle plants when they are wet (from dew)','Where bacterial spot has been a recurring problem, consider using preventative applications of copper-based products registered for use on tomato, especially during warm, wet periods.'],
['Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.','Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost.'
'Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.','Do NOT save seeds from infected crops.'],
['TYLCV identification based only on symptomatology is unreliable, because similar symptoms can be caused by other viruses or various growing conditions.','Maintain good weed control in the field and surrounding areas. Prevent the spread of any whiteflies to healthy plants. '
' Tomato and pepper fields should be cleaned up immediately after harvest.','Also destroy crop residues of melons and cotton immediately after harvest to reduce whitefly migration.']
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    print(' in home')
    return render_template('index.html')
@app.route('/index')
def index():
    #print(' in home')
    return render_template('index.html')


@app.route('/checkimagequality')
def checkimagequality():
    return render_template("checkimagequality.html")
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/', methods=['POST'])
def upload_image():
    if 'file1' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file1 = request.files['file1']
    if file1.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file1 and allowed_file(file1.filename):
        filename1 = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        # print('upload_image filename: ' + filename)
        flash('Images successfully uploaded and displayed below')
        # flash('\n FileName = '+filename)
        f1 = UPLOAD_FOLDER+filename1
        '''bscore = imageQuality(f1)
        if(bscore>30):
            flash(filename1+' Quality is low please reupload it')
        bscore = imageQuality(f2)
        if (b   score > 30):
            flash(filename2 + ' Quality is low please reupload it')'''

        print('FileName1 = '+filename1)
        print('about to call output')
        a,b,c= output(f1)
        #check((f1),(f2))
        s = 'static/uploads/'
        flash('disease is :')
        flash(a)
        print(c)
        if(c!=2):
            for i in range(0,3):
                flash(solutions[c][i])
        #print(file_arr)
        print(a, b,c)
        return render_template('index.html', filename1=filename1)

    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
#@app.route('/first')
'''def first():
    print('array = '+file_arr[0])
    flash("Final Photo and Signature")
    return render_template("first.html",filename1=file_arr[0])'''
@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    filename= cv2.resize(filename, (750, 750))
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.debug = True
    app.run()
