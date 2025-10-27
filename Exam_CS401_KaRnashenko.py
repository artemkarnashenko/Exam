temps = [
    {"date": "27.10.2025", "morning": 11, "day": 14, "evening": 12, "status": "дощ"},
    {"date": "28.10.2025", "morning": 9, "day": 15, "evening": 13, "status": "дощ"},
    {"date": "29.10.2025", "morning": 6, "day": 18, "evening": 10, "status": "мінлива хмарність"},
    {"date": "30.10.2025", "morning": 7, "day": 18, "evening": 12, "status": "мінлива хмарність"},
    {"date": "31.10.2025", "morning": 9, "day": 20, "evening": 12, "status": "сонячно"},
    {"date": "01.11.2025", "morning": 9, "day": 19, "evening": 12, "status": "мінлива хмарність"},
    {"date": "02.11.2025", "morning": 9, "day": 19, "evening": 12, "status": "похмуро"},
    {"date": "03.11.2025", "morning": 8, "day": 19, "evening": 14, "status": "похмуро"},
    {"date": "04.11.2025", "morning": 11, "day": 19, "evening": 14, "status": "мінлива хмарність"},
    {"date": "05.11.2025", "morning": 11, "day": 21, "evening": 15, "status": "мінлива хмарність"},
]
for i in temps:
    avg_temp = round((i["morning"] + i["day"] + i["evening"]) / 3, 1)
    i["avarage_temp"] = avg_temp
for i in temps:
    print(f"{i['date']}\t{i['status']:<12}\t{i['avarage_temp']}°C")
print("\nІнтерактивний прогноз погоди Bucharest:")
print("Введіть дату (або 'exit' для завершення)")
while True:
    user_input = input("Введіть дату: ").strip()
    if user_input.lower() == "exit":
        print("Програму завершено. Дякуємо за використання!")
        break
    found = False
    for i in temps:
        if i["date"] == user_input:
            found = True
            avg = i["average"]
            status = i["status"]
            print(f"\nДата: {i['date']}")
            print(f"Середня температура: {avg} °C")
            print(f"Статус: {status}")
            if "дощ" in status:
                print("Рекомендація: можливий дощ — не забудьте парасольку!")
            elif avg < 5:
                print("Рекомендація: холодно — вдягніться тепліше!")
            elif avg > 15:
                print("Рекомендація: тепло, можна йти без куртки.")
            else:
                print("Рекомендація: погода помірна, вдягайтесь зручно.")
            print()
            break
    if not found:
        print("Дату не знайдено у прогнозі. Спробуйте ще раз.\n")