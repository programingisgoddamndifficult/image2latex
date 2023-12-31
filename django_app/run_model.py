from django.http import HttpResponse
from django.shortcuts import render
import base64
import requests
from model.manager import ModelManager


def predict_by_image_filename(image_filename="2.png"):
    IMAGE_PATH = "LaTeX_OCR_PRO-master/data/images/train/"+image_filename
    # try:
    print("entering predition")
    return ModelManager.instance().predict_png(IMAGE_PATH)
    # except:
    #     return 'something wrong happend'


def search_form(request):
    # start page
    return render(request,'search_form.html')


def search(request):
    # result page
    request.encoding = 'utf-8'
    print(request.GET)
    if len(request.GET) > 0:
        image_url = request.GET['info']  # “0.png”
        # a = predict_by_image_filename(image_url)
        # predict_string, gif_path = a[0], a[1]
        predict_string = predict_by_image_filename(image_url)
        image_url = "http://localhost:8020/" + image_url.split("/")[-1].split("\\")[-1]
        gif_path = "LaTeX_OCR_PRO-master/results/vis/"+"vis_82_visualization1.gif"
        gif_path = "http://localhost:8030/" + gif_path.split("/")[-1].split("\\")[-1]
        return render(request,'search_result.html', {
            'image_url': image_url,
            'gif_path': gif_path,
            'predict_string': predict_string
        })
    else:
        return render(request,'search_result.html', {
            'image_url': 'incorrect',
            'gif_path': 'Please input right image URL',
            'predict_string': 'Please input right image URL'
        })
