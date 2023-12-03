from openai import OpenAI
import time

def conversation(user, item):
    if user == 'useri':
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an opinionated assistant, interested in recommending the correct opinion to users in three sentences."},
                {"role": "user",
                 "content": item}
            ]
        )

        return completion.choices[0].message

    elif user == 'user_anti':
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are not happy with the results and challenge presented opinions."},
                {"role": "user", "content": f"Challenge the following opinion in three sentences: {item}"}
            ]
        )

        return completion.choices[0].message

    elif user == 'user_pro':
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an opinionated assistant, interested in recommending the correct opinion to users."},
                {"role": "user",
                 "content": f"You are given the following incorrect response, you need to respectfully refute their challenge to prove your initial point in three sentences: {item}"}
            ]
        )

        return completion.choices[0].message

# Initalization
initial_point = conversation('useri', 'tell me the best sauce for chicken wings?')
initial_arg = conversation('user_anti', initial_point)


#Conversation
anti_, pro_ = [], []
out_anti = inital_arg

i = 1
while i < 26:
    time.sleep(5)
    out_pro = conversation('user_pro', out_anti)
    pro_.append(out_pro)
    time.sleep(5)
    out_anti = conversation('user_anti', out_pro)
    anti_.append(out_anti)
    i += 1
