# by Kami Bigdely
# Consolidate conditional expressions
all_ingredients = ['cucumber','tomato','onion','lemon juice']
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients):
    if 'cucumber' or 'tomato' or 'onion' or 'lemon juice' not in ingredients:
        print('lacks ingredients.')
        dice(ingredients)
        mix_all(ingredients)
        add_salt()
        pour('lemon juice')
        print('Your yummy shirazi salad is ready!')
    else:
        print("You have all the ingredients for your salad and it is ready!")
if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])