from flask import Flask
from focloir import Focloir
app = Flask(__name__)

@app.route("/translate/<word>")
def translate_word(word):
  translator = Focloir()
  translation = translator.translate(word)
  return f'{translation}'

if __name__ == "__main__":
  app.run()