import json
import socket

host = '127.0.0.1'
port = 8066

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



with socket.socket() as sock:
	sock.connect((host, port))
	print("client connected")
	print("Select any of the operation to perform:")
	print("enter 1 for pi computation")
	print("enter 2 for add")
	print("enter 3 for sort")
	print("enter 4 for matrix multiplication")
	while True:
		data = input("#")
		request_obj = None
		if data == "1":
			print("Enter number to calculate Pi Value")
			request_obj = calculate_pi(int(input()))
		elif data == "2":
			print("input numbers to add with out a new line")
			request_obj = calculate_sum([int(x) for x in input().split()])
		elif data == "3":
			print("input numbers to sort with out a new line")
			request_obj = sort_the_array([int(x) for x in input().split()])
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
			request_obj = matrix_parameters(mat , mbt ,mct)

		request = json.dumps(request_obj)
		sock.sendall(bytes(request, encoding='utf8'))
		data = sock.recv(2048)
		response = json.loads(data)
		print(response)

