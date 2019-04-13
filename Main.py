# можна добавити ак в список
follower = []
# логін та пароль
username = ""
password = ""

# Тут прописуємо шлях до текстового документу з майбутніми підписниками
handle = open("AK.txt", "r")
for line in handle:
    follower.append(line)
handle.close()
