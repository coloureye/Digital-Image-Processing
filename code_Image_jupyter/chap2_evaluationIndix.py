#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.metrics import structural_similarity as compare_ssim
import math
import cv2

#计算两图像的均方误差 MSE
def MSE(image0,image1):
    [m,n]=image0.shape
    MSE=0
    for i in range(m):
        for j in range(n):
            MSE=MSE+(int(image0[i,j])-int(image1[i,j]))**2              #按公式计算误差累加和
    MSE=MSE/(m*n)
    return MSE

# 计算两图像的信噪比 SNR
def SNR(image0,image1):
    tmp1 = 0
    tmp2 = 0
    [m, n] = image0.shape
    for i in range(m):
        for j in range(n):
            tmp1 += pow(int(image0[i,j]),2)
            tmp2 += pow(int(image0[i,j])-int(image1[i,j]),2)
    snr = 10*math.log10(tmp1/tmp2)
    return snr

# 计算两图像的峰值信噪比 PSNR
def PSNR(image0,image1):
    mse = MSE(image0,image1)
    psnr = 10*math.log10(pow(255,2)/mse)
    return psnr

# 计算两图像的平均绝对误差 MAE
def MAE(image0,image1):
    MAE=0
    [m, n] = image0.shape
    for i in range(m):
        for j in range(n):
            MAE += abs(image0[i, j] - image1[i, j])  # 按公式计算误差累加和
    MAE = MAE / (m * n)
    return MAE

# 计算两图像的结构相似度 SSIM
def SSIM(image0,image1):
    # grayA = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
    # grayB = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    grayA = image0
    grayB = image1
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    return score

