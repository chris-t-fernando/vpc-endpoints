import boto3

client = boto3.client("ec2")

services_to_create = [
    "com.amazonaws.us-west-2.sqs",
    "com.amazonaws.us-west-2.s3",
    "com.amazonaws.us-west-2.rds",
    "com.amazonaws.us-west-2.lambda",
    "com.amazonaws.us-west-2.ec2",
]

for service in services_to_create:
    try:
        if service == "com.amazonaws.us-west-2.s3":
            private_dns = False
        else:
            private_dns = True
        response = client.create_vpc_endpoint(
            VpcEndpointType="Interface",
            VpcId="vpc-9953e9fc",
            ServiceName=service,
            SubnetIds=["subnet-a752c0c2", "subnet-325eee45", "subnet-6577a03c"],
            SecurityGroupIds=[
                "sg-8b5c50ee",
            ],
            PrivateDnsEnabled=private_dns,
        )
    except Exception as e:
        print(f"{service}: Failed to create.  Error: {str(e)}")
