# bloggers_data.py

class BloggerData:
    def __init__(self):
        self.bloggers = {
            1: {
                "name": "Лебіга",
                "category": "Лайфстайл",
                "description": "Популярний український лайфстайл-блогер.",
                "social": {
                    "instagram": "https://www.instagram.com/misha_lebiga/",
                    "youtube": "https://www.youtube.com/@leb1gastreams"
                },
                "posts": ["Влог №1", "Поради по стилю", "Топ 5 книг"],
            },
            2: {
                "name": "Леви на Джипі",
                "category": "Розважальні",
                "description": "Різні шоу.",
                "social": {
                    "instagram": "https://www.instagram.com/levi_na_jeepi/",
                    "youtube": "https://www.youtube.com/@lions_on_a_jeep/"
                },
                "posts": ["Подорож Карпатами", "Екстремальні дороги України", "Топ 5 джип-тріпів"],
            },
        }

        self.news = [
            "Блогер Лебіга відвідала Київський кінофестиваль",
            "Леви на Джипі випустили нове відео з подорожі Карпатами",
        ]

    def get_all_bloggers(self):
        return self.bloggers

    def get_blogger_by_id(self, blogger_id):
        return self.bloggers.get(blogger_id, None)

    def get_news(self):
        return self.news
