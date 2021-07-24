from flask import Flask, render_template, url_for, request, redirect
from caption import *
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/', methods==['GET'])
def hello():
    return render_template('index.html')


@app.route('/', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)

	
		caption = caption_this_image("static/"+img.filename)



		
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption
		}
	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)
