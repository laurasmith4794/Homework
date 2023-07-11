# CFG Degree Foundation Assessment 2

## Section 1: Theory Questions

1.1	SDLC stands for Systems Development Life Cycle.

1.2	ZeroDivisionError is thrown when you divide a number by 0.

1.3	The git push command is used to move code from the local repository to the remote repository.

1.4	NULL is used to signify missing or unknown values in a database.

1.5	The Scrum Master will conduct Scrum ceremonies which included Sprint Planning, Daily Standup, Sprint Review, and Sprint Retrospective to ensure the project is kept on track. They are also responsible for coaching the team and ensuring clear communication between the team, the product owner and any other stakeholders involved.

1.6	Print debugging technique: This involves printing out values of variables using the print() function, at different points in the code to see what is going wrong.

Debugger: This is a tool used to step through code line by line.

Debugging methods are used in Python when you encounter an error in your code and want to identify what the problem is. For example you can use the print debugging technique to display values in real time and see what is going wrong in the code, or you can use debugger to step through your code line by line and inspect the values of variables at different points in your code.

1.7  The function will throw an error if the price or cash_given parameter is not an integer or float. For example, if a string value is passed as an argument instead then the function will throw a TypeError exception.
To handle this exception, you can use the try-except block in Python as below:

```
def can_pay(price, cash_given):
    try:
        if cash_given >= price:
           return True
        else:
            return False
    except TypeError:
        print("Invalid input. Please enter a number.")
```
        
This means the code will catch the TypeError exception and print an error message and avoid the program crashing.

1.8	Git branching allows you to diverge from the main line of development and continue working on a separate branch without affecting the main codebase(your main branch in Git). You may want to use it if you are experimenting with your code before committing it to your main branch or when collaborating with others on a project.


To create a new branch in Git, you can use the git branch command followed by the name of the new branch. To switch to a new branch, you can use the git checkout command followed by the name of the branch you want to switch to. Then if you want to add your branch to the main codebase you can merge it using the git merge command.

1.9 
### List of key requirements:
- Needs to be able to handle multiple orders at the same time
- Needs to be able to handle different payment methods (e.g. cash, card, etc)
- Needs to be able to handle different types of orders (e.g. pick up, delivery)
- Needs to be able to handle special requests from customer (e.g. dietary restrictions)
- Needs to be able to remove items if unavailable or out of stock

### Main considerations and problems:
- Scalability for handling large orders during peak times
- Security to protect customer’s data and payment data
- Integration with other systems for accounting and inventory management
- User experience to ensure customer’s and staff are able to easily use the system

### Components and Tools:
- Point of sale system to handle the processing of orders and customers' payments
- App and/or website for customers to place orders and make payment
- Payment gateway to securely process customer payments
- Database management system for storing customer information and order data
- Web server to handle customers' order and requests and sending responses back
