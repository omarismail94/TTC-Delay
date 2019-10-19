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



 # Query for finding when delays happen

 For one hour only:
 ```sql
 SELECT day, count(*) as "10-11"
FROM subwaydelays
WHERE subwaydelays.time > '10:00:00' and subwaydelays.time < '11:00:00'
GROUP BY day
```

For three hours:


 
 ```sql
 SELECT nine.day, "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"

FROM (
SELECT day, count(*) as "9-10"
FROM subwaydelays
WHERE subwaydelays.time > '9:00:00' and subwaydelays.time <= '10:00:00'
GROUP BY day) AS nine

JOIN
(
SELECT day, count(*) as "10-11"
FROM subwaydelays
WHERE subwaydelays.time > '10:00:00' and subwaydelays.time <= '11:00:00'
GROUP BY day) as ten 
ON nine.day = ten.day

JOIN
(
SELECT day, count(*) as "11-12"
FROM subwaydelays
WHERE subwaydelays.time > '11:00:00' and subwaydelays.time <= '12:00:00'
GROUP BY day) as eleven 
ON nine.day = eleven.day


JOIN
(
SELECT day, count(*) as "12-13"
FROM subwaydelays
WHERE subwaydelays.time > '12:00:00' and subwaydelays.time <= '13:00:00'
GROUP BY day) as twelve 
ON nine.day = twelve.day

JOIN
(
SELECT day, count(*) as "13-14"
FROM subwaydelays
WHERE subwaydelays.time > '13:00:00' and subwaydelays.time <= '14:00:00'
GROUP BY day) as thirteen 
ON nine.day = thirteen.day


JOIN
(
SELECT day, count(*) as "14-15"
FROM subwaydelays
WHERE subwaydelays.time > '14:00:00' and subwaydelays.time <= '15:00:00'
GROUP BY day) as fourteen 
ON nine.day = fourteen.day

JOIN
(
SELECT day, count(*) as "15-16"
FROM subwaydelays
WHERE subwaydelays.time > '15:00:00' and subwaydelays.time <= '16:00:00'
GROUP BY day) as fifteen 
ON nine.day = fifteen.day

ORDER BY nine."9-10" DESC
```


# Delays per day

```sql
SELECT date, sum(min_delay)

FROM subwaydelays
GROUP BY date
ORDER BY date
```