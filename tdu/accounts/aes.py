import codecs
from Crypto.Cipher import AES

class aesEncryption:

    # def PaddingMes(self,mes):
    #     mes_length = len(mes)
    #     len = round(mes_length / 16)  #四捨五入
    #     new_mes = mes + " "*len
    #     return new_mes


    def Encrypt(self,mes1):
        secret = (b'\xf0\x0e3nE\xa1\x9a\xff\x7f\xf6r\xd6\xf4\x9c\xa9\xaa')
        counter = (b'\xa7\r\xa5u\xd4\xa0h\xb2\x04\x19<8\x8e\xc6$\x82\xc8\x7f\xe9\x99\x0b3\xe3\x05\xe8\x999j-\xf1\xf7\xd5')
        crypto = AES.new(counter, AES.MODE_CTR, counter=lambda: secret)
        mes_length = len(mes1)
        leng = round(mes_length / 16)  # 四捨五入
        mes = mes1 + " " * leng
        encrypted = crypto.encrypt(mes)
        return encrypted

    def Decrypt(self,mes2):
        secret = (b'\xf0\x0e3nE\xa1\x9a\xff\x7f\xf6r\xd6\xf4\x9c\xa9\xaa')
        counter = ( b'\xa7\r\xa5u\xd4\xa0h\xb2\x04\x19<8\x8e\xc6$\x82\xc8\x7f\xe9\x99\x0b3\xe3\x05\xe8\x999j-\xf1\xf7\xd5')
        crypto = AES.new(counter, AES.MODE_CTR, counter=lambda: secret)

        mes = crypto.decrypt(mes2)
        mes = codecs.decode(mes, 'utf-8')
        decrypt = mes.strip()

        return decrypt

