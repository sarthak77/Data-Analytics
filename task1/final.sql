drop table IF EXISTS team;
CREATE TABLE team(
	team_id INT NOT NULL,
	team_name VARCHAR(255),
    PRIMARY KEY(team_id)
);

LOAD DATA INFILE './team.csv'
INTO TABLE team
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

drop table IF EXISTS player;
CREATE TABLE IF NOT EXISTS player(
	player_id INT NOT NULL,
	player_name VARCHAR(255),
	dob DATE,
	batting_hand VARCHAR(255),
	bowling_skill VARCHAR(255),
	country VARCHAR(255),
    PRIMARY KEY(player_id)
);

LOAD DATA INFILE './player.csv'
INTO TABLE player
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



drop table IF EXISTS venue;
CREATE TABLE IF NOT EXISTS venue(
	venue_name VARCHAR(255) NOT NULL,
	city_name VARCHAR(255),
	country_name VARCHAR(255),
    PRIMARY KEY(venue_name)
);

LOAD DATA INFILE './venue.csv'
INTO TABLE venue
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


drop table IF EXISTS matches;
CREATE TABLE matches(
	match_id INT NOT NULL,
	match_date DATE,
	season_year INT,
	venue_name VARCHAR(255),
	PRIMARY KEY(match_id),
	FOREIGN KEY (venue_name) REFERENCES venue(venue_name)
);
LOAD DATA INFILE './match.csv'
INTO TABLE matches
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


drop table IF EXISTS ball_by_ball;
CREATE TABLE IF NOT EXISTS ball_by_ball(
	match_id INT,
	over_no INT NOT NULL,
	ball_no INT NOT NULL,
	innings_no INT,
	team_batting INT,
	team_bowling INT,
	extra_type VARCHAR(255),
	runs_scored INT,
	extras_runs INT,
	out_type VARCHAR(255),
	bowler_wicket VARCHAR(255),
	striker INT,
	non_striker INT,
	bowler INT,
	player_out INT DEFAULT NULL,
	fielder INT
);

LOAD DATA INFILE './ball_by_ball.csv'
INTO TABLE ball_by_ball
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;