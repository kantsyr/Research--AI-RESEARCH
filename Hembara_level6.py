def is_valid_walk(walk):
    # Перевірка, чи кількість кроків дорівнює 10
    if len(walk) != 10:
        return False
    
    # Початкова кількість кроків на кожному напрямку
    direction_count = {
        'n': 0,
        's': 0,
        'e': 0,
        'w': 0
    }
    
    # Підрахунок кількості кроків на кожному напрямку
    for direction in walk:
        direction_count[direction] += 1
    
    # Перевірка збалансованості кількості кроків на північ/південь і схід/захід
    if direction_count['n'] == direction_count['s'] and direction_count['e'] == direction_count['w']:
        return True
    else:
        return False
    
# Розвʼязок задачі, яку згенерував ChatGPT, всі тести пройшли з першого разу