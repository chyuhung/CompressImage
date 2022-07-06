from PIL import Image
import os

##图片压缩
def compressImage(srcPath,dstPath):
    for filename in os.listdir(srcPath):

        ##如果存储目录不存在，则创建
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
            print("未找到导出目录 " + dstPath + " 将进行创建！")
            print("导出目录 "+dstPath+" 创建成功!")

        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)

        if os.path.isfile(srcFile):
            sImg=Image.open(srcFile)
            w,h=sImg.size
            print("\n图片名称："+str(sImg))
            print("长："+str(h)+"  宽："+str(w)+" 乘积："+str(w*h))
            num=float(input("请输入压缩比例："))
            dImg=sImg.resize((int(w*num),int(h*num)),Image.ANTIALIAS)
            dImg.save(dstFile)
            w,h=dImg.size
            print("长："+str(h)+"  宽："+str(w)+" 乘积："+str(w*h))
            print(dstFile+" 压缩成功!")

        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

if __name__ == '__main__':
        srcPath = input("导入目录:")
        dstPath = input("导出目录:")
        compressImage(srcPath,dstPath)
