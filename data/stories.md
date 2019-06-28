## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## greet2
* greet2
  - utter_good
  - utter_how_are_you

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## ask_help
* ask_help
  - utter_Help

## ask temperature
* ask_weather
  - Action_weather

## thanks
* thanks
  - utter_cool

## askname
* ask_whoisit
  - utter_name
* thank
  - utter_cool

## bye
* bye
  - utter_goodbye

## Developers
* Developers
  - utter_developers

## ask_day
* date
   - Action_date
   
## ask_day2
* date
   - Action_date
* affirm
  - utter_cool