import numpy as np
import pandas as pd

df = pd.read_csv("vgsales.csv")

missing_Publishers = {'wwe Smackdown vs. Raw 2006': 'THQ',
                      'Triple Play 99': 'EA Sports',
                      'Shrek / Shrek 2 2-in-1 Gameboy Advance Video': 'NA',
                      "Bentley's Hackpack": 'Sony Computer Entertainment',
                      'Nicktoons Collection: Game Boy Advance Video Volume 1': 'NA',
                      'SpongeBob SquarePants: Game Boy Advance Video Volume 1': 'NA',
                      'SpongeBob SquarePants: Game Boy Advance Video Volume 2': 'NA',
                      'Sonic the Hedgehog': 'Sega',
                      'The Fairly Odd Parents: Game Boy Advance Video Volume 1': 'NA',
                      'The Fairly Odd Parents: Game Boy Advance Video Volume 2': 'NA',
                      'Dragon Ball Z: Budokai Tenkaichi 2 (JP sales)': 'Namco Bandai Games',
                      'Cartoon Network Collection: Game Boy Advance Video Platinum Edition': 'Majesco Entertainment',
                      'The Legend of Zelda: The Minish Cap(weekly JP sales)': 'Nintendo',
                      'Sonic X: Game Boy Advance Video Volume 1': 'NA',
                      'Dora the Explorer: Game Boy Advance Video Volume 1': 'NA',
                      'Cartoon Network Collection: Game Boy Advance Video Volume 1': 'NA',
                      'All Grown Up!: Game Boy Advance Video Volume 1': 'NA',
                      'Nicktoons Collection: Game Boy Advance Video Volume 2': 'NA',
                      'Yu Yu Hakusho: Dark Tournament': 'Atari',
                      'SpongeBob SquarePants: Game Boy Advance Video Volume 3': 'NA',
                      'Thomas the Tank Engine & Friends': 'NA',
                      'Dragon Ball GT: Game Boy Advance Video Volume 1': 'NA',
                      'Codename: Kids Next Door: Game Boy Advance Video Volume 1': 'NA',
                      'Teenage Mutant Ninja Turtles: Game Boy Advance Video Volume 1': 'NA',
                      'Stronghold 3': 'SouthPeak Games',  # 7sixty was a subsidiary of southpeack games
                      'Cartoon Network Collection: Game Boy Advance Video Special Edition': 'NA',
                      'Pokémon: Johto Photo Finish: Game Boy Advance Video': 'NA',
                      'Strawberry Shortcake: Game Boy Advance Video Volume 1': 'NA',
                      'Farming Simulator 2011': 'GIANTS Software',
                      'Super Robot Wars OG Saga: Masou Kishin II - Revelation of Evil God': 'Namco Bandai Games',
                      'Disney Channel Collection Vol. 1': 'NA',
                      'Atsumare! Power Pro Kun no DS Koushien': 'Konami Digital Entertainment',
                      'Action Man-Operation Extreme': 'Hasbro Interactive',
                      'Cartoon Network Collection: Game Boy Advance Video Volume 2': 'NA',
                      'Chou Soujuu Mecha MG': 'Nintendo',
                      'Prinny: Can I Really Be The Hero? (US sales)': 'Nippon Ichi Software',
                      'Monster Hunter Frontier Online': 'Capcom',
                      'B.L.U.E.: Legend of Water': 'Hudson Soft',
                      'World of Tanks': 'Xbox Game Studios',
                      'Housekeeping': 'Nintendo',
                      'Bikkuriman Daijiten': '3 OClock',
                      'Silverlicious': 'GameMill Entertainment',
                      'UK Truck Simulator': "SCS Software",
                      'Umineko no Naku Koro ni San: Shinjitsu to Gensou no Yasoukyoku': 'Alchemist',
                      'Xia-Xia': 'GameMill Entertainment',
                      'Mario Tennis': 'Nintendo',
                      'Nicktoons Collection: Game Boy Advance Video Volume 3': 'NA',
                      'Demolition Company: Gold Edition': 'GIANTS Software',
                      'Moshi, Kono Sekai ni Kami-sama ga Iru to suru Naraba.': 'Rejet',
                      'Dream Dancer': 'Zoo Digital Publishing',
                      'Homeworld Remastered Collection': 'Gearbox',
                      'AKB1/48: Idol to Guam de Koishitara...': 'Namco Bandai Games',
                      'Super Robot Monkey Team: Game Boy Advance Video Volume 1': 'NA',
                      'Brothers in Arms: Furious 4': 'Ubisoft',
                      'Dance with Devils': 'Rejet',
                      "Legends of Oz: Dorothy's Return": 'GameMill Entertainment',
                      'Driving Simulator 2011': 'Lightrock Entertainment',
                      'Bound By Flame': 'Focus Home Interactive'}

missing_Publishers


def fill_publisher(name, pub):
    if pd.isnull(pub) and missing_Publishers.get(name, None) != None:
        return missing_Publishers.get(name, None)

    return pub


df["Publisher"] = df.apply(lambda x: fill_publisher(x['Name'], x['Publisher']), axis=1)


#checking for null value again
print((df.isnull().sum()/len(df.index)) * 100)