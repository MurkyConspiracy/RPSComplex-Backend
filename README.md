# RPSComplex-Backend
Rock Paper Scissors broken into a multi server application to show use of Docker and code collaboration.
Utilizing socket programming to take requests from the frontend, parse data, and store it on a database.

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
##### ID:1
  
  Validate packet integrity and send back Boolean
