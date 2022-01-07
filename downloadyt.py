import pafy

video = input("Masukan Link : ")
scrap = pafy.new(video)
print("Judul :")
print(scrap.title)
print("Like :")
print(scrap.likes)
print("Mendownload...")
fzx = scrap.getbest()
fzx.download()
print("Sukses..")
print("Cek Folder Dimana Script Ini Berada")
## SC YTDOWNLOAD BY FAIZGANZ