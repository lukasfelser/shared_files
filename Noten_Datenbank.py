
def Note_ausrechnen(kreuzerl, praesentationen, projekt):

    n_kreuz = ((kreuzerl/61)*104+8)/100 * 30
    n_praes = (praesentationen/100)*30
    n_proj = (projekt/100)*40

    prozent = n_kreuz + n_praes + n_proj
    round_proz = round(prozent, 3)

    notenliste = [100, 91, 80, 70, 60, 50]

    note = 0

    if prozent < notenliste[4]:
        note = 5
    if prozent >= notenliste[4] and notenliste[3]:
        note = 4
    if prozent >= notenliste[3] and prozent < notenliste[2]:
        note = 3
    if prozent >= notenliste[2] and prozent < notenliste[1]:
        note = 2
    if prozent >= notenliste[1]:
        note = 1

    fuer_besser = round((notenliste[note-1] - prozent)*2.5 , 3)
    abgebbar = round((prozent - 91)*2.5, 3)

    if note != 1:
        print(f'Du hast insgesamt {round_proz} Prozent und damit einen {note}er! \nFür einen {note-1}er bräuchtest du {fuer_besser} Prozent zusätzlich in der Projektpräsentation.')
        if fuer_besser < (100-projekt):
            print('Das geht sich aus, wenn dir deine Projektkolleg*innen genug Punkte schenken können, dass du auf 100% kommst!')
        else:
            print('Das wird leider nix, so viele Punkte sind in der Projektpräsentation nicht über!')
    else:
        print(f'Herzlichen Glückwunsch! Du hast einen Einser! Woop woop! /(* ___ *)/ \nInsgesamt hast du {round_proz} Prozent. Du könntest also {abgebbar} Prozent in der Projektpräsentation abgeben und wärst immer noch auf Sehr Gut!')

    return note


# Bitte Anzahl der Kreuzerl, Durchschnitt der beiden besten Präsentation, und Projektpräsentationsdurchschnitt eintragen!
Note_ausrechnen(36, 95, 92)
