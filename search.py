import json
import statistics

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []

def search_json(json_data, search_string):
    results = []
    keyword = search_string.lower()

    related_items = {}

    for entry in json_data:
        for key, value in entry.items():
            if keyword in key.lower() and key.lower() != "user":
                try:
                    num_value = float(value)
                    if key not in related_items:
                        related_items[key] = []
                    related_items[key].append(num_value)
                except ValueError:
                    continue 

    if not related_items:
        return {"No Item Found"}

    for item, reviews in related_items.items():
        results.append({
            "Item": item,
            "Total Reviews": len(reviews),
            "Average Review": round(statistics.mean(reviews), 2),
            "Minimum Review": min(reviews),
            "Maximum Review": max(reviews),
        })

    
    return results
