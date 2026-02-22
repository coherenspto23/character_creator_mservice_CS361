from flask import Flask, request, jsonify

app = Flask(__name__)


#global dict
character_data = {}

#
@app.route('/api/character/name', methods=["GET"])
def character_getname():
    global character_data
    #name = character_data["name"]
    return jsonify({"name": character_data.get("name")})

@app.route('/api/character/create', methods=["POST"])
def character_creator():
    global character_data
    """
    Character stat calculator from character creator

    Will support:
    Occupation + background based system
    Item based system
    Possible hybrid system
    """


    data = request.json

    name = data.get('name', 'Adventurer')
    occupation = data.get('occupation', None) # Optional
    background = data.get('background', None) # Optional
    equipped_items = data.get('equipped_items', [])

    # Random base stats can obviously be changed at later date
    stats = { 
        'name': name,
        'level': 1,
        'health': 100,
        'mana': 50,
        'strength': 5,
        'magic': 5,
        'luck': 5,
        'stamina': 5,
        'defense': 5,
        'agility': 5
    }

    stats['occupation'] = occupation if occupation else None
    stats['background'] = background if background else None

    if occupation:
            occupation = occupation.lower()
            
            if occupation == 'warrior':
                stats['health'] += 90
                stats['stamina'] += 25
                stats['mana'] -= 30
                stats['strength'] = 8
                stats['magic'] = 2
                stats['defense'] += 2
                stats['agility'] -= 1
                
            elif occupation == 'mage':
                stats['health'] -= 30
                stats['stamina'] += 15
                stats['mana'] += 80
                stats['strength'] = 2
                stats['magic'] = 9
                stats['defense'] -= 3
                stats['agility'] += 1
                
            elif occupation == 'rogue':
                stats['health'] -= 20
                stats['stamina'] += 30
                stats['mana'] -= 10
                stats['strength'] -= 1
                stats['magic'] -= 2
                stats['agility'] += 3



    if background:
            background = background.lower()
            
            if background == 'noble':
                stats['luck'] += 3
                stats['defense'] += 1
                
            elif background == 'soldier':
                stats['strength'] += 2
                stats['health'] += 10
                stats['defense'] += 1
                
            elif background == 'scholar':
                stats['magic'] += 2
                stats['mana'] += 10
                stats['luck'] += 1
                
            elif background == 'commoner':
                stats['stamina'] += 5
                stats['health'] += 5
                stats['strength'] += 1
                stats['agility'] += 1
                
            elif background == 'merchant':
                stats['luck'] += 3
                stats['defense'] += 1
                
            elif background == 'outlaw':
                stats['agility'] += 2
                stats['stamina'] += 10
                stats['luck'] += 1
                stats['defense'] -= 1
        



    # check which items are equipped and change stats based on it
    if equipped_items:
        for item in equipped_items:
            bonuses = item.get('bonuses', {})
            # Add each bonus to the corresponding stat
            for stat, value in bonuses.items():
                if stat in stats:
                    stats[stat] += value

    stats['max_health'] = stats['health']
    stats['max_mana'] = stats['mana']
    stats['max_stamina'] = stats['stamina']

    character_data = stats
    # return calculated stats 
    return jsonify(stats), 200



# Tests

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if service is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'character_creator'
    }), 200


if __name__ == '__main__':
    print("="*60)
    print("  CHARACTER CREATOR MICROSERVICE")
    print("="*60)
    print("Running on http://localhost:5003")
    print("Endpoint: POST /api/character/create")
    print("Health check: GET /api/health")
    print("="*60)
    app.run(host='0.0.0.0', port=5003, debug=True)
