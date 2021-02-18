# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

toxins = ['sodium nitrate', 'sodium benzonate', 'sodium oxide']
# toxin1 = 'sodium nitrate'
# toxin2 = 'sodium benzonate'
# toxin3 = 'sodium oxide'

ingredients = 'sodium benzonate'
def toxin_check(food):
    for i in toxins:
        if i == ingredients:
            print('!!!')
            print('there is a toxin in the food!')    
            print('!!!')
            make_alert_sound()
            break
        else:
            print('***')
            print('Toxin Free')
            print('***')
            make_accept_sound()

toxin_check(ingredients)
# if toxin1 or toxin2 or toxin3 == ingredients:
#     print('!!!')
#     print('there is a toxin in the food!')    
#     print('!!!')
#     make_alert_sound()
# else:
#     print('***')
#     print('Toxin Free')
#     print('***')
#     make_accept_sound()


# for i in toxins:
#     if i == ingredients:
#         print('!!!')
#         print('there is a toxin in the food!')    
#         print('!!!')
#         make_alert_sound()
#     else:
#         print('***')
#         print('Toxin Free')
#         print('***')
#         make_accept_sound()