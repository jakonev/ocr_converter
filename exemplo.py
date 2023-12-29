import string
import re
import cv2
import nltk
import pytesseract
import spacy

spacy.__version__
nltk.download('punkt')
nltk.__version__

# pln = spacy.load('pt_core_news_sm')

img = cv2.imread('pag.jpg')

pytesseract.pytesseract.tesseract_cmd = "caminho da instalacao do tesseract/Arquivos de Programas/tesee/tesseract.exe"

paragrafos = pytesseract.image_to_string(img)

b = string.punctuation

conteudo = ''
for p in paragrafos:
    conteudo += p

    conteudo

conteudo = conteudo.lower()

lista_sentencas = nltk.sent_tokenize(conteudo)

stop_words = string.punctuation

#
# def preprocessamento(texto):
#     lista = []
#     texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', lista_sentencas)
#     # for token in texto:
#     #     lista.append(token.lemma_)
#     #
#     lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
#     lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
#
#     return lista
#
#
# print(lista_sentencas)