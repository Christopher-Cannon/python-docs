class entity:
    def __init__(self, name, entity_type, stats):
        self.name = name
        self.entity_type = entity_type
        self.level = 1
        self.stats = stats
        self.poison = False

    def print_entity_info(self):
        print("Name:\t{}\nType:\t{}".format(self.entity_type))

    def poison_add(self):
        self.poison = True

    def poison_remove(self):
        self.poison = False

class player(entity):
    def __init__(self, name, entity_type, stats):
        entity.__init__(self, name, entity_type, stats)
        self.inventory = {"gold":0, "potions":0}

    def inventory_change_gold(self, value):
        self.inventory["gold"] += value

        # So we don't have a negative gold value
        if(self.inventory["gold"] < 0):
            self.inventory["gold"] = 0

    def potion_use(self):
        if(self.inventory["potion"] > 0):
            self.inventory["potion"] -= 1
            self.stats[1] += 50

            # Set hp to max hp if we go over
            if(self.stats[1] > self.stats[0]):
                self.stats[1] = self.stats[0]
        else:
            print("No potions available!")

class enemy(entity):
    def __init__(self, name, entity_type, stats):
        entity.__init__(self, name, entity_type, stats)
        self.drop_items = {"gold":5, "item":""}

def job_menu_ui():
    print('''
Enter a number to choose a job
------------------------------
1 - Fighter
2 - Magician
3 - Medic
''')

def choose_player_job():
    job_menu_ui()

    while(True):
        try:
            choice = int(input("-> "))
        except:
            print("Invalid input")
            continue

        if(not(1 <= choice <= 3)):
            print("Number out of range")
            continue
        else:
            if(choice == 1):
                return "Fighter"
            elif(choice == 2):
                return "Magician"
            else:
                return "Medic"

def generate_stats(job):
    if(job == "Fighter"):
        return {"max_hp":100, "hp":100, "max_mp":30, "mp":30, "str":18, "def":16, "mag":6, "lck":7}
    elif(job == "Magician"):
        return {"max_hp":60, "hp":60, "max_mp":80, "mp":80, "str":8, "def":8, "mag":18, "lck":9}
    elif(job == "Medic"):
        return {"max_hp":80, "hp":80, "max_mp":50, "mp":50, "str":12, "def":18, "mag":10, "lck":12}
    # Enemy stats -- must handle different enemy job types next
    else:
        return {"max_hp":90, "hp":90, "max_mp":40, "mp":40, "str":13, "def":13, "mag":10, "lck":10}

def create_player_character():
    job = choose_player_job():
    bob = player("Bob", job, generate_stats(job))
