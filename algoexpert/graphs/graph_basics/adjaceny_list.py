from collections import defaultdict
love_connections = [("gamal", "erin"), ("kit", "evan"),
                    ("deniz", "pan"),
                    ("danial", "lydia"),
                    ("liana", "sam"),
                    ("jane", "alex"),
                    ("cami", "juampi")
                ]
lovers = defaultdict(list)
for source, target in love_connections:
    lovers[source].append(target)

print(lovers) 