from flask import Flask, request, Response
from base64 import b64encode
from people import people
import json

PORT = 5000
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    print('Request received on root path.')

    formatted_headers = " ".join(request.headers.values())
    formatted_params = str(json.dumps(request.args, sort_keys=True, indent=2))
    formatted_body = str(json.dumps(str(request.data), sort_keys=True, indent=2))

    print('Request headers:\n\t'+formatted_headers)
    print('Query parameters:\n\t'+formatted_params)
    print('Request body:\n\t'+formatted_body)

    return 'Hello!'

@app.route('/people/<id>', methods=['GET'])
def get_people(id):

    # Input validation
    try:
        int(id)
    except ValueError:
        return Response(
            'id of %s could not be cast to an integer.' %id,
            status=400
        )

    # Find the matching person
    for person in people:
        if person['id'] == int(id):
            print(person)
            match = person
            break
        else:
            match = None
    
    # Prepare and send response
    if match is not None:
        return match
    else:
        return Response(
            'No person found for id = %s.' % id,
            status=404
        )

if __name__ == '__main__':
    
    print('Starting Flask app on port %s...' % PORT)
    app.run(port=PORT)