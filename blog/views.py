from django.shortcuts import render
from django.http import HttpResponse

postlar =  [
    {
        "id":1,
        "title": "Python Backend Dasturlashga Kirish",
        "date": "15 Mart, 2024",
        "content": "Python – boshlovchilar uchun eng qulay va kuchli backend tillaridan biridir. Avvaliga HTTP, server va API nima ekanini tushunib oling. Keyin Flask yoki FastAPI kabi engil framework bilan kichik REST API yozib ko‘ring. Har kuni biror kichik endpoint yozish – o‘rganishni tezlashtiradi.",
        "tags": ["dasturlash"]
    },
    {
        "id":2,
        "title": "Nega API Muhim?",
        "date": "10 Mart, 2024",
        "content": "API – backendning yuragi. U frontend bilan muloqot qiladi, ma’lumotlarni yuboradi va qaytaradi. Agar yaxshi API qursangiz, frontendchilar sizni qahramondek ko‘radi. Maslahat: Postman yoki Thunder Client’da API’laringizni test qilib turing – bu ishlab chiqarishda xatolarni kamaytiradi.",
        "tags": ["last", "dasturlash"]
    },
    {
        "id":3,
        "title": "Birinchi Backend Loyihangiz",
        "date": "5 Mart, 2024",
        "content": "Birinchi backend loyihangizni yaratish – haqiqiy dasturchilikni his qilishning eng yaxshi usuli. Masalan, oddiy “To-do list” REST API qiling: foydalanuvchi yaratadi, o‘chiradi, yangilaydi. Kodni GitHub’ga yuklashni unutmang – portfolio uchun juda foydali!",
        "tags": ["last", "dasturlash"]
    },
        {
        "id":2,
        "title": "Nega Sport Muhim?",
        "date": "10 Mart, 2024",
        "content": "API – backendning yuragi. U frontend bilan muloqot qiladi, ma’lumotlarni yuboradi va qaytaradi. Agar yaxshi API qursangiz, frontendchilar sizni qahramondek ko‘radi. Maslahat: Postman yoki Thunder Client’da API’laringizni test qilib turing – bu ishlab chiqarishda xatolarni kamaytiradi.",
        "tags": ["sport"]
    },
    {
        "id":3,
        "title": "Birinchi Sport Loyihangiz",
        "date": "5 Mart, 2024",
        "content": "Birinchi backend loyihangizni yaratish – haqiqiy dasturchilikni his qilishning eng yaxshi usuli. Masalan, oddiy “To-do list” REST API qiling: foydalanuvchi yaratadi, o‘chiradi, yangilaydi. Kodni GitHub’ga yuklashni unutmang – portfolio uchun juda foydali!",
        "tags": ["sport"]
    }
]


# Create your views here.
def index(request):
    songgi_yangiliklar = [post for post in postlar if "last" in post["tags"]]
    data = {
        "posts": songgi_yangiliklar
    }
    return render(request, "blog/index.html", data)


def sport(request):
    sport_postlari = [post for post in postlar if "sport" in post["tags"]]
    data = {
        "posts": sport_postlari
    }
    return render(request, "blog/sport.html", data)

def dasturlash(request):
    dasturlash_postlari = [post for post in postlar if "dasturlash" in post["tags"]]
    data = {
        "posts": dasturlash_postlari
    }
    return render(request, "blog/dasturlash.html", data)


def article(request, post_id):
    post = [post for post in postlar if post["id"]==post_id]
    if post:
        data = post[0]
        return render(request, "blog/article.html", data)
    return HttpResponse("Not found 404 page")