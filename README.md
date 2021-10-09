# vpc-endpoints
Python scripts to set up and tear down VPC endpoints

I ended up tying the delete script in to my MySQL RDS idle script - when the instance is idle and shutdown, I also tear down the VPC endpoints.  If my development RDS instance is offline, its a safe assumption that I've finished with the whole environment and therefore can delete the VPC endpoints.

## todo
At some point I will probably enumerate regions and VPCs to dynamically delete these instead of hardcoding the VPC ID.
