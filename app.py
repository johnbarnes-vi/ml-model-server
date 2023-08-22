from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/flip', methods=['POST'])
def flip_image():
    try:
        # Retrieve the Base64-encoded image from the request
        base64_image = request.json['image']

        # Pad the Base64 string if necessary
        padding_needed = len(base64_image) % 4
        if padding_needed != 0:
            base64_image += "=" * (4 - padding_needed)

        # Decode the Base64 string
        image_data = base64.b64decode(base64_image)
        image_np = np.frombuffer(image_data, np.uint8)

        # Read the image using OpenCV
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Flip the image horizontally
        flipped_image = cv2.flip(image, 1)

        # Encode the flipped image as JPEG
        _, buffer = cv2.imencode('.jpg', flipped_image)
        flipped_base64_image = base64.b64encode(buffer).decode('utf-8')

        # Return the flipped image as Base64
        return jsonify({'flipped_image': flipped_base64_image})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7077)