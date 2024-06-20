questions = [
    {
        'Main question': 'What is concurrency and parallelism in Python?',
        'Explanation': 'Concurrency is the ability of a program to execute multiple tasks simultaneously, while parallelism is the ability of a program to execute multiple tasks in parallel. Python provides built-in libraries and frameworks for writing concurrent and parallel code.',
        'Follow-up questions': ['How does the Global Interpreter Lock (GIL) in Python impact concurrency and parallelism?', 'Can you explain the difference between threading and multiprocessing in Python?', 'What are some common challenges faced when working with concurrent and parallel code in Python?']
    },
    {
        'Main question': 'How does threading support concurrency in Python?',
        'Explanation': 'Threading allows multiple threads to run concurrently within a single process, enabling better responsiveness and utilization of resources.',
        'Follow-up questions': ['What are the advantages and disadvantages of using threads for concurrency in Python?', 'How does Python\'s Global Interpreter Lock (GIL) affect threading performance?', 'Can you discuss any thread synchronization mechanisms in Python for managing shared resources?']
    },
    {
        'Main question': 'What is the role of the Global Interpreter Lock (GIL) in Python concurrency?',
        'Explanation': 'The Global Interpreter Lock (GIL) in Python impacts multi-threaded performance and influences concurrency and parallelism.',
        'Follow-up questions': ['How does the GIL affect CPU-bound versus I/O-bound tasks in Python programs?', 'Are there ways to work around the limitations imposed by the GIL for achieving true parallelism?', 'Can you discuss any alternative approaches to concurrency and parallelism in Python that do not rely on threads?']
    },
    {
        'Main question': 'How can the asyncio library be used for asynchronous programming in Python?',
        'Explanation': 'The asyncio module in Python provides a framework for writing asynchronous code using coroutines to manage concurrent I/O operations efficiently.',
        'Follow-up questions': ['What are the benefits of asynchronous programming using asyncio compared to traditional synchronous code?', 'Can you explain how event loops work in asyncio for handling multiple asynchronous tasks?', 'What are some common pitfalls to avoid when working with asyncio for concurrent programming?']
    },
    {
        'Main question': 'What are some common pitfalls and best practices for ensuring thread safety in Python concurrency?',
        'Explanation': 'Common pitfalls such as race conditions, deadlocks, and ensuring thread safety through synchronization mechanisms like locks, semaphores, and threading libraries.',
        'Follow-up questions': ['How can deadlocks be prevented in Python concurrent programs?', 'Can you explain the concept of thread safety and its importance in multi-threaded applications?', 'What tools or techniques can be used for debugging and profiling concurrent Python programs?']
    }
]