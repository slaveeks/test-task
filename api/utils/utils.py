from flask import jsonify, make_response


class Utils:
    """
    The Utils has helpful methods
    """
    @staticmethod
    def make_response_to_client(data):
        """
        Make response to the client
        :param data: data to send
        :return: Response
        """
        response = make_response(jsonify(data))

        # Set header of access control
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response
