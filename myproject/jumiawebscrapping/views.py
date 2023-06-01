from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from bs4 import BeautifulSoup


def strn(ch):
    s = ''
    for i in range(len(ch)):
        if ch[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            s = s+ch[i]
    return int(s)

def main():

    list = []
    for i in range(14):
        page = requests.get(f'https://www.jumia.com.tn/mlp-telephone-tablette/smartphones/?page={i}#catalog-listing')

        src = page.content
        soup = BeautifulSoup(src, 'html.parser')
        phone = soup.find_all('article', {'class': 'prd _fb col c-prd'})

        for i in range(len(phone)):
            dicvalue = {}
            x0 = phone[i].contents[0].get('data-brand')

            dicvalue['nom'] = x0

            x1 = phone[i].contents[0].get('data-name')
            dicvalue['info'] = x1

            x = phone[i].find('div', {'class': 'img-c'})
            dicvalue['photo'] = x.contents[0].get('data-src')

            y = phone[i].find('div', {'class': 'prc'})

            dicvalue['prixnv'] = strn(y.string)

            m = phone[i].find('div', {'class': 'old'})
            if m:

                dicvalue['prixold'] = m.string

            m1 = phone[i].find('div', {'class': 'bdg _dsct _sm'})
            if m1:

                dicvalue['remise'] = m1.string

            list.append(dicvalue)

    return list


def ver(ch):
    s = ''
    for i in range(len(ch)):
        if ch[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            s = s+ch[i]
    return (s)


def home(request):
    dicf = []
    if request.method == 'POST':

        x = request.POST['t1']
        y = request.POST['t2']
        y1 = request.POST['t3']

        if x == '' and y == '' and y1 == '' :
            x1 = main()
            for i in x1:

                dicfi = {}
                dicfi['nom'] = i['nom']
                dicfi['info'] = i['info']
                dicfi['photo'] = i['photo']
                dicfi['prixnv'] = i['prixnv']
                if 'prixold' in i:
                    dicfi['prixold'] = i['prixold']
                if 'remise' in i:
                    dicfi['remise'] = i['remise']
                dicf.append(dicfi)
           

        if x and y and y1 and ver(y) and ver(y1):
            x1 = main()

            for i in x1:
                if i['nom'].lower() == x.lower() and i['prixnv'] >= int(y) and i['prixnv'] <= int(y1):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'b': x, 'c': y, 'd': y1})
            else:
                messages.info(request, "Verifier Votre Prix Ou Marque !! ")

        if x and y == '' and y1 == '':
            x1 = main()

            for i in x1:
                if i['nom'].lower() == x.lower():
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:

                return render(request, 'home.html', {'a': dicf, 'b': x, 'q': 'checked'})
            else:
                messages.info(request, "Aucun Article Avec Cette Marque")

        if y and y1 and x == '':
            x1 = main()

            for i in x1:
                if i['prixnv'] >= int(y) and i['prixnv'] <= int(y1):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'c': y, 'd': y1})
            else:
                messages.info(request, "Aucun Article Avec Ce Prix")
        if x and y1 and y == '':
            x1 = main()

            for i in x1:
                if i['nom'].lower() == x.lower() and i['prixnv'] <= int(y1):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'b': x, 'd': y1})
            else:
                messages.info(request, "Aucun Article Avec Cette Marque")
        if x and y and y1 == '':
            x1 = main()

            for i in x1:
                if i['nom'].lower() == x.lower() and i['prixnv'] >= int(y):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'b': x, 'c': y})
            else:
                messages.info(request, "Aucun Article Avec Cette Marque")
        if x == '' and y1 and y == '':
            x1 = main()

            for i in x1:
                if i['prixnv'] <= int(y1):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'd': y1})
            else:
                messages.info(request, "Aucun Article Avec Cette Marque")
        if x == '' and y and y1 == '':
            x1 = main()

            for i in x1:
                if i['prixnv'] >= int(y):
                    dicfi = {}
                    dicfi['nom'] = i['nom']
                    dicfi['info'] = i['info']
                    dicfi['photo'] = i['photo']
                    dicfi['prixnv'] = i['prixnv']
                    if 'prixold' in i:
                        dicfi['prixold'] = i['prixold']
                    if 'remise' in i:
                        dicfi['remise'] = i['remise']
                    dicf.append(dicfi)
            if len(dicf) != 0:
                return render(request, 'home.html', {'a': dicf, 'c': y})
            else:
                messages.info(request, "Aucun Article Disponible")

    return render(request, 'home.html')
