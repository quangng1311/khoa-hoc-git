def display_reading_list(manga_list):
    print("Danh sách đang đọc:")
    for i, manga in enumerate(manga_list, 1):
        print(f"{i}. {manga}")

favorites = ["Chainsaw Man", "Insomniacs After School", "Banished from the Hero's Party"]
display_reading_list(favorites)