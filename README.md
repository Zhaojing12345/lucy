Kalshi President Election API

`requirement.txt` is used to set up the environment

`kalshi-key-2.key` is what I created to store private key. It need to be used in `request API.py`

`request API.py` is copied from https://trading-api.readme.io/reference/api-keys  code, and made some changes based on that

Steps:

1. used `requirement.txt` to set up the enviroment and load packages

2. run `request API.py` to test if you can use the API

3. If you pass step 2, it means you can run `request DJT.py` and `request KH.py`, they are used to get `Donald Trump Data.csv` and `Kamala Harris Data.csv`.
Or you can just download them from here. If you "Restricts the response to trades before/after a unix timestamp", you can change the parameter in `request DJT.py` and `request KH.py`: find `path = ` and add parameter `min_ts` and `max_ts`



`request DJT.py` output:

```
Data saved to 'Donald Trump Data.csv'
Number of trades: 287494
First 5 rows:
                               trade_id         ticker count                 created_time yes_price no_price taker_side
0  146c1eef-5acc-45f6-b33d-06aaf110a62f  PRES-2024-DJT  1500  2025-01-20T17:03:38.649664Z        99        1         no
1  1bfa4de7-2b0d-4b75-87fb-317573a419c5  PRES-2024-DJT  4237  2025-01-20T17:03:31.604045Z        99        1         no
2  bc143d94-2cee-4707-b069-5820f2ac2374  PRES-2024-DJT   447  2025-01-20T17:03:25.792642Z        99        1         no
3  8a797302-e73e-4dd9-b4ab-811e49ccb3a2  PRES-2024-DJT   310  2025-01-20T17:02:22.151372Z        99        1         no
4  e50d4316-a3ba-458b-89cf-0d8c93fb3732  PRES-2024-DJT   847   2025-01-20T17:00:52.84875Z        99        1         no
Last 5 rows:
                                    trade_id         ticker count                 created_time yes_price no_price taker_side
287489  87a20f70-a085-4f44-9719-e5f7045779de  PRES-2024-DJT    25  2024-10-04T12:38:09.439532Z        49       51         no
287490  91f1e23a-5900-4fa0-b9d2-c7a823523c21  PRES-2024-DJT    20  2024-10-04T12:38:08.798698Z        49       51         no
287491  65dd3e40-0e7e-4e7a-9b5b-5096c742d75e  PRES-2024-DJT   100  2024-10-04T12:24:24.858613Z        51       49        yes
287492  248fa9a0-f449-4bc5-bb7b-9c123e65b5a7  PRES-2024-DJT    10  2024-10-04T12:22:38.315415Z        49       51         no
287493  70666ca3-d373-4e8e-b3bd-0a7f431ca448  PRES-2024-DJT     1  2024-10-04T12:16:59.818671Z        49       51         no
Columnstrade_id: The unique identifier for the tradeticker: The market tickercount: The number of shares tradedcreated_time: The time the trade was createdyes_price: The price of a 'yes' shareno_price: The price of a 'no' sharetaker_side: The side of the trade (maker or taker)
```


`request KH.py` output:

```
Data saved to 'Kamala Harris Data.csv'
Number of trades: 213961
First 5 rows:
                               trade_id        ticker count                 created_time yes_price no_price taker_side
0  39ff02ea-9633-4db3-ab2b-b2b57a4a29e3  PRES-2024-KH     6  2025-01-20T16:31:20.081725Z         1       99        yes
1  4468ab94-9447-49b7-98be-5b05927808b2  PRES-2024-KH    44  2025-01-20T15:09:03.779531Z         1       99        yes
2  fa6f90f4-c9d4-4c32-a1d4-f70448250f0d  PRES-2024-KH  3695  2025-01-20T14:44:12.842579Z         1       99        yes
3  c4e2a0e4-4604-4628-b5b2-c607b651ec93  PRES-2024-KH   200  2025-01-20T14:44:12.842579Z         1       99        yes
4  5581c486-9ca2-4538-b39e-a3020ca9b609  PRES-2024-KH   400  2025-01-20T14:44:12.842579Z         1       99        yes
Last 5 rows:
                                    trade_id        ticker count                 created_time yes_price no_price taker_side
213956  28eeaff9-aa70-45b8-a99a-da06a38ad0a7  PRES-2024-KH     1  2024-10-04T12:21:02.923353Z        51       49        yes
213957  71c51312-cb3e-41c5-b832-cb808a5e4728  PRES-2024-KH     1  2024-10-04T12:20:23.296372Z        51       49        yes
213958  938f7697-0a1d-4f07-a049-b5dfbe9e105c  PRES-2024-KH    25  2024-10-04T12:20:08.375707Z        51       49        yes
213959  4e5e7ea3-4b21-426a-9a19-720957fcc178  PRES-2024-KH     1  2024-10-04T12:15:38.821062Z        51       49        yes
213960  66b54bef-71e2-493e-8f88-f6b06d2b802a  PRES-2024-KH   100  2024-10-04T12:15:05.870113Z        51       49        yes
Columnstrade_id: The unique identifier for the tradeticker: The market tickercount: The number of shares tradedcreated_time: The time the trade was createdyes_price: The price of a 'yes' shareno_price: The price of a 'no' sharetaker_side: The side of the trade (maker or taker)
```

