import mysql.connector
kydb = mysql.connector.connect(
    host = "bjngncktssejoh2aveqb-mysql.services.clever-cloud.com",
    user = "u46ncc7myfzsh8zr",
    password = "BVK9GOH4hnPr7PB9QcCp",
    database = 'bjngncktssejoh2aveqb'
)

kycursor = kydb.cursor()
kycursor.execute("SELECT url FROM url_imag WHERE tipo = 'saludo'")
resultado = kycursor.fetchall()
print(len(resultado))

    




