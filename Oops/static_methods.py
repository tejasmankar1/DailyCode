class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "water ,    ginger,  milk,honey"
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
print(type(ChaiUtils))