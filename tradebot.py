import time

def run_bot():
    print("Торговый бот запущен!")
    while True:
        print("Анализ рынка...")  # Здесь будет логика торговли
        time.sleep(5)  # Пауза между циклами

if __name__== "__main__":
    run_bot()
