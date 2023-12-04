import asyncio
import aiohttp
import json
from datetime import datetime, timedelta


async def wait_60_seconds():
    print("Waiting for 60 seconds...")
    await asyncio.sleep(60)
    print("60 seconds have passed. Now executing the code.")



async def get_api_data():
    #API's URL
    api_url = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            data = await response.json()
            return data


async def main(duration_minutes):
    while datetime.now().minute != 0:   # Waiting for the minute to be as close to 0 as possible to start
        await asyncio.sleep(0.1)

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    #print("check1")
    while datetime.now() < end_time:
        # Get current time
        current_time = datetime.now()
        #print('check2')
        # See if time is at 00
        #if current_time.minute == 0:
        ## DO YOU THINK THE ABOVE CODE IS WHAT ITS SUPPOSED TO BE?
        if 1 == 1:
            api_data = await get_api_data()
            #print('check3')
            try:
                with open('api_data_test.json', 'r') as json_file:
                    existing_data = json.load(json_file)
            except FileNotFoundError:
                existing_data = {}
            #print('check4')
            existing_data[current_time.strftime('%Y-%m-%d %H:%M:%S')] = api_data
            # put new data into JSON file
            with open(r'C:\Users\natha\PycharmProjectsEmilyBrown\DS2002chatbot\api_data_test.json', 'w') as json_file:
                json.dump(existing_data, json_file, indent=2)
            #print('check5')
            print(f"API data appended to 'api_data_test.json' at {current_time}")

        await wait_60_seconds()


if __name__ == "__main__":
   # Run the main function for 60 minute
    asyncio.run(main(duration_minutes=60))
    #Done to indicate the code is complete and JSON file should have all the information
    print("Done")


