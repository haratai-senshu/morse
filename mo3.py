import tkinter
import os
import time
from pygame import mixer

a="－－・－－"
i="・－"
u="・・－"
e="－・－－－"
o="・－・・・"

ka="・－・・"
ki="－・－・・"
ku="・・・－"
ke="－・－－"
ko="－－－－"

sa="－・－・－"
si="－－・－・"
su="－－－・－"
se="・－－－・"
so="－－－・"

ta="－・"
ti="・・－・"
tu="・－－・"
te="・－・－－"
to="・・－・・"

na="・－・"
ni="－・－・"
nu="・・・・"
ne="－－・－"
no="・・－－"

ha="－・・・"
hi="－－・・－"
hu="－－・・"
he="・"
ho="－・・"

ma="－・・－"
mi="・・－・－"
mu="－"
me="－・・・－"
mo="－・・－・"

ya="・－－"
yu="－・・－－"
yo="－－"

ra="・・・"
ri="－－・"
ru="－・－－・"
re="－－－"
ro="・－・－"

wa="－・－"
wo="・－－－"
nn="・－・－・"

daku="・・"
handaku="・・－－・"

ten="・－・－・－"

kako="－・－－・－"
kakotoji="・－・・－・"

hatena="・・－－・・"


root = tkinter.Tk()
root.title(u"モールス信号")
root.geometry("1000x350")

j1 = os.path.dirname(os.path.abspath(__file__))
j2 = j1 + '/' + 'mu' + '/' + 'tan.wav'
print(j2)
j3 = j1 + '/' + 'mu' + '/' + 'cho.wav'
j4 = j1 + '/' + 'mu' + '/' + 'fn.wav'

txt = tkinter.Entry(width=20)
txt.place(x=-90, y=-70)
txt2 = tkinter.Entry(width=20)
txt2.place(x=-100, y=-100)



lbl = tkinter.Label(text='モールスで入力された文字')
lbl.place(x=300, y=10)

frame1 = tkinter.Frame(root , height=300 , width=500, bg="black")
frame1.place(x=10 , y=10)

txt3 = tkinter.Text(root,height=15 , width=138)
txt3.place(x=10 , y=40)

scroll = tkinter.Scrollbar(frame1, orient=tkinter.VERTICAL, command=txt3.yview)
scroll.pack(side=tkinter.RIGHT, fill="y")
#動きをスクロールバーに反映
txt3["yscrollcommand"] = scroll.set

txt4 = tkinter.Entry(width=50)
txt4.place(x=10,y=300)







def tanmu3(event):
    tx0=txt.get()
    if tx0=="1234":
        print(" ")
        time_end2 = time.time()
        txt222= txt2.get()
        tim2 = time_end2- float(txt222)
        print(" ")
        print("______________________")
        print("?? スパン??")
        print(tim2)
        if "r"=="r":
            if tim2 > 0.3:
                q = txt4.get()
                if q==a :
                    txt3.insert('end','ア')
                    txt4.delete(0, tkinter.END)
                elif q==i :
                    txt3.insert('end', "イ")
                    txt4.delete(0, tkinter.END)
                elif q==u :
                    txt3.insert('end', "ウ")
                    txt4.delete(0, tkinter.END)
                elif q==e :
                    txt3.insert('end', "エ")
                    txt4.delete(0, tkinter.END)
                elif q==o :
                    txt3.insert('end', "オ")
                    txt4.delete(0, tkinter.END)
                elif q==ka :
                    txt3.insert('end', "カ")
                    txt4.delete(0, tkinter.END)
                elif q==ki :
                    txt3.insert('end', "キ")
                    txt4.delete(0, tkinter.END)
                elif q==ku :
                    txt3.insert('end', "ク")
                    txt4.delete(0, tkinter.END)
                elif q==ke :
                    txt3.insert('end', "ケ")
                    txt4.delete(0, tkinter.END)
                elif q==ko :
                    txt3.insert('end', "コ")
                    txt4.delete(0, tkinter.END)
                elif q==sa :
                    txt3.insert('end', "サ")
                    txt4.delete(0, tkinter.END)
                elif q==si :
                    txt3.insert('end', "シ")
                    txt4.delete(0, tkinter.END)
                elif q==su :
                    txt3.insert('end', "ス")
                    txt4.delete(0, tkinter.END)
                elif q==se :
                    txt3.insert('end', "セ")
                    txt4.delete(0, tkinter.END)
                elif q==so :
                    txt3.insert('end', "ソ")
                    txt4.delete(0, tkinter.END)
                elif q==ta :
                    txt3.insert('end', "タ")
                    txt4.delete(0, tkinter.END)
                elif q==ti :
                    txt3.insert('end', "チ")
                    txt4.delete(0, tkinter.END)
                elif q==tu :
                    txt3.insert('end', "ツ")
                    txt4.delete(0, tkinter.END)
                elif q==te :
                    txt3.insert('end', "テ")
                    txt4.delete(0, tkinter.END)
                elif q==to :
                    txt3.insert('end', "ト")
                    txt4.delete(0, tkinter.END)
                elif q==na :
                    txt3.insert('end', "ナ")
                    txt4.delete(0, tkinter.END)
                elif q==ni :
                    txt3.insert('end', "ニ")
                    txt4.delete(0, tkinter.END)
                elif q==nu :
                    txt3.insert('end', "ヌ")
                    txt4.delete(0, tkinter.END)
                elif q==ne :
                    txt3.insert('end', "ネ")
                    txt4.delete(0, tkinter.END)
                elif q==no :
                    txt3.insert('end', "ノ")
                    txt4.delete(0, tkinter.END)
                elif q==ha :
                    txt3.insert('end', "ハ")
                    txt4.delete(0, tkinter.END)
                elif q==hi :
                    txt3.insert('end', "ヒ")
                    txt4.delete(0, tkinter.END)
                elif q==hu :
                    txt3.insert('end', "フ")
                    txt4.delete(0, tkinter.END)
                elif q==he :
                    txt3.insert('end', "ヘ")
                    txt4.delete(0, tkinter.END)
                elif q==ho :
                    txt3.insert('end', "ホ")
                    txt4.delete(0, tkinter.END)
                elif q==ma :
                    txt3.insert('end', "マ")
                    txt4.delete(0, tkinter.END)
                elif q==mi :
                    txt3.insert('end', "ミ")
                    txt4.delete(0, tkinter.END)
                elif q==mu :
                    txt3.insert('end', "ム")
                    txt4.delete(0, tkinter.END)
                elif q==me :
                    txt3.insert('end', "メ")
                    txt4.delete(0, tkinter.END)
                elif q==mo :
                    txt3.insert('end', "モ")
                    txt4.delete(0, tkinter.END)
                elif q==ya :
                    txt3.insert('end', "ヤ")
                    txt4.delete(0, tkinter.END)
                elif q==yu :
                    txt3.insert('end', "ユ")
                    txt4.delete(0, tkinter.END)
                elif q==yo :
                    txt3.insert('end', "ヨ")
                    txt4.delete(0, tkinter.END)
                elif q==ra :
                    txt3.insert('end', "ラ")
                    txt4.delete(0, tkinter.END)
                elif q==ri :
                    txt3.insert('end', "リ")
                    txt4.delete(0, tkinter.END)
                elif q==ru :
                    txt3.insert('end', "ル")
                    txt4.delete(0, tkinter.END)
                elif q==re :
                    txt3.insert('end', "レ")
                    txt4.delete(0, tkinter.END)
                elif q==ro :
                    txt3.insert('end', "ロ")
                    txt4.delete(0, tkinter.END)
                elif q==wa :
                    txt3.insert('end', "ワ")
                    txt4.delete(0, tkinter.END)
                elif q==wo :
                    txt3.insert('end', "ヲ")
                    txt4.delete(0, tkinter.END)
                elif q==nn :
                    txt3.insert('end', "ン")
                    txt4.delete(0, tkinter.END)


                elif q==daku :
                    txt3.insert('end', "゛")
                    txt4.delete(0, tkinter.END)
                elif q==handaku :
                    txt3.insert('end', "゜")
                    txt4.delete(0, tkinter.END)
                elif q==ten :
                    txt3.insert('end', "、")
                    txt4.delete(0, tkinter.END)
                elif q==kako :
                    txt3.insert('end', "（")
                    txt4.delete(0, tkinter.END)
                elif q==kakotoji :
                    txt3.insert('end', "）")
                    txt4.delete(0, tkinter.END)
                elif q==hatena :
                    txt3.insert('end', "？")
                    txt4.delete(0, tkinter.END)
                else:
                    txt3.insert('end', " ")
                    txt4.delete(0, tkinter.END)
            else:
                print("no2")
        else:
            print(" ")
        txt2.delete(0, tkinter.END)
    else :
        print(" ")
        #j4
    time_sta = time.time()
    mixer.init()        #初期化
    mixer.music.load(j4)
    mixer.music.play(1)
    def tanmu4(event):
        time_end = time.time()
        tim = time_end- time_sta
        tim = tim
        time.sleep(0.03)
        mixer.music.load(j4)
        mixer.music.stop() # 再生の終了
        
        tx1=txt.get()
        if tx1=="1234":
            print(" ")
        else:
            txt.insert(tkinter.END,"1234")
            print(" ")
        time_sta2 = time.time()
        txt2.insert(tkinter.END, time_sta2)

        if tim > 0.125:
            mo1 = "－"
        else :
            mo1 = "・"

        txt4.insert('end',mo1)

    root.bind('<KeyRelease-Control_L>', tanmu4)
root.bind('<KeyPress-Control_L>', tanmu3)


root.focus_set()
root.mainloop()
