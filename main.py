meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "LMAO": "gülmekten yarılıyorum",
            "SHEESH": "Şaşırma",
            "💀": "komik olmayan bir şey"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    print("Daha fazla düşünüyorsan tekrar dene!")
    
else:
    print("Yanlış sözcüğü koydunuz!Tekrar deneyin!")
