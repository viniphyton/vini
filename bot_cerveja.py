from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Insira o token do seu bot aqui
TOKEN = '7546924817:AAEGDwmue39poczoGlYuL-cvfTcY35fCZcE'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🍻 Olá! Eu sou o bot que calcula o preço por litro da cerveja. \n"
        "Envie a mensagem no formato: \n\n"
        "Preço em R$ e Volume em ml. \n"
        "Exemplos válidos:\n"
        "5 350\n"
        "3.50 550\n"
        "3,50 550"
    )

def calcular(update: Update, context: CallbackContext) -> None:
    try:
        # Pega a mensagem enviada pelo usuário e substitui vírgulas por pontos
        mensagem = update.message.text.strip().replace(',', '.')
        
        # Divide a mensagem em duas partes (preço e volume)
        preco, volume = map(float, mensagem.split())

        # Converte o volume para litros
        volume_em_litros = volume / 1000

        # Calcula o preço por litro
        preco_por_litro = preco / volume_em_litros

        # Responde com o resultado formatado
        update.message.reply_text(f"🍺 Preço por litro: R$ {preco_por_litro:.2f}/L")

    except ValueError:
        update.message.reply_text(
            "❌ Formato inválido. Envie o preço e o volume separados por espaço.\n\n"
            "Exemplos válidos:\n"
            "5 350\n"
            "3.50 550\n"
            "3,50 550"
        )

def main() -> None:
    # Configura o Updater e o Dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Comandos que o bot aceita
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, calcular))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
