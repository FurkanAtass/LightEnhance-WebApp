import torch
import numpy as np
from model.IAT_main import IAT
from PIL import Image
from flask import Flask, request, jsonify
import numpy as np
from io import BytesIO
import base64

#device = "cuda" if torch.cuda.is_available() else "cpu"

device = "cpu"

print("App is started.")
app = Flask(__name__)

enhance_pretrain = r'best_Epoch_lol_v1.pth'

## Load Pre-train Weights
model = IAT().to(device)
if device == "cuda":
	model.load_state_dict(torch.load(enhance_pretrain))
else:
	model.load_state_dict(torch.load(enhance_pretrain, map_location=torch.device("cpu")))
print("Model Loaded.")


def scaleDownImage(image):
    width, height = image.size
    
    if width > 500 or height > 500:
        if width > height:
            new_width = 500
            new_height = int(height * (500 / width))
        else:
            new_height = 500
            new_width = int(width * (500 / height))
            
        resized_image = image.resize((new_width, new_height), resample=Image.LANCZOS)
        return resized_image
    
    return image

def readFromBase64(encoded_data):
    decoded_data = base64.b64decode(encoded_data)
    image = Image.open(BytesIO(decoded_data)).convert("RGB")
    return image

@app.route("/enhance", methods=["POST"])
def enhance():
    data = request.get_json()
    imgPil = readFromBase64(data["image"])

    imgPil = scaleDownImage(imgPil)

    imgNp = np.array(imgPil)

    imgNp = imgNp / 255.0

    if imgNp.shape[2] == 4:
        imgNp = imgNp[:, :, :3]
    inputImg = torch.from_numpy(imgNp).float().to(device)
    inputImg = inputImg.permute(2,0,1).unsqueeze(0)

    with torch.no_grad():
        _, _, enhancedImg = model(inputImg)
    print("Model output is obtained.")
    enhancedImgNp = enhancedImg.squeeze(0).permute(1, 2, 0).detach().cpu().numpy()
    enhancedImgNp = (enhancedImgNp * 255).astype(np.uint8)

    enhancedImgPillow = Image.fromarray(enhancedImgNp)
    buffered = BytesIO()
    enhancedImgPillow.save(buffered, format="JPEG")
    imgStr = base64.b64encode(buffered.getvalue()).decode('utf-8')

    result = {
        "result_image" : imgStr
    }
    print("Result is created.")
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
