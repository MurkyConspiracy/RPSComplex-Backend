# RPSComplex-Backend
Rock Paper Scissors broken into a multi server application to show use of Docker and code collaboration. Utilizing socket programming to take requests from the frontend, parse data and store it on a database.

## Packet Structure and Layout
Incoming Packet Structure

##### Request Header "RPS" (3 Bytes):

    82, 80, 83

##### Request ID (1 Byte):

    FF

##### Request Data length (4 Bytes) [Byte Order=big]:

    FF, FF, FF, FF

##### Data (Request Length Bytes)

    FF, .. .. .. .. FF
 
##### Request Footer "COMPLEX" (7 Bytes):

    43, 4F, 4D, 50, 4C, 45, 58

# Request Types
#### ID:0 - Incoming
  
    Validate packet integrity and send back Boolean

#### ID:1 - Incoming

    Create user based on incoming data.
    Incoming data will be accepted in the form of a json string containing the following:
        "username"
        "email"
        "password_hash"

#### ID:127 - Outgoing

    Return packet from incoming validity check.
    Return data is a json string formatted containging the following:
        "status" ("passed")

#### ID:128 - Outgoing

    Return packet from incoming create account request.
    Return data is a json string formatted containging the following:
        "status" ("passed" / "failed")
        "reason" ("Account Created" / Error Message) 
            Failure Status Messages:
                Email already registered
                Username already taken
                Malformed User Data

#### ID:255 -Outgoing

    Return packet that had malformed data with error code.
    Return data is a json string formatted containing the following:
        "status" ("failed")
        "reason" (Check Fail Reasoning)
            Failure Status Messages:
                Failed header check
                Failed footer check
                Failed packet ID check
                Failed packet length check
