import flask
from flask import Flask, request, jsonify

app = flask.Flask(__name__)

modified_dictionary = {}


# this function creates a dictionary of given words and modifies it for a further search
@app.route('/load', methods = ['POST'])
def create_dictionary():
    anagram_dictionary = request.json
    for word in anagram_dictionary:
        modified_word = ''.join(sorted(word.lower()))
        if modified_word in modified_dictionary:
            modified_dictionary[modified_word].append(word)
            modified_dictionary[modified_word] = list(set(modified_dictionary[modified_word]))
        else:
            modified_dictionary[modified_word] = [word]
    return jsonify(modified_dictionary)


# this function modifies the given word the same way as the dictionary was modified and performs a search
@app.route('/get', methods = ['GET'])
def get_word():
    given_word = request.args.get('word')
    mod_word = ''.join(sorted(given_word.lower()))
    if mod_word in modified_dictionary:
        return jsonify(modified_dictionary[mod_word])
    else:
        return None
                    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



