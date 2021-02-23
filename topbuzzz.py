# -*- coding: utf-8 -*-

from helium import *
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import sys
from random import randint

contador = 1
diretorio = os.path.dirname(os.path.abspath(__file__))
categorias = os.listdir(diretorio + '/videos/')
loop = int(input('Quantas contas quer colocar vídeos? '))
emails = {}
conta_atual = False
senha_atual = False

for n in range(loop):

    conta_atual = input(f'Insira o email da {contador}ª conta: ')
    senha_atual = input('\nAgora a senha: ')
    emails[conta_atual] = senha_atual
    contador+=1
    os.system('cls')


contador = 1

for categoria in categorias:

    print(f'{contador} - '+categoria)
    contador+=1

selec = int(input('Selecione a categoria: '))
videos = os.listdir(diretorio+'/videos/'+categorias[selec - 1])
print(videos)
thumbs = os.listdir(diretorio + '/thumbs/')
videos_loop = int(input('Quantas postagens em cada conta? '))
options = Options()
options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
browser = start_chrome('https://www.topbuzz.com/creators?language=ja-jp', options = options)
click('ログイン')
click('Emailからログイン')

for email in emails:

    write(email, into ='メール')
    write(emails[email], into = 'パスワードを入力する')
    click('ログイン')
    sleep(5)
    go_to('https://www.topbuzz.com/profile_v2/video')
    send = browser.find_element_by_tag_name('input')

    for n in range(videos_loop):

        video_selecionado = videos[randint(0, len(videos) - 1)]
        print(video_selecionado)
        print(diretorio + '/videos/'+ categorias[selec - 1]+ '/' + video_selecionado)
        input(' ')
        send.send_keys(diretorio + '/videos/'+ categorias[selec - 1]+ '/' + video_selecionado)
        write(video_selecionado.split('.')[0], into = 'タイトル（3-45バイト）')
        write(video_selecionado.split('.')[0], into = '動画の説明（1000バイト以内）')
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div').click()
        click('サムネイル設定')
        elementos = browser.find_elements_by_tag_name('input')
        elementos[1].send_keys(diretorio+'/thumbs/'+video_selecionado.split('.')[0] + '.jpg')
        click('提出')

        while 1:

            try:
                click('公開する')
            except:
                sleep(10)
            else:
                break
        try:
            click('公開する')
        except:
            pass

        wait_until(Text('全部').exists, timeout_secs = 60)
        go_to('https://www.topbuzz.com/profile_v2/video')
