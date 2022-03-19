def return_array(filename): # im too lazy to change this
    with open(f"./data/{filename}", 'r') as f:
        import random
        return random.choice([line.split() for line in f.readlines()][0])

class text:
    def single():
        return return_array("words")
    
    def phrase(words):
        return "".join(f"{return_array('words')} " for i in range(words)).lstrip(" ")

class personal:
    class name:
        def first():
            return return_array('first_names')
        
        def last():
            return return_array('last_names')
        
        def full():
            return f"{personal.name.first()} {personal.name.last()}"