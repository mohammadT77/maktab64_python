import re

t = """ASDASd [1] A  [2] strong personality and a successful general, Akbar gradually enlarged the Mughal Empire to include much of the Indian subcontinent. His power and influence, however, extended over the entire subcontinent because of Mughal military, political, cultural, and economic dominance. To unify the vast Mughal state, Akbar established a centralised system of administration throughout his empire and adopted a policy of conciliating conquered rulers through marriage and diplomacy. To preserve peace and order in a religiously and culturally diverse empire, he adopted policies that won him the support of his non-Muslim subjects. Eschewing tribal bonds and Islamic state identity, Akbar strove to unite far-flung lands of his realm through loyalty, expressed through an Indo-Persian culture, to himself as an emperor.

Mughal India developed a strong and stable economy, leading to commercial expansion and greater patronage of culture. Akbar himself was a patron of art and culture. He was fond of literature, and created a library of over 24,000 volumes written in Sanskrit, Urdu, Persian, Greek, Latin, Arabic and Kashmiri, staffed by many scholars, translators, artists, calligraphers, scribes, bookbinders and readers. He did much of the cataloging himself through three main groupings.[15] Akbar also established the library of Fatehpur Sikri exclusively for women,[16] and he decreed that schools for the education of both Muslims and Hindus should be established throughout the realm. He also encouraged bookbinding to become a high art.[15] Holy men of many faiths, poets, architects, and artisans adorned his court from all over the world for study and discussion. Akbar's courts at Delhi, Agra, and Fatehpur Sikri became centres of the arts, letters, and learning. Timurid and Perso-Islamic culture began to merge and blend with indigenous Indian elements, and a distinct Indo-Persian culture emerged characterized by Mughal style arts, painting, and architecture. Disillusioned with orthodox Islam and perhaps hoping to bring about religious unity within his empire, Akbar promulgated Din-i-Ilahi, a syncretic creed derived mainly from Islam and Hinduism as well as some parts of Zoroastrianism and Christianity.

Akbar's reign significantly influenced the course of Indian history. During his rule, the Mughal Empire tripled in size and wealth. He created a powerful military system and instituted effective political and social reforms. By abolishing the sectarian tax on non-Muslims and appointing them to high civil and military posts, he was the first Mughal ruler to win the trust and loyalty of the native subjects. He had Sanskrit literature translated, participated in native festivals, realising that a stable empire depended on the co-operation and good-will of his subjects. Thus, the foundations for a multicultural empire under Mughal rule were laid during his reign. Akbar was succeeded as emperor by his son, Prince Salim, later known as Jahangir.
Defeated in battles at Chausa and Kannauj in 1539 to 1541 by the forces of Sher Shah Suri, Mughal emperor Humayun fled westward to Sindh.[17] There he met and married the then 14-year-old Hamida Banu Begum, daughter of Shaikh Ali Akbar Jami, a Persian teacher of Humayun's younger brother Hindal Mirza. Jalal ud-din Muhammad Akbar was born the next year on 25 October 1542[a] (the fifth day of Rajab, 949 AH)[11] at the Rajput Fortress of Amarkot in Rajputana (in modern-day Sindh), where his parents had been given refuge by the local Hindu ruler Rana Prasad.[19]


Akbar as a boy
During the extended period of Humayun's exile, Akbar was brought up in Kabul by the extended family of his paternal uncles, Kamran Mirza and Askari Mirza, and his aunts, in particular Kamran Mirza's wife. He spent his youth learning to hunt, run, and fight, making him a daring, powerful and brave warrior, but he never learned to read or write. This, however, did not hinder his search for knowledge as it is always said when he retired in the evening he would have someone read.[20][21] On 20 November 1551, Humayun's youngest brother, Hindal Mirza, died fighting in a battle against Kamran Mirza's forces. Upon hearing the news of his brother's death, Humayun was overwhelmed with grief.[22]

Out of affection for the memory of his brother, Humayun betrothed Hindal's nine-year-old daughter, Ruqaiya Sultan Begum, to his son Akbar. Their betrothal took place in Kabul, shortly after Akbar's first appointment as a viceroy in the province of Ghazni.[23] Humayun conferred on the imperial couple all the wealth, army, and adherents of Hindal and Ghazni. One of Hindal's jagir was given to his nephew, Akbar, who was appointed as its viceroy and was also given the command of his uncle's army.[24] Akbar's marriage with Ruqaiya was solemnized in Jalandhar, Punjab, when both of them were 14-years-old.[25] She was his first wife and chief consort.[26][4]"""

emails = """
Valid test cases:
akbar@reza.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123

Invalid test cases:
plainaddress
#@%^%#$@#$@#.com
@example.com
Joe Smith <email@example.com>
email.example.com
email@example@example.com

"""
# res = re.search("\[\d+\]", t)  # [123]
# print(re.findall("\[\d+\]", t))
pattern = r"(?P<username>[a-z0-9+._\-]+)@(?P<host>(([0-9\-a-zA-Z]+\.)+([a-zA-Z]{2,4}))|(\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b))"
for match in re.finditer(pattern, emails):
    print(match.groupdict())
