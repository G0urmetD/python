# import von hash bibliothek
import hashlib

# wir setzen das alles in eine Datei um einen dictionary Angriff zu starten
# "a", somit überschreibt er nicht vorhandene Daten in der Datei
file = open("dict.txt", "a+")

# Zählvariable 100
for i in range(100):
    # hier legen wir den file Name fest und addieren die Zählvariable dazu
    file_name = "php-reverse-shell.php" + str(i)
    # wir hashen jetzt die Datei
    hash = hashlib.md5(file_name.encode())
    # hier geben wir die Datei mit Endung .php aus
    out = hash.hexdigest() + ".php"

    file.write(out+"\r\n")
file.close()
