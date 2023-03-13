import socket, json, math ,numpy

host = '127.0.0.1'  # loopback ip address
port = 8066 # listening port number


def response_obj():
    return {"result": ""}


# serverstub
def calculate_pi(k):
    result = response_obj()
    result["result"] = 3.141592653589793 * k
    return result

# sum of numbers
def calculate_sum(arr):
    result = response_obj()
    result["result"] = sum(arr)
    return result

# sock.send(bytes(response,encoding='utf8'))
def sort_the_array(arr):
    result = response_obj()
    result["result"] = sorted(arr)
    return result

def mat_multi(mats):
    result = response_obj()
    result["result"] = numpy.matmul(numpy.matmul(mats[0],mats[1]),mats[2]).tolist()
    return result


with socket.socket() as sock:
    print("Server initiated")
    sock.bind((host, port))
    sock.listen()
    client_sock_obj, address = sock.accept()
    with client_sock_obj:
        while True:
            data = client_sock_obj.recv(2048)
            request = json.loads(data)
            response = {"ERROR": "Server failed to process the request"}

            if request["method"] == 'pi':
                response = calculate_pi(request["params"][0])
            elif request["method"] == 'sum':
                response = calculate_sum(request["params"][0])
            elif request["method"] == 'sort':
                response = sort_the_array(request["params"][0])
            elif request["method"] == 'mat_multi':
                response = mat_multi(request["params"])



            response["request-ID"] = request["request-ID"]
            response = json.dumps(response)
            client_sock_obj.send(bytes(response.encode('utf-8')))
