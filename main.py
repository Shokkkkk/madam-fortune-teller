# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import random


def check_user_name():
    print('Как я могу к тебе обращаться?')
    name = input()
    print(name)

    return name


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Здравствуй, {name}.')  # Press ⌘F8 to toggle the breakpoint.
    print('Хочешь получить предсказание?')


def view_prediction():
    id_prediction = random.randint(0, 10)
    with open('predictions.json') as f:
        predict_json = json.loads(f.read())

    predict = predict_json.get(str(id_prediction))
    print(predict)

    return predict


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
