import tkinter as tk
from tkinter import messagebox, Scrollbar
from app.core import JogoAdivinhacao
from app.config import Config


class JogoUI:
    def __init__(self, root):
        self.jogo = JogoAdivinhacao(Config.NUMERO_MINIMO, Config.NUMERO_MAXIMO, Config.MAXIMO_DE_TENTATIVAS)

        self.root = root
        self.root.title("🎯 Adivinhe o Número")
        self.root.geometry(Config.DIMENSAO_DA_TELA)
        self.root.resizable(False, False)

        self.criar_widgets()
        self.root.bind('<Return>', self.verificar_palpite)

    def criar_widgets(self):
        tk.Label(self.root, text="🎯 Adivinhe o Número 🎯", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(
            self.root,
            text=f"Pensei em um número entre {self.jogo.minimo} e {self.jogo.maximo}.\n"
                 f"Você tem {self.jogo.max_tentativas} tentativas.",
            font=("Arial", 10)
        ).pack(pady=5)

        self.entry_palpite = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry_palpite.pack(pady=10)
        self.entry_palpite.focus()

        tk.Button(
            self.root, text="Verificar", command=self.verificar_palpite,
            font=("Arial", 12), bg="#4CAF50", fg="white", width=15
        ).pack(pady=5)

        frame_historico = tk.Frame(self.root)
        frame_historico.pack(pady=10)

        scrollbar = Scrollbar(frame_historico)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.historico = tk.Text(
            frame_historico, height=10, width=50, state="disabled",
            font=("Arial", 10), yscrollcommand=scrollbar.set, bg="#f0f0f0"
        )
        self.historico.pack(side=tk.LEFT)

        scrollbar.config(command=self.historico.yview)

        tk.Button(
            self.root, text="Reiniciar Jogo", command=self.reiniciar_jogo,
            font=("Arial", 10), bg="#f44336", fg="white"
        ).pack(pady=5)

    def adicionar_historico(self, texto):
        self.historico.config(state="normal")
        self.historico.insert("1.0", texto + "\n")
        self.historico.see("1.0")
        self.historico.config(state="disabled")

    def verificar_palpite(self, event=None):
        try:
            palpite = int(self.entry_palpite.get())
            resultado = self.jogo.verificar_palpite(palpite)

            if resultado == "baixo":
                self.adicionar_historico(
                    f"🔼 {palpite} é muito baixo! ({self.jogo.tentativas_restantes()} restantes)"
                )
            elif resultado == "alto":
                self.adicionar_historico(
                    f"🔽 {palpite} é muito alto! ({self.jogo.tentativas_restantes()} restantes)"
                )
            else:
                self.adicionar_historico(
                    f"✅ {palpite} é o número certo! Você acertou em {self.jogo.tentativas} tentativa(s)!"
                )
                messagebox.showinfo("🎉 Parabéns!", f"Você acertou em {self.jogo.tentativas} tentativa(s)!")
                self.reiniciar_jogo()
                return

            if self.jogo.jogo_acabou():
                messagebox.showinfo("❌ Fim de Jogo", f"Você perdeu! O número era {self.jogo.numero_secreto}.")
                self.reiniciar_jogo()

        except ValueError:
            messagebox.showwarning("Entrada inválida", "⚠️ Digite um número inteiro válido!")

        self.entry_palpite.delete(0, tk.END)
        self.entry_palpite.focus()

    def reiniciar_jogo(self):
        self.jogo.reiniciar()
        self.historico.config(state="normal")
        self.historico.delete(1.0, tk.END)
        self.historico.config(state="disabled")
        self.entry_palpite.delete(0, tk.END)
        self.entry_palpite.focus()
