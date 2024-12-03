text = "fallen"
s = '*'*len(text)
while True:
    a = input("Digite um letra ")
    if len(a) > 1:
        print("Digite uma letra")
        continue
    
    s_new = ''
    for se in range(len(text)):
        if text[se] == a:
            s_new += a
        else:
            s_new += s[se]

    s = s_new
    print(s)
    if set(s) == set(text):
        print("Parabens vc acerto")
        break

    
