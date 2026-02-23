# Character Creator Microservice - Mael and Charis

## Communication Contract

1. We will communicate primarily through Teams. 
2. We will respond to messages within 24 hours, even if it’s just “I see this and have no objections”. 
3. If a team member has been unresponsive, we will check in over email or on Canvas. 
4. We will be polite and willing to listen to each other, and focus on finding solutions to problems instead of arguing.
5. We will minimize unspoken assumptions about classwork. In particular, we will prioritize communication about our personal intents for completing assignment work and expectations from the other team member. 
6. If a team member is concerned they will not be able to complete their work by the deadline, reach out to team members for help at least 24 hours before the deadline.

## Microservice Description

This microservice is a way to calculate character stats, and it communicates with the client with Flask. The client sends data about the character (such as equipped items, name, background, and/or occupation) and then the microservice calculates stats such as Luck, Strength, and Defense. This is what is returned to the client program.

## Requesting Data
### Formatting the data so the microservice can read it
''' python

data = {
    "name": "Callipso",

    "background": "noble",
    "occupation": "mage",
    "equipped_items":[
        {
        "hat" : "top_hat",
        "shoes" : "spats"
        }]
}
'''
Data must be in a dictionary. Not all key/value pairs must be entered, there are standard values if you do not wish to assign a name. The key "name" can be given any value as long as it is a string. The key "occupation" must have one of the following values: None, "warrior", "mage", "rogue". The key "background" must have one of the following values: None, "noble", "soldier", "scholar", "commoner", "merchant", "outlaw". The equipped_items key must have it's values placed in a dictionary within a list. See example above.

### Sending the Request through Flask

First, you must start the microservice. In a seperate terminal, run the main program. This will send the data dictionary to the microservice, as seen in the example below.
'''
response = requests.post(service_url, json = data)
'''
## Receiving Data
'''
response = requests.post(service_url, json = data)
print(response.json())
'''
Data will be returned from the microservice and stored in the response variable. To view it easily, use a print statement.

## UML Diagram
<img width="581" height="612" alt="charactercreator_v1 drawio" src="https://github.com/user-attachments/assets/fa498f6c-efef-45c0-b39d-7243ed401678" />
