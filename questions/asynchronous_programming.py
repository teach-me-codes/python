questions = [
    {
        'Main question': 'What is asynchronous programming in Python?',
        'Explanation': 'The candidate should explain the concept of asynchronous programming as a programming paradigm that allows tasks to run concurrently without blocking the main program execution. In Python, this is achieved using asynchronous frameworks like asyncio.',
        'Follow-up questions': ['How does asynchronous programming differ from synchronous programming in Python?', 'Can you explain the role of event loops in asynchronous programming?', 'What are the benefits of using asynchronous programming for I/O-bound tasks?']
    },
    {
        'Main question': 'How does the asyncio library facilitate asynchronous programming in Python?',
        'Explanation': 'The candidate should discuss the asyncio library in Python, which provides support for writing asynchronous code using coroutines, event loops, and asynchronous I/O operations.',
        'Follow-up questions': ['What is a coroutine and how is it related to asynchronous programming with asyncio?', 'How can tasks be managed and executed concurrently using asyncio?', 'Can you explain the concept of awaitable objects in the context of asyncio?']
    },
    {
        'Main question': 'What are the key components of an asynchronous coroutine in Python?',
        'Explanation': 'The candidate should describe the essential components of an asynchronous coroutine, including the async def keyword for defining coroutines, await for suspending execution, and the asyncio.run() function for running the event loop.',
        'Follow-up questions': ['How can multiple coroutines be scheduled and executed in parallel?', 'What is the significance of using asyncio.gather() for running multiple coroutines concurrently?', 'Can you discuss any potential pitfalls or common errors when working with asynchronous coroutines?']
    },
    {
        'Main question': 'How can you handle exceptions in asynchronous Python code?',
        'Explanation': 'The candidate should explain the various approaches to handling exceptions in asynchronous Python code, including try-except blocks within coroutines, using asyncio.error\_handler(), and dealing with exceptions in asynchronous tasks.',
        'Follow-up questions': ['What are the best practices for error handling in asynchronous programming to maintain code reliability?', 'How can you propagate exceptions raised in one coroutine to other parts of the asynchronous program?', 'Can you explain the difference between handling exceptions in synchronous versus asynchronous Python code?']
    },
    {
        'Main question': 'What are the common use cases for applying asynchronous programming in Python?',
        'Explanation': 'The candidate should discuss real-world scenarios where asynchronous programming is beneficial, such as web scraping, API interactions, network programming, and handling concurrent I/O operations efficiently.',
        'Follow-up questions': ['How does asynchronous programming improve the performance of I/O-bound tasks compared to synchronous programming?', 'In what situations is asynchronous programming not recommended or may not be suitable?', 'Can you provide examples of Python libraries or frameworks that extensively use asynchronous programming for specific tasks?']
    }
]
