#include <pthread.h>    // pthread
#include <stdio.h>      // prinftf
#include <stdlib.h>     // random
#include <unistd.h>     // sleep
#include <semaphore.h>  // semaphores
// you might need more header files

void *doctor_actions();
void *car_actions(void *car_id);

int NUM_CARS = 5;

//To set a limit for the line
int line = 0;
int maxLength = 3;

//Id to the first car in the line
int first;

//Define semaphores
sem_t queue;
sem_t lock;
sem_t docWait;
sem_t carWait;

//Methods
void vaccine(int id) {
	first = id;
	sem_wait(&lock);
	if (line == 1)
		printf("Car %d honks to wake the doctor. \n", id);
	sem_post(&lock);
	//Wakes up the doctor
	sem_post(&docWait);
	//Wait for the doctor
	sem_wait(&carWait);
}

void entering(int id) {
	line = (line + 1);
	printf("Car %d enters the line. Car waiting = %d. \n", id, line);
}

void exiting() {
	line = (line - 1);
}


//Main
int main(int argc, char **argv) {

    int car_ids[NUM_CARS];

    pthread_t cars[NUM_CARS];
    pthread_t doctor;
    
    //init. semaphores
    sem_init(&queue, 0, 1);
    sem_init(&lock, 0, 1);
    sem_init(&docWait, 0, 0);
    sem_init(&carWait, 0, 0);

    // create threads
    pthread_create(&doctor, NULL, doctor_actions, NULL);
    for (int i = 0; i < NUM_CARS; i++) {
        car_ids[i] = i;
        pthread_create(&cars[i], NULL, car_actions, (void *)&car_ids[i]);
    }

    // join threads
    pthread_join(doctor, NULL);
    for (int i = 0; i < NUM_CARS; i++) {
        pthread_join(cars[i], NULL);
    }

    return 0;
}


//Doctor thread
void *doctor_actions() {
    while (1) {
    	//Sleeps utill another car wakes it up
	sem_wait(&docWait);
	
	//Taking the vaccine
	int vacTime = rand() % 10;
	printf("Patient in car %d is getting tested. Testing for %d seconds. \n", first, vacTime);
	sleep(vacTime);
	printf("Patient in car %d finished testing. \n", first);
	sem_post(&carWait);
	sem_wait(&lock);
    	if(line == 0)
    		printf("No cars waiting. Sleeping");
    	sem_post(&lock);
    }
}

//Car thread
void *car_actions(void *car_id) {
	// get the id of this car
    	int id_car = *(int *)car_id;
    
    
    	while (1) {
    		//Taking a sunday drive around the block
    		int time = rand() % 10;
    		printf("Car %d is driving for %d seconds. \n",id_car,time);
    		sleep(time);
    
    		//Critical! If the line is full, start over
    		sem_wait(&lock);
    		if (line >= maxLength){
    			printf("Car %d will try again later. \n", id_car);
    			sem_post(&lock);
        		continue;
    		}
    		sem_post(&lock);
    		
    		//Critical! Entring the queue
	    	sem_wait(&lock);
	    	entering(id_car);
	    	sem_post(&lock);
	    
	    	//Critical! Waiting in queue, to take the vaccine
	    	sem_wait(&queue);
	    	vaccine(id_car);
	    	
	    	//Critical! Exiting the queue
	    	sem_wait(&lock);
	    	exiting();
	    	sem_post(&lock);
	    
	    	sem_post(&queue);
	}
}





//Yes
