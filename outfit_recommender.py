def recommend_outfit(weather, occasion):
    outfit = ""

    if weather == "cold":
        if occasion == "formal":
            outfit = "Wool coat, dress shirt, trousers"
        else:
            outfit = "Sweater, jeans, boots"
    elif weather == "rainy":
        outfit = "Waterproof jacket, umbrella, waterproof shoes"
    else:  # sunny or warm
        if occasion == "formal":
            outfit = "Blazer, dress shirt, chinos"
        else:
            outfit = "T-shirt, shorts, sneakers"

    return outfit

def main():
    print("Welcome to Outfit Recommender!")
    weather = input("Enter the weather (cold, rainy, sunny): ").lower()
    occasion = input("Enter the occasion (formal, casual): ").lower()

    outfit = recommend_outfit(weather, occasion)
    print(f"Recommended outfit: {outfit}")

if __name__ == "__main__":
    main()
#hii
