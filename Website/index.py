from flask import Flask,render_template,request,redirect, url_for
import smtplib
import sqlite3 	


app = Flask(__name__) 
@app.route("/") 
def home(): 
	return render_template("index.html") 
@app.route("/home")
def main(): 
	return render_template("index.html")
@app.route("/error")
def error(): 
	return render_template("error.html")
@app.route("/hakkimizda") 
def hakkimizda(): 
	return render_template("hakkimizda.html")
@app.route("/berkay") 
def berkay(): 
	return render_template("berkay.html") 
@app.route("/ali") 
def ali(): 
	return "Başarılı"
@app.route("/blog") 
def blog(): 
	return "" 	
@app.route("/admin", methods = ["GET","POST"])  
def admin(): 
	return redirect(url_for("error"))

@app.route("/iletisim", methods = ["GET","POST"])  
def iletisim():
	try: 
		if request.method == "POST": 
			adsoyad = request.form.get("adsoyad") 
			mesaj = request.form.get("mesaj")
			content = mesaj
			mail = smtplib.SMTP("smtp.gmail.com",587)
			mail.ehlo()
			mail.starttls()
			mail.login("sentmaildayps@gmail.com","BD010101BD")
			mail.sendmail("sentmaildayps@gmail.com","daypsec@gmail.com",content) 	
	except:  
		return redirect(url_for("error"))
	return render_template("iletisim.html")

@app.route("/yardim") 	
def yardim(): 
	return "" 


@app.route("/giris", methods= ["GET","POST"])
def giris(): 
	db = sqlite3.connect("dayyip.db") 
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS uyeler(kadi,sifre)")
	if request.method == "POST":
		kadi = 	request.form.get("kadi") 
		sifre = request.form.get("sifre") 
		def uyekontrol():
			cursor.execute("SELECT kadi FROM uyeler WHERE kadi = ?",kadi) 
			kullanici_ad = 	cursor.fetchone()
			if (kadi == kullanici_ad):
				cursor.execute("SELECT kadi,sifre FROM uyeler WHERE kadi = ?",kadi)  
				kullanici_sifre = cursor.fetchone() 
				if sifre == kullanici_sifre[1]: 
					return redirect(url_for("home"))
				else: 
					abort(403)
			else: 
				return "KULLANICI ADI BULUNAMADI" 
			uyekontrol() 
	return render_template("giris.html") 
@app.route("/kayit", methods= ["GET","POST"])
def kayit():
	db = sqlite3.connect("dayyip.db") 
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS uyeler(kadi TEXT ,sifre TEXT)") 
	if request.method == "POST": 
		yeni_kadi = request.form.get("yenikadi") 
		yeni_sifre = request.form.get("yenisifre") 
		redeem_kadi = request.form.get("redeemkadi") 
		redeem_sifre = request.form.get("redeemsifre") 
		def uyekayit(): 
			cursor.execute("SELECT kadi FROM uyeler")
			kontrol = cursor.fetchall()
			for i in kontrol:
				if yeni_kadi == i:  
					return redirect(url_for("error")) 
				else: 
					cursor.execute("INSERT INTO uyeler (kadi,sifre) VALUES (?,?)",(yeni_kadi,yeni_sifre)) 
					db.commit()
		if ((redeem_kadi == yeni_kadi) and (redeem_sifre == yeni_sifre)): 
			uyekayit()
		else: 
			return redirect(url_for("error"))
	return render_template("kayit.html")

if __name__ == "__main__": 
	app.run(debug=True)