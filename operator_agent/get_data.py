[{'operator_address': '0xffed2c14005d332b388fb3b3be3f745bc886653c', 'operator_id': '0xf254b62f9dce21cad74791e26c2dc04d7ec06786af3eed6ce6e1687c9bc5726e', 'percentage': 0.0004524375070693587, 'quorum_id': 0, 'total_batches': 8841, 'total_unsigned_batches': 4}]

import requests
import datetime
import time
import pandas as pd

headers = {
    'x-api-key': 'AIzaSyCsXFyQ9BFHfckdaF492RhkwwsKoXOV5RE',
}
gateway_url = 'https://data-lambda-eigenda-us-east-1-api-2i70evhq.ue.gateway.dev/'

# end_time = 1717934400
end_time = 1714046400

n = 60

for i in range(n):
    interval = 86400
    response = requests.get(
        f"{gateway_url}/api/v1/get_eigenda_operator_nonsigning_percentage",
        params={'end_time':end_time, 'interval': interval},
        headers=headers
    )
    data = response.json()
    if response.status_code == 200:
        df = pd.DataFrame({
            'operator_address': [str(item['operator_address']) for item in data],
            'operator_id': [str(item['operator_id']) for item in data],
            'percentage': [float(item['percentage']) for item in data],
            'quorum_id': [int(item['quorum_id']) for item in data],
            'total_batches': [int(item['total_batches']) for item in data],
            'total_unsigned_batches': [int(item['total_unsigned_batches']) for item in data]
        })
        print(f"Data fetched for {datetime.datetime.fromtimestamp(end_time)} timestamp: {end_time} with {len(df)} rows.")
        df['timestamp'] = int(end_time)
        df.to_csv('operators_data.csv', mode='a', header=False, index=False)   
    else:
        print(response.json())
        print(f"Failed to fetch data for {datetime.datetime.fromtimestamp(end_time)} {end_time} {i}")
        break
    # time.sleep(5)
    end_time = end_time - interval
