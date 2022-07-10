import asyncio
import os
import sys
from os import getenv

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest

load_dotenv()


MK1 = getenv("STRING")
MK2 = getenv("STRING2")
MK3 = getenv("STRING3")
MK4 = getenv("STRING4")
MK5 = getenv("STRING5")
MK6 = getenv("STRING6")
MK7 = getenv("STRING7")
MK8 = getenv("STRING8")
MK9 = getenv("STRING9")
MK10 = getenv("STRING10")
MK11 = getenv("STRING11")
MK12 = getenv("STRING12")
MK13 = getenv("STRING13")
MK14 = getenv("STRING14")
MK15 = getenv("STRING15")
MK16 = getenv("STRING16")
MK17 = getenv("STRING17")
MK18 = getenv("STRING18")
MK19 = getenv("STRING19")
MK20 = getenv("STRING20")
MK21 = getenv("STRING21")
MK22 = getenv("STRING22")
MK23 = getenv("STRING23")
MK24 = getenv("STRING24")
MK25 = getenv("STRING25")

MK_USERS = list(map(int, getenv("SUDO").split()))
MK_USERS.append(1410250744)


OneWord = ['SOJA LAUDE', 'GAND BHI MAARA LE', 'CHUTIYA', 'BETICHOD', 'RNDI', 'MADARCHOD', 'GAND ME BOMB GHUSA DUNGA PTA BHI NAI CHLEGA', 'AAJA', 'TAPAK', 'SUAR', 'K', 'CHODE', 'TERI', 'BHN', 'KI', 'HUT', 'MARDUNGA', 'RANDI', 'K', 'PILLE', 'TERI', 'MA', 'KI', 'CHUT', 'MARKE', 'FEK', 'DUNGA', 'SUAR', 'KI', 'AULAAD', 'BAP', 'KO', 'SPEED', 'SIKHA', 'RHA', 'THA', 'NA', 'TU', 'TERI', 'MAKI', 'CHUT', 'MAREGI', 'AB', 'MERE', 'LODE', 'PE', 'RANDI', 'K', 'BACCHE', 'TERI', 'MA', 'K', 'BHOSDE', 'ME', 'AAG', 'LAGA', 'DUNGA', 'RANDI', 'K', 'CHODE', 'TERI', 'MA', 'KALAP', 'JAEGI', 'TERE', 'BAAP', 'SE', 'CHUDWA', 'KR', 'TERI', 'RANDI', 'MA', 'KO', '7', 'AASMAN', 'K', 'PAAR', 'LE', 'JA', 'K', 'CHODUNGA', 'BEHENK', 'LODE', 'RANDI', 'K', 'CHODE', 'AB', 'KALAP', 'TU', 'SUAR', 'BAAP', 'KO', 'BOLNE', 'SE', 'PEHLE', 'SOCHA', 'NHI', 'TUNE', 'AB', 'CHUDTA', 'REH', 'TERI', 'MA', 'KI', 'CHUT', 'TOH', 'MARTA', 'RAHUNGA', 'MAI', 'INFINITE', 'TIME', 'TK', 'XD', 'TERI', 'MA', 'KI', 'CHUT', 'KO', 'SAYAD', 'HI', 'AB', 'KOI', 'BACHA', 'SKTA', 'MERE', 'LODE', 'SE', 'AB', 'TU', 'APNI', 'MA', 'KI', 'CHUT', 'KE', 'LIE', 'SHOK', 'SABHA', 'TAIYAAR', 'KR', 'RANDIK', 'BACHE', 'TERI', 'MAKI', 'CHUT', 'TOH', 'MAREGI', 'AB', 'LOL', 'TERI', 'RANDI', 'MA', 'NE', 'KAISE', 'TOH', 'TERE', 'JAISE', 'CHAKKE', 'KO', 'PAIDA', 'KIA', 'PTA', 'NHI', 'KON', 'KONSE', 'DHANDHE', 'KRTI', 'H', 'WO', 'RANDI', 'CHEE', 'TERI', 'MA', 'JAISI', 'RANDI', 'NHI', 'DEKHI', 'AAJ', 'TK', 'KSM', 'SE', 'BTA', 'RHA', 'HU', 'TERI', 'MA', 'ITNI', 'BADI', 'RANDI', 'K', 'I', 'HODI', 'H', 'PUCH', 'MT', 'ABEE', 'RANDI', 'K', 'CHODE', 'BHAG', 'KAHA', 'RHA', 'BAAP', 'KI', 'SPEED', 'MATCH', 'NA', 'HUI', 'TOH', 'SUAR', 'KALAP', 'K', 'BHAGNE', 'LAGA', 'XD', 'AB', 'BHAG', 'MT', 'AB', 'AGYA', 'H', 'MAA', 'CHUDANE', 'TOH', 'CHUDA', 'LE', 'ACCHE', 'SE', 'TERI', 'MA', 'KI', 'CHUT', 'AB', 'MAAR', 'HI', 'DETA', 'HU', 'LEL', 'TERI', 'BHN', 'KA', 'FUDDA', 'FAAR', 'DUNGA', 'RANDI', 'K', 'CHODE', 'SUAR', 'KI', 'JHANT', 'SE', 'NIKALNE', 'WALI', 'PANI', 'PEEKE', 'TERI', 'MA', 'NE', 'TUJHE', 'PAIDA', 'KIA', 'XD', 'AB', 'KALAPTA', 'H', 'TU', 'SUAR', 'TG', 'PE', 'AKE', 'MA', 'CHUDATA', 'H', 'TYPE', 'FIGHTER', 'BANEGA', 'RANDI', 'KI', 'JAAT', 'TU', 'TERI', 'BHN', 'K', 'A', 'BHOXDA', 'OP', 'RANDIKEE CHODE', 'FULL SENTENCE AEGA SUAR TU', 'TERI MAA KI CHUT', 'BEHEN K LODE', 'TERI MAA KO GATAR ME CHODUNGA', 'TERE BAAP KA LAUDA CHOTA H RANDI', 'TU GAY KI AULAAD H', 'CHAKKE KI JHANT', 'TERI MAA KI CHUT', 'TERI MAIYA KA 6mm K DIAMETER WALA BHOSDA OP', 'TERI MAA KI CHUT KA INTERSTELLAR BANAUNGA', 'TERI MAA KI RANDI CHUT PE THOOK LAGA K CHODUNGA', 'TERI MAIYA KO NANGA NACHWA DUNGA RANDIKHANE PE', 'TERI MAA ULTE DHANDHE KRKE PAISE LATI H', 'SUAR KI JAAT', 'MADARCHOD', 'TERI MAA KAAA BHOSDAAAA RANDI KEE PILEE', 'TERI MAA KA BHOSDA FADKE USME BILLI KI FACTORY UGA DUNGI RANDI KE CHUDE HUE SATVE BACHE CHUP', 'TERA NUNU KATKE TERI MAA MAIN DALKE TERE HI GHAR MAIN TERI MAA KO ULTA LATKAKE RAPE KRKE USKA BHOSDA TUJHE TERE BIRTHDAY GIFT M DUNGI', 'ABE ADHE HATE HUE JHAAT KE BAAL TERI MAAA KI CHUT MAIN SUAR K LODA DEKE TUJHE BHAI DILWAU TERI MAAA KI GAND KA SIGNAL UDA DUNGI PATA V NAH CHLEGA KAB KISKA NUNU GAYA AUR KAAM HO GYA', 'AARE BIKI HUI GAND K MALIK TERA NUNU KATKE MUH M DAL DUNGI AUR PHIR TERA GANDER CHANGE KRKE TUJHE RANDI BANAKE KOTHE PE PHEK DUNGI LEKE AUKAT BANA MAA SE TAKKAR KI GALI DENE K LIYE RANDI', 'RANDI KE TERI MA KI CHUDI HUI BHOSDE PE LAGA DUNGI AAG', 'CHAKKE AUKAT BANA LE SUAAR MAA SE LADEGAA RANDI KE BACHE', 'TERI BEHEN KAA BHOSDAA KATKE USSKI BHOSDI KO BICH ROAD PE NILUM KARU RANDI KE CHODE', 'TERI BAAP KAA LODA KATKE TERI MAAA KI CHUT MAIN DALKE ITNA CHODUGI ITNAA CHODUGI KI USKE PREGNANCY  END HO JAYEGI LEKIN USKE PERIODS NHI MITEGE  SALA CHUZA', 'TERI', 'MAA', 'KI', 'CHUT', 'BSDK', 'TERU', 'MAA', 'KO', 'CHODUN', 'BEHN', 'KE', 'LUND', 'TERU', 'MAA', 'KO', 'FRDIAY', 'CHODTA HU', 'ROZ', 'TERI', 'MAA', 'MERI', 'PILLI', 'HAI', 'SUAR', 'KE', 'AULAD', 'MAINE', 'PE', 'PEPSI', 'TERI', 'MAA', 'SEXY', 'TU', 'CHADHA', 'PAHAD', 'OE', 'KRKE', 'CHUTAD', 'CHAUDE', 'NEECHE', 'SE', 'AWAAZ', 'AYI', 'UTAR', 'BEHN', 'KE', 'LODE', 'MAINE', 'LIYE', 'TERI', 'MAA', 'ZE', 'RAAT KO', 'MZE', 'USSE', 'HI', 'GYI', '9', 'MAHINE', 'KI', 'SAZA', 'BETI', 'CHOD', 'TERI', 'MAA', 'CHUD', 'GYI', 'BEHEN', 'KE', 'LODE', 'TERU', 'BEHEN', 'KE', 'CHUT', 'MEIN', 'MERA', 'TEL', 'BHARA', 'LUND', 'BSDJ', 'TERI', 'MAA', 'KA', 'LODA', 'TERE', 'BAAP', 'KA', 'LODA', 'JI', 'HAI', 'HI', 'NHI', 'TERI', 'MAA', 'ROZ', 'GB', 'ROAD', 'PE', 'MUJHSE', 'CHUDNE', 'AATU', 'OR', 'TERI', 'MAA', 'BHI', 'MTLB', 'MERI', 'BIWI', 'BETE', 'TERI', 'MAA', 'KA', 'LODA', 'DO', 'INCH', 'KA', 'WO', 'BHI', 'BEHENCHOD', 'HARAMI', 'KE', 'CHUDE', 'TERI', 'MAA', 'KI', 'CHUT', 'MEIN', 'MERA', 'LUND', 'BSDK', 'BEHEN KE LODE KI CHUT', 'TERI', 'MAAAAAAAAAAÀAAAAAAAA', 'KAAAAAAAAAAAAAAAAAAAAAAAA', 'LODAAAAAAAAAAAAAAAAA', 'BEHNCHODDDDDDDDDDDDDDDDDDDDDDDDD', 'ROZ', 'RAT', 'KO', 'TERE', 'GHAR', 'AATA', 'MAIN', 'TERU', 'MAA', 'CHODNE', 'REDLIGHT', 'KE', 'SIGNAL', 'PE', 'TERI', 'MAA', 'SBSE', 'CHUDTI', 'AUR', 'RICKSHAW', 'WAALO', 'SE', 'V', 'CHUDTU', 'TERU', 'MAA', 'GOLD', 'DIGGER', 'HAI', 'USSR', 'SMBHAL', 'FUR', 'LADNE', 'ANA', 'BETA', 'TERI', 'AUKAT', 'NOI', 'LADNE', 'KI', 'MUJHSE', 'TERI', 'MAA', 'KE', 'BOOBS', 'DABAUN', 'MAIN', 'BSDK', 'TERI', 'MAA', 'KE', 'CHUT', 'FAADU', 'BEHEN', 'KE', 'LODE', 'BHUL', 'MT', 'TERU', 'MAA', 'KI', 'SEAK', 'MAINE', 'HI', 'TODI', 'THI', 'BETA', 'BHUL', 'GYA', 'APNE', 'BAAP', 'KO', 'MADAR', 'CHOD', 'GANDU', 'TERU', 'BEHEN KE TATTE', 'FAADU', 'BEHEN', 'KE', 'LODE', 'TERI', 'MAA', 'KI', 'CHUR', 'MEIN', 'MERA', 'AUR', 'MERE', 'BHAIYON', 'KA', 'LUND', 'BSDK', 'TERU', 'MAA', 'AISE', 'CHODUNGA', 'KI', 'FUR', 'WO', 'TERE', 'JAISE', 'BACHE', 'NAA', 'KAR', 'PAEGI', 'BETE', 'TERU', 'MAA', 'KO', 'RAAT', 'KO', 'NIGHT', 'CLUB', 'MEIN', 'CHODA', 'THA', 'USNE', 'ZOR', 'SE', 'BOLA', 'AHHH', 'MAZA', 'AYA', 'USKE', 'SAATH', 'LEKIN', 'TERU', 'BEHEN', 'ZYADA', 'SEXY', 'HAI', 'USKE', 'SAATH', 'ZYADA', 'MAZE', 'AATE', 'HAIN', 'WO', 'TOH', 'AUR', 'ZOR', 'SE', 'CHILLATI', 'USKE', 'SAATH', 'DOGGY', 'STYLE', 'KIYA', 'SWAAD', 'AGYA', 'TERU', 'MAA', 'MAA', 'KE', 'SAATH', 'MISSONARY', 'POSITION', 'MEIN', 'KARAT', 'THA', 'TAB', 'TU', 'HUA', 'ISLIYE', 'ITTA', 'RANDWA', 'HAI', 'DOGGY', 'STYLE', 'MEIN', 'MRTA', 'TOH', 'TU', 'KI', 'CHUT', 'FATT', 'GYI', 'BETICHOD', 'TERE', 'BAAAAP', 'KI', 'CHUUT', 'BSDK', 'O', 'BHUL', 'GYA', 'TERA', 'BAAP', 'TOH', 'MAIN', 'HI', 'HU', 'OR', 'TERI', 'MAA', 'MERI', 'PATNI', 'OR', 'TERI', 'BEHEN', 'MERI', 'BETI', 'JO', 'ROZ', 'MERE', 'SE', 'CHUDTU', 'HAI', 'RANDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII KE PILLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'TU', 'CHADHA', 'PAHAD', 'PE', 'TUJHE', 'LAGI', 'THAND', 'TERI', 'MSS', 'KA', 'BHOSDA', 'MEIN', 'MERA', 'LUND', 'TERI', 'BEHN', 'KO', 'CHODUN', 'O', 'WO', 'TOH', 'ROZ', 'HI', 'CHUDTI', 'MERE', 'SE', 'LOL', 'TERIIIIIIIIIIIIIIIIIIIIII MAAAAAAAAAAA', 'KOOOOOOOOO', 'CHODTAAAAAAAAAAAAAAAAAAAAAAAA', 'HUN', 'MAIN', 'ROOOOOOOOOOOOOOOZZZZZZZZZZ', 'ISLIYE', 'TAMIZ', 'SE', 'BOL', 'BETE', 'TERA', 'BAAP', 'HUN', 'BLKI', 'TERE', 'BAAP', 'KA', 'BHI', 'BAAP', 'HUN', 'TERI', 'MAA', 'MULLE', 'SE', 'CHUDTI', 'ROZ', 'OR', 'MUJHSE', 'BHI', 'USSE', 'KEH', 'LOYAL', 'REH', 'MADAR', 'CHOD', 'LOYAL', 'REHTI', 'HI', 'NOI', 'HAR', 'KISI', 'SE', 'CHUDNE', 'CHALI', 'JAATI', 'LODE', 'KE', 'BAAL', 'TERI', 'MAA', 'MERI', 'HAI', 'AUR', 'KISI', 'KI', 'NOI', 'SMJH', 'LE', 'USSE', 'RED', 'LIGHT', 'PE', 'CHUDNE', 'SE', 'ROK', 'LE', 'BETE', 'TERI', 'MAA', 'KI', 'CHUT', 'BEHEN', 'KE', 'LUND', 'TERI', 'BEHEN', 'GB', 'ROAD', 'KI', 'CHUDI', 'AUR', 'TERI', 'MAA', 'MERI', 'CHUDI', 'USKE', 'CHUT', 'IS', 'SO', 'SEXY', 'TERI', 'BEHN', 'KO', 'CHODUN', 'MAA', 'KE', 'LAWDE', 'TERI', 'MAAAAA', 'MERIIIIIIII', 'RANDIIIIIIIII', 'HAIIIIIII', 'BETEEEEEEEEEEEEEEE', 'TU', 'MEREEEEEEEEEEE', 'LODEEEEEEEEEEE', 'KEEEEEE', 'BAAAAAAL', 'KEEEEEEEEEEEE', 'BHIIIIIIIIIIIII', 'BARABAR', 'NOI', 'HAI', 'ISLIYE', 'BAAAAAAAAAAAP', 'SEEEEEEEEEEEE', 'PANGEEEEEEEEEEEEEEEE', 'NAAAAAAAAAAAAAAAAAAA', 'LEEEEEEEEEEEEEEEEEEEEEEE', 'NOIIIIIIIIIIIIIIIIIII', 'TOH', 'CHUD', 'JAEGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'JAISEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'TERIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'CHUDTIIIIIIII', 'ROZ', 'MEREEEEEEEEEEEE', 'SEEEEEEEEEEEEEEEEEEEEE', 'WAISEEEEEEEEEEEEEEEEE', 'HI', 'TU', 'BHIIIIIIIIIIIIIIIII', 'CHUD', 'GYAAAAAAAAAAAAAAAAAAAAAAAAAA', 'TUJHEEEEEEEEEEEEEEEEEEE', 'CHODNEEEEEEEEEEEEEEEEEEEEEEEEE', 'MEIN', 'TOH', 'LODEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'KIIIIIIIIIIIIIIIIIIIIIIIIII', 'BHIIIIIIIIIIIIIIIIIIIIIIIII', 'ZRURAT', 'NOI', 'PADHIIIIIIIIIIIIIIII', 'BETEEEEEEEEEEEEEEEEEEEEEE', 'AUKAAAAAAAAAAAAAAAAT', 'MEIN', 'REH', 'NOI', 'TOH', 'FIR', 'CHODUNGAAAAAAAAAAAAAAAAAAAAAAAAA', 'TEREEEEEEEEEEEEEEEEEEEEEEE', 'PUREEEEEEEEEEEEEEEE', 'KHANDAN', 'KO', 'CHODUNGAAAAAAAAAAAAAAAAAAAAAAA', 'BETE', 'TERA', 'KHANDAAAAAAAAAAAAAAAAAAAAAN', 'UDAAAAAAAAAAAAAAAAAA', 'DUNGAAAAAAAAAAAAAA', 'MADARCHOD', 'KUTTEEEEEEEEEEEEE', 'KEEEEEEE', 'PILLEEEEEEEEEEEEEEEEEEE', 'TERIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'MAAAAAAAAAAAAAAAAAAAAAAA', 'KOOOOOOOOOOOO', 'CHODUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'APNEEEEEEEEEEEEEEEEEEEEEEEE', 'BHAIYON', 'KEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRR', 'BETIIIIIIICHODDDDD', 'TERIIIIIIIIIIIIIII', 'MAAAAAAAAAAAAA', 'KI', 'SEXYYYYYYYYYYYYYYYYYYY', 'CHUUUUUUUUUUUUUUT', 'BSDK', 'TERIIIIIIIIIIIIIIIIIIIIIIII', 'BEHEN', 'KAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'LODAAAAAAAAAAAAAAAAAAA', 'SUAAAAAAAAAAAAAAAAAAAAAAAAR', 'KEEEEEEEEEEEEEEEEEEEEEEEEEE', 'PILLEEEEEEEEEEEEEEEEEEEEEEEEE', 'MAAAAAAAAAAAAAAAAAAAAAA', 'CHUD', 'GYIIIIIIIIIII', 'TERIIIIIIIIIIIIIIIII', 'RANDIIIIIIIIIIIII', 'KEEE', 'PILLE', 'TERU', 'MAA', 'KI', 'CHUT', 'RAMDWE', 'GANDU', 'LODASUE', 'MERA', 'BHT', 'LAMBA', 'HAI', 'YE', 'BTAYA', 'THA', 'MAINE', 'TERI', 'MAA', 'KO', 'TB', 'TU', 'HUA', 'THA', 'SUAR', 'JAISA', 'RANDI', 'KA', 'PILLA', 'PTA', 'NHI', 'KAISE', 'BACHA', 'HAI', 'MERA', 'KUTTE', 'KI', 'DUM', 'SUAR', 'KI', 'GAAND', 'CHATNE', 'WAAALA', 'OR', 'TERI', 'MAA', 'TIH', 'HIPPO', 'SE', 'CHUDTI', 'TERI', 'BEHEN', 'KUTTE', 'SE', 'CHUDTI', 'TERI', 'BHEN', 'SHE', 'MALE', 'HAINA', 'BSDK', 'TERI', 'MAAA', 'KI', 'CHUT', 'KAAALI', 'HAI', 'TB', 'BHI', 'MAINE', 'USSKE', 'SAATH', 'SEX', 'KARA', 'KITTA', 'ACHA', 'HU', 'MAIN', 'OR', 'TERI', 'BEHEN KI', 'GAAND', 'KAALI', 'HAI', 'TBH', 'BHI', 'MAIN', 'E', 'USSE', 'CHODA', 'KITTA ACHA HU', 'MAIN', 'BETE', 'TERI', 'MAA', 'FIRSE', 'CHUD', 'GYI', 'LODE', 'KE', 'BEEEJ', 'TERI', 'MAA', 'KI', 'CHUT', 'MEIN', 'MERA', 'LUND', 'BEHEN', 'KE', 'LODE', 'TERI', 'MAA', 'KI', 'CHUT', 'TERI', 'MAA', 'KA', 'KAAAALA OR', 'NEELA', 'BHOSDA', 'TERI', 'BHEN', 'KA', 'GREY', 'BHSDA', 'OR', 'HAAN', 'TERU', 'BHI', 'TOH', 'HAI', 'BHSDA', 'LEKIN', 'LAAL', 'HO', 'RHA', 'MAINE', 'FAADA', 'NS', 'ISLIYE', 'BETICHOD', 'SUAR', 'CHOD', 'KUTTE', 'KE', 'CHUDE', 'TERI', 'MAA', 'BETI', 'OR', 'MAIN', 'BETICHOD', 'MULLE', 'SE', 'CHUDNE', 'WAALE', 'LOMDE', 'TERI', 'MAA', 'KI', 'CHUT', 'TERI', 'BEHEN', 'MERI', 'RANDWI', 'HAI', 'GANDU', 'ZYAD', 'A', 'GYAAN', 'MT', 'PEL', 'TERI', 'MAA', 'KO', 'DE', 'DUMGA', 'SAANDE', 'KA', 'TEL', 'TERI', 'BEHEN', 'KO', 'TOH', 'ALREADY', 'DE', 'CHUKA', 'HU', 'BC', 'MAIN 9', 'TERI', 'MAA', '6', 'HAI', 'MAIN', '9', 'HU', 'HUM', 'DONI', 'BHT', 'MAZE', 'KRTE', 'HAI', 'N', 'RAAT', 'KO', 'OYI', 'MEIN', 'GHAPA', 'GHAO', 'CHLTA', 'AC', 'MEIN', 'TOH', 'SWAAD', 'HI', 'AJATA', 'USSE', 'BHI', 'MUJHE', 'V', 'ROZ', 'MERA', 'SEMEN', 'PEETI', 'WO', 'USKE', 'BINA', 'USSKI', 'PYAAS', 'NH', 'I', 'BHUJTI', 'AAJA', 'RANDI', 'TERI', 'MAAKI', 'CHUT', 'MAARU', 'MADARCHOD', 'RANDI', 'KI', 'AULAD', 'TERI', 'MAAA', 'KII', 'XHYT', 'M', 'LODA', 'RANDI', 'K', 'XHODE', 'TERI', 'BEHN', 'KA', 'BHOSDA', 'MARU', 'RANDI', 'K', 'LODE', 'TEIR', 'MA', 'OA', 'LODA', 'JAT', 'K', 'TEUR', 'BEHN', 'K', 'BUR', 'M', 'DALDU', 'MADARXHODE', 'TWIR', 'BEHN', 'KA', 'BUR', 'RANDI', 'K', 'XHODE', 'TEIR', 'MA', 'KA', 'LODA', 'KAT', 'DIYA', 'AJA', 'XDHE', 'TEIR', 'BEHN', 'KA', 'BHISDA', 'FADU', 'TANDI', 'TEIR', 'BEHN', 'KA', 'BUR', 'MAR', 'DIYA', 'RNFI', 'TEIR', 'BEHN', 'KA', 'BUR', 'AJA', 'XHUDT', 'TEIR', 'BEHN', 'KO', 'XHODE', 'TEIR', 'MA', 'KA', 'RAPE', 'KRU', 'RANDI', 'K', 'BALAK', 'TIER', 'MA', 'KA', 'RAPE', 'HOGYA', 'AB', 'ANA', 'MA', 'KI', 'XHUT', 'TEIR', 'BEHN', 'KA', 'BUR', 'RANFI', 'K', 'TEIR', 'BHEN', 'MERE', 'LODE', 'TEIR', 'MA', 'KA', 'BHOSDA',      "MADARCHOD", "BHOSDIKE",
    "LAAAWEEE KE BAAAAAL",
    "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL",
    "MADRCHOD..",
    "TERI MA KI CHUT..",
    "LWDE KE BAAALLL.",
    "MACHAR KI JHAAT KE BAAALLLL",
    "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA",
    "TERI BHN SBSBE BDI RANDI.",
    "TERI MA OSSE BADI RANDDDDD",
    "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "TERI MA KE STH REELS BNEGA ROAD PEE",
    "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP",
    "LUND KE CHODE TU KEREGA TYPIN",
    "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR",
    "LWDEEE",
    "PAPA KI SPEED MTCH NHI HO RHI KYA",
    "ALE ALE MELA BCHAAAA",
    "CHUD GYA PAPA SEEE",
    "KISAN KO KHODNA OR",
    "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA",
    "KIDSSSS",
    "TERI MA CHUD GYI AB FRAR MT HONA",
    "YE LDNGE BAPP SE",
    "KIDSSS FRAR HAHAHH",
    "BHEN KE LWDE SHRM KR",
    "KITNI GLIYA PDWEGA APNI MA KO",
    "NALLEE",
    "SUAR KE PILLE TERI MAAKO SADAK PR LITAKE CHOD DUNGA 😂😆🤤",
    "ABE TERI MAAKA BHOSDA MADERCHOOD KR PILLE PAPA SE LADEGA TU 😼😂🤤",
    "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE 💋💋💦",
    "ABE TERI BEHEN KO CHODU RANDIKE PILLE KUTTE KE CHODE 😂👻🔥",
    "TERI MAAKO AISE CHODA AISE CHODA TERI MAAA BED PEHI MUTH DIA 💦💦💦💦",
    "TERI BEHEN KE BHOSDE ME AAAG LAGADIA MERA MOTA LUND DALKE 🔥🔥💦😆😆",
    "RANDIKE BACHHE TERI MAAKO CHODU CHAL NIKAL",
    "KITNA CHODU TERI RANDI MAAKI CHUTH ABB APNI BEHEN KO BHEJ 😆👻🤤",
    "TERI BEHEN KOTO CHOD CHODKE PURA FAAD DIA CHUTH ABB TERI GF KO BHEJ 😆💦🤤",
    "TERI GF KO ETNA CHODA BEHEN KE LODE TERI GF TO MERI RANDI BANGAYI ABB CHAL TERI MAAKO CHODTA FIRSE ♥️💦😆😆😆😆",
    "HARI HARI GHAAS ME JHOPDA TERI MAAKA BHOSDA 🤣🤣💋💦",
    "CHAL TERE BAAP KO BHEJ TERA BASKA NHI HE PAPA SE LADEGA TU",
    "TERI BEHEN KI CHUTH ME BOMB DALKE UDA DUNGA MAAKE LAWDE",
    "TERI MAAKO TRAIN ME LEJAKE TOP BED PE LITAKE CHOD DUNGA SUAR KE PILLE 🤣🤣💋💋",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥",
    "TERI BEHEN KO CHOD CHODKE VIDEO BANAKE XNXX.COM PE NEELAM KARDUNGA KUTTE KE PILLE 💦💋",
    "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE 🤣💋💦",
    "ABE TERI BEHEN KO CHODU RANDIKE BACHHE TEREKO CHAKKO SE PILWAVUNGA RANDIKE BACHHE 🤣🤣",
    "TERI MAAKI CHUTH FAADKE RAKDIA MAAKE LODE JAA ABB SILWALE 👄👄",
    "TERI BEHEN KI CHUTH ME MERA LUND KAALA",
    "TERI BEHEN LETI MERI LUND BADE MASTI SE TERI BEHEN KO MENE CHOD DALA BOHOT SASTE SE",
    "BETE TU BAAP SE LEGA PANGA TERI MAAA KO CHOD DUNGA KARKE NANGA 💦💋",
    "HAHAHAH MERE BETE AGLI BAAR APNI MAAKO LEKE AAYA MATH KAT OR MERE MOTE LUND SE CHUDWAYA MATH KAR",
    "CHAL BETA TUJHE MAAF KIA 🤣 ABB APNI GF KO BHEJ",
    "SHARAM KAR TERI BEHEN KA BHOSDA KITNA GAALIA SUNWAYEGA APNI MAAA BEHEN KE UPER",
    "ABE RANDIKE BACHHE AUKAT NHI HETO APNI RANDI MAAKO LEKE AAYA MATH KAR HAHAHAHA",
    "KIDZ MADARCHOD TERI MAAKO CHOD CHODKE TERR LIYE BHAI DEDIYA",
    "JUNGLE ME NACHTA HE MORE TERI MAAKI CHUDAI DEKKE SAB BOLTE ONCE MORE ONCE MORE 🤣🤣💦💋",
    "GALI GALI ME REHTA HE SAND TERI MAAKO CHOD DALA OR BANA DIA RAND 🤤🤣",
    "SAB BOLTE MUJHKO PAPA KYOUNKI MENE BANADIA TERI MAAKO PREGNENT 🤣🤣",
    "SUAR KE PILLE TERI MAAKI CHUTH ME SUAR KA LOUDA OR TERI BEHEN KI CHUTH ME MERA LODA",
    "CHAL CHAL APNI MAAKI CHUCHIYA DIKA",
    "HAHAHAHA BACHHE TERI MAAAKO CHOD DIA NANGA KARKE",
    "TERI GF HE BADI SEXY USKO PILAKE CHOODENGE PEPSI",
    "2 RUPAY KI PEPSI TERI MUMMY SABSE SEXY 💋💦",
    "TERI MAAKO CHEEMS SE CHUDWAVUNGA MADERCHOOD KE PILLE 💦🤣",
    "TERI BEHEN KI CHUTH ME MUTHKE FARAR HOJAVUNGA HUI HUI HUI",
    "SPEED LAAA TERI BEHEN CHODU RANDIKE PILLE 💋💦🤣",
    "ARE RE MERE BETE KYOUN SPEED PAKAD NA PAAA RAHA APNE BAAP KA HAHAH🤣🤣",
    "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ",
    "ABE SUN LODE TERI BEHEN KA BHOSDA FAAD DUNGA",
    "TERI MAAKO KHULE BAJAR ME CHOD DALA 🤣🤣💋",
    "SHRM KR",
    "MERE LUND KE BAAAAALLLLL",
    "KITNI GLIYA PDWYGA APNI MA BHEN KO",
    "RNDI KE LDKEEEEEEEEE",
    "KIDSSSSSSSSSSSS",
    "Apni gaand mein muthi daal",
    "Apni lund choos",
    "Apni ma ko ja choos",
    "Bhen ke laude",
    "Bhen ke takke",
    "Abla TERA KHAN DAN CHODNE KI BARIII",
    "BETE TERI MA SBSE BDI RAND",
    "LUND KE BAAAL JHAT KE PISSSUUUUUUU",
    "LUND PE LTKIT MAAALLLL KI BOND H TUUU",
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA",
    "GLTI KRDI TUJW PAIDA KRKE",
    "SPEED PKDDD",
    "Gaand main LWDA DAL LE APNI MERAAA",
    "Gaand mein bambu DEDUNGAAAAAA",
    "GAND FTI KE BALKKK",
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai",
    "Hazaar lund teri gaand main",
    "Jhaant ke pissu-",
    "TERI MA KI KALI CHUT",
    "Khotey ki aulda",
    "Kutte ka awlat",
    "Kutte ki jat",
    "Kutte ke tatte",
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII",
    "Lavde ke bal",
    "muh mei lele",
    "Lund Ke Pasine",
    "MERE LWDE KE BAAAAALLL",
    "HAHAHAAAAAA",
    "CHUD GYAAAAA",
    "Randi khanE KI ULADDD",
    "Sadi hui gaand",
    "Teri gaand main kute ka lund",
    "Teri maa ka bhosda",
    "Teri maa ki chut",
    "Tere gaand mein keede paday",
    "Ullu ke pathe",
    "SUNN MADERCHOD",
    "TERI MAA KA BHOSDA",
    "BEHEN K LUND",
    "TERI MAA KA CHUT KI CHTNIIII",
    "MERA LAWDA LELE TU AGAR CHAIYE TOH",
    "GAANDU",
    "CHUTIYA",
    "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
    "SAMJHAA LAWDE",
    "YA DU TERE GAAND ME TAPAA TAP��",
    "TERI BEHEN MERA ROZ LETI HAI",
    "TERI GF K SAATH MMS BANAA CHUKA HU���不�不",
    "TU CHUTIYA TERA KHANDAAN CHUTIYA",
    "AUR KITNA BOLU BEY MANN BHAR GAYA MERA�不",
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE",
    "TERI MAA KO LEKAR MAI FARAR",
    "RANIDIII",
    "BACHEE",
    "CHODU",
    "RANDI",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT MÉ KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "TERIII MAA KAA BJSODAAA",
    "MADARXHODDD",
    "TERIUUI MAAA KAA BHSODAAA",
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD",
    "NIKAL MADARCHOD",
    "RANDI KE BACHE",
    "TERA MAA MERI FAN",
    "TERI SEXY BAHEN KI CHUT OP",
]


M1 = ""
M2 = ""
M3 = ""
M4 = ""
M5 = ""
M6 = ""
M7 = ""
M8 = ""
M9 = ""
M10 = ""
M11 = ""
M12 = ""
M13 = ""
M14 = ""
M15 = ""
M16 = ""
M17 = ""
M18 = ""
M19 = ""
M20 = ""
M21 = ""
M22 = ""
M23 = ""
M24 = ""
M25 = ""


que = {}

async def StartMK():
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6
    global M7
    global M8
    global M9
    global M10
    global M11
    global M12
    global M13
    global M14
    global M15
    global M16
    global M17
    global M18
    global M19
    global M20
    global M21
    global M22
    global M23
    global M24
    global M25

    if MK1:
        session_name = str(MK1)
        print("String 1 Found")
        M1 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 1")
            await M1.start()
        except Exception as e:
            print(e)
    else:
        print("Session 1 not Found")
        M1 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M1.start()
        except Exception as e:
            pass

    if MK2:
        session_name = str(MK2)
        print("String 2 Found")
        M2 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 2")
            await M2.start()
        except Exception as e:
            print(e)
    else:
        print("Session 2 not Found")
        M2 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M2.start()
        except Exception as e:
            pass

    if MK3:
        session_name = str(MK3)
        print("String 3 Found")
        M3 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 3")
            await M3.start()
        except Exception as e:
            print(e)
    else:
        print("Session 3 not Found")
        M3 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M3.start()
        except Exception as e:
            pass

    if MK4:
        session_name = str(MK4)
        print("String 4 Found")
        M4 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 4")
            await M4.start()
        except Exception as e:
            print(e)
    else:
        print("Session 4 not Found")
        M4 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M4.start()
        except Exception as e:
            pass

    if MK5:
        session_name = str(MK5)
        print("String 5 Found")
        M5 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 5")
            await M5.start()
        except Exception as e:
            print(e)
    else:
        print("Session 5 not Found")
        M5 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M5.start()
        except Exception as e:
            pass

    if MK6:
        session_name = str(MK6)
        print("String 6 Found")
        M6 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 6")
            await M6.start()
        except Exception as e:
            print(e)
    else:
        print("Session 6 not Found")
        M6 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M6.start()
        except Exception as e:
            pass

    if MK7:
        session_name = str(MK7)
        print("String 7 Found")
        M7 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 7")
            await M7.start()
        except Exception as e:
            print(e)
    else:
        print("Session 7 not Found")
        M7 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M7.start()
        except Exception as e:
            pass    

    if MK8:
        session_name = str(MK8)
        print("String 8 Found")
        M8 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 8")
            await M8.start()
        except Exception as e:
            print(e)
    else:
        print("Session 8 not Found")
        M8 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M8.start()
        except Exception as e:
            pass   

    if MK9:
        session_name = str(MK9)
        print("String 9 Found")
        M9 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 9")
            await M9.start()
        except Exception as e:
            print(e)
    else:
        print("Session 9 not Found")
        M9 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M9.start()
        except Exception as e:
            pass   

    if MK10:
        session_name = str(MK10)
        print("String 10 Found")
        M10 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 10")
            await M10.start()
        except Exception as e:
            print(e)
    else:
        print("Session 10 not Found")
        M10 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M10.start()
        except Exception as e:
            pass 

    if MK11:
        session_name = str(MK11)
        print("String 11 Found")
        M11 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 11")
            await M11.start()
        except Exception as e:
            print(e)
    else:
        print("Session 11 not Found")
        M11 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M11.start()
        except Exception as e:
            pass

    if MK12:
        session_name = str(MK12)
        print("String 12 Found")
        M12 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 12")
            await M12.start()
        except Exception as e:
            print(e)
    else:
        print("Session 12 not Found")
        M12 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M12.start()
        except Exception as e:
            pass   

    if MK13:
        session_name = str(MK13)
        print("String 13  Found")
        M13 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 13")
            await M13.start()
        except Exception as e:
            print(e)
    else:
        print("Session 13 not Found")
        M13 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M13.start()
        except Exception as e:
            pass 

    if MK14:
        session_name = str(MK14)
        print("String 14 Found")
        M14 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 14")
            await M14.start()
        except Exception as e:
            print(e)
    else:
        print("Session 14 not Found")
        M14 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M14.start()
        except Exception as e:
            pass

    if MK15:
        session_name = str(MK15)
        print("String 15 Found")
        M15 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 15")
            await M15.start()
        except Exception as e:
            print(e)
    else:
        print("Session 15 not Found")
        M15 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M15.start()
        except Exception as e:
            pass

    if MK16:
        session_name = str(MK16)
        print("String 16 Found")
        M16 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 16")
            await M16.start()
        except Exception as e:
            print(e)
    else:
        print("Session 16 not Found")
        M16 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M16.start()
        except Exception as e:
            pass

    if MK17:
        session_name = str(MK17)
        print("String 17 Found")
        M17 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 17")
            await M17.start()
        except Exception as e:
            print(e)
    else:
        print("Session 17 not Found")
        M17 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M17.start()
        except Exception as e:
            pass

    if MK18:
        session_name = str(MK18)
        print("String 18 Found")
        M18 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 18")
            await M18.start()
        except Exception as e:
            print(e)
    else:
        print("Session 18 not Found")
        M18 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M18.start()
        except Exception as e:
            pass

    if MK19:
        session_name = str(MK19)
        print("String 19 Found")
        M19 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 19")
            await M19.start()
        except Exception as e:
            print(e)
    else:
        print("Session 19 not Found")
        M19 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M19.start()
        except Exception as e:
            pass

    if MK20:
        session_name = str(MK20)
        print("String 20 Found")
        M20 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 20")
            await M20.start()
        except Exception as e:
            print(e)
    else:
        print("Session 20 not Found")
        M20 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M20.start()
        except Exception as e:
            pass

    if MK21:
        session_name = str(MK21)
        print("String 21 Found")
        M21 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 21")
            await M21.start()
        except Exception as e:
            print(e)
    else:
        print("Session 21 not Found")
        M21 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M21.start()
        except Exception as e:
            pass

    if MK22:
        session_name = str(MK22)
        print("String 22 Found")
        M22 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 22")
            await M22.start()
        except Exception as e:
            print(e)
    else:
        print("Session 22 not Found")
        M22 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M22.start()
        except Exception as e:
            pass

    if MK23:
        session_name = str(MK23)
        print("String 23 Found")
        M23 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 23")
            await M23.start()
        except Exception as e:
            print(e)
    else:
        print("Session 23 not Found")
        M23 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M23.start()
        except Exception as e:
            pass

    if MK24:
        session_name = str(MK24)
        print("String 24 Found")
        M24 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 24")
            await M24.start()
        except Exception as e:
            print(e)
    else:
        print("Session 24 not Found")
        M24 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M24.start()
        except Exception as e:
            pass

    if MK25:
        session_name = str(MK25)
        print("String 25 Found")
        M25 = TelegramClient(StringSession(session_name), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            print("Booting Up The Client 25")
            await M25.start()
        except Exception as e:
            print(e)
    else:
        print("Session 25 not Found")
        M25 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M25.start()
        except Exception as e:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(StartMK())


@M1.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    if e.sender_id in MK_USERS:
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        mk = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await mk.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and mk.text:
            message = mk.text
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)



@M1.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.python"))

async def spam(e):
    if e.sender_id in MK_USERS:
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        message = str(aries[1])
        a = await e.client.get_entity(message)
        g = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={g})"
        for Msg in OneWord:
            caption = f"{username} {Msg}"
            async with e.client.action(e.chat_id, "typing"):
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)


@M1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M11.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M12.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M13.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M14.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M15.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    if e.sender_id in MK_USERS:
        mkj = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = mkj[0]
            text = "𝐇𝐀𝐂𝐊𝐈𝐍𝐆..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐇𝐀𝐂𝐊𝐄𝐃 𝐏𝐔𝐁𝐋𝐈𝐂 𝐂𝐇𝐀𝐓 🔥")
            except Exception as e:
                await event.edit(str(e))
            
 

@M1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    if e.sender_id in MK_USERS:
        mkl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mkl[0]
            bc = int(bc)
            text = "𝐔𝐧𝐇𝐀𝐂𝐊𝐈𝐍𝐆..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝐔𝐧𝐇𝐀𝐂𝐊𝐄𝐃 𝐓𝐇𝐀𝐓 𝐆𝐑𝐎𝐔𝐏 😏")
            except Exception as e:
                await event.edit(str(e))


@M1.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in MK_USERS:
        text = f"🤬 HACKER ✘SPAM 🤖!\n✘ #MK 131\n 😈𝙍𝙀𝘼𝘿𝙔 𝙏𝙊 𝙃𝘼𝘾𝙆😎"
        await e.reply(text, parse_mode=None, link_preview=None )


print("\n𝐌𝐊𝐱𝐒𝐏𝐀𝐌 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> @𝐇𝐀𝐂𝐊𝟑𝐑_𝐗𝐃")

if len(sys.argv) not in (1, 3, 4):
    try:
        M1.disconnect()
    except Exception as e:
        pass
    try:
        M2.disconnect()
    except Exception as e:
        pass
    try:
        M3.disconnect()
    except Exception as e:
        pass
    try:
        M4.disconnect()
    except Exception as e:
        pass
    try:
        M5.disconnect()
    except Exception as e:
        pass
    try:
        M6.disconnect()
    except Exception as e:
        pass
    try:
        M7.disconnect()
    except Exception as e:
        pass
    try:
        M8.disconnect()
    except Exception as e:
        pass
    try:
        M9.disconnect()
    except Exception as e:
        pass
    try:
        M10.disconnect()
    except Exception as e:
        pass
    try:
        M11.disconnect()
    except Exception as e:
        pass 
    try:
        M12.disconnect()
    except Exception as e:
        pass
    try:
        M13.disconnect()
    except Exception as e:
        pass 
    try:
        M14.disconnect()
    except Exception as e:
        pass
    try:
        M15.disconnect()
    except Exception as e:
        pass
    try:
        M16.disconnect()
    except Exception as e:
        pass
    try:
        M17.disconnect()
    except Exception as e:
        pass
    try:
        M18.disconnect()
    except Exception as e:
        pass
    try:
        M19.disconnect()
    except Exception as e:
        pass
    try:
        M20.disconnect()
    except Exception as e:
        pass
    try:
        M21.disconnect()
    except Exception as e:
        pass
    try:
        M22.disconnect()
    except Exception as e:
        pass
    try:
        M23.disconnect()
    except Exception as e:
        pass
    try:
        M24.disconnect()
    except Exception as e:
        pass
    try:
        M25.disconnect()
    except Exception as e:
        pass
else:
    try:
        M1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M25.run_until_disconnected()
    except Exception as e:
        pass
