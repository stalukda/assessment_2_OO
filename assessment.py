"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

They are used for: 
-Encapsulation: Data lives close to its functionality so its great for organizing code 
-Abstraction: hiding details we do not need, meaning that we can undestand the code generally without having to know exact mechanics  
-Polymorphism: interchangeability of components, making it fast to make quick instances 

2. What is a class?

Classes are a central component of object-oriented programming. They describe a "type of thing. 
They are comprised of attributes and methods that is used as a blueprint for any istances of the class. 

3. What is an instance attribute?

Variables/data owned by a specific instance of a class. 

4. What is a method?

A method is a function define on class. They get called with self(called with instance) as the first parameter.  

5. What is an instance in object orientation?

An individual occurence of a class. It is synomous with the word "object". __init__() gets called to set up an instance

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is defined on the class and passed down to the children of the class. However, an instance
attribute is defined only on the instance and does not pertain to the whole class. 

An example is if you had a Class called "Fruits", and an attribute would be that "Has Seeds" is True for the whole class. 
However, an instance of the Class, say an Apple, could have an attribute "Has Core" that is True for the instance. 
However, this would not be defined or applicable to the whole Class of Fruits. 

"""

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Class for all students' biographical info """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address 


class Question(object):
    """Class for all questions """ 

    def __init__(self, question, correct_answer):
        self.question = question  
        self.correct_answer = correct_answer

    """Ask user for answer to question and return True if correct """ 
    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        if answer == self.correct_answer:
            return True
        else:
            return False 


class Exam(object):
    """A class to hold info about exams """
    
    def __init__(self, name):
        self.name = name 
        self.questions = []


    def add_question(self, question, correct_answer):
        """Add questions to the exam"""
        current_question = Question(question, correct_answer)
        self.questions.append(current_question)

    
    def administer(self):
        """Administers questions and returns a score based on correct answers """ 
        score = 0  
        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1
        return float(score)/len(self.questions)


class Quiz(Exam):
    """A subclass or child of the parent/superclass Exam """ 

    def __init__(self, name):
        super(Quiz, self).__init__(name)

    ###Refactored previous code to one below 
    # def administer(self):
    #     score = 0  

    #     for question in self.questions:
    #         if question.ask_and_evaluate() == True:
    #             score += 1
    #         final_score = float(score)/len(self.questions)

    #     if final_score >= .5:
    #         print "Pass"
    #         return True
    #     else: 
    #         print "Fail"
    #         return False 

    def administer(self):
    """Administers questions and returns True for passing (50% and over)""" 
        final_score = super(Quiz, self).administer()

        if final_score >= .5:
            print "Pass"
            return True
        else: 
            print "Fail"
            return False 

##DRIVER CODE

def take_test(exam, student):
    """Administers exam and assigns score to the student """ 
    student.score = exam.administer()
    print "The student score is:", student.score 


def example():
    """ Creates an example of the exam""" 
    exam = Exam("midterm") 
    exam.add_question("How tall am I?", "5 foot 3")
    exam.add_question("2+2?", "4")
    student = Student("Sumaiya", "Talukdar", "Oakland")
    take_test(exam, student)


def quiz_example():
    """ Creates an example of the quiz""" 
    quiz = Quiz("quiz")
    quiz.add_question("How tall am I?", "5 foot 3")
    quiz.add_question("2+2?", "4")
    student = Student("Sumaiya", "Talukdar", "Oakland")
    take_test(quiz, student)


# example()
quiz_example()


