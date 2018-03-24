# Mobile Phone Number Country Identifier (simple example)

#### Description
Really simple server that accepts a phone number(in international format) and tries to identify the country.

#### Developed by
**Tibebeselasie Mehari**  -  **ATR/9941/08**  -  **S.E** (Regular, Section 2)

#### Implementation details
It uses "**Server-Client** Architecture":
+ `server`  - a __python__ script (`server.py`)
+ `client`  - browser (`index.html`)

#### Environment
Python 3.x (Cross - platform)

#### 3rd party Dependencies
None (only `socket` & `json` are used. which are built-in libraries)

#### Usage
###### To start the server
`python ./server.py`

###### Commands
The following commands are to be used from the client (browser)
+ to locate             - navigate to `<ip address>/locate?phone=<phone number>`
+ to stop the server    - naviate to  `<ip address>/stop`

__Example__:
    `http://localhost/locate?phone=2519111233445`  will try to locate the phone
    `http://localhost/stop`  will terminate the server remotely

