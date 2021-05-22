from googletrans import Translator


translater =Translator()
out =translater.translate("क्या हाल है",dest="en")
print(out)