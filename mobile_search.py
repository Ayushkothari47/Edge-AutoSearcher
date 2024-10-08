import subprocess
import time
import random

words = [
    "cat", "dog", "elephant", "giraffe", "tiger", "lion", "bear", "wolf", "fox", "deer", "rabbit", "squirrel", "zebra", "leopard", "cheetah", "horse", "cow", "sheep", "goat", "pig", "chicken", "duck", "goose", "penguin", "owl", "hawk", "eagle", "sparrow", "pigeon", "parrot", "shark", "dolphin", "whale", "seal", "otter", "jellyfish", "starfish", "octopus", "lobster", "crab", "snake", "lizard", "frog", "toad", "butterfly", "bee", "ant", "spider", "scorpion", "beetle", "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "grey", "violet", "indigo", "teal", "cyan", "magenta", "maroon", "beige", "navy", "lime", "chair", "table", "lamp", "phone", "computer", "book", "pencil", "pen", "notebook", "cup", "bottle", "mirror", "spoon", "fork", "knife", "plate", "television", "keyboard", "mouse", "fan", "clock", "bed", "pillow", "blanket", "sofa", "curtain", "door", "window", "carpet", "rug", "doctor", "teacher", "engineer", "lawyer", "nurse", "pilot", "chef", "actor", "musician", "artist", "writer", "police", "firefighter", "scientist", "architect", "designer", "plumber", "electrician", "mechanic", "farmer", "judge", "detective", "driver", "gardener", "carpenter", "accountant", "dentist", "veterinarian", "pharmacist", "photographer","usa", "canada", "mexico", "brazil", "argentina", "germany", "france", "italy", "spain", "portugal", "russia", "china", "india", "japan", "australia", "southafrica", "nigeria", "egypt", "turkey", "greece", "sweden", "norway", "finland", "denmark", "iceland", "thailand", "vietnam", "indonesia", "philippines", "malaysia", "happy", "sad", "angry", "excited", "nervous", "calm", "bored", "curious", "confident", "frustrated", "jealous", "anxious", "relaxed", "grateful", "fearful", "hopeful", "surprised", "shocked", "proud", "embarrassed", "soccer", "basketball", "baseball", "tennis", "cricket", "rugby", "volleyball", "hockey", "swimming", "cycling", "running", "gymnastics", "boxing", "wrestling", "skiing", "snowboarding", "skating", "surfing", "karate", "judo", "software", "hardware", "internet", "cloud", "database", "server", "router", "algorithm", "network", "AI", "robotics", "blockchain", "cybersecurity", "coding", "programming", "automation", "machine", "data", "encryption", "sensor", "car", "bike", "bus", "train", "airplane", "boat", "subway", "motorcycle", "scooter", "tram", "ferry", "yacht", "helicopter", "spaceship", "rocket", "skateboard", "rollerblades", "taxi", "van", "truck", "mountain", "river", "ocean", "forest", "desert", "valley", "volcano", "lake", "waterfall", "canyon", "beach", "island", "rainforest", "savanna", "prairie", "glacier", "hill", "reef", "jungle", "swamp", "apple", "banana", "cherry", "date", "grape", "kiwi", "lemon", "lime", "mango", "melon", "orange", "papaya", "peach", "pear", "pineapple", "plum", "raspberry", "strawberry", "watermelon", "blueberry", "carrot", "broccoli", "spinach", "potato", "onion", "garlic", "pepper", "cucumber", "tomato", "zucchini", "pumpkin", "lettuce", "cauliflower", "celery", "radish", "beet", "cabbage", "eggplant", "asparagus", "mushroom", "star", "planet", "moon", "comet", "asteroid", "galaxy", "blackhole", "nebula", "spaceship", "satellite", "astronaut", "alien", "orbit", "universe", "meteor", "eclipse", "telescope", "constellation", "supernova", "gravity", "guitar", "piano", "drums", "violin", "flute", "trumpet", "saxophone", "cello", "clarinet", "harmonica", "microphone", "speaker", "headphones", "album", "concert", "melody", "lyrics", "song", "band", "orchestra", "shirt", "pants", "dress", "skirt", "hat", "shoes", "socks", "jacket", "coat", "scarf", "gloves", "belt", "tie", "sweater", "blouse", "jeans", "shorts", "suit", "uniform", "boots", "head", "arm", "leg", "hand", "foot", "finger", "toe", "eye", "ear", "nose", "mouth", "teeth", "tongue", "heart", "brain", "stomach", "lung", "liver", "kidney", "skin", "car", "truck", "van", "bus", "motorcycle", "bicycle", "scooter", "skateboard", "train", "airplane", "helicopter", "boat", "submarine", "spaceship", "rocket", "tram", "ferry", "yacht", "glider", "balloon", "circle", "square", "triangle", "rectangle", "oval", "hexagon", "octagon", "pentagon", "cube", "sphere", "pyramid", "cylinder", "cone", "prism", "diamond", "star", "heart", "cross", "parallelogram", "rhombus", "teacher", "doctor", "nurse", "engineer", "scientist", "farmer", "pilot", "chef", "firefighter", "police", "lawyer", "artist", "musician", "actor", "writer", "photographer", "journalist", "architect", "plumber", "electrician", "run", "walk", "jump", "swim", "climb", "dance", "sing", "write", "read", "draw", "paint", "cook", "bake", "drive", "cycle", "fly", "throw", "catch", "lift", "push", "city", "village", "town", "capital", "money", "bank", "restaurant", "school", "university", "hospital", "police", "firestation", "library", "museum", "theater", "park", "zoo", "airport", "hotel", "market", "apple", "banana", "chair", "doctor", "engineer", "mountain", "river", "table", "laptop", "phone", "moon", "space", "planet", "star", "shirt", "pants", "skirt", "cat", "dog", "lion", "eagle", "falcon", "hawk", "swan", "pigeon", "sparrow", "shark", "dolphin", "whale", "octopus", "car", "bus", "train", "plane", "bike", "motorcycle", "ball", "bat", "glove", "goal", "robot", "AI", "network", "software", "cloud", "database", "virus", "malware", "firewall", "security"
]


usedWords = []
timeGap = [9,10,11,13,15]
timeIntrvl = [0.3,0.4,0.5,0.6]


def getRandomTimeGap():
    return random.choice(timeIntrvl)

def adb_tap(x, y):
    """Simulates a tap at coordinates (x, y) on the mobile screen."""
    command = f"adb shell input tap {x} {y}"
    subprocess.run(command, shell=True)
    print(f"Tapped on ({x}, {y})")



def adb_press_key(keycode):
    """Simulates a key press by sending a keycode to the device."""
    command = f"adb shell input keyevent {keycode}"
    subprocess.run(command, shell=True)
    print(f"Pressed key with keycode: {keycode}")


keyMap = [(29,'a'),(30,'b'),(31,'c'),(32,'d'),(33,'e'),(34,'f'),(35,'g'),(36,'h'),(37,'i'),(38,'j'),(39,'k'),(40,'l'),(41,'m'),(42,'n'),(43,'o'),(44,'p'),(45,'q'),(46,'r'),(47,'s'),(48,'t'),(49,'u'),(50,'v'),(51,'w'),(52,'x'),(53,'y'),(54,'z')]


def startSearch():
    counter = 0
    while True:
        print('\n\n')
        i = random.choice(words)
        if counter==30:
            exit()
        time.sleep(random.choice(timeGap))
        if i not in usedWords:
            for j in i:
                # pyautogui.press(j)
                

                for val, alpha in keyMap:
                    if j==alpha:
                        pressBtn = val
                        break
                print(j,"with keystroke",pressBtn)
                    
                adb_press_key(pressBtn)
                time.sleep(getRandomTimeGap())
            # pyautogui.press('enter')
            time.sleep(2)
            adb_tap(965, 2250)
            print("Tap on enter")
            usedWords.append(i)
            time.sleep(2)
            adb_tap(500, 150)
            print("Tap on search bar")
            time.sleep(2)
            adb_tap(950, 175)
            print("Clear search bar")
            counter+=1


def main():
    if __name__ == "__main__":
        DND = input("\nIs your phone in DND Mode [y/n]: ")
        if DND=='n':
            print("\nTurn off DND ! [ENTER TO CONTINUE]...")
            input()
            main()
        else:
            subprocess.run("adb kill-server", shell=True)
            subprocess.run("adb start-server", shell=True)
            subprocess.run("adb devices", shell=True)
            time.sleep(2)
            print("Open your bing and then click on search bar then wait 10 second!")
            time.sleep(2)
            startSearch()
            

        
  
    # Example usage
    # adb_tap(500, 1000)            # Simulate a tap at (500, 1000)
    # adb_press_key(3)               # Press the Home button (keycode 3)

main()