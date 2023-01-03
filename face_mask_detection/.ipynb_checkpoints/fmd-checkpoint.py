{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5e1e99c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-03-26 22:26:21.281970: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /home/fansan/anaconda3/lib/python3.9/site-packages/cv2/../../lib64:\n",
      "2022-03-26 22:26:21.282036: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "from tensorflow.keras.models import load_model\n",
    "from keras.preprocessing.image import load_img, img_to_array \n",
    "import numpy as np\n",
    "model=load_model('saved_model.h5')\n",
    "img_width,img_height=150,150;\n",
    "face_cascade-cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n",
    "cap=cv2.VideoCapture('video.mp4')\n",
    "img_count_full=0\n",
    "font=cv2.FONT_HERSHEY_SIMPLEX\n",
    "org=(1,1)\n",
    "class_label=''\n",
    "fontScale=1\n",
    "color=(255,0,0)\n",
    "thickness=2\n",
    "while True:\n",
    "    img_count_full+=1\n",
    "    response,color_img=cap.read()\n",
    "    if response==False:\n",
    "        break\n",
    "    scale=50\n",
    "    width=int(color_img.shape[1]*scale/100)\n",
    "    height=int(color_img.shape[0]*scale/100)\n",
    "    dim=(width,height)\n",
    "    color_img=cv2.resize(color_img,dim,interpolation=cv2.INTER_AREA)\n",
    "    gray_img=cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)\n",
    "    faces=face_cascade.detectMultiScale(grey_img,1.1,6)\n",
    "    img_count=0\n",
    "    for(x,y,w,h)in faces:\n",
    "        org=(x-10,y-10)\n",
    "        img_count+=1\n",
    "        color_face=color_img[y:y+h,x:x+w]\n",
    "        cv2.imwrite('input/%d%dface.jpg'%(img_count_full,img_count),color_face)\n",
    "        img=load_img('input/%d%dface.jpg'%(img_count_full,img_count),target_size=(img_width,img_height))\n",
    "        img=img_to_array(img)\n",
    "        img=np.expand_dims(img,axis=0)\n",
    "        prediction=model.predict(img)\n",
    "        if prediction==0:\n",
    "            class_label=\"Mask\"\n",
    "            color=(0,255,0)\n",
    "        else:\n",
    "            class_label=\"No_Mask\"\n",
    "            color=(0,0,255)\n",
    "        cv2.rectangle(color_img,(x,y),(x+w,y+h),(255,0,0),3)\n",
    "        cv2.putText(color_img,class_label,org,font,fontScale,color,thickness,cv2.LINE_AA)\n",
    "    cv2.imshow('Face mask detection',color_img)\n",
    "    if cv2.waitkey(1)&0xFF==ord('q'):\n",
    "        break                     \n",
    "cap.release()\n",
    "cv2.destroyALLWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e7094bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
