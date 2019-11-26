# SRI2018
A repository of all resources and code used for my SRI 2018 project at FIU.

## Instructions for Data Collection
To reproduce the same procedures that were performed for the 2018 project, please see the following steps:

1. Create a Mininet network with 2 hosts, h1 and h2, connected to a network switch, s1.
Note: Let h1 act as a client and h2 act as a server. 

2. Run the trafficGenServer.py script on the server. Let this wait for connections.

3. Initialize tshark on the switch to begin to listen for network traffic. Ensure that this is filtering for only the ACS traffic by specifiying only TCP traffic on whatever port you chose your ACS to listen on.

4. Start the ACS server on h2 with your desired configuration.

5. Start the ACS client on h1 with your desired configuration.

6. Run the trafficGenClient.py script on h1 with proxychains to ensure that the network traffic is tunneled through the ACS and not as regular traffic.

7. Record data until traffiGenClient and trafficGenServer stop.

8. Save pcap file to desired location.

9. Repeat steps 1-8 9 more times for this tool making a total of 10 pcaps.

10. Repeat steps 1-9 for all ACS tools.
