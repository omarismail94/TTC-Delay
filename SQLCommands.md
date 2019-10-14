# Command used to create SQL Table

```sql
CREATE TABLE subwayDelays (
    Date DATE NOT NULL ,
    Time TIME(0)  NOT NULL,
    Day  VARCHAR(16) NOT NULL,
    Station VARCHAR(255),
    Code VARCHAR(8),
    Min_Delay INT CHECK (Min_Delay >=0),
    Min_Gap INT CHECK (Min_Delay >=0),
    Bound VARCHAR(2),
    Line VARCHAR(4),
    Vehicle INT 
)
```

# Command used to import csv into database
Once the table has been created, I then import the csv into the database

```sql
 COPY subwaydelays FROM '{directory}/subway-srt-logs-september-2019.csv' WITH (FORMAT csv);
```

 did the same for the other months in the year