from mibot.app import create_app
from mibot.settings import getConfig

app = create_app(getConfig())

if __name__ == '__main__':
  app.run(debug=True)