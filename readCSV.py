import boto3

def lambda_handler(event, context):
    """Read file from s3 on trigger."""
    s3 = boto3.client("s3")
    total_led_uptime = 0
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8')
        for row in file_content.splitlines():
            items = row.split(',')
            if(int(items[2]) == 1):
                total_led_uptime += 1
        print("Total LED Uptime: ", total_led_uptime, "seconds")
        power = 20*20*110*10**-6
        energy = total_led_uptime*power
        print("Energy consumed for ",total_led_uptime," seconds: ", energy, " Ws")
    return 'Thanks'