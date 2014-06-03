import pygame
from multiprocessing import Process
import time
from multiprocessing import Lock
from multiprocessing import Queue


q = Queue()
class CTest:

	def __init__(self,color):
		self.color = color
		pygame.init()
		size = [400, 300]
		screen = pygame.display.set_mode(size)
	
		pygame.display.set_caption("Thread Window")
			
	
	def func1(self, queue):
		lock = Lock()
	
		print "In Function 1"
			
	
		clock = pygame.time.Clock()
		done = False
	
		while not done:
			
			print "In Function 1"
			#clock.tick(10)
	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				
			screen.fill([255,255,255])
			
			#lock.acquire()
			temp = queue.get()
			print "Color",temp
			if(temp[0] == 0):
				pygame.draw.line(screen, [255, 0, 0], [0,0], [50, 30], 5)
			else:
				pygame.draw.line(screen, [0, 255, 0], [0,0], [50, 30], 5)
			#lock.release()
			pygame.display.flip()
			
		pygame.quit()		
	
	def func2(self, queue):
		print "In Function 2"
		
		lock = Lock()
		
		pygame.init()                              #initialize pygame
	
	        #We need to setup the display. Otherwise, pygame events will not work
	        screen_size = [500, 500]
	        pygame.display.set_mode(screen_size)
	
	
	        #Initialize the Joysticks
	        pygame.joystick.init()
	
	        #Get count of joysticks
	        joystickCount = pygame.joystick.get_count()
	
	        #Initialize joysticks
	        for i in range(joystickCount):
	        	#We need to initialize the individual joystick instances to receive the events
	        	pygame.joystick.Joystick(i).init()
	
	
	        #Capturing Joystick Events
	        print("Press buttons on the Joystick and see if they are captured by this program")
	
	        #Get the first joystick
	        Joystick1 = pygame.joystick.Joystick(0)
	
		quit = False
	
	        clock = pygame.time.Clock()
	
	        while (quit != True):
	                for event in pygame.event.get():
				print "Event", event.type
	                	if event.type == pygame.QUIT:
	                        	quit = True
	                        if event.type == pygame.JOYAXISMOTION:
					print "Axis Moved"
					#lock.acquire()
	                                if(queue.get() == 0):
						print "Color changed 1"
						queue.put([1])
					else:
						print "Color changed 0"
						queue.put([0])
					#lock.release()
	
				
		pygame.quit()

	def main(self):
		


if __name__ == "__main__":
	test = CTest(1)
	thread1 = Process(target = test.func1, args=(q,))
	thread2 = Process(target = test.func2, args=(q,))
	
	thread1.start()
	thread2.start()
	
	thread1.join()
	thread2.join()

