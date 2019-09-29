from heapq import heappush, heappop

class Elevator():
	def __init__(self,id):
		self.id = id
		self.currentFloor = 0
		self.finalFloor = 0
		self.direction = 1
		self.floorRequests = []
		
	def getStatus(self):
		return {'id':self.id, 'currentFloor':self.currentFloor, 'finalFloor':self.finalFloor, 'direction':self.direction, 'floorRequests' : self.floorRequests}
		
	def getFloorRequests(self):
		return len(self.floorRequests)

	def addRequest(self, currentFloor, finalFloor, direction):
		if self.getFloorRequests() == 0:
			self.direction = 1 if currentFloor < finalFloor else -1
			self.finalFloor = finalFloor * self.direction

		if self.direction == direction:
			revisedFinalFloor = self.direction * finalFloor
			if revisedFinalFloor not in self.floorRequests:
				heappush(self.floorRequests, revisedFinalFloor)

			revisedCurrentFloor = self.direction * currentFloor
			if self.currentFloor != currentFloor and revisedCurrentFloor not in self.floorRequests:
				heappush(self.floorRequests, revisedCurrentFloor)
		else:
			self.direction = direction
			self.currentFloor = currentFloor
			self.finalFloor = finalFloor
			self.floorRequests.clear()
			heappush(self.floorRequests, self.direction * currentFloor)
			heappush(self.floorRequests, self.direction * finalFloor)