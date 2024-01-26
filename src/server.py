import routes.auth  # pylint:disable=unused-import
import routes.meals  # pylint:disable=unused-import

from config import PORT
from app import app

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
