import random
import time

def lambda_handler(event, context):
    # Randomly choose a duration between 25 and 45 seconds
    duration = random.randint(25, 45)
    print(f"Function will run for {duration} seconds.")

    # Sleep for the duration
    time.sleep(duration)

    # Return a message indicating successful execution and duration
    return {
        'statusCode': 200,
        'body': f"Function executed successfully for {duration} seconds."
    }