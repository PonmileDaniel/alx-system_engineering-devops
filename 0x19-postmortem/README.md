#Postmortem task using webstack debugging #1

# Issue Summary
Duration of the outage: The outage started at 14:00pm to 15:00pm west African Time.

# Impact:
The web application experienced a complete outage unable for users to access the site or its services.

# Root Cause
The Nginx server was updated, but something went wrong. This caused two problem
1. The Update messed uo the setting for the load balancer 
2. The server stopped directing requests to the right place.

# Timeline
14:00pm: The issue was detected via spike in error rates by the monitoring system.
14:05pm: Monitoring system alerts indicating that the site was down the issue got to me.
14:10pm: Inital investigation focused on the application accessing the code that was just pushed.
14:20pm: The Application team rolled back the latest deployment, but the issue persisted.
14:35pm: Further investigation was down which led to the database layer, where the conection was checked, but no anomalies were found.
14:40pm: Then I identified the issue with Nginx load balancer configuration, which has not been updated correctly
14:45pm: The misconfiguration was corrected, and the server was restarted.
15:00: Full service  was restored, with monitoring confirming normal operation.

# Root Cause And Resolution
THe cause of the outage was a misconfigured Nginx server update. Recent update to the Nginx load balancer included changes to the routing rules. These changes were not thoroughly tested in the staging environment before being applied to production. The misconfiguration led to a conflict in the load balancer, causing it to fail to route requests properly, resulting in a complete outage of the web application.

To resolve te issue, reverted the Nginx configuration to its previous state and thoroughly tested the routing rules before reapplying them to production, The Nginx server was then restarted, and the normal services was restored.

# Corrective and Preventative Measures
Implement more rigorous testing protocols in the staging environment, particularly for infrastructure changes like load balancer configurations

Develop automated rollback mechanisms for infrastructure updates to allow for faster recovery in case of failure.

Enhance monitoring to include specific alerts for load balancer  misconfiguration or failure.

# Task list
Implement a more robust testing pipeline for load balancer configuration.
Add specific monitoring alerts for load balancer routing issues.
Patch Nginx server to include the latest security and stability updates.

https://github.com/PonmileDaniel/alx-system_engineering-devops/blob/master/0x19-postmortem/WhatsApp%20Image%202024-08-18%20at%2017.33.51.jpeg