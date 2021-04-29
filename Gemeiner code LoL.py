name = input("Wie heist du?\n\n" + "Name :")
name = name.lower()    #macht das groß und kleinscreibung egal ist solange "arvid"

if name in ("arvid"):
#andere möglichleiten sind;
#("arvid", "Arvid"):
#if name == ("arvid") or name == ("Arvid"):


    print ("\nOk " + name + "," + "\n" + "Ich würde sie gerne besträuseln ;)")
else:
    print ("\nOk " + name + "..." + "\n" + "Ich glaube du bist geistig behindert LoL\n\n\n")
