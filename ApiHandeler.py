from typing import Any
import requests

class API:
    def __init__(self) -> dict[str, str]:
        # Api Endpoint
        API_KEY: str = "YOUR API KEY"
        self.URL: str = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        # Getting The Json Data
        self.JSON_DATA: Any = requests.get(self.URL).json()
        # Getting The Wanted Information From The Json
        self.DATE: str = str(self.JSON_DATA["date"])
        self.TITLE: str = str(self.JSON_DATA["title"])
        self.EXPLANATION: str = str(self.JSON_DATA["explanation"])
        self.URL: str = str(self.JSON_DATA["url"])
        self.MEDIA_TYPE: str = str(self.JSON_DATA["media_type"]).capitalize()
        # If The Image Or The Video Is Not Copyrighted Then The JSON Won't Include The Parameter Which Would Result In An Error 
        try:
            self.COPYRIGHT: str = str(self.JSON_DATA["copyright"])
        
        except KeyError:
            self.COPYRIGHT: str = " "
        # Returning The Data In An Accessible Format    
        return {
            "title": self.TITLE,
            "explanation": self.EXPLANATION,
            "date": self.DATE,
            "copyright": self.COPYRIGHT,
            "url": self.URL,
            "media_type": self.MEDIA_TYPE
        }
    
