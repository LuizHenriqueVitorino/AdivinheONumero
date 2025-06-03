import tkinter as tk
from tkinter import messagebox, Scrollbar
from random import randint

# TODO: Separar os métodos em classes
# Constantes
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 1000000
MAXIMO_DE_TENTATIVAS = 20
DIMENSAO_DA_TELA = "450x475"

# Variáveis globais
numero_secreto = randint(NUMERO_MINIMO, NUMERO_MAXIMO)
tentativas = 0

# Função de verificar o palpite
def verificar_palpite(event=None):
    global tentativas
    global numero_secreto

    try:
        palpite = int(entry_palpite.get())
        tentativas += 1
        tentativas_restantes = MAXIMO_DE_TENTATIVAS - tentativas

        if palpite < numero_secreto:
            adicionar_historico(f"🔼 {palpite} é muito baixo! ({tentativas_restantes} restantes)")
        elif palpite > numero_secreto:
            adicionar_historico(f"🔽 {palpite} é muito alto! ({tentativas_restantes} restantes)")
        else:
            adicionar_historico(f"✅ {palpite} é o número certo! Você acertou em {tentativas} tentativa(s)!")
            messagebox.showinfo("🎉 Parabéns!", f"Você acertou em {tentativas} tentativa(s)!")
            reiniciar_jogo()
            return

        if tentativas >= MAXIMO_DE_TENTATIVAS:
            messagebox.showinfo("❌ Fim de Jogo", f"Você perdeu! O número era {numero_secreto}.")
            reiniciar_jogo()

    except ValueError:
        messagebox.showwarning("Entrada inválida", "⚠️ Digite um número inteiro válido!")

    entry_palpite.delete(0, tk.END)
    entry_palpite.focus()

# Função para adicionar texto ao histórico
def adicionar_historico(texto):
    historico.config(state="normal")
    historico.insert("1.0", texto + "\n")
    historico.see("1.0")
    historico.config(state="disabled")

# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto
    global tentativas
    numero_secreto = randint(NUMERO_MINIMO, NUMERO_MAXIMO)
    tentativas = 0
    historico.config(state="normal")
    historico.delete(1.0, tk.END)
    historico.config(state="disabled")
    entry_palpite.delete(0, tk.END)
    entry_palpite.focus()

# Criando a janela
janela = tk.Tk()
janela.title("🎯 Adivinhe o Número")
janela.geometry(DIMENSAO_DA_TELA)
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="🎯 Adivinhe o Número 🎯", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Instruções
instrucao = tk.Label(
    janela, 
    text=f"Pensei em um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}.\nVocê tem {MAXIMO_DE_TENTATIVAS} tentativas.",
    font=("Arial", 10)
)
instrucao.pack(pady=5)

# Campo de entrada
entry_palpite = tk.Entry(janela, font=("Arial", 14), justify="center")
entry_palpite.pack(pady=10)
entry_palpite.focus()

# Botão de verificar
botao_verificar = tk.Button(
    janela, text="Verificar", command=verificar_palpite,
    font=("Arial", 12), bg="#4CAF50", fg="white", width=15
)
botao_verificar.pack(pady=5)

# Widget de histórico
frame_historico = tk.Frame(janela)
frame_historico.pack(pady=10)

scrollbar = Scrollbar(frame_historico)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

historico = tk.Text(
    frame_historico, height=10, width=50, state="disabled",
    font=("Arial", 10), yscrollcommand=scrollbar.set, bg="#f0f0f0"
)
historico.pack(side=tk.LEFT)

scrollbar.config(command=historico.yview)

# Botão de reiniciar manual
botao_reiniciar = tk.Button(
    janela, text="Reiniciar Jogo", command=reiniciar_jogo,
    font=("Arial", 10), bg="#f44336", fg="white"
)
botao_reiniciar.pack(pady=5)

# Atalho para Enter ativar o botão verificar
janela.bind('<Return>', verificar_palpite)

# Rodando a janela
janela.mainloop()
