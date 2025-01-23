#!/bin/bash

# Step 1: Describe the AMI and output the name
echo "Describing AMIs to fetch AMI names..."
ami_id=$(aws ec2 describe-images --filters "Name=name,Values=RHEL-9-DevOps-Practice" --query "Images[*].ImageId" --output text)

if [ "$ami_id" == "None" ]; then
    echo "No AMIs found."
    exit 1
fi

ami_name=$(aws ec2 describe-images --image-ids "$ami_id" --query "Images[0].Name" --output text)

echo "AMI Name: $ami_name"

# Step 2: Use the AMI name to describe instances using that AMI
echo "Describing instances using the AMI: $ami_name..."
instances=$(aws ec2 describe-instances  --filters "Name=image-id,Values=$ami_id" --query "Reservations[].Instances[].InstanceId" --output text)

if [ -z "$instances" ]; then
    echo "No instances found using this AMI."
    exit 1
fi

# Output the instance IDs
echo "Instances using the AMI are listed below"
echo instance_list=$ami_name:$instances
