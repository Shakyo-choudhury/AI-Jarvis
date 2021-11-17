from my_weather import talk
import datetime
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning I am sars Sir. Please tell me how may I help you")
    elif hour>=12 and hour<18:
        talk("Good Afternoon! I am sars  Sir. Please tell me how may I help you")   
    else:
        talk("Good Evening! I am sars Sir. Please tell me how may I help you")  
if __name__==("__main__"):
    wishme()