def return_data(filename): # im too lazy to change this
    with open(f"./data/{filename}", 'r') as f:
        import random
        return random.choice([line.split() for line in f.readlines()][0])

class text:
    def single():
        return return_data("words")
    
    def phrase(words):
        return "".join(f"{return_data('words')} " for i in range(words)).lstrip(" ")

class personal:
    class name:
        def first():
            return return_data('first_names')
        
        def last():
            return return_data('last_names')
        
        def full():
            return f"{personal.name.first()} {personal.name.last()}"
    class age:
        def number():
            import random
            return random.randint(4,99)
        
        def dob():
            import random, time, datetime
            random.seed(random.randint(1, 999))
            d = random.randint(1, int(time.time()))
            return datetime.date.fromtimestamp(d).strftime('%Y-%m-%d')
        
class conversion:
    def dob_to_age(dob):
        import datetime
        return datetime.datetime.now().year - datetime.datetime.strptime(dob, '%Y-%m-%d').year