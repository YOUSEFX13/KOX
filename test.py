from ursina import *

app = Ursina()

tooltip_test = Tooltip(
    '<scale:1.5><pink>' + 'Rainstorm' + '<scale:1> \n \n' +
    '''Summon a <blue>rain
storm <default>to deal 5 <blue>water
damage <default>to <red>everyone, <default>including <orange>yourself. <default>
Lasts for 4 rounds.'''.replace('\n', ' '),
    background_color=color.red
)


gay = Text("""
        Rules:
        A round begins with all the tiles in the down position. A player will roll two dice and add them together. The player will then lower an equal amount of tiles. 

        For example, if the player rolls a total of 9, he/she can lower any tiles to 9.

        * 9
        * 8 and 1
        * 7 and 2
        * 6 and 3
        * 5 and 4
        * 6, 2 and 1
        *4, 3, and 2
        
        The player continues to roll as long as he/she has an equal number of tiles to lower. When no more tiles can be lowered the game is over. 
        The player will win by closing the box!
        """, wordwrap=50, scale=0.5)
tooltip_test.enabled = True


wp = WindowPanel(
    title='Rules',
    content=(
        Text("""
        Rules:
        A round begins with all the tiles in the down position. A player will roll two dice and add them together. The player will then lower an equal amount of tiles. 

        For example, if the player rolls a total of 9, he/she can lower any tiles to 9.

        * 9
        * 8 and 1
        * 7 and 2
        * 6 and 3
        * 5 and 4
        * 6, 2 and 1
        *4, 3, and 2
        
        The player continues to roll as long as he/she has an equal number of tiles to lower. When no more tiles can be lowered the game is over. 
        The player will win by closing the box!
        """, wordwrap=50, scale=0.7), closewp_b)

    ),
    popup=True,
    enabled=True
)
