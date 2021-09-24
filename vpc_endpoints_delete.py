import boto3


def get_tag(tags, search_tag):
    for tag in tags:
        if tag["Key"].upper() == str(search_tag).upper():
            if str(tag["Value"]).upper() == "TRUE":
                return True
    return False


client = boto3.client("ec2")

# could use Filter but its case sensitive sadface
response = client.describe_vpc_endpoints()

count_endpoints_total = 0
count_endpoints_deleted = 0
count_endpoints_retained = 0

for endpoint in response["VpcEndpoints"]:
    count_endpoints_total += 1
    # if vpcendpoints_idle_exempt tag is present and set to true, then this won't run
    # but if its not present, or present and set to false, then it will run
    if get_tag(endpoint["Tags"], "VPCENDPOINTS_IDLE_EXEMPT") == False:
        try:
            client.delete_vpc_endpoints(VpcEndpointIds=[endpoint["VpcEndpointId"]])
            count_endpoints_deleted += 1
        except Exception as e:
            print(
                f"{endpoint['VpcEndpointId']} in {endpoint['VpcId']}: Failed to delete - {str(e)}"
            )
            count_endpoints_retained += 1

    else:
        count_endpoints_retained += 1

print(
    f"Finished endpoint check. {count_endpoints_deleted} deleted, {count_endpoints_retained} retained, {count_endpoints_total} endpoints total."
)
