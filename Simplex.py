x=int(input("Bazis va bazis bo'lmagan o'zgaruvchilar soni: "))
# Simpleks jadvaldagi bitta satrdagi koeffitsiyentlar soni
y=int(input("Tenglamalar soni: "))
# tenglamalar sistemasidagi tenglamalar soni
cki=[]
cj=[]
for i in range(x):
# for sikl operatori orqali Maqsad funksiya
# koeffitsiyentlarini maxsus cj listga ketma-ket kiritib o'tamiz
    cj.append(float(input(f"Maqsad funksiya {i+1}-hadi: ")))
# Maqsad funksiyasini dastur davomida kiritish
cj.append(0)
# Maqsad funksiya qiymati natijasi dastlab 0 bo'ladi.
# Biz buni cj listning oxiriga qo'shib qo'yamiz
for i in range(y):
    cki.append(0)
# delta j ni topish uchun Cki va Cj lar kerak bo'ladi
bazis=[]
# bazis nomli list bizga jadval tuzib olishimiz uchun kerak
for j in range(y):
# har bir satr uchun ushbu for orqali amallarni bajaramiz
    a=[]
# a nomli list boshidan bo'sh holatda kerak bo'ladi sababi har bir satr
    print(">>>>>>",'')
    for i in range(x):
        a.append(float(input(f"{j+1}-satr x{i+1}-hadning koeffitsiyenti: ")))
    a.append(float(input("ozod hadi: ")))
# har bir satrdan alohida list tuzib olinyapti
    bazis.append(a)
# tuzib olingan listlar bazis nomli listga qo'shilmoqda
xindex=[]
# bizga maxsus indekslar maqsad funksiyadagi qiymatlari
# nolga teng bolmagan ozgaruvchilarni yuklash uchun kerak
delta=[]
# Simpleks jadvalidagi deltaning mos qiymatlarini saqlab
# olish uchun delta nomli list zarur
def transponir(arr):
# maxsus transponirlash uchun funksiya yaratamiz
    x=len(arr)
# x satrlar
    y=len(arr[0])
#y ustunlar
    arr1=[]
# arr1 nomli list hosil qilamiz
    for i in range(len(arr)):
# i ning qiymati 0 va x matritsaning satrlar
#soni(satrlar soni kirmaydi) oralig'ida joylashgan
# ya'ni har bir satr uchun amallar bajarish imkonini beradi
        for j in range(len(arr[0])):
# j ning qiymati 0 va x matritsaning ustunlar
#soni(ustunlar soni kirmaydi) oralig'ida joylashgan
#ya'ni har bir ustun uchun amallar bajarish imkonini beradi
            arr1.append(arr[i][j])
# bu yerda ikki o'lchovli matritsadan oddiy
# bir o'lchovli matritsaga o'tilmoqda
# va qiymatlar arr nomli listga qoshib borilmoqda
    arr2=[]
    for i in range(y):
# ustunlar bo'yicha amallar bajarish
        arr3=[]
        for j in range(x):
# satrlar bo'yicha amallar bajarish
            arr3.append(arr1[i+j*y])
#oradagi elementlarini tashlab faqat bitta
# ustundagilarni qoshib olish
        arr2.append(arr3)
# arr2 ga arr3 ni element sifatida qo'shib boramiz
    return arr2
# bizga arr2 yani transponirlangan qiymatini qaytaradi
newbas=transponir(bazis[:])
# newbas nomli o'zgaruvchiga bazisni
# transponirlangan qiymatini yuklayapmiz
for argument in newbas:
    n=0
    for j in argument:
        n+= j * cki[argument.index(j)]
    n = n-cj[newbas.index(argument)]
    delta.append(n)

while True:
# cheksiz takrorlash amalga oshirilmoqda
#bu jarayon break komandasi bajarilguncha davom etadi
    sigma = []
# simpleks jadvalidagi sigma qiymatlarini
# to'ldirish uchun sigma list yaratib olinmoqda
    for i in bazis:
# simpleks jadvali satrlariga murojaat qilinyapti
        sigma.append(i[-1]/i[delta.index(min(delta))])
# sigma elementlarini tenglama ozod
# hadlarini deltaning minimal elemeti bo'lgan
# hal qiluvchi ustundan tanlab olamiz
    sigmamusb=[]
# sigmausb nomli yangi list yaratilmoqda
    for sigmaelem in sigma:
# sigma nomli list elementlariga sigmaelem
# nom bilan murojaat qilinmoqda
        if sigmaelem>=0:
            sigmamusb.append(sigmaelem)
# agar sigmaelem musbat bo'lsa biz sigmausb listga qo'shib qo'yamiz
    halnuqta=(bazis[sigma.index(min(sigmamusb))][delta.index(min(delta))])
# hal qiluvchi nuqta hal qiluvchi ustun va hal qiluvchi  satr tutashgan nuqta
# hal qiluvhi satr sigmaning musbat eng kichik elementi joylashgan qismda bo'ladi
# hal qiluvchi nuqta halnuqta nomli o'zgaruvchiga o'zlashtirilmoqda
    indexx = [sigma.index(min(sigmamusb)),delta.index(min(delta))]
# hal qiluvchi element joylashgan o'rinni indexxga saqlaymiz
    xindex.append(indexx)
# xindexga indexx
    halsatr = bazis[sigma.index(min(sigmamusb))]
# hal qiluvchi satrni halsatrga o'zlashtirish
    i=0
# siklni sanash uchun i o'zgaruvchi kerak
    for x in halsatr:
        bazis[bazis.index(halsatr)][i] = x / halnuqta
    # hal qiluchi satr elementlarining har birini hal qiluvchi elementga bo'lib chiqamiz
        i += 1
    bazis.append(delta)
    # bazis matritsasiga delta listini qo'shib qo'yamiz

    for satr in range(len(bazis)):
        # bazis satrlari ustida amal bajarish satr bazis satrining indeksi uchun
        for ust in range(len(halsatr)):
            # ust hal qiluvchi satr elementlari indeksi uchun ishlatiladi
            if bazis[satr] != halsatr:
                # hal qiluvchi satr ni o'zidan ayirib qo'ysak 0 bo'lib qoladi
                # shuning uchun hal qiluvchi satrdan tashqari boshqa elementlar bilan amallarni bajaramiz
                if ust != delta.index(min(delta)):
# bazis hal qiluchi ustunni ustida amallar bajarganda bir amaldan keyin bazis va hal qiluvchi
# satr elementlari boshqa elementlarga bog'lanishi o'zgarib ketmasligi uchun bazis hal qiluvchi ustunni o'zgartirmaymiz
                    bazis[satr][ust] -= halsatr[ust] * bazis[satr][delta.index(min(delta))]
# bazis har bir satr hal qiluvchi ustun elementlarini nolga aylantirish uchun ayirishlarni amalga oshiramiz
        bazis[satr][delta.index(min(delta))] = 0
    bazis.pop(-1)
    # delta ni qayta bazis matritsadan chiqarib olamiz
    x = 0
    for deltaem in delta:
        if deltaem >= 0:
            x += 1
# delta qiymatlarini har birini manfiy emaslikka tekshirish
# va agar katta bolsa qiymatni birga oshirish
    if x == len(delta):
        break
# agar delta uzunligi xga teng bo'lganda sikldan chiqish
print("Natija: ")
for indexx in xindex:
    print(f"x{indexx[1] + 1}={round(bazis[indexx[0]][-1], 2)}")
# indeksga ko'ra ozgaruvchilarni qiymatlarni yaxlitlab chiqarish
print("Qolgan o'zgaruvchilar 0 ga teng ")
print(f"Maqsad funksiya L = {round(delta[-1], 3)}")
# Maqsad funksiyasini qiymatini yaxlitlab chiqarib berish
