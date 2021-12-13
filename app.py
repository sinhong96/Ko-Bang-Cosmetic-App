import io
import os
import torch
import torchvision.transforms as transforms
from flask import Flask, jsonify, request, render_template, redirect
from PIL import Image
from MobileNetV2 import *

app = Flask(__name__)

# Modelling Task
DEVICE ='cpu'
MODEL = mobilenetv2_19(num_classes=5)
MODEL.load_state_dict(torch.load("epoch_99.pth.tar", map_location=torch.device(DEVICE))) 
MODEL.to(DEVICE)
MODEL.eval()

class_names =  ["Dry skin","Normal skin","Oily skin","Acne skin","Sensitive skin"]

def transform_image(image_bytes):
	my_transforms = transforms.Compose([
		transforms.Resize(256),
		transforms.CenterCrop(224),
		transforms.ToTensor(),
		transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
	])

	image = Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
	tensor = transform_image(image_bytes=image_bytes)
	outputs = MODEL.forward(tensor)
	_, prediction = torch.max(outputs, 1)
	return class_names[prediction]

Cosmetic_recomm = {
	"Dry skin": "Your skin type is dry! We  would like to recommend you to try our company cosmetic products for dry skin!",
	"Normal skin": "Your skin is normal! However, We would like to recommend you to try our company cosmetic products for normal skin!",
	"Oily skin": "Your skin type is oily! We  would like to recommend you to try our company cosmetic products for oily skin!",
    "Acne skin": "Your skin type is acne skin! We  would like to recommend you to try our company cosmetic products for acne skin!",
    "Sensitive skin": "Your skin type is sensitive skin! We  would like to recommend you to try our company cosmetic products for sensitive skin!"
}

# Treat the web process
@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files.get('file')
		if not file:
			return
		img_bytes = file.read()
		prediction_name = get_prediction(img_bytes)
		return render_template('result.html', name=prediction_name, description=Cosmetic_recomm[prediction_name])

	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True,host='0.0.0.0',port=port)  # app.run(debug=True) # app.run(debug=True,host='0.0.0.0',port=port) # 