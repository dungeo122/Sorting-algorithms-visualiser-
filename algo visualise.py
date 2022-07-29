from ast import Continue
from http.client import CONTINUE
from multiprocessing import Event
from turtle import delay
import pygame 
import random
import sys
pygame.init()

window_w = 800
window_l = 1000
background_colour = (234, 212, 252)
rect_color = [(100,200,125), (255,0,0)]
screen = pygame.display.set_mode((window_l, window_w))
pygame.display.set_caption('algo visualiser')
screen.fill(background_colour)
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Press "b" for bubble sort \n Press "i" for insertion sort \n Press "q" for quick sort \n "r" for reset',True, (0,0,255),(255,255,0))
textrect = text.get_rect()
textrect.center = (window_l/2,50)

def random_arr(n, max_val, min_val):
    arr = []
    for _ in range(n):
        val = random.randint(min_val,max_val)
        arr.append(val)
    return(arr)

def rectangles(arr,n):

    for i in range(n):
        screen.blit(text, textrect)
        pygame.draw.rect(screen,rect_color[i%2],pygame.Rect((20+((window_l-40)/n)*i),100,(window_l-40)/n,arr[i]))
        pygame.display.flip()


def bubbleSort(arr):
    n = len(arr) 

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            screen.fill(background_colour)
            rectangles(arr,n)
            pygame.time.wait(10)

    return(arr)


def partition(l, r, arr):
    pivot, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[r] = arr[r], arr[ptr]
    return ptr
 

def quicksort(l, r, arr):
    if len(arr) == 1:  
        return arr
    if l < r:
        pi = partition(l, r, arr)
        quicksort(l, pi-1, arr)  
        quicksort(pi+1, r, arr)  
       
        screen.fill(background_colour)
        rectangles(arr, len(arr))
        pygame.time.wait(10)
    return arr


def insertionSort(arr):
  
    for i in range(1, len(arr)):
  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        screen.fill(background_colour)

        rectangles(arr, len(arr))
        pygame.time.wait(10)
    return(arr)


def main():
    running = True
    clock = pygame.time.Clock()
    n = 20
    max_val = 500
    min_val = 1
    arr = random_arr(n,max_val,min_val)
    rectangles(arr,n)
    # pygame.time.wait(5000)
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.key == pygame.K_b:
                    bubbleSort(arr)
                elif event.key == pygame.K_i:
                    insertionSort(arr)
                elif event.key == pygame.K_q:
                    quicksort(0, len(arr)-1, arr)
                elif event.key == pygame.K_r:
                    screen.fill(background_colour)
                    main()


if __name__ == "__main__":
    main()
    
                    


            

    
    
   