import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter, ImageEnhance

UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def home():
    return '''Hello World!'''


@app.route('/blur', methods=['GET', 'POST'])
def blur():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            factor = request.args.get('factor', type=float, default=2.0)

            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            enhancer = ImageEnhance.Sharpness(im)
            im = enhancer.enhance(factor)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to Blur</title>
    <h1>Choose Image to Blur</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/sharpen', methods=['GET', 'POST'])
def sharp():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            factor = request.args.get('factor', type=float, default=4.0)

            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            enhancer = ImageEnhance.Sharpness(im)
            im = enhancer.enhance(factor)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to Sharpen</title>
    <h1>Choose Image to Sharpen</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/brighten', methods=['GET', 'POST'])
def brighten():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            factor = request.args.get('factor', type=float, default=1.3)

            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            enhancer = ImageEnhance.Brightness(im)
            im = enhancer.enhance(factor)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to Brighten</title>
    <h1>Choose Image to Brighten</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

    
@app.route('/contrast', methods=['GET', 'POST'])
def contrast():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            factor = request.args.get('factor', type=float, default=2.0)

            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            enhancer = ImageEnhance.Color(im)
            im = enhancer.enhance(factor)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to Saturate</title>
    <h1>Choose Image to Saturate</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

    
@app.route('/halfcompress', methods=['GET', 'POST'])
def halfcompress():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            factor = request.args.get('factor', type=float, default=2.0)

            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            x,y = im.size()
            im.resize((x/factor,y/factor),Image.ANTIALIAS)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to halfcompress</title>
    <h1>Choose Image to halfcompress</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
    
  
@app.route('/rightrotate', methods=['GET', 'POST'])
def rightrotate():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im  = im.transpose(Image.ROTATE_90)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to rightrotate</title>
    <h1>Choose Image to rightrotate</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
@app.route('/leftrotate', methods=['GET', 'POST'])
def leftrotate():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im  = im.transpose(Image.ROTATE_270)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to leftrotate</title>
    <h1>Choose Image to leftrotate</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    

@app.route('/fliphorizontal', methods=['GET', 'POST'])
def fliphorizontal():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im  = im.transpose(Image.FLIP_LEFT_RIGHT)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to fliphorizontal</title>
    <h1>Choose Image to fliphorizontal</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
@app.route('/flipvertical', methods=['GET', 'POST'])
def flipvertical():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            im  = im.transpose(Image.FLIP_TOP_BOTTOM)
            im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Choose Image to flipvertical</title>
    <h1>Choose Image to flipvertical</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

