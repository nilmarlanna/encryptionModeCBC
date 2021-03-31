from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC,SHA256
from Crypto.Random import random, get_random_bytes
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib


class BlocoCifrado:
    def __init__(self):
        self.senha = ""
        self.dados = ""
        self.modo = ""
        self.modo_hash = ""
        self.chave = None
        self.tag = None
        self.resulto = ""
        self.chave2 = ""
   

    #Todas as chaves secretas devem ser geradas utilizando a fun¸c˜ao PBKDF2 do m´odulo Crypto.Protocol.KDF.
    #Esta fun¸c˜ao gera uma chave secreta a partir de uma senha e um valor aleat´orio de sal (que deve ser armazenado para que se possa recuperar a chave posteriormente).

    def gerar_chave(self, senha):
    #Retorna uma chave do AES, a partir da senha definida pelo usu´ario, e guarda
    #o valor utilizado de sal para recuperação posterior da chave.
        self.salt = get_random_bytes(4)
        self.chave = PBKDF2(self.senha, self.salt)
        pass

    def recuperar_chave(self):
    #Recupera uma chave previamente gerada com o valor armazenado do sal e a senha
    #especificada pelo usu´ario.
        return self.chave


    def gerar_MAC(self, dados):
    #Gera uma tag a partir dos dados, utilizando a chave especificada.
        
        # Encrypt-then-MAC
        if self.modo_hash == 1:
            senha = b'123'
            salt = get_random_bytes(4)
            chave = PBKDF2(senha, salt)
            self.chave2 = chave
            h = HMAC.new(chave, digestmod=SHA256)
            h.update(dados)
            self.tag = h.hexdigest()
            
        # Encrypt-and-MAC
        if self.modo_hash == 2:
            h = HMAC.new(self.chave, digestmod=SHA256)
            h.update(dados)
            self.tag = h.hexdigest()   

        # MAC-then-Encrypt 
        if self.modo_hash == 3:
            h = HMAC.new(self.chave, digestmod=SHA256)
            h.update(dados)
            self.tag = h.hexdigest()        
            

       
    

    def encriptar(self, dados, chave, modo):
    #Encripta os dados, utilizando a chave e o modo de encriptação autenticada
    #que foram especificados.
        if modo == 1:
            cipher = AES.new(chave, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(dados, AES.block_size))
            iv = b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            self.gerar_MAC (ct_bytes)
            ct = ct +str(self.tag)
            self.resultado = json.dumps({'iv':iv, 'ciphertext':ct})
            print(self.resultado)
        
        elif modo == 2:
            cipher = AES.new(chave, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(dados, AES.block_size))
            iv = b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            self.gerar_MAC (dados)
            ct = ct +str(self.tag)
            self.resultado = json.dumps({'iv':iv, 'ciphertext':ct})
            print(self.resultado)
                     
        elif modo == 3:
            cipher = AES.new(chave, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(dados, AES.block_size))
            iv = b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            self.gerar_MAC (dados)
            ct = ct +str(self.tag)
            self.resultado = json.dumps({'iv':iv, 'ciphertext':ct})
            print(self.resultado)             


    def decriptar(self, chave, modo, chave2, tag):
    #Decripta os dados, utilizando a chave e o modo de encriptação autenticada
    #que foram especificados, e realiza a verificação da tag, retornando True
    #ou False, dependendo da validade da tag.
        if modo == 1:
            b64 = json.loads(self.resultado)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(chave, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            print("A messagem e: ", pt)
            h = HMAC.new(chave2, digestmod=SHA256)
            h.update(ct)
            try:
                h.hexverify(tag)
                print("A mensagem '%s' e autentica" % ct)
            except:
                print("A messagem não e autenticada")

        elif modo == 2:
            b64 = json.loads(self.resultado)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(chave, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            print("A messagem e: ", pt)
            h = HMAC.new(chave, digestmod=SHA256)
            h.update(pt)
            try:
                h.hexverify(tag)
                print("A mensagem '%s' e autentica" % ct)
            except:
                print("A messagem não e autenticada")

        elif modo == 3:
            b64 = json.loads(self.resultado)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(chave, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            print("A messagem e: ", pt)
            h = HMAC.new(chave, digestmod=SHA256)
            h.update(pt)
            try:
                h.hexverify(tag)
                print("A mensagem '%s' e autentica" % ct)
            except:
                print("A messagem não e autenticada")
            
        

    def seleciona_hash(self):
        print('''

        [1] - Encrypt-then-MAC
        [2] - Encrypt-and-MAC
        [3] - MAC-then-Encrypt
       
       ''')

        n = int(input('Escolha uma opção: '))

        self.modo_hash = n


    def main(self):
    #Interface da aplicação.
        while True:
            print('''
                    Menu:

                    [1] - Gerar chave
                    [2] - Recuperar chave
                    [3] - Selecionar MAC
                    [4] - Encriptar
                    [5] - Decriptar
            ''')
            n = int(input('Escolha uma opção: '))

            if n == 3:
                self.seleciona_hash()

            if n == 1:
                senha = bytes(input('Digite uma senha: ').encode('utf-8'))
                self.gerar_chave(senha)
                
            if n == 2:
                print (self.recuperar_chave())
            
            resultado = ""
            if n == 4:
                dados = bytes(input('Digite a menssagem para encriptar: ').encode('utf-8'))
                resultado = self.encriptar(dados, self.chave, self.modo_hash)

            if n == 5:
                self.decriptar(self.chave, self.modo_hash, self.chave2, self.tag)

                
            gerar_chave = 1
            recuperar_chave = 2
            gerar_MAC = 3
            encriptar = 4
            decriptar = 5



c = BlocoCifrado()
c.main()