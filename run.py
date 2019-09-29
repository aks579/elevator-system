from flask import Flask, jsonify, request
from elevator import Elevator
import heapq

app = Flask(__name__)

elevators = []
elevator_count = 4
floors = 10

@app.before_first_request
def before_first_request_func():
	global elevators 
	elevators = [Elevator(i) for i in range(elevator_count)]
	
@app.route('/elevator/<int:id>/goto',methods=['PUT'])
def goToFloor(id):
	content = request.get_json()
	currentFloor = content['currentFloor']
	finalFloor = content['finalFloor']
	if currentFloor > floors or finalFloor > floors:
		return jsonify({'Error':'invalid floor selection'})
	selected_elevator = elevators[id]
	direction = 1 if currentFloor < finalFloor else -1
	selected_elevator.addRequest(currentFloor,finalFloor,direction)
	return jsonify({'Data':selected_elevator.getStatus()})

@app.route('/elevator/<int:id>/status',methods=['GET'])
def getStatus(id):
	return jsonify({'Data':elevators[id].getStatus()})

@app.route('/elevator/<int:id>/stop',methods=['PUT'])
def stopElevator(id):
	elevators[id].direction = 0
	return jsonify({'Message':'elevator stopped'})

@app.route('/elevator',methods=['GET'])
def getAllElevators():
	elevator_list = []
	for elevator in elevators:
		elevator_list.append(elevator.getStatus())
	return jsonify({'Data':elevator_list})
	
@app.route('/building',methods=['POST'])
def createRequest():
	content = request.get_json()
	currentFloor = content['currentFloor']
	direction = content['direction']
	capableElevators = []	
	if currentFloor > floors:
		return jsonify({'Error':'invalid floor selection'})
	elevator_list = [e for e in elevators if e.direction == direction]
	for e in elevator_list:
		print(e.floorRequests[0])
		diff = (currentFloor*direction) - (e.floorRequests[0])
		print(diff)
		if diff >= 0:
			capableElevators.append((diff, e.id))
	if capableElevators:
		d, id = min(capableElevators)
		selected_elevator = elevators[id]
		return jsonify({'id':selected_elevator.id})
		
	else:
		capableElevators = []
		elevator_list = [e for e in elevators if e.direction != direction]
		for e in elevator_list:
			diff = (currentFloor*direction) + (e.floorRequests[-1]*e.direction)
			if diff >= 0:
				capableElevators.append((diff, e.id))
		if capableElevators:
			d, id = min(capableElevators)
			selected_elevator = elevators[id]
			return jsonify({'id':selected_elevator.id})
	return jsonify({'Data':'Error'})

@app.route('/elevator/<int:id>/state',methods=['PUT'])
def setState(id):
	content = request.get_json()
	elevators[id].currentFloor = content['currentFloor']
	elevators[id].finalFloor = content['finalFloor']
	elevators[id].floorRequests = content['floorRequests']
	elevators[id].direction = content['direction']
	
	return jsonify({'Data':elevators[id].getStatus()})	
	
if __name__ == '__main__':
	app.run(debug=True);