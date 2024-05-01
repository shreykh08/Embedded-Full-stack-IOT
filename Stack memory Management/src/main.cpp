#include <Arduino.h>

#if CONFIG_FREERTOS_UNICORE
static const BaseType_t app_cpu = 0;
#else
static const BaseType_t app_cpu = 1;
#endif

//task1 - create a task
void test_task(void *parameter)
{
  while(1)
{
int a = 1;
int b[100]; //it will take space of 400 bytes (int -  bytes) and already we have 768 bytes i.e.total 1168 bytes which is more than 1024 but we will allocate only 1024 in such case the stack will overflow.

for(int i=0;i<100;i++){
  b[i] = a+1;
}
Serial.println(b[0]);

//printing the remaminig memory stack
Serial.print("High water mark (words)");
Serial.print(uxTaskGetStackHighWaterMark(NULL));
//print the number of free heap memory bytes
vTaskDelay(2000/portTICK_PERIOD_MS);

Serial.print("Heap before malloc (bytes): ");
Serial.println(xPortGetFreeHeapSize());
int *ptr = (int*)pvPortMalloc(1024*sizeof(int));


/*if(ptr ==NULL)
{
  Serial.println("Not enough heap");
}
else*/
  for(int i = 0;i<1024;i++)
  {
    ptr[i] = 3;
  }

Serial.println("Heap memory after+");

vTaskDelay(500/portTICK_PERIOD_MS);


}

}



void setup() {
  Serial.begin(115200);
  vTaskDelay(2000/portTICK_PERIOD_MS);
  Serial.println("memory overflow");

  //create and run the task
  xTaskCreatePinnedToCore(test_task,"test task",1500,NULL,1,NULL,app_cpu);
  vTaskDelete(NULL);
  
}

void loop() {
 // code execution never reaches here
}



/*
int global_variable;
static int static_variable;

void some fnution(int some_arguement)
{
 static int local_static_variable;
 int local_variable;
 int *dyanmic_ptr;

 dynamic_ptr = (int*)malloc(32*sizeof(int));
/ /your function does something here

free(dynamic_ptr);


}
Static Memory
global variables are saved in static memory or we explicitally forcwe the variable to get stored 
in the static memory either global or local.  (49,50,54).it depends on the architecture of the processor.
once it is created it cannt be changed during the execution of the code.


Stack Memory 
We store the things that we need during the execution of the function i.e. locl variables or some other recursive funtions
such as array as we come out of the function these things or values will be popped out or completely eliminated
(53 int ,55,56)-> these values will go to the stack memory.
Nature of stack memory is to go down if initialised at the top everytime we initialise,i.e. its size can change during the execution of the programme i.e.
it may increase.

Heap Memory
Dynamic memory allocation takes place in the heap.(ex.malloc)
Whenever we need a special area of block of memory it is stored in the heap memory.
There are two things one is to store the heap and the other is to look at the stack from our programme.
stack may coincide with the heap durng programme execution
heap may also increase its size during the execution

  when we create a task it is created in th heap memory.Collection of diff datatypes."struct" and its declaration is same as that of a class
  TCB(task control block).

  if we start allocating the memory in the task then (malloc searches for a acontiguous memory block and allocates it that)
  repeating alloationt the size of task will incrase the size of the heap and each time whn we declare the variables
  then the stack size also increases and overlapping tales place in such a case

dwnld and archive the rtos files...

Memory leak
information security
the both sections of heap and stack are dynamic that is they may increase or decrease.if we increase the both memories.Wheneve two parts
overlap each other then processor is unabke to understand whether it is heap or stack and it strts from the beginning in sucha case it is said
that theprocessor is crashed.



*/