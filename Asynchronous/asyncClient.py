# Import WebSocket client library (and others)
#Please install the websockets
#pip install websocket-client
#pip install websockets
import json
import socket
import websocket
import _thread
import time
import rel
import asyncio



global wsc


'''
def ws_message(ws, message):
    #print(f'Answer: {message}')
    get_results(ws,message)
    print(f'---------------------------------------------')
'''
def ws_open(ws):
    print("Opened connection")
    get_choice()

def on_close(ws, close_status_code, close_msg):
    # print("### closed ###")
    _thread.start_new_thread(ws_thread, ())

def on_error(ws, error):
    print(error)


def ws_thread(*args):
    global wsc
    wsc = websocket.WebSocketApp("ws://127.0.0.1:8092/",
                                on_open = ws_open,
                                on_message = get_results,
                                on_error=on_error,
                                on_close=on_close)
    # websocket.enableTrace(True)
    wsc.run_forever()  # Set dispatcher to automatic reconnection

# Start a new thread for the WebSocket interface
_thread.start_new_thread(ws_thread, ())


req_counter = 0


def get_request_object():
	global req_counter
	source_request_object = {
		"request-ID": req_counter,
		"method": "PI",  # method names
		"params": []
	}
	req_counter += 1
	return source_request_object


# client stub
def calculate_pi(k):
	request_object = get_request_object()
	request_object["method"] = "pi"
	request_object["params"].append(k)
	return request_object


def calculate_sum(sum_arr):
	request_object = get_request_object()
	request_object["method"] = "sum"
	request_object["params"].append(sum_arr)
	return request_object


def sort_the_array(sort_arr):
	request_object = get_request_object()
	request_object["method"] = "sort"
	request_object["params"].append(sort_arr)
	return request_object

def matrix_parameters(mat ,mbt ,mct):
	request_object = get_request_object()
	request_object["method"] = "mat_multi"
	request_object["params"].append(mat)
	request_object["params"].append(mbt)
	request_object["params"].append(mct)
	return request_object


#Asking for the Option to run function
def get_choice():
    print("client connected")
    print("Select any of the operation to perform:")
    print("enter 1 for pi computation")
    print("enter 2 for add")
    print("enter 3 for sort")
    print("enter 4 for matrix multiplication")
    

    data = input("#")
    request_obj = None
    if data == "1":
        request_obj = calculate_pi(int(data))
        request = json.dumps(request_obj)
        wsc.send(bytes(request, encoding='utf8'))
        time.sleep(3)


    elif data == "2":
        print("input numbers to add with out a new line")
        request_obj = calculate_sum([int(x) for x in input().split()])
        request = json.dumps(request_obj)
        wsc.send(bytes(request, encoding='utf8'))
        time.sleep(3)

        
    elif data == "3":
        print("input numbers to sort with out a new line")
        request_obj = sort_the_array([int(x) for x in input().split()])
        request = json.dumps(request_obj)
        wsc.send(bytes(request, encoding='utf8'))
        time.sleep(3)

        
    elif data == "4":
        print("input row and column size of a matrix a")
        a_size = [int(x) for x in input().split()]
        mat = []
        for i in range(int(a_size[0])):
            a =[]
            for j in range(int(a_size[1])): 
                a.append(int(input()))
            mat.append(a)


        print("input row and column size of a matrix b")
        b_size = [int(x) for x in input().split()]
        mbt = []
        for i in range(int(b_size[0])):
            b = []
            for j in range(int(b_size[1])): 
                b.append(int(input()))
            mbt.append(b)
            
        
        print("input row and column size of a matrix b")
        c_size = [int(x) for x in input().split()]
        mct = []
        for i in range(int(c_size[0])):
            c = []
            for j in range(int(c_size[1])): 
                c.append(int(input()))
            mct.append(c)
        print(mat)
        print(mbt)
        print(mct)
        request_obj = matrix_parameters(mat , mbt ,mct)
        request = json.dumps(request_obj)
        wsc.send(bytes(request, encoding='utf8'))
        time.sleep(3)
 
        
		
#For getting the results
def get_results(ws,message):
        print("Select the options to see your results:")
        print("enter 1 to get pi results")
        print("enter 2 to get add")
        print("enter 3 to get sort")
        print("enter 4 to get matrix multiplication")
    
        data = input("#")
        request_obj = None
        if data == "1":
            print("Enter number to get Pi Value")
            print("Result from server is...")
            time.sleep(1)
            print(message)
            print('----- completed ------ \n')
            

        elif data == "2":
            print("Enter number to get addition details")
            print("Result from server is...")
            time.sleep(1)
            print(message)
            print('----- completed ------ \n')
            
            
        elif data == "3":
            print("Enter number to get sorted array")
            print("Result from server is...")
            time.sleep(1)
            print(message)
            print('----- completed ------ \n')
            
        elif data == "4":
            print("Enter number to get matrix multiplication")
            print("Result from server is...")
            time.sleep(1)
            print(message)
            print('----- completed ------ \n')
        

while True:
    time.sleep(3)
        

    
