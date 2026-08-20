from steampy.client import SteamClient

USERNAME = "username"
PASSWORD = "password"
MAFILE = "account.maFile"

steam = SteamClient("")

steam.login(
    "AaronFlux514",
    "T2!vQ9#pL6@mX8z",
    r"C:\Users\ki\Desktop\cs2sell\data\maFiles\aaronflux514.maFile"
)