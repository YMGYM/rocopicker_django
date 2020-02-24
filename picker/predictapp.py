import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2, os, base64
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings

keras = tf.keras

def predict(model, sent_img):
    # model = keras.models.load_model('../model/rocopicker2') # for debug
    # https://github.com/marcogdepinto/Deep-learning-model-deploy-with-django/blob/master/App/views.py
    
    model = model
    
    try:
        im = cv2.imdecode(np.fromstring(sent_img.read(), np.uint8), cv2.IMREAD_UNCHANGED).astype(np.float32) 
        # https://stackoverflow.com/questions/27517688/can-an-uploaded-image-be-loaded-directly-by-cv2
    except AttributeError:
        im = np.array(sent_img).astype(np.float32)
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        
    regu_im = im * (1.0/255.0) # 이미지 정규화
    resized_img = cv2.resize(regu_im, (299,299)) # 이미지 크기를 맞게 변형
    rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    expdim_img = np.expand_dims(rgb_img, axis=0) # 배치는 1
    result = model.predict(expdim_img)



    frame_buff = cv2.imencode('.jpg', im)[1]
    frame_b64 = base64.b64encode(frame_buff).decode("utf-8")
    
    score = result[0][1]

    if score >= 0.7:
        resultMsg = "이건 로코의 퍼스널리티에 저스트-핏! 이네요! 확실해요!"
    elif score >= 0.6:
        resultMsg = "흠.. 조금 낫-클리어한 로코의 퍼스널리티의 필링이에요!"
    elif score >= 0.3:
        resultMsg = "이건 로코라고 하기엔 낫-클리어한 인스피레이션이네요..."
    else:
        resultMsg = ".. 이건 로코의 포트레이트는 아니네요!"
        
    score = (score * 100)
    return result, frame_b64, score, resultMsg
    #https://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format
    
def load_model():
    model = keras.models.load_model(os.path.join(settings.MODEL_ROOT, "rocopicker2"))
    
    return model