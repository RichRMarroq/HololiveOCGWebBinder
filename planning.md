## Card Breakdown ##

- Card Name
- Card Number
- Card Set
- Card Color
    - Can be multicolored max 2 for now
- Card Image
- Card Illustrator
- Card Life
    - HP if Holomem/Buzz Holomem Type
    - Life if Oshi Type
- Card Type
    - Oshi
    - Holomem/Buzz Holomem
    - Support
        - multiple different sub-types
        - all have the subtype of Limited or Non-limited
    - Cheer
        - Color
- Card Stage
    - Holomem/Buzz Holomem are further identified by their "evolution stage"
    - Debut -> 1st/1st Buzz -> 2nd
    - Some holomem have a stage named "spot"
- Card Abilities
    - Holomem
        - Can have multiple attacks
            - attack has Cheer Cost (can require multiple colors)
            - attack has title
            - attack can have extra text.
    - Oshi
        - has 2 abilities
            - cost is "holo power" instead of cheer
            - has title
            - has text
    Support
        - Just text block to describe card effect.
- Card Effects
    - Some Holomem/Buzz Holomem have additional effects
        - Trigger (Collab, Bloom, Gift)
        - Text
    - Tags
    - Extra, this debut can have any number

### CSV Structure to import cards into Database ###

**Cards.csv** - This will be the main library of cards and will store core card data:
card_id,card_number,name,set_code,set_name,card_type,rarity,color_1,color_2,image_url,artist,life,hp,stage,support_type,is_limited,effect_text

**card_attacks.csv** - For Holomem type cards, this csv/table will store the specific card attacks and cost.
attack_id,card_id,name,cost,text

**card_oshi_skills.csv** - Similar to card_attacks, stores details for oshi cards
skill_id,card_id,name,cost,text,is_special

**card_effects.csv** - For Holomem type cards, store additional card effects like (Bloom, collab, gift)
effect_id,card_id,trigger,text,tags,is_extra 

## Database Breakdown ##

### Tables ###

- users
- cards
    - card_attacks
    - card_effects
    - card_oshi_skilles
- collections
- collection_cards
- decks
- deck_cards
- binders
- binder_cards