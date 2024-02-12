import requests
import re, random
import telebot

api_key = "6682167872:AAG2da2p_PjcyYsL5GlZUaCWHB2cGF8LzU4"

bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message,
"""Welcome to DarkWeb OSINT 
How to use this
/search (your request)
Eg. /search data leaks                 

You need to use TOR to access these links!
                 
Created by github.com/ZDV16""")
    
@bot.message_handler(commands=['search', 'getonions'])
def send_welcome(message): 
    bot.reply_to(message, "Searching...")
    data=message.text
    newdata=data.replace('/search', '')
    bot.reply_to(message, scrape(newdata))
    
def scrape(newdata): 
    query = newdata
    
    if " " in query:
        query = query.replace(" ","+")
        url = "https://ahmia.fi/search/?q={}".format(query)
        request = requests.get(url)
        content = request.text
        regexquery = "\w+\.onion"
        mined_data = re.findall(regexquery, content)
        
        number = random.randint(1, 9999)
        
        filename = "sites{}.txt".format(str(number))
        print("Saving to", filename)
        mined_data = list(dict.fromkeys(mined_data))
        
        with open(filename, "w+") as _:
            print("")
        for k in mined_data:
            with open(filename, "a") as newfile:
                k = k + "\n"
                newfile.write(k)
        print("Saved to", filename)
        
        with open(filename) as input_file:
            head = [next(input_file) for _ in range(10)]
            contents = '\n'.join(head)
            print(contents)
            
        return contents
    
bot.infinity_polling()                   