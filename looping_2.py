def looping(teks):
    for i in range (100):
        if i % 2 == 1:
            print("Ini bilangan ganjil ke-", i)
        else:
            continue
looping("Ini bilangan ganjil ke-")
