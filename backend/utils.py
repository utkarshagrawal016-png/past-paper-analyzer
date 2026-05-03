def analyze_text(text):
    topics = {
        "DBMS": ["database", "dbms"],
        "SQL Joins": ["join", "inner join", "outer join"],
        "Normalization": ["normalization"],
        "Indexing": ["index"],
        "Transactions": ["transaction"]
    }

    counts = {k: 0 for k in topics}

    text = text.lower()

    for topic, keywords in topics.items():
        for word in keywords:
            counts[topic] += text.count(word)

    return counts


def generate_plan(topic_counts):
    sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

    plan = []
    day = 1
    for topic, _ in sorted_topics:
        plan.append(f"Day {day}: Study {topic}")
        day += 1

    return plan