import random

def draw_tarot_card():
    cards = {
        "Eight of Wands": "Vật dụng đang ở rất gần, có thể bạn đã vô tình di chuyển nó trong lúc vội vã.",
        "Queen of Swords": "Hãy suy nghĩ logic và kiểm tra lại những nơi có liên quan đến giấy tờ hoặc bàn làm việc.",
        "The Fool": "Có thể nó bị rơi ở một nơi bạn không ngờ tới, hãy thử tìm ở những góc khuất.",
        "The Magician": "Bạn hoàn toàn có thể tìm ra nó, hãy tập trung nhớ lại hành động cuối cùng."
    }
    drawn_card = random.choice(list(cards.keys()))
    print(f"Lá bài bạn bốc được là: {drawn_card}")
    print(f"Gợi ý tìm đồ: {cards[drawn_card]}")

if __name__ == "__main__":
    print("--- Trợ lý Tarot tìm đồ thất lạc ---")
    draw_tarot_card()