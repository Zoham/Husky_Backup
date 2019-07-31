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

## email_open1
* send_email
  - open_email
  - utter_did_that_help


## email_open2
* send_email
  - open_email
  - utter_did_that_help
* affirm
  - utter_cool


## email_open1
* send_email
  - open_email
  - utter_did_that_help
* deny
  - utter_still_developing

## email_open2
* question_email
  - utter_still_developing

## cricket score
* ask_score
  - cricket_score_choices
* number_choices
  - cricket_score_info

## in_between
* number_choices
  - cricket_score_info

## give_tutorial1
* tutorial
  - utter_tutorial
  - utter_did_that_help
* affirm
  - utter_cool

## give_tutorial2
* tutorial
  - utter_tutorial
  - utter_did_that_help
* deny
  - utter_still_developing

## give_tutorial3
* tutorial
  - utter_tutorial
  - utter_did_that_help
