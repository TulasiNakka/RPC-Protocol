
import datetime
import random
import websockets
import asyncio
import time
import socket, json, math ,numpy

print("Server initiated")

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
#sort array
def sort_the_array(arr):
    result = response_obj()
    result["result"] = sorted(arr)
    return result

#matrix multiplication
def mat_multi(mats):
    result = response_obj()
    result["result"] = numpy.matmul(numpy.matmul(mats[0],mats[1]),mats[2]).tolist()
    return result


#asyncio
async def handler(websocket, path):
    data = await websocket.recv()
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
    await websocket.send(response)

start_server = websockets.serve(handler, '127.0.0.1', 8092)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()