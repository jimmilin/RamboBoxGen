BOX_URL_TEMPLATE = "https://neulionmdnyc-a.akamaihd.net/fs/nba/feeds_s2012/stats/2016/boxscore/%s.js?%d"

TEAM_DICT = {
    "BOS": "Boston Celtics",
    "BKN": "Brooklyn Nets",
    "NYK": "New York Knicks",
    "PHI": "Philadelphia 76ers",
    "TOR": "Toronto Raptors",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DET": "Detroit Pistons",
    "IND": "Indiana Pacers",
    "MIL": "Milwaukee Bucks",
    "ATL": "Atlanta Hawks",
    "CHA": "Charlotte Hornets",
    "MIA": "Miami Heat",
    "ORL": "Orlando Magic",
    "WAS": "Washington Wizards",
    "GSW": "Golden State Warriors",
    "LAC": "LA Clippers",
    "LAL": "Los Angeles Lakers",
    "PHX": "Phoenix Suns",
    "SAC": "Sacramento Kings",
    "DAL": "Dallas Mavericks",
    "HOU": "Houston Rockets",
    "MEM": "Memphis Grizzlies",
    "NOP": "New Orleans Pelicans",
    "SAS": "San Antonio Spurs",
    "DEN": "Denver Nuggets",
    "MIN": "Minnesota Timberwolves",
    "OKC": "Oklahoma City Thunder",
    "POR": "Portland Trail Blazers",
    "UTA": "Utah Jazz"
}

class BoxColors:
    STATS_HEADER = '\033[1;33;44m'
    HOME_FRAME = '\033[1;31m'
    HOME_HEADER = '\033[1;33;41m'
    VISITOR_FRAME = '\033[1;35m'
    VISITOR_HEADER = '\033[1;33;45m'
    WHITE = '\033[1;37m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[1;36m'
    RED = '\033[1;31m'
    DARK_GREEN = '\033[32m'
    END = '\033[0m'
