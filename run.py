from braintutor.app import create_app
from braintutor.settings import getConfig

app = create_app(getConfig())

if __name__ == '__main__':
  app.run(debug=True)