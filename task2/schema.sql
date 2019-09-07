-------------create table-----------------------

drop table IF EXISTS ytv;
CREATE TABLE IF NOT EXISTS ytv(
    views int,
    likes int,
    dislikes int,
    comments int
);

-------------load data-----------------------

-- clean.csv contains "views","likes","dislikes","comments" columns for category_id=24
LOAD DATA INFILE './clean.csv'
INTO TABLE ytv
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-------------modify table and show the values according to the ranges fixed-----------------------

update ytv set views=1 where views<500000;
update ytv set views=2 where views>=500000 and views<5000000;
update ytv set views=3 where views>=5000000;

update ytv set likes=4 where likes<10000;
update ytv set likes=5 where likes>=10000;

update ytv set dislikes=6 where dislikes<500;
update ytv set dislikes=7 where dislikes>=500;

update ytv set comments=8 where comments<1000;
update ytv set comments=9 where comments>=1000 and comments<5000;
update ytv set comments=10 where comments>=5000;

select views,likes,dislikes,comments,count(*)
from ytv
group by views,likes,dislikes,comments
order by views,likes,dislikes,comments;


-- then the values in columns were to changed to specific ranges manually--------------------------
-- using ctrl+find feature

-------------export as csv-----------------------

select views,likes,dislikes,comments,count(*)
from ytv
group by views,likes,dislikes,comments
order by views,likes,dislikes,comments
INTO OUTFILE 'final.csv'
FIELDS TERMINATED BY ','
ESCAPED BY '"' 
LINES TERMINATED BY '\n';