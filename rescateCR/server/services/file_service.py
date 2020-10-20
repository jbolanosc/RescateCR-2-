import os
from werkzeug import secure_filename
from .. import app


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def upload_file(file):
    if file and allowed_file(file):
        filename = secure_filename(file)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return filename
