from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad

key = 'y8X49agNjGK2rj7M'  # 秘钥，b就是表示为bytes类型
iv = 'y8X49agNjGK2rj7M'  # iv偏移量，bytes类型


def myEnCode(text, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))  # 创建一个aes对象 # AES.MODE_CBC 表示模式是CBC模式
    en_text = aes.encrypt(pad(text.encode('utf-8'), 16, 'pkcs7'))
    encodestrs = base64.b64encode(en_text)  # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')  # 对byte字符串按utf-8进行解码
    return enctext


def myDeCode(dataStr, key, iv):
    encodebytes = base64.decodebytes(dataStr.encode('utf-8'))
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))  # CBC模式下解密需要重新创建一个aes对象
    den_text = aes.decrypt(encodebytes)
    final = unpad(den_text, 16, 'pkcs7')
    return final.decode('utf-8')


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/decode/', methods=['POST'])
@cross_origin()
def decode():
    if request.method == 'POST':
        return myDeCode(request.json.get('text'), key, iv)


@app.route('/encode/', methods=['POST'])
@cross_origin()
def encode():
    if request.method == 'POST':
        return myEnCode(request.json.get('text'), key, iv)


if __name__ == '__main__':
    app.run()
"""
Token:241add6f13a611edacb100163e164883
UserName:U002_U004_qyu
data_type:kr_2pzJiyXdmS7fOOmilzCLoQ==
arg_dict:7dL21SUXKqZtXEv8vlTaONMO14kvMeoWCi+6/teT7NKrizYsNy3V1DNupzscKlA+TYFsDBExWrhqcNGZNGGB8BtA0QMY6SSUgBM1a8f2d9ZJ/DeDrPh5rM+HIem7rLxvTzJJu+PtyBuqUN0eTGOlYg==
"""
