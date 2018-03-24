# A Denial Of Service(DOS) script example in python

#### Description
a proof of concept python script that sends packets continously to the victim in the intent to cause DOS.

#### Developed by
**Tibebeselasie Mehari**  -  **ATR/9941/08**  -  **S.E** (Regular, Section 2)

#### Implementation details
It uses `socket` library(built-in library in `python 3.x`) to prepare and send random packets to the server(victim)

#### Environment
Python 3.x (Cross - platform)

#### 3rd party Dependencies
None (only uses `socket`, `threading` and `random`. All of them come with the standard python 3.x runtime)

#### Usage
###### To perform the attack
`python ./flooder.py <ip address> <port>`

__Example__:
    `python ./flooder.py localhost 80`  will perform the DOS attack on `http://localhost` on port `80`. 

