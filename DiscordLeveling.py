from aiohttp import ClientSession
from PIL import Image, ImageFont, ImageDraw
import io

async def level_maker(background,avatar,username,current_exp:int,level:int,max_exp:int,bar_color:str):
    async with ClientSession() as client:
        async with client.get(avatar) as response:
            avatar = await response.read()
    avatar = Image.open(io.BytesIO(avatar)).resize((170,170))

    async with ClientSession() as client:
        async with client.get(background) as response:
            background = await response.read()

    background = Image.open(io.BytesIO(background))

    overlay = Image.open("./assets/overlay1.png")
    
    background = background.resize(overlay.size)
    background.paste(overlay,(0,0),overlay)

    myFont = ImageFont.truetype("./assets/welcomedont.otf",40)
    draw = ImageDraw.Draw(background)

    draw.text((205,(327/2)+20), username,font=myFont, fill="white",stroke_width=1,stroke_fill=(0, 0, 0))
    bar_exp = (current_exp/max_exp)*420
    if bar_exp <= 50:
        bar_exp = 50    

    try:
        if current_exp >= 100000:
            current_exp = str(current_exp)[0:3] + "." + str(current_exp)[3] + "k"
    
        if max_exp >= 100000:
            max_exp = str(max_exp)[0:3] + "." + str(max_exp)[3] + "k"
    except Exception:
        pass
    
    
    try:
        if current_exp >= 10000:
            current_exp = str(current_exp)[0:2] + "." + str(current_exp)[2] + "k"
    
        if max_exp >= 10000:
            max_exp = str(max_exp)[0:2] + "." + str(max_exp)[2] + "k"
    except Exception:
        pass
    


    try:
        if current_exp >= 1000:
            current_exp = str(current_exp)[0]+"."+str(current_exp)[1]+"k"
    
        if max_exp >= 1000:
            max_exp = str(max_exp)[0]+"."+str(max_exp)[1]+"k"
    except Exception:
        pass

    

    myFont = ImageFont.truetype("./assets/welcomedont.otf",30)
    draw.text((197,(327/2)+125), f"LEVEL - {level}",font=myFont, fill="white",stroke_width=1,stroke_fill=(0, 0, 0))

    draw.text((525,(327/2)+125), f"{current_exp}/{max_exp}",font=myFont, fill="white",stroke_width=1,stroke_fill=(0, 0, 0))

    mask_im = Image.open("./assets/mask_circle.jpg").convert('L').resize((170,170))
    background.paste(avatar, (13, 65), mask_im)

    im = Image.new("RGB", (490, 51), (0, 0, 0))
    draw = ImageDraw.Draw(im, "RGBA")
    draw.rounded_rectangle((0, 0, 420, 50), 30, fill=(255,255,255,50))
    draw.rounded_rectangle((0, 0, bar_exp, 50), 30, fill=bar_color)
    background.paste(im, (190, 235))
    f= open("./level.png", "wb") 
    background.save(f, "PNG")
    return "./level.png"