
## Task 1

The program in task 1 follows the requirements of the At-Most-Once Property because 
of 
>x is not written by another process and e contains no references to variables
changed by other processes.
> 
and since the first while loop doesn't write to the Y variable and the second while loop doesn't write
ti the X variable.

## Task 2

```
// global variables
int buf;
bool buf_full = false;
const int N = 100, Ps = 10, Cs = 10; 

 

process Producer[i = 1 to Ps] {
  int a[N]; 
  // ... here we would have some code to fill array a with data (we don't care how exactly --
  // -- you don't have to provide this code here!)
  int p = 0;
 
  while (p < N) {
    <await (buf_full == false) buf = a[p]; buf_full = true>
    p = p + 1;
  }
}

 

process Consumer[i = 1 to Cs] {
  int b[N]; 
  int c = 0;
  
  while (c < N) {
    <await (buf_full == true) b[c] = buf; buf_full = false>
    c = c + 1;      
  }

  // ... here we would have some code code that uses b (we don't care how exactly -- 
  // -- you don't have to provide this code here!)
}

```

instead of just continuing when the buf_full the processes needs to wait for a change in the
variable, or else they lose some products.

## Task 3

```
sem a = 1;
sem b = 0;
sem c = 0;

process P1 {
    P(a);
    write("Bergen");
    write("is");
    V(b);
}

process P2 {
    P(b);
    write("a");
    write("city");
    V(c);
}

process P3 {
    P(c);
    write("in");
    write("Norway");
}

```

Here we need process 2 & 3 to wait until the previous process have finished executing so
sem b & c are set to 0 until sem a can tell b to continue processing

## Task 4

```
sem refillFood = 0;
sem eat = 1;
food = f;
process parent(){
    while(true){
        P(refillFood);
        food = f;
        V(eat);
    }
}
process child()[i = 1 to N]{
    P(eat);
    food--;
    if(food == 0){
        V(refillFood);
    } else {
        V(eat);
    }
    sleep();
}
```

we make one process for the parent and one process for each of the birds. Since each

## Task 5

```
monitor Account {
    int balance = 0;
    cond cv;
    
    procedure deposit(int amount) {
        balance = balance + amount;
        signal(cv)
    }
    
    procedure withdraw(int amount) {
        while(amount > balance){
            wait(cv)
        }
        balance = balance - amount;
    }
}

```

## Task 6

```
sem chilling = 1;
int checking = 0;

process passangerVac()[i = 1 to N]{
    while(true){
        P(chilling)
        if(checking >= 0){
            checking++;
            V(chilling)
            break;
        }
        V(chilling)
        wait(5)
    }
    // Chilling while waiting for checking papers
    wait(10)
    P(chilling)
    checking--;
    V(chilling)
}

process passengerUVac()[i = 1 to M]{
    while(true){
        P(chilling)
        if(checking <= 0){
            checking--;
            V(chilling)
            break;
        }
        V(chilling)
        wait(5)
    }
    // Chilling while waiting for checking papers
    wait(10)
    P(chilling)
    checking++;
    V(chilling)
}
```