import tkinter as tk
from tkinter import messagebox

class Giocatore:
    def __init__(self, nome, ruolo):
        self.nome = nome
        self.ruolo = ruolo
        self.voto = 0

    def assegna_voto(self, voto):
        self.voto = voto


class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = []
        self.punti_totali = 0

    def aggiungi_giocatore(self, giocatore):
        self.giocatori.append(giocatore)

    def calcola_punti(self):
        self.punti_totali = sum(giocatore.voto for giocatore in self.giocatori)
        return self.punti_totali


class Partita:
    def __init__(self, squadra1, squadra2):
        self.squadra1 = squadra1
        self.squadra2 = squadra2

    def gioca(self):
        for squadra in [self.squadra1, self.squadra2]:
            for giocatore in squadra.giocatori:
                pass

        punti1 = self.squadra1.calcola_punti()
        punti2 = self.squadra2.calcola_punti()

        return punti1, punti2


class FantacalcioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fantacalcio")

        self.squadra_a = Squadra("Squadra A")
        self.squadra_b = Squadra("Squadra B")

        self.squadra_a.aggiungi_giocatore(Giocatore("Giocatore 1", "Attaccante"))
        self.squadra_a.aggiungi_giocatore(Giocatore("Giocatore 2", "Difensore"))

        self.squadra_b.aggiungi_giocatore(Giocatore("Giocatore 3", "Centrocampista"))
        self.squadra_b.aggiungi_giocatore(Giocatore("Giocatore 4", "Portiere"))

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Voti Squadra A").grid(row=0, column=0)
        tk.Label(self.root, text="Voti Squadra B").grid(row=0, column=1)

        self.voti_a = []
        self.voti_b = []

        for i, giocatore in enumerate(self.squadra_a.giocatori):
            tk.Label(self.root, text=giocatore.nome).grid(row=i + 1, column=0)
            voto_entry = tk.Entry(self.root)
            voto_entry.grid(row=i + 1, column=1)
            self.voti_a.append(voto_entry)

        for i, giocatore in enumerate(self.squadra_b.giocatori):
            tk.Label(self.root, text=giocatore.nome).grid(row=i + 1, column=2)
            voto_entry = tk.Entry(self.root)
            voto_entry.grid(row=i + 1, column=3)
            self.voti_b.append(voto_entry)

        tk.Button(self.root, text="Calcola Risultato", command=self.calcola_risultato).grid(row=len(self.squadra_a.giocatori) + 1, column=0, columnspan=4)

    def calcola_risultato(self):
        for i, giocatore in enumerate(self.squadra_a.giocatori):
            try:
                voto = float(self.voti_a[i].get())
                giocatore.assegna_voto(voto)
            except ValueError:
                messagebox.showerror("Errore", f"Voto non valido per {giocatore.nome} (Squadra A)")
                return

        for i, giocatore in enumerate(self.squadra_b.giocatori):
            try:
                voto = float(self.voti_b[i].get())
                giocatore.assegna_voto(voto)
            except ValueError:
                messagebox.showerror("Errore", f"Voto non valido per {giocatore.nome} (Squadra B)")
                return

        punti_a, punti_b = Partita(self.squadra_a, self.squadra_b).gioca()

        risultato = f"Punteggio finale:\n{self.squadra_a.nome}: {punti_a}\n{self.squadra_b.nome}: {punti_b}"
        if punti_a > punti_b:
            risultato += f"\n{self.squadra_a.nome} vince!"
        elif punti_a < punti_b:
            risultato += f"\n{self.squadra_b.nome} vince!"
        else:
            risultato += "\nLa partita finisce in pareggio!"

        messagebox.showinfo("Risultato", risultato)


if __name__ == "__main__":
    root = tk.Tk()
    app = FantacalcioApp(root)
    root.mainloop()
