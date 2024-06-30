import ApiHandeler as AH
from flask import *

SERVER: Flask = Flask(__name__)

@SERVER.route("/")
def HOME() -> str:
    PICTURE_INFO: dict[str, str] = AH.API.__init__(self= AH.API)
    # Getting The Data
    TITLE: str = PICTURE_INFO["title"]
    EXPLANATION: str = PICTURE_INFO["explanation"]
    DATE: str = PICTURE_INFO["date"]
    COPYRIGHT: str = PICTURE_INFO["copyright"]
    URL: str = PICTURE_INFO["url"]
    MEDIA_TYPE: str = PICTURE_INFO["media_type"]
    # Retuning And Displaying The Data
    return render_template("index.html", 
                           TITLE= TITLE,
                           EXPLANATION= EXPLANATION,
                           DATE= DATE,
                           COPYRIGHT= COPYRIGHT,
                           URL= URL,
                           MEDIA_TYPE= MEDIA_TYPE)


if __name__ == "__main__":
    SERVER.run(debug= True)